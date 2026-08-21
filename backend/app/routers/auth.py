import hashlib
import logging
import secrets
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.deps import get_current_user
from app.email_client import send_password_reset_email
from app.models import PasswordResetToken, Track, User
from app.schemas import ForgotPasswordIn, MessageOut, ResetPasswordIn, Token, UserCreate, UserOut, UserUpdate
from app.security import create_access_token, hash_password, verify_password

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["auth"])

GENERIC_FORGOT_PASSWORD_MESSAGE = "If an account exists for that email, we've sent a password reset link."


def _naive_utcnow() -> datetime:
    return datetime.utcnow()


def _hash_reset_token(raw_token: str) -> str:
    return hashlib.sha256(raw_token.encode("utf-8")).hexdigest()


def _valid_track_slugs(slugs: list, db: Session) -> list:
    if not slugs:
        return []
    return [t.slug for t in db.query(Track).filter(Track.slug.in_(slugs)).all()]


@router.post("/signup", response_model=Token)
def signup(payload: UserCreate, db: Session = Depends(get_db)):
    email = payload.email.strip().lower()
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    valid_slugs = _valid_track_slugs(payload.selected_tracks, db)

    user = User(
        email=email,
        hashed_password=hash_password(payload.password),
        display_name=payload.display_name,
        selected_tracks=valid_slugs,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return Token(access_token=create_access_token(user.id))


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    email = form_data.username.strip().lower()
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return Token(access_token=create_access_token(user.id))


@router.post("/forgot-password", response_model=MessageOut)
def forgot_password(payload: ForgotPasswordIn, db: Session = Depends(get_db)):
    email = payload.email.strip().lower()
    user = db.query(User).filter(User.email == email).first()

    # Always return the same generic message, whether or not the email is registered,
    # so this endpoint can't be used to enumerate which emails have accounts.
    if user:
        raw_token = secrets.token_urlsafe(32)
        db.add(
            PasswordResetToken(
                user_id=user.id,
                token_hash=_hash_reset_token(raw_token),
                expires_at=_naive_utcnow() + timedelta(minutes=settings.password_reset_expire_minutes),
            )
        )
        db.commit()

        reset_url = f"{settings.frontend_url}/reset-password?token={raw_token}"
        try:
            send_password_reset_email(user.email, reset_url)
        except Exception:
            logger.exception("Failed to send password reset email to user %s", user.id)

    return MessageOut(message=GENERIC_FORGOT_PASSWORD_MESSAGE)


@router.post("/reset-password", response_model=MessageOut)
def reset_password(payload: ResetPasswordIn, db: Session = Depends(get_db)):
    token_hash = _hash_reset_token(payload.token)
    token_row = db.query(PasswordResetToken).filter(PasswordResetToken.token_hash == token_hash).first()

    if (
        not token_row
        or token_row.used_at is not None
        or token_row.expires_at < _naive_utcnow()
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This reset link is invalid or has expired. Request a new one.",
        )

    user = db.query(User).filter(User.id == token_row.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This reset link is invalid.")

    user.hashed_password = hash_password(payload.new_password)
    token_row.used_at = _naive_utcnow()
    db.commit()

    return MessageOut(message="Your password has been reset. You can now log in.")


@router.get("/me", response_model=UserOut)
def me(current_user: User = Depends(get_current_user)):
    return current_user


@router.patch("/me", response_model=UserOut)
def update_me(
    payload: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    current_user.selected_tracks = _valid_track_slugs(payload.selected_tracks, db)
    db.commit()
    db.refresh(current_user)
    return current_user
