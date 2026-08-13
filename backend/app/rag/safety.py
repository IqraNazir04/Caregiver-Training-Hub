"""Lightweight keyword-based emergency flag. NOT a clinical triage classifier.

This is a placeholder for the planned full 3-tier symptom triage feature — it exists only to
demonstrate the escalation-logging pattern (flag + log) on the chat feature shipped in this pass.
"""

from typing import Optional

EMERGENCY_KEYWORDS = [
    "chest pain",
    "can't breathe",
    "cannot breathe",
    "not breathing",
    "unresponsive",
    "unconscious",
    "severe bleeding",
    "bleeding through",
    "suicid",
    "overdose",
    "seizure",
    "stroke symptoms",
    "signs of a stroke",
    "call 911",
]


def is_emergency_flagged(text: str) -> Optional[str]:
    """Returns the matched keyword if the text looks emergency-adjacent, else None."""
    lowered = text.lower()
    for keyword in EMERGENCY_KEYWORDS:
        if keyword in lowered:
            return keyword
    return None
