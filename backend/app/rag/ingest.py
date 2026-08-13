from app.models import SourceDocument
from app.rag.chroma_client import get_collection
from app.rag.openai_client import embed_texts


def chunk_text(text: str, max_chars: int = 1000) -> list[str]:
    """Naive paragraph-based chunking: group paragraphs until max_chars, never split a paragraph."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    current = ""
    for paragraph in paragraphs:
        candidate = f"{current}\n\n{paragraph}".strip() if current else paragraph
        if len(candidate) > max_chars and current:
            chunks.append(current)
            current = paragraph
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks or [text]


def ingest_source_document(doc: SourceDocument) -> None:
    chunks = chunk_text(doc.body_text)
    embeddings = embed_texts(chunks)
    collection = get_collection()
    collection.upsert(
        ids=[f"doc-{doc.id}-chunk-{i}" for i in range(len(chunks))],
        embeddings=embeddings,
        documents=chunks,
        metadatas=[
            {
                "source_document_id": doc.id,
                "track_id": doc.track_id,
                "title": doc.title,
            }
            for _ in chunks
        ],
    )
