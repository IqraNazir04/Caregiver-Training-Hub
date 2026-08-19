import io
import json

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


def _signup(client):
    signup_response = client.post(
        "/auth/signup",
        json={"email": "meds@example.com", "password": "supersecret1", "display_name": "Meds Tester"},
    )
    token = signup_response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_add_list_and_delete_medication(tmp_path, monkeypatch):
    app.dependency_overrides[get_db] = _make_test_db(tmp_path)
    client = TestClient(app)
    headers = _signup(client)

    add_response = client.post(
        "/medications",
        json={"name": "Metformin", "dosage": "500mg", "schedule_note": "Twice daily with food"},
        headers=headers,
    )
    assert add_response.status_code == 200
    med = add_response.json()
    assert med["source"] == "manual"

    list_response = client.get("/medications", headers=headers)
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1

    delete_response = client.delete(f"/medications/{med['id']}", headers=headers)
    assert delete_response.status_code == 204

    list_response = client.get("/medications", headers=headers)
    assert list_response.json() == []

    app.dependency_overrides.clear()


def test_scan_medication_parses_json_response(tmp_path, monkeypatch):
    app.dependency_overrides[get_db] = _make_test_db(tmp_path)
    monkeypatch.setattr("app.config.settings.anthropic_api_key", "sk-ant-test-fake-key")
    monkeypatch.setattr(
        "app.routers.medications.extract_medication_from_image",
        lambda image_bytes, media_type: json.dumps(
            {"name": "Lisinopril", "dosage": "10mg", "schedule_note": "Once daily in the morning"}
        ),
    )

    client = TestClient(app)
    headers = _signup(client)

    response = client.post(
        "/medications/scan",
        files={"file": ("label.jpg", io.BytesIO(b"fake-image-bytes"), "image/jpeg")},
        headers=headers,
    )
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Lisinopril"
    assert body["dosage"] == "10mg"

    app.dependency_overrides.clear()


def test_scan_medication_rejects_unsupported_type(tmp_path, monkeypatch):
    app.dependency_overrides[get_db] = _make_test_db(tmp_path)
    monkeypatch.setattr("app.config.settings.anthropic_api_key", "sk-ant-test-fake-key")

    client = TestClient(app)
    headers = _signup(client)

    response = client.post(
        "/medications/scan",
        files={"file": ("label.txt", io.BytesIO(b"not an image"), "text/plain")},
        headers=headers,
    )
    assert response.status_code == 400

    app.dependency_overrides.clear()


def test_check_interactions_requires_at_least_one_medication(tmp_path, monkeypatch):
    app.dependency_overrides[get_db] = _make_test_db(tmp_path)
    monkeypatch.setattr("app.config.settings.anthropic_api_key", "sk-ant-test-fake-key")

    client = TestClient(app)
    headers = _signup(client)

    response = client.post("/medications/check-interactions", headers=headers)
    assert response.status_code == 400

    app.dependency_overrides.clear()


def test_check_interactions_returns_content_and_disclaimer(tmp_path, monkeypatch):
    app.dependency_overrides[get_db] = _make_test_db(tmp_path)
    monkeypatch.setattr("app.config.settings.anthropic_api_key", "sk-ant-test-fake-key")
    monkeypatch.setattr(
        "app.routers.medications.chat_completion",
        lambda system, messages: "No obvious concerns found. Review with a pharmacist.",
    )

    client = TestClient(app)
    headers = _signup(client)

    client.post("/medications", json={"name": "Metformin", "dosage": "500mg"}, headers=headers)

    response = client.post("/medications/check-interactions", headers=headers)
    assert response.status_code == 200
    body = response.json()
    assert "disclaimer" in body
    assert "pharmacist" in body["content"].lower()

    app.dependency_overrides.clear()


def test_medication_endpoints_without_anthropic_key_return_friendly_error(tmp_path, monkeypatch):
    app.dependency_overrides[get_db] = _make_test_db(tmp_path)
    monkeypatch.setattr("app.config.settings.anthropic_api_key", "")

    client = TestClient(app)
    headers = _signup(client)
    client.post("/medications", json={"name": "Metformin"}, headers=headers)

    response = client.post("/medications/check-interactions", headers=headers)
    assert response.status_code == 503
    assert "configured" in response.json()["detail"].lower()

    app.dependency_overrides.clear()
