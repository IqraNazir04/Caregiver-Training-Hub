import logging

from anthropic import APIConnectionError as AnthropicAPIConnectionError
from anthropic import APIError as AnthropicAPIError
from fastapi import APIRouter, Depends, HTTPException, status
from openai import OpenAIError
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.deps import get_current_user
from app.models import Track, User
from app.rag.ai_clients import chat_completion
from app.rag.prompts import DISCLAIMER, build_checklist_prompt
from app.rag.retrieval import retrieve
from app.schemas import ChecklistIn, ChecklistOut, Citation

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/checklist", tags=["checklist"])


@router.post("/generate", response_model=ChecklistOut)
def generate_checklist(
    payload: ChecklistIn,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not settings.openai_api_key or not settings.anthropic_api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=(
                "The checklist generator isn't configured in this environment yet. Set OPENAI_API_KEY "
                "(embeddings) and ANTHROPIC_API_KEY (chat) on the backend to enable it."
            ),
        )

    tracks = db.query(Track).filter(Track.slug.in_(payload.track_slugs)).all()
    if not tracks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No matching tracks found")

    try:
        retrieved_chunks = []
        seen_chunks = set()
        for track in tracks:
            for chunk in retrieve(f"daily care checklist for {track.name}", track.id, k=3):
                key = (chunk["source_document_id"], chunk["snippet"])
                if key in seen_chunks:
                    continue
                seen_chunks.add(key)
                retrieved_chunks.append(chunk)

        system_prompt, messages = build_checklist_prompt(
            [t.name for t in tracks], payload.medications, retrieved_chunks
        )
        answer = chat_completion(system_prompt, messages)
    except (OpenAIError, AnthropicAPIError, AnthropicAPIConnectionError):
        logger.exception(
            "AI provider call failed while generating checklist for user %s", current_user.id
        )
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="The checklist generator is having trouble reaching the AI service right now. Please try again shortly.",
        )

    seen_ids = set()
    citations = []
    for chunk in retrieved_chunks:
        if chunk["source_document_id"] in seen_ids:
            continue
        seen_ids.add(chunk["source_document_id"])
        citations.append(
            Citation(
                source_document_id=chunk["source_document_id"],
                title=chunk["title"],
                snippet=chunk["snippet"],
            )
        )

    return ChecklistOut(content=answer, citations=citations, disclaimer=DISCLAIMER)
