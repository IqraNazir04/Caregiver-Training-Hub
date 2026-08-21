from datetime import datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app
from app.models import PasswordResetToken
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


def _signup(client, email="reset@example.com", password="supersecret1"):
    response = client.post(
        "/auth/signup",
        json={"email": email, "password": password, "display_name": "Reset Tester"},
    )
    return response.json()["access_token"]


def test_forgot_password_sends_email_for_known_account(tmp_path, monkeypatch):
    override_get_db, _ = _make_test_db(tmp_path)
    app.dependency_overrides[get_db] = override_get_db
    monkeypatch.setattr("app.config.settings.resend_api_key", "re_test_fake_key")

    sent = {}

    def fake_send(to_email, reset_url):
        sent["to_email"] = to_email
        sent["reset_url"] = reset_url

    monkeypatch.setattr("app.routers.auth.send_password_reset_email", fake_send)

    client = TestClient(app)
    _signup(client, email="reset@example.com")

    response = client.post("/auth/forgot-password", json={"email": "reset@example.com"})
    assert response.status_code == 200
    assert "reset link" in response.json()["message"].lower()
    assert sent["to_email"] == "reset@example.com"
    assert "token=" in sent["reset_url"]

    app.dependency_overrides.clear()


def test_forgot_password_same_generic_message_for_unknown_email(tmp_path, monkeypatch):
    override_get_db, _ = _make_test_db(tmp_path)
    app.dependency_overrides[get_db] = override_get_db
    monkeypatch.setattr("app.config.settings.resend_api_key", "re_test_fake_key")

    called = []
    monkeypatch.setattr(
        "app.routers.auth.send_password_reset_email",
        lambda to_email, reset_url: called.append(to_email),
    )

    client = TestClient(app)
    known = client.post("/auth/forgot-password", json={"email": "nobody@example.com"})

    assert known.status_code == 200
    assert "reset link" in known.json()["message"].lower()
    assert called == []  # no email attempted for an unregistered address

    app.dependency_overrides.clear()


def test_reset_password_end_to_end(tmp_path, monkeypatch):
    override_get_db, _ = _make_test_db(tmp_path)
    app.dependency_overrides[get_db] = override_get_db
    monkeypatch.setattr("app.config.settings.resend_api_key", "re_test_fake_key")

    captured = {}
    monkeypatch.setattr(
        "app.routers.auth.send_password_reset_email",
        lambda to_email, reset_url: captured.update(reset_url=reset_url),
    )

    client = TestClient(app)
    _signup(client, email="reset2@example.com", password="oldpassword1")

    client.post("/auth/forgot-password", json={"email": "reset2@example.com"})
    token = captured["reset_url"].split("token=")[1]

    reset_response = client.post(
        "/auth/reset-password", json={"token": token, "new_password": "newpassword2"}
    )
    assert reset_response.status_code == 200

    old_login = client.post(
        "/auth/login", data={"username": "reset2@example.com", "password": "oldpassword1"}
    )
    assert old_login.status_code == 401

    new_login = client.post(
        "/auth/login", data={"username": "reset2@example.com", "password": "newpassword2"}
    )
    assert new_login.status_code == 200

    # Token is single-use — trying it again must fail even with a valid-looking token.
    reuse_response = client.post(
        "/auth/reset-password", json={"token": token, "new_password": "thirdpassword3"}
    )
    assert reuse_response.status_code == 400

    app.dependency_overrides.clear()


def test_reset_password_rejects_invalid_token(tmp_path, monkeypatch):
    override_get_db, _ = _make_test_db(tmp_path)
    app.dependency_overrides[get_db] = override_get_db

    client = TestClient(app)
    response = client.post(
        "/auth/reset-password", json={"token": "not-a-real-token", "new_password": "whatever1"}
    )
    assert response.status_code == 400

    app.dependency_overrides.clear()


def test_reset_password_rejects_expired_token(tmp_path, monkeypatch):
    override_get_db, TestSessionLocal = _make_test_db(tmp_path)
    app.dependency_overrides[get_db] = override_get_db
    monkeypatch.setattr("app.config.settings.resend_api_key", "re_test_fake_key")

    captured = {}
    monkeypatch.setattr(
        "app.routers.auth.send_password_reset_email",
        lambda to_email, reset_url: captured.update(reset_url=reset_url),
    )

    client = TestClient(app)
    _signup(client, email="expired@example.com")
    client.post("/auth/forgot-password", json={"email": "expired@example.com"})
    token = captured["reset_url"].split("token=")[1]

    # Force the stored token to already be expired.
    db = TestSessionLocal()
    row = db.query(PasswordResetToken).first()
    row.expires_at = datetime.utcnow() - timedelta(minutes=1)
    db.commit()
    db.close()

    response = client.post(
        "/auth/reset-password", json={"token": token, "new_password": "newpassword2"}
    )
    assert response.status_code == 400

    app.dependency_overrides.clear()
