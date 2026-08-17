from typing import Optional

from app.rag.chroma_client import get_collection
from app.rag.ai_clients import embed_texts


def retrieve(query: str, track_id: Optional[int], k: int = 4) -> list:
    collection = get_collection()
    if collection.count() == 0:
        return []

    [query_embedding] = embed_texts([query])
    where = {"track_id": track_id} if track_id is not None else None

    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(k, collection.count()),
        where=where,
    )

    documents = result.get("documents") or [[]]
    metadatas = result.get("metadatas") or [[]]
    distances = result.get("distances") or [[]]

    hits = []
    for doc, meta, distance in zip(documents[0], metadatas[0], distances[0]):
        hits.append(
            {
                "source_document_id": meta["source_document_id"],
                "title": meta["title"],
                "snippet": doc,
                "score": distance,
            }
        )
    return hits
