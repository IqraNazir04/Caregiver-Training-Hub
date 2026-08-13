from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user
from app.models import Lesson, QuizQuestion, Track, User
from app.schemas import LessonOut, QuizResultItem, QuizSubmitIn, QuizSubmitOut, TrackDetailOut, TrackOut

router = APIRouter(prefix="/tracks", tags=["tracks"])


def _get_track_or_404(slug: str, db: Session) -> Track:
    track = db.query(Track).filter(Track.slug == slug).first()
    if not track:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Track not found")
    return track


@router.get("", response_model=list[TrackOut])
def list_tracks(db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    return db.query(Track).order_by(Track.name).all()


@router.get("/{slug}", response_model=TrackDetailOut)
def get_track(slug: str, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    return _get_track_or_404(slug, db)


@router.get("/{slug}/lessons/{lesson_id}", response_model=LessonOut)
def get_lesson(
    slug: str, lesson_id: int, db: Session = Depends(get_db), _: User = Depends(get_current_user)
):
    track = _get_track_or_404(slug, db)
    lesson = (
        db.query(Lesson).filter(Lesson.id == lesson_id, Lesson.track_id == track.id).first()
    )
    if not lesson:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
    return lesson


@router.post("/{slug}/lessons/{lesson_id}/quiz/submit", response_model=QuizSubmitOut)
def submit_quiz(
    slug: str,
    lesson_id: int,
    payload: QuizSubmitIn,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    track = _get_track_or_404(slug, db)
    lesson = (
        db.query(Lesson).filter(Lesson.id == lesson_id, Lesson.track_id == track.id).first()
    )
    if not lesson:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")

    questions = (
        db.query(QuizQuestion)
        .filter(QuizQuestion.lesson_id == lesson.id)
        .order_by(QuizQuestion.id)
        .all()
    )
    if len(payload.answers) != len(questions):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Expected {len(questions)} answers, got {len(payload.answers)}",
        )

    results = []
    score = 0
    for question, answer_index in zip(questions, payload.answers):
        correct = answer_index == question.correct_index
        if correct:
            score += 1
        results.append(
            QuizResultItem(
                question_id=question.id,
                correct=correct,
                correct_index=question.correct_index,
                explanation=question.explanation,
            )
        )

    return QuizSubmitOut(score=score, total=len(questions), results=results)
