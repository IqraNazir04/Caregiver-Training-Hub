from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# --- Auth ---

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    display_name: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    display_name: str

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# --- Tracks / Lessons / Quiz ---

class TrackOut(BaseModel):
    id: int
    slug: str
    name: str
    description: str

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
