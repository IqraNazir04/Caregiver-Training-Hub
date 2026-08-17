"""Seed content for the Realistic Self-Care track.

Written as plausible caregiving guidance in the style of NIA/AARP caregiver-wellbeing materials
for demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted,
properly licensed source text before any real-world use.
"""

TRACK = {
    "slug": "realistic-self-care",
    "name": "Realistic Self-Care (Not Spa-Day Advice)",
    "theme": "emotional-mental-load",
    "description": "Self-care that fits into an actual caregiving schedule — small, repeatable resets instead of advice that assumes free time you don't have.",
    "lessons": [
        {
            "title": "Why the usual self-care advice doesn't fit",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Most self-care advice assumes free time\n\n"
                "Vacations, spa days, and hour-long workouts are the default image of self-care, "
                "but they assume a spare block of time and money many caregivers don't have. That "
                "gap is often why self-care advice feels unhelpful or even irritating rather than "
                "useful.\n\n"
                "## Small and frequent beats big and rare\n\n"
                "A 10-minute reset that happens most days does more for sustained wellbeing than a "
                "once-a-year vacation that requires massive planning to make happen at all.\n\n"
                "## Self-care isn't selfish\n\n"
                "Caregivers often feel guilty prioritizing their own needs. But a caregiver running "
                "on empty provides worse care, not more devoted care — maintaining yourself is "
                "part of maintaining the care you provide."
            ),
            "quiz": [
                {
                    "question_text": "Why does typical self-care advice (spa days, vacations) often not work for caregivers?",
                    "choices": [
                        "It assumes free time and resources many caregivers don't have",
                        "Caregivers don't deserve self-care",
                        "It's always bad advice for everyone",
                    ],
                    "correct_index": 0,
                    "explanation": "Advice built around large blocks of free time often doesn't match the reality of a caregiver's schedule, which is why it can feel unhelpful.",
                },
                {
                    "question_text": "What tends to work better for sustained wellbeing?",
                    "choices": [
                        "A once-a-year vacation",
                        "Small, frequent resets that happen most days",
                        "Waiting until burnout forces a change",
                    ],
                    "correct_index": 1,
                    "explanation": "Small, repeatable practices tend to have more sustained impact than infrequent large gestures that are hard to schedule.",
                },
            ],
        },
        {
            "title": "Building resets that actually fit",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Attach it to something that already happens\n\n"
                "A two-minute breathing pause during medication time, or listening to one song "
                "during a specific daily task, is more likely to actually happen than a "
                "standalone activity that needs to be remembered separately.\n\n"
                "## Lower the bar on purpose\n\n"
                "A realistic goal ('step outside for two minutes') gets done far more often than "
                "an ambitious one ('exercise for 30 minutes') that quietly gets skipped every day "
                "it doesn't happen.\n\n"
                "## Notice what actually restores you\n\n"
                "Not everyone recharges the same way — some people need quiet, some need "
                "connection, some need to move their body. A generic self-care list matters less "
                "than knowing what specifically helps you."
            ),
            "quiz": [
                {
                    "question_text": "Why attach a small self-care moment to something that already happens daily?",
                    "choices": [
                        "It makes the moment take longer",
                        "It's more likely to actually happen than something standalone",
                        "It has no real benefit",
                    ],
                    "correct_index": 1,
                    "explanation": "Anchoring a small practice to an existing routine, similar to habit-building for care tasks, makes it more likely to stick.",
                },
                {
                    "question_text": "Why is a smaller, more achievable goal often better than an ambitious one?",
                    "choices": [
                        "It gets done far more consistently than a goal that quietly gets skipped",
                        "Ambitious goals are always better",
                        "Smaller goals don't count as real self-care",
                    ],
                    "correct_index": 0,
                    "explanation": "A realistic, low-bar goal is more sustainable and actually gets done, compared to an ambitious goal that's easy to skip.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Rethinking Self-Care for Caregivers",
            "source_name": "AARP Caregiving Resource Center (sample/seed content)",
            "url": "https://www.aarp.org/caregiving/life-balance/info-2017/self-care-for-caregivers.html",
            "body_text": (
                "Much of the common self-care advice — vacations, spa days, long workouts — "
                "assumes a spare block of time and money that many caregivers don't have, which is "
                "part of why it often feels unhelpful rather than useful. A short reset that "
                "happens most days tends to do more for sustained wellbeing than an infrequent, "
                "large gesture that requires significant planning.\n\n"
                "Caregivers often feel guilty prioritizing their own needs, but a caregiver running "
                "on empty tends to provide worse care, not more devoted care. Maintaining oneself "
                "is part of maintaining the quality of care provided."
            ),
        },
        {
            "title": "Building Self-Care Habits That Actually Fit",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/caregiving/taking-care-yourself-tips-caregivers",
            "body_text": (
                "Attaching a brief self-care moment to something that already happens daily — such "
                "as a short breathing pause during a routine task — makes it more likely to "
                "actually occur than a standalone activity that needs to be remembered separately. "
                "A realistic, low-effort goal tends to get done far more consistently than an "
                "ambitious one that quietly gets skipped whenever it doesn't happen.\n\n"
                "Not everyone recharges the same way — some people need quiet, others need "
                "connection or movement — so identifying what specifically restores an individual "
                "caregiver matters more than following a generic self-care list."
            ),
        },
    ],
}
