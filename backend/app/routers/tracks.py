from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user
from app.models import Lesson, LessonProgress, QuizQuestion, Track, User
from app.schemas import (
    LessonOut,
    QuizQuestionOut,
    QuizResultItem,
    QuizSubmitIn,
    QuizSubmitOut,
    TrackDetailOut,
    TrackOut,
)

router = APIRouter(prefix="/tracks", tags=["tracks"])


def _get_track_or_404(slug: str, db: Session) -> Track:
    track = db.query(Track).filter(Track.slug == slug).first()
    if not track:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Track not found")
    return track


def _track_out(track: Track, db: Session, user: Optional[User]) -> TrackOut:
    lesson_ids = [l.id for l in track.lessons]
    completed_count = 0
    if user and lesson_ids:
        completed_count = (
            db.query(LessonProgress)
            .filter(LessonProgress.user_id == user.id, LessonProgress.lesson_id.in_(lesson_ids))
            .count()
        )
    return TrackOut(
        id=track.id,
        slug=track.slug,
        name=track.name,
        description=track.description,
        theme=track.theme,
        lesson_count=len(lesson_ids),
        completed_count=completed_count,
    )


@router.get("", response_model=list[TrackOut])
def list_tracks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    tracks = db.query(Track).order_by(Track.name).all()
    return [_track_out(t, db, current_user) for t in tracks]


@router.get("/public", response_model=list[TrackOut])
def list_tracks_public(db: Session = Depends(get_db)):
    """Unauthenticated track listing (name/slug/description/theme only) for pre-signup topic selection."""
    tracks = db.query(Track).order_by(Track.name).all()
    return [_track_out(t, db, None) for t in tracks]


@router.get("/{slug}", response_model=TrackDetailOut)
def get_track(slug: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    track = _get_track_or_404(slug, db)
    lesson_ids = [l.id for l in track.lessons]
    progress_by_lesson = {}
    if lesson_ids:
        progress_rows = (
            db.query(LessonProgress)
            .filter(LessonProgress.user_id == current_user.id, LessonProgress.lesson_id.in_(lesson_ids))
            .all()
        )
        progress_by_lesson = {p.lesson_id: p for p in progress_rows}

    lessons_out = []
    for lesson in track.lessons:
        progress = progress_by_lesson.get(lesson.id)
        lessons_out.append(
            LessonOut(
                id=lesson.id,
                title=lesson.title,
                order_index=lesson.order_index,
                body_markdown=lesson.body_markdown,
                estimated_minutes=lesson.estimated_minutes,
                quiz_questions=[
                    QuizQuestionOut(id=q.id, question_text=q.question_text, choices=q.choices)
                    for q in lesson.quiz_questions
                ],
                completed=progress is not None,
                quiz_score=progress.quiz_score if progress else None,
                quiz_total=progress.quiz_total if progress else None,
                completed_at=progress.completed_at if progress else None,
            )
        )

    base = _track_out(track, db, current_user)
    return TrackDetailOut(**base.model_dump(), lessons=lessons_out)


@router.get("/{slug}/lessons/{lesson_id}", response_model=LessonOut)
def get_lesson(
    slug: str, lesson_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    track = _get_track_or_404(slug, db)
    lesson = (
        db.query(Lesson).filter(Lesson.id == lesson_id, Lesson.track_id == track.id).first()
    )
    if not lesson:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")

    progress = (
        db.query(LessonProgress)
        .filter(LessonProgress.user_id == current_user.id, LessonProgress.lesson_id == lesson.id)
        .first()
    )

    return LessonOut(
        id=lesson.id,
        title=lesson.title,
        order_index=lesson.order_index,
        body_markdown=lesson.body_markdown,
        estimated_minutes=lesson.estimated_minutes,
        quiz_questions=[
            QuizQuestionOut(id=q.id, question_text=q.question_text, choices=q.choices)
            for q in lesson.quiz_questions
        ],
        completed=progress is not None,
        quiz_score=progress.quiz_score if progress else None,
        quiz_total=progress.quiz_total if progress else None,
        completed_at=progress.completed_at if progress else None,
    )


@router.post("/{slug}/lessons/{lesson_id}/quiz/submit", response_model=QuizSubmitOut)
def submit_quiz(
    slug: str,
    lesson_id: int,
    payload: QuizSubmitIn,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
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

    total = len(questions)
    progress = (
        db.query(LessonProgress)
        .filter(LessonProgress.user_id == current_user.id, LessonProgress.lesson_id == lesson.id)
        .first()
    )
    if progress:
        progress.quiz_score = score
        progress.quiz_total = total
    else:
        db.add(
            LessonProgress(
                user_id=current_user.id, lesson_id=lesson.id, quiz_score=score, quiz_total=total
            )
        )
    db.commit()

    return QuizSubmitOut(score=score, total=total, results=results)
