from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


# --- Auth ---

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    display_name: str
    selected_tracks: list[str] = []


class UserOut(BaseModel):
    id: int
    email: EmailStr
    display_name: str
    selected_tracks: list[str] = []

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    selected_tracks: list[str]


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ForgotPasswordIn(BaseModel):
    email: EmailStr


class ResetPasswordIn(BaseModel):
    token: str = Field(min_length=1)
    new_password: str = Field(min_length=8)


class MessageOut(BaseModel):
    message: str


# --- Tracks / Lessons / Quiz ---

class TrackOut(BaseModel):
    id: int
    slug: str
    name: str
    description: str
    theme: str
    lesson_count: int = 0
    completed_count: int = 0

    model_config = ConfigDict(from_attributes=True)


class QuizQuestionOut(BaseModel):
    id: int
    question_text: str
    choices: list[str]

    model_config = ConfigDict(from_attributes=True)


class LessonOut(BaseModel):
    id: int
    title: str
    order_index: int
    body_markdown: str
    estimated_minutes: int
    quiz_questions: list[QuizQuestionOut] = []
    completed: bool = False
    quiz_score: Optional[int] = None
    quiz_total: Optional[int] = None
    completed_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class TrackDetailOut(TrackOut):
    lessons: list[LessonOut] = []


class QuizSubmitIn(BaseModel):
    answers: list[int]


class QuizResultItem(BaseModel):
    question_id: int
    correct: bool
    correct_index: int
    explanation: str


class QuizSubmitOut(BaseModel):
    score: int
    total: int
    results: list[QuizResultItem]


# --- Chat ---

class ChatSessionCreate(BaseModel):
    track_slug: Optional[str] = None


class ChatSessionOut(BaseModel):
    id: int
    track_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)


class ChatMessageIn(BaseModel):
    content: str = Field(min_length=1)

    @field_validator("content")
    @classmethod
    def content_must_not_be_blank(cls, v):
        v = v.strip()
        if not v:
            raise ValueError("Message cannot be blank")
        return v


class Citation(BaseModel):
    source_document_id: int
    title: str
    snippet: str


class ChatMessageOut(BaseModel):
    id: int
    role: str
    content: str
    citations: list[Citation]
    is_flagged: bool
    disclaimer: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# --- Checklist ---

class ChecklistIn(BaseModel):
    track_slugs: list[str] = Field(min_length=1)
    medications: list[str] = []


class ChecklistOut(BaseModel):
    content: str
    citations: list[Citation]
    disclaimer: str


# --- Medications ---

class MedicationCreate(BaseModel):
    name: str = Field(min_length=1)
    dosage: str = ""
    schedule_note: str = ""

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, v):
        v = v.strip()
        if not v:
            raise ValueError("Medication name cannot be blank")
        return v

    @field_validator("dosage", "schedule_note")
    @classmethod
    def strip_optional_fields(cls, v):
        return v.strip()


class MedicationOut(BaseModel):
    id: int
    name: str
    dosage: str
    schedule_note: str
    source: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class MedicationScanOut(BaseModel):
    name: str
    dosage: str
    schedule_note: str


class InteractionCheckOut(BaseModel):
    content: str
    disclaimer: str
