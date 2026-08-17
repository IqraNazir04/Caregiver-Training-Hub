from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app
from app.models import Lesson, QuizQuestion, Track
from fastapi.testclient import TestClient


def _make_test_db(tmp_path):
    db_path = tmp_path / "test.db"
    engine = create_engine(f"sqlite:///{db_path}", connect_args={"check_same_thread": False})
    TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestSessionLocal()
        try:
            yield db
        finally:
            db.close()

    return override_get_db, TestSessionLocal


def _seed_track(SessionLocal):
    db = SessionLocal()
    track = Track(
        slug="test-track",
        name="Test Track",
        description="A track for testing.",
        theme="foundational",
    )
    db.add(track)
    db.flush()
    lesson = Lesson(
        track_id=track.id,
        title="Test Lesson",
        order_index=0,
        body_markdown="Body.",
        estimated_minutes=3,
    )
    db.add(lesson)
    db.flush()
    db.add(
        QuizQuestion(
            lesson_id=lesson.id,
            question_text="2 + 2?",
            choices=["3", "4"],
            correct_index=1,
            explanation="Basic arithmetic.",
        )
    )
    db.commit()
    db.close()


def test_quiz_submission_records_progress_and_is_idempotent_per_lesson(tmp_path):
    override_get_db, SessionLocal = _make_test_db(tmp_path)
    app.dependency_overrides[get_db] = override_get_db
    _seed_track(SessionLocal)

    client = TestClient(app)

    signup_response = client.post(
        "/auth/signup",
        json={"email": "learner@example.com", "password": "supersecret1", "display_name": "Learner"},
    )
    token = signup_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # before any quiz attempt: lesson not completed
    detail = client.get("/tracks/test-track", headers=headers).json()
    assert detail["theme"] == "foundational"
    assert detail["lesson_count"] == 1
    assert detail["completed_count"] == 0
    lesson_id = detail["lessons"][0]["id"]
    assert detail["lessons"][0]["completed"] is False

    # wrong answer
    submit = client.post(
        f"/tracks/test-track/lessons/{lesson_id}/quiz/submit",
        json={"answers": [0]},
        headers=headers,
    )
    assert submit.status_code == 200
    assert submit.json()["score"] == 0

    detail_after_wrong = client.get("/tracks/test-track", headers=headers).json()
    assert detail_after_wrong["completed_count"] == 1
    assert detail_after_wrong["lessons"][0]["completed"] is True
    assert detail_after_wrong["lessons"][0]["quiz_score"] == 0

    # retake with correct answer — should update in place, not duplicate
    submit2 = client.post(
        f"/tracks/test-track/lessons/{lesson_id}/quiz/submit",
        json={"answers": [1]},
        headers=headers,
    )
    assert submit2.json()["score"] == 1

    detail_after_retake = client.get("/tracks/test-track", headers=headers).json()
    assert detail_after_retake["completed_count"] == 1  # still just one lesson's worth of progress
    assert detail_after_retake["lessons"][0]["quiz_score"] == 1

    list_response = client.get("/tracks", headers=headers).json()
    test_track = next(t for t in list_response if t["slug"] == "test-track")
    assert test_track["completed_count"] == 1
    assert test_track["lesson_count"] == 1

    app.dependency_overrides.clear()
