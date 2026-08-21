"""Thin wrapper around the Resend SDK so call sites are easy to monkeypatch in tests."""

import resend

from app.config import settings


def send_password_reset_email(to_email: str, reset_url: str) -> None:
    resend.api_key = settings.resend_api_key
    resend.Emails.send(
        {
            "from": settings.email_from,
            "to": to_email,
            "subject": "Reset your Caregiver Training Hub password",
            "html": f"""
                <p>Someone requested a password reset for this email address on Caregiver Training Hub.</p>
                <p><a href="{reset_url}">Click here to choose a new password</a>. This link expires in
                {settings.password_reset_expire_minutes} minutes.</p>
                <p>If you didn't request this, you can safely ignore this email — your password won't change.</p>
            """,
        }
    )
