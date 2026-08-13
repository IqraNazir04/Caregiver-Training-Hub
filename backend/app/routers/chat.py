from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user
from app.models import ChatMessage, ChatSession, EscalationLog, Track, User
from app.rag.openai_client import chat_completion
from app.rag.prompts import DISCLAIMER, build_prompt
from app.rag.retrieval import retrieve
from app.rag.safety import is_emergency_flagged
from app.schemas import ChatMessageIn, ChatMessageOut, ChatSessionCreate, ChatSessionOut

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/sessions", response_model=ChatSessionOut)
def create_session(
    payload: ChatSessionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    track_id = None
    if payload.track_slug:
        track = db.query(Track).filter(Track.slug == payload.track_slug).first()
        if not track:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Track not found")
        track_id = track.id

    session = ChatSession(user_id=current_user.id, track_id=track_id)
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def _get_session_or_404(session_id: int, current_user: User, db: Session) -> ChatSession:
    session = (
        db.query(ChatSession)
        .filter(ChatSession.id == session_id, ChatSession.user_id == current_user.id)
        .first()
    )
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat session not found")
    return session


@router.get("/sessions/{session_id}/messages", response_model=list[ChatMessageOut])
def list_messages(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = _get_session_or_404(session_id, current_user, db)
    return [
        ChatMessageOut(
            id=m.id,
            role=m.role,
            content=m.content,
            citations=m.citations,
            is_flagged=m.is_flagged,
            disclaimer=DISCLAIMER,
            created_at=m.created_at,
        )
        for m in session.messages
    ]


@router.post("/sessions/{session_id}/messages", response_model=ChatMessageOut)
def post_message(
    session_id: int,
    payload: ChatMessageIn,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = _get_session_or_404(session_id, current_user, db)

    user_message = ChatMessage(session_id=session.id, role="user", content=payload.content)
    db.add(user_message)
    db.commit()
    db.refresh(user_message)

    history = [{"role": m.role, "content": m.content} for m in session.messages[:-1]]
    retrieved_chunks = retrieve(payload.content, session.track_id)
    prompt = build_prompt(history, retrieved_chunks, payload.content)
    answer = chat_completion(prompt)

    seen_ids = set()
    citations = []
    for chunk in retrieved_chunks:
        if chunk["source_document_id"] in seen_ids:
            continue
        seen_ids.add(chunk["source_document_id"])
        citations.append(
            {
                "source_document_id": chunk["source_document_id"],
                "title": chunk["title"],
                "snippet": chunk["snippet"],
            }
        )

    matched_keyword = is_emergency_flagged(payload.content) or is_emergency_flagged(answer)
    is_flagged = matched_keyword is not None

    assistant_message = ChatMessage(
        session_id=session.id,
        role="assistant",
        content=answer,
        citations=citations,
        is_flagged=is_flagged,
    )
    db.add(assistant_message)
    db.commit()
    db.refresh(assistant_message)

    if is_flagged:
        db.add(
            EscalationLog(
                chat_message_id=assistant_message.id,
                user_id=current_user.id,
                reason_text=f"Matched emergency keyword: '{matched_keyword}'",
            )
        )
        db.commit()

    return ChatMessageOut(
        id=assistant_message.id,
        role=assistant_message.role,
        content=assistant_message.content,
        citations=citations,
        is_flagged=is_flagged,
        disclaimer=DISCLAIMER,
        created_at=assistant_message.created_at,
    )
