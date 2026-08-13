from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app
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

    return override_get_db


def test_signup_login_and_chat_message(tmp_path, monkeypatch):
    app.dependency_overrides[get_db] = _make_test_db(tmp_path)

    monkeypatch.setattr(
        "app.routers.chat.chat_completion",
        lambda messages: "Here is some general caregiving guidance based on the context.",
    )

    client = TestClient(app)

    signup_response = client.post(
        "/auth/signup",
        json={"email": "caregiver@example.com", "password": "supersecret1", "display_name": "Jamie"},
    )
    assert signup_response.status_code == 200
    token = signup_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    login_response = client.post(
        "/auth/login",
        data={"username": "caregiver@example.com", "password": "supersecret1"},
    )
    assert login_response.status_code == 200

    session_response = client.post("/chat/sessions", json={"track_slug": None}, headers=headers)
    assert session_response.status_code == 200
    session_id = session_response.json()["id"]

    message_response = client.post(
        f"/chat/sessions/{session_id}/messages",
        json={"content": "What should I keep in mind as a new caregiver?"},
        headers=headers,
    )
    assert message_response.status_code == 200
    body = message_response.json()
    assert "disclaimer" in body
    assert "citations" in body
    assert body["role"] == "assistant"

    app.dependency_overrides.clear()


def test_emergency_keyword_flags_and_logs_escalation(tmp_path, monkeypatch):
    app.dependency_overrides[get_db] = _make_test_db(tmp_path)

    monkeypatch.setattr(
        "app.routers.chat.chat_completion",
        lambda messages: "If this is happening now, call 911 immediately.",
    )

    client = TestClient(app)

    signup_response = client.post(
        "/auth/signup",
        json={"email": "caregiver2@example.com", "password": "supersecret1", "display_name": "Alex"},
    )
    token = signup_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    session_response = client.post("/chat/sessions", json={"track_slug": None}, headers=headers)
    session_id = session_response.json()["id"]

    message_response = client.post(
        f"/chat/sessions/{session_id}/messages",
        json={"content": "They are unresponsive and I don't know what to do"},
        headers=headers,
    )
    assert message_response.status_code == 200
    assert message_response.json()["is_flagged"] is True

    app.dependency_overrides.clear()
