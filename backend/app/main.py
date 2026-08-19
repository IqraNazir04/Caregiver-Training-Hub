from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import auth, chat, checklist, medications, tracks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Caregiver Training Hub API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(tracks.router)
app.include_router(chat.router)
app.include_router(checklist.router)
app.include_router(medications.router)


@app.get("/health")
def health():
    return {"status": "ok"}
