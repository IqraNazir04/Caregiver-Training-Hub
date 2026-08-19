from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app
from app.models import Track
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

    return override_get_db, TestSessionLocal


def _isolate_chroma(tmp_path, monkeypatch):
    monkeypatch.setattr("app.config.settings.chroma_persist_dir", str(tmp_path / "chroma_test"))
    monkeypatch.setattr("app.config.settings.openai_api_key", "sk-test-fake-key")
    monkeypatch.setattr("app.config.settings.anthropic_api_key", "sk-ant-test-fake-key")
    get_collection.cache_clear()


def _signup(client):
    signup_response = client.post(
        "/auth/signup",
        json={"email": "checklist@example.com", "password": "supersecret1", "display_name": "Checklist Tester"},
    )
    token = signup_response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_generate_checklist_returns_content_and_citations(tmp_path, monkeypatch):
    override_get_db, TestSessionLocal = _make_test_db(tmp_path)
    app.dependency_overrides[get_db] = override_get_db
    _isolate_chroma(tmp_path, monkeypatch)

    db = TestSessionLocal()
    track = Track(slug="basic-first-aid-caregivers", name="Basic First Aid for Caregivers", description="d", theme="practical-skills")
    db.add(track)
    db.commit()
    db.close()

    monkeypatch.setattr(
        "app.routers.checklist.chat_completion",
        lambda system, messages: "## Medication timing\n- Take with breakfast\n\n## Vitals to watch\n- Blood pressure\n\n## Red-flag symptoms\n- Chest pain",
    )

    client = TestClient(app)
    headers = _signup(client)

    response = client.post(
        "/checklist/generate",
        json={"track_slugs": ["basic-first-aid-caregivers"], "medications": ["Metformin", "Lisinopril"]},
        headers=headers,
    )
    assert response.status_code == 200
    body = response.json()
    assert "disclaimer" in body
    assert "citations" in body
    assert "Medication timing" in body["content"]

    app.dependency_overrides.clear()


def test_generate_checklist_unknown_track_returns_404(tmp_path, monkeypatch):
    override_get_db, _ = _make_test_db(tmp_path)
    app.dependency_overrides[get_db] = override_get_db
    _isolate_chroma(tmp_path, monkeypatch)

    client = TestClient(app)
    headers = _signup(client)

    response = client.post(
        "/checklist/generate",
        json={"track_slugs": ["not-a-real-track"], "medications": []},
        headers=headers,
    )
    assert response.status_code == 404

    app.dependency_overrides.clear()


def test_generate_checklist_without_ai_keys_returns_friendly_error(tmp_path, monkeypatch):
    override_get_db, TestSessionLocal = _make_test_db(tmp_path)
    app.dependency_overrides[get_db] = override_get_db
    monkeypatch.setattr("app.config.settings.chroma_persist_dir", str(tmp_path / "chroma_test"))
    monkeypatch.setattr("app.config.settings.openai_api_key", "")
    monkeypatch.setattr("app.config.settings.anthropic_api_key", "")
    get_collection.cache_clear()

    db = TestSessionLocal()
    track = Track(slug="basic-first-aid-caregivers", name="Basic First Aid for Caregivers", description="d", theme="practical-skills")
    db.add(track)
    db.commit()
    db.close()

    client = TestClient(app)
    headers = _signup(client)

    response = client.post(
        "/checklist/generate",
        json={"track_slugs": ["basic-first-aid-caregivers"], "medications": []},
        headers=headers,
    )
    assert response.status_code == 503
    assert "configured" in response.json()["detail"].lower()

    app.dependency_overrides.clear()
