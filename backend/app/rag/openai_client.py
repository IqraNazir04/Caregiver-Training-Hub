"""Thin wrappers around the OpenAI SDK so call sites are easy to monkeypatch in tests."""

from functools import lru_cache

from openai import OpenAI

from app.config import settings


@lru_cache
def _client() -> OpenAI:
    return OpenAI(api_key=settings.openai_api_key)


def embed_texts(texts: list[str]) -> list[list[float]]:
    response = _client().embeddings.create(model=settings.embedding_model, input=texts)
    return [item.embedding for item in response.data]


def chat_completion(messages: list[dict]) -> str:
    response = _client().chat.completions.create(
        model=settings.chat_model,
        messages=messages,
        temperature=0.3,
    )
    return response.choices[0].message.content or ""
