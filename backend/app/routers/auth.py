from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user
from app.models import Track, User
from app.schemas import Token, UserCreate, UserOut, UserUpdate
from app.security import create_access_token, hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])


def _valid_track_slugs(slugs: list, db: Session) -> list:
    if not slugs:
        return []
    return [t.slug for t in db.query(Track).filter(Track.slug.in_(slugs)).all()]


@router.post("/signup", response_model=Token)
def signup(payload: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    valid_slugs = _valid_track_slugs(payload.selected_tracks, db)

    user = User(
        email=payload.email,
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
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return Token(access_token=create_access_token(user.id))


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
