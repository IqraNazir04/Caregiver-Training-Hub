from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app
from app.rag.chroma_client import get_collection
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


def _isolate_chroma(tmp_path, monkeypatch):
    """Point Chroma at an empty temp dir so tests never see the real dev-seeded collection
    (which would otherwise make `retrieve()` call the real, unmocked OpenAI embeddings API),
    and set fake API keys so the router's "is chat configured" check passes in tests."""
    monkeypatch.setattr("app.config.settings.chroma_persist_dir", str(tmp_path / "chroma_test"))
    monkeypatch.setattr("app.config.settings.openai_api_key", "sk-test-fake-key")
    monkeypatch.setattr("app.config.settings.anthropic_api_key", "sk-ant-test-fake-key")
    get_collection.cache_clear()


def test_signup_login_and_chat_message(tmp_path, monkeypatch):
    app.dependency_overrides[get_db] = _make_test_db(tmp_path)
    _isolate_chroma(tmp_path, monkeypatch)

    monkeypatch.setattr(
        "app.routers.chat.chat_completion",
        lambda system, messages: "Here is some general caregiving guidance based on the context.",
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
    _isolate_chroma(tmp_path, monkeypatch)

    monkeypatch.setattr(
        "app.routers.chat.chat_completion",
        lambda system, messages: "If this is happening now, call 911 immediately.",
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


def test_chat_without_ai_keys_returns_friendly_error_not_500(tmp_path, monkeypatch):
    """Regression test: sending a message with no OPENAI_API_KEY/ANTHROPIC_API_KEY configured must
    return a clean, friendly 503 — not an unhandled 500 with a raw stack trace leaking to the client."""
    app.dependency_overrides[get_db] = _make_test_db(tmp_path)
    monkeypatch.setattr("app.config.settings.chroma_persist_dir", str(tmp_path / "chroma_test"))
    monkeypatch.setattr("app.config.settings.openai_api_key", "")
    monkeypatch.setattr("app.config.settings.anthropic_api_key", "")
    get_collection.cache_clear()

    client = TestClient(app)

    signup_response = client.post(
        "/auth/signup",
        json={"email": "nokeytest@example.com", "password": "supersecret1", "display_name": "No Key"},
    )
    token = signup_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    session_response = client.post("/chat/sessions", json={"track_slug": None}, headers=headers)
    session_id = session_response.json()["id"]

    message_response = client.post(
        f"/chat/sessions/{session_id}/messages",
        json={"content": "Hello"},
        headers=headers,
    )
    assert message_response.status_code == 503
    assert "configured" in message_response.json()["detail"].lower()

    app.dependency_overrides.clear()
