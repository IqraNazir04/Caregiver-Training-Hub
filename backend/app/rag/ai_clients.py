"""Thin wrappers around the OpenAI and Anthropic SDKs so call sites are easy to monkeypatch in
tests. Embeddings stay on OpenAI (Anthropic has no embeddings API); chat generation uses Claude."""

import base64
from functools import lru_cache

from anthropic import Anthropic
from openai import OpenAI

from app.config import settings
from app.rag.prompts import MEDICATION_SCAN_SYSTEM_PROMPT


@lru_cache
def _openai_client() -> OpenAI:
    return OpenAI(api_key=settings.openai_api_key)


@lru_cache
def _anthropic_client() -> Anthropic:
    return Anthropic(api_key=settings.anthropic_api_key)


def embed_texts(texts: list[str]) -> list[list[float]]:
    response = _openai_client().embeddings.create(model=settings.embedding_model, input=texts)
    return [item.embedding for item in response.data]


def chat_completion(system: str, messages: list[dict]) -> str:
    response = _anthropic_client().messages.create(
        model=settings.chat_model,
        max_tokens=1024,
        system=system,
        thinking={"type": "disabled"},
        messages=messages,
    )
    if response.stop_reason == "refusal":
        return "I'm not able to help with that request."
    return "".join(block.text for block in response.content if block.type == "text")


def extract_medication_from_image(image_bytes: bytes, media_type: str) -> str:
    b64_data = base64.standard_b64encode(image_bytes).decode("utf-8")
    response = _anthropic_client().messages.create(
        model=settings.chat_model,
        max_tokens=512,
        system=MEDICATION_SCAN_SYSTEM_PROMPT,
        thinking={"type": "disabled"},
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "image", "source": {"type": "base64", "media_type": media_type, "data": b64_data}},
                    {
                        "type": "text",
                        "text": "Extract the medication name, dosage/strength, and frequency from this label photo.",
                    },
                ],
            }
        ],
    )
    if response.stop_reason == "refusal":
        return ""
    return "".join(block.text for block in response.content if block.type == "text")
