# Caregiver Training Hub

Bite-sized microlearning + AI chat support for home health aides and family caregivers of elderly or chronically ill relatives.

## What's built

- **Condition-specific learning tracks**: short lessons + quizzes, seeded with 3 tracks (Dementia/Alzheimer's Care, Post-Stroke Recovery, Diabetes Management).
- **Track-scoped RAG chat**: caregivers ask questions and get answers grounded in seeded reference content, with inline citations, a visible "not medical advice" disclaimer on every response, and lightweight keyword-based escalation logging for emergency-adjacent messages.
- **Auth**: email/password signup and login with JWT sessions.

## Roadmap (not yet built)

Daily care checklist generator, medication OCR/interaction assistant, full 3-tier symptom triage, voice-first mode, burnout/respite check-ins, family care coordination board, pre-appointment prep tool.

## Project layout

```
backend/    FastAPI app, SQLAlchemy models, RAG pipeline, seed data
frontend/   React + Vite SPA
```

## Running locally

### Backend

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
cp .env.example .env   # then set OPENAI_API_KEY (embeddings) and ANTHROPIC_API_KEY (chat, Claude Sonnet 5)
python -m seed.seed_data   # loads tracks/lessons/quizzes into SQLite and embeds source docs into Chroma
uvicorn app.main:app --reload
```

API docs at http://localhost:8000/docs.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

App at http://localhost:5173 (proxies API calls to http://localhost:8000 by default — override with `VITE_API_URL`).

### Tests

```bash
cd backend
pytest
```

Backend tests mock all OpenAI and Anthropic calls, so no API key or network access is required to run them.

## Safety notes

Every chat response carries a visible disclaimer that it is educational, not medical advice, and to call 911 for emergencies. Messages that match a small set of emergency-adjacent keywords are flagged in the UI and logged to an `EscalationLog` table for later review — this is a lightweight placeholder for the planned full 3-tier symptom triage feature, not a clinical triage system.
