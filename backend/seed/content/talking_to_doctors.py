"""Seed content for the Talking to Doctors — Advocating Effectively track.

Written as plausible caregiving guidance in the style of AHRQ/AARP patient-advocacy materials for
demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted, properly
licensed source text before any real-world use.
"""

TRACK = {
    "slug": "talking-to-doctors",
    "name": "Talking to Doctors — Advocating Effectively",
    "theme": "communication-behavior",
    "description": "Make the most of short appointment windows and advocate effectively for the person you're caring for.",
    "lessons": [
        {
            "title": "Preparing before the appointment",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Lead with the most important concern\n\n"
                "In a short appointment, the first thing mentioned tends to get the most "
                "attention. Write down concerns in priority order beforehand so the most "
                "important one doesn't get raised in the last 30 seconds.\n\n"
                "## Bring specifics, not impressions\n\n"
                "'Worse lately' is harder to act on than 'fell twice this week, hasn't fallen in "
                "the two months before that.' Specific, dated observations are more useful to a "
                "doctor than general impressions.\n\n"
                "## Know what you're hoping to leave with\n\n"
                "A referral, a medication change, a test, clarity on a diagnosis — knowing your "
                "goal for the visit helps keep the conversation focused if time runs short."
            ),
            "quiz": [
                {
                    "question_text": "Why write concerns down in priority order before an appointment?",
                    "choices": [
                        "So the most important concern doesn't get raised too late to be addressed",
                        "Doctors require a written list",
                        "It makes the appointment take longer",
                    ],
                    "correct_index": 0,
                    "explanation": "Short appointments mean the first concern raised often gets the most attention, so leading with the priority issue matters.",
                },
                {
                    "question_text": "Which is more useful to bring to an appointment?",
                    "choices": [
                        "A general impression, like 'seems worse lately'",
                        "Specific, dated observations, like 'fell twice this week'",
                        "No information — let the doctor ask everything",
                    ],
                    "correct_index": 1,
                    "explanation": "Specific, dated observations give a doctor something concrete and actionable, unlike a vague general impression.",
                },
            ],
        },
        {
            "title": "Advocating during and after the visit",
            "estimated_minutes": 5,
            "body_markdown": (
                "## It's okay to ask for a repeat or plain-language explanation\n\n"
                "Medical explanations move fast. Asking 'can you explain that in a different way' "
                "or 'can you repeat that so I can write it down' isn't a burden to the provider — "
                "it's part of getting useful information out of the visit.\n\n"
                "## Push gently on vague answers\n\n"
                "If a plan sounds vague ('let's keep an eye on it'), it's reasonable to ask what "
                "specifically would prompt the next step, and when to check back in.\n\n"
                "## Write down what was decided before you leave the room\n\n"
                "Memory fades fast after a stressful appointment. Confirm and write down next "
                "steps, medication changes, and follow-up timing before leaving, rather than "
                "trying to recall it later."
            ),
            "quiz": [
                {
                    "question_text": "What's a reasonable thing to ask if a doctor's explanation moves too fast?",
                    "choices": [
                        "Nothing — it's better not to interrupt",
                        "To repeat it or explain it a different way",
                        "To end the appointment early",
                    ],
                    "correct_index": 1,
                    "explanation": "Asking for a repeat or a plain-language explanation is a normal and useful part of getting real value out of a medical visit.",
                },
                {
                    "question_text": "What's a good response to a vague plan like 'let's keep an eye on it'?",
                    "choices": [
                        "Accept it without follow-up questions",
                        "Ask what specifically would prompt the next step and when to check back",
                        "Assume it means nothing needs to be done",
                    ],
                    "correct_index": 1,
                    "explanation": "Asking for specifics turns a vague plan into something actionable and clarifies what to watch for.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Preparing for a Medical Appointment",
            "source_name": "Agency for Healthcare Research and Quality (sample/seed content)",
            "url": "https://www.ahrq.gov/patients-consumers/patient-involvement/index.html",
            "body_text": (
                "In a short appointment window, the concern raised first tends to receive the most "
                "attention, so writing down concerns in priority order beforehand helps ensure the "
                "most important issue isn't raised too late. Specific, dated observations — such as "
                "the exact number and timing of recent falls — are more actionable for a provider "
                "than general impressions like 'seems worse lately.'\n\n"
                "Knowing what outcome is being hoped for from the visit, such as a referral, "
                "medication change, or test, helps keep the conversation focused if time runs "
                "short."
            ),
        },
        {
            "title": "Advocating Effectively During and After the Visit",
            "source_name": "AARP Caregiving Resource Center (sample/seed content)",
            "url": "https://www.aarp.org/caregiving/health/",
            "body_text": (
                "Asking a provider to repeat information or explain it in plain language is a "
                "normal and useful part of a medical visit, not a burden on the provider. If a "
                "plan sounds vague, it's reasonable to ask what specifically would prompt a next "
                "step and when to follow up.\n\n"
                "Because memory of a stressful appointment fades quickly, writing down what was "
                "decided — next steps, medication changes, and follow-up timing — before leaving "
                "the room is more reliable than trying to recall it later."
            ),
        },
    ],
}
