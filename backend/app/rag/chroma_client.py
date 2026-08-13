from functools import lru_cache

import chromadb

from app.config import settings

COLLECTION_NAME = "caregiver_docs"


@lru_cache
def get_collection():
    client = chromadb.PersistentClient(path=settings.chroma_persist_dir)
    return client.get_or_create_collection(COLLECTION_NAME)
