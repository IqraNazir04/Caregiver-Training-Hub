"""Idempotent seed script: loads seed tracks/lessons/quizzes into SQL and embeds source docs into Chroma.

Run with: python -m seed.seed_data
"""

from app.database import Base, SessionLocal, engine
from app.models import Lesson, QuizQuestion, SourceDocument, Track
from app.rag.ingest import ingest_source_document
from seed.content import dementia, diabetes, post_stroke

ALL_TRACKS = [dementia.TRACK, diabetes.TRACK, post_stroke.TRACK]


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        for track_data in ALL_TRACKS:
            existing = db.query(Track).filter(Track.slug == track_data["slug"]).first()
            if existing:
                print(f"Skipping '{track_data['slug']}' — already seeded.")
                continue

            track = Track(
                slug=track_data["slug"],
                name=track_data["name"],
                description=track_data["description"],
            )
            db.add(track)
            db.flush()  # populate track.id

            for order_index, lesson_data in enumerate(track_data["lessons"]):
                lesson = Lesson(
                    track_id=track.id,
                    title=lesson_data["title"],
                    order_index=order_index,
                    body_markdown=lesson_data["body_markdown"],
                    estimated_minutes=lesson_data["estimated_minutes"],
                )
                db.add(lesson)
                db.flush()

                for quiz_data in lesson_data["quiz"]:
                    db.add(
                        QuizQuestion(
                            lesson_id=lesson.id,
                            question_text=quiz_data["question_text"],
                            choices=quiz_data["choices"],
                            correct_index=quiz_data["correct_index"],
                            explanation=quiz_data["explanation"],
                        )
                    )

            source_docs = []
            for doc_data in track_data["source_documents"]:
                doc = SourceDocument(
                    track_id=track.id,
                    title=doc_data["title"],
                    source_name=doc_data["source_name"],
                    url=doc_data["url"],
                    body_text=doc_data["body_text"],
                )
                db.add(doc)
                source_docs.append(doc)

            db.commit()

            for doc in source_docs:
                db.refresh(doc)
                ingest_source_document(doc)
                print(f"Ingested source document '{doc.title}' into Chroma.")

            print(f"Seeded track '{track.slug}'.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
