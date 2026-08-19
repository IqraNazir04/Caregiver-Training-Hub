import json
import logging

from anthropic import APIConnectionError as AnthropicAPIConnectionError
from anthropic import APIError as AnthropicAPIError
from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.deps import get_current_user
from app.models import Medication, User
from app.rag.ai_clients import chat_completion, extract_medication_from_image
from app.rag.prompts import MEDICATION_DISCLAIMER, build_interaction_prompt
from app.schemas import InteractionCheckOut, MedicationCreate, MedicationOut, MedicationScanOut

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/medications", tags=["medications"])

ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/webp", "image/gif"}
MAX_IMAGE_BYTES = 5 * 1024 * 1024


def _require_anthropic_configured():
    if not settings.anthropic_api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="The medication assistant isn't configured in this environment yet. Set ANTHROPIC_API_KEY on the backend to enable it.",
        )


@router.get("", response_model=list[MedicationOut])
def list_medications(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return (
        db.query(Medication)
        .filter(Medication.user_id == current_user.id)
        .order_by(Medication.created_at)
        .all()
    )


@router.post("", response_model=MedicationOut)
def add_medication(
    payload: MedicationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    medication = Medication(
        user_id=current_user.id,
        name=payload.name,
        dosage=payload.dosage,
        schedule_note=payload.schedule_note,
        source="manual",
    )
    db.add(medication)
    db.commit()
    db.refresh(medication)
    return medication


@router.delete("/{medication_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medication(
    medication_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    medication = (
        db.query(Medication)
        .filter(Medication.id == medication_id, Medication.user_id == current_user.id)
        .first()
    )
    if not medication:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medication not found")
    db.delete(medication)
    db.commit()


@router.post("/scan", response_model=MedicationScanOut)
def scan_medication(
    file: UploadFile,
    current_user: User = Depends(get_current_user),
):
    _require_anthropic_configured()

    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported image type. Upload a JPEG, PNG, WEBP, or GIF photo of the label.",
        )

    image_bytes = file.file.read(MAX_IMAGE_BYTES + 1)
    if len(image_bytes) > MAX_IMAGE_BYTES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Image is too large (max 5MB).")
    if not image_bytes:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Uploaded file is empty.")

    try:
        raw = extract_medication_from_image(image_bytes, file.content_type)
    except (AnthropicAPIError, AnthropicAPIConnectionError):
        logger.exception("Anthropic call failed while scanning medication photo for user %s", current_user.id)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="The label scanner is having trouble reaching the AI service right now. Please try again shortly.",
        )

    try:
        parsed = json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        parsed = {}

    return MedicationScanOut(
        name=str(parsed.get("name") or ""),
        dosage=str(parsed.get("dosage") or ""),
        schedule_note=str(parsed.get("schedule_note") or ""),
    )


@router.post("/check-interactions", response_model=InteractionCheckOut)
def check_interactions(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    _require_anthropic_configured()

    medications = (
        db.query(Medication)
        .filter(Medication.user_id == current_user.id)
        .order_by(Medication.created_at)
        .all()
    )
    if not medications:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Add at least one medication first.")

    try:
        system_prompt, messages = build_interaction_prompt(
            [{"name": m.name, "dosage": m.dosage} for m in medications]
        )
        answer = chat_completion(system_prompt, messages)
    except (AnthropicAPIError, AnthropicAPIConnectionError):
        logger.exception(
            "Anthropic call failed while checking medication interactions for user %s", current_user.id
        )
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="The interaction check is having trouble reaching the AI service right now. Please try again shortly.",
        )

    return InteractionCheckOut(content=answer, disclaimer=MEDICATION_DISCLAIMER)
