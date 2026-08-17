"""Seed content for the Medication Management & Tracking track.

Written as plausible caregiving guidance in the style of NIA/FDA caregiving materials for
demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted, properly
licensed source text before any real-world use.
"""

TRACK = {
    "slug": "medication-management-tracking",
    "name": "Medication Management & Tracking",
    "theme": "practical-skills",
    "description": "Build a reliable system for tracking medications, doses, and timing so nothing gets missed or doubled up.",
    "lessons": [
        {
            "title": "Setting up a medication system",
            "estimated_minutes": 5,
            "body_markdown": (
                "## One list, not several\n\n"
                "Keep a single master list of every medication, including over-the-counter drugs "
                "and supplements, with dose, timing, and purpose. Multiple partial lists — one at "
                "home, one at the pharmacy, one in someone's head — are how doses get missed or "
                "duplicated.\n\n"
                "## Pill organizers reduce errors, not eliminate them\n\n"
                "A weekly pill organizer helps catch missed doses at a glance, but it doesn't "
                "replace checking the label when refilling it. Refill the organizer at the same "
                "time each week so it becomes part of the routine, not an extra task to remember.\n\n"
                "## Keep the list with the person, not just at home\n\n"
                "A current medication list should go to every appointment and to the ER if needed. "
                "Photograph it on your phone as a backup."
            ),
            "quiz": [
                {
                    "question_text": "Why is a single master medication list better than several partial ones?",
                    "choices": [
                        "It's required by pharmacies",
                        "Partial lists are how doses get missed or duplicated",
                        "It takes less time to write",
                    ],
                    "correct_index": 1,
                    "explanation": "When information is split across several lists or memories, it becomes easy for a dose to be missed or accidentally repeated.",
                },
                {
                    "question_text": "What should go with the medication list to every appointment?",
                    "choices": [
                        "Nothing — the doctor already has it on file",
                        "A current, up-to-date version of the list",
                        "Only the prescriptions started that month",
                    ],
                    "correct_index": 1,
                    "explanation": "A current list at every appointment (and in an emergency) ensures providers are working from accurate information.",
                },
            ],
        },
        {
            "title": "Catching interactions and errors early",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Use one pharmacy when possible\n\n"
                "Filling all prescriptions at the same pharmacy lets their system flag "
                "interactions automatically. Splitting prescriptions across pharmacies removes "
                "that safety net.\n\n"
                "## Watch for the same drug under two names\n\n"
                "Generic and brand names can make it look like two different medications are "
                "being taken when it's really one, doubling the dose. When in doubt, check with "
                "the pharmacist.\n\n"
                "## Review the full list at every visit\n\n"
                "Ask the doctor or pharmacist to review the complete list, not just what they "
                "prescribed, at each visit — this is when duplicate therapies and unnecessary "
                "medications are most often caught."
            ),
            "quiz": [
                {
                    "question_text": "Why does using one pharmacy help catch medication problems?",
                    "choices": [
                        "It's cheaper",
                        "Their system can automatically flag interactions across all prescriptions",
                        "It's required by insurance",
                    ],
                    "correct_index": 1,
                    "explanation": "A single pharmacy has visibility into the full medication list and can flag interactions that a split system would miss.",
                },
                {
                    "question_text": "What's a risk of not recognizing a drug's brand and generic name are the same medication?",
                    "choices": [
                        "Accidentally taking a double dose",
                        "Paying a higher co-pay",
                        "Nothing significant",
                    ],
                    "correct_index": 0,
                    "explanation": "If a brand-name and generic version of the same drug are both listed as separate medications, it can lead to an unintentional double dose.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Building a Reliable Medication Tracking System",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/safe-use-medicines/taking-medicines-safely-you-age",
            "body_text": (
                "A single, current master list of every medication — including over-the-counter "
                "drugs and supplements — with dose, timing, and purpose reduces the risk of missed "
                "or duplicated doses compared to keeping information split across multiple partial "
                "lists. Weekly pill organizers help catch missed doses at a glance, but should be "
                "refilled by checking the original label each time rather than from memory.\n\n"
                "This list should travel with the person to every medical appointment and be "
                "available in an emergency, since providers can only work from information they "
                "actually have in front of them."
            ),
        },
        {
            "title": "Avoiding Medication Interactions and Duplication",
            "source_name": "FDA Consumer Updates (sample/seed content)",
            "url": "https://www.fda.gov/drugs/special-features/medication-safety-tips-caregivers",
            "body_text": (
                "Filling all prescriptions at a single pharmacy allows their system to "
                "automatically screen for interactions across the full medication list — a safety "
                "check that is lost when prescriptions are split across multiple pharmacies. "
                "Caregivers should also be alert to a medication appearing under both its brand and "
                "generic name, which can look like two separate drugs and lead to an accidental "
                "double dose.\n\n"
                "Reviewing the complete medication list, not just newly prescribed drugs, at every "
                "medical visit is one of the most effective ways to catch duplicate therapies or "
                "medications that are no longer needed."
            ),
        },
    ],
}
