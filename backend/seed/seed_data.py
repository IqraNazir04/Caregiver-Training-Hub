"""Idempotent seed script: loads seed tracks/lessons/quizzes into SQL and embeds source docs into Chroma.

Run with: python -m seed.seed_data
"""

from app.database import Base, SessionLocal, engine
from app.models import Lesson, QuizQuestion, SourceDocument, Track
from app.rag.ingest import ingest_source_document
from seed.content import (
    basic_first_aid,
    boundaries_with_family,
    building_support_network,
    caregiver_roles,
    communicating_cognitive_decline,
    coordinating_family_care,
    daily_routine,
    deescalating_agitation,
    dementia,
    diabetes,
    end_of_life_planning,
    legal_financial_basics,
    managing_guilt_grief,
    medication_management,
    mobility_fall_prevention,
    nutrition_meal_planning,
    planning_respite_care,
    post_stroke,
    realistic_self_care,
    recognizing_burnout,
    talking_to_doctors,
    warning_signs,
)

ALL_TRACKS = [
    # Foundational / Getting Started
    dementia.TRACK,
    diabetes.TRACK,
    post_stroke.TRACK,
    caregiver_roles.TRACK,
    daily_routine.TRACK,
    # Practical Skills
    medication_management.TRACK,
    warning_signs.TRACK,
    basic_first_aid.TRACK,
    mobility_fall_prevention.TRACK,
    nutrition_meal_planning.TRACK,
    # Communication & Behavior
    deescalating_agitation.TRACK,
    communicating_cognitive_decline.TRACK,
    talking_to_doctors.TRACK,
    boundaries_with_family.TRACK,
    # Emotional & Mental Load
    recognizing_burnout.TRACK,
    managing_guilt_grief.TRACK,
    building_support_network.TRACK,
    realistic_self_care.TRACK,
    # Family & Logistics
    coordinating_family_care.TRACK,
    legal_financial_basics.TRACK,
    planning_respite_care.TRACK,
    end_of_life_planning.TRACK,
]


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
                theme=track_data.get("theme", "foundational"),
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
