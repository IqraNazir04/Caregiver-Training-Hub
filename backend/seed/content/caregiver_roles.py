"""Seed content for the Caregiver Roles & Boundaries track.

Written as plausible caregiving guidance in the style of AARP/NIA caregiving materials for
demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted, properly
licensed source text before any real-world use.
"""

TRACK = {
    "slug": "caregiver-roles-boundaries",
    "name": "Caregiver Roles & Boundaries",
    "theme": "foundational",
    "description": "Understand what you're responsible for as a caregiver, what needs professional help, and how to set sustainable boundaries.",
    "lessons": [
        {
            "title": "What's yours to carry (and what isn't)",
            "estimated_minutes": 4,
            "body_markdown": (
                "## You are not the whole care team\n\n"
                "Family caregivers often take on tasks — medical decisions, physical care, "
                "medication management — that were never meant to be handled alone. Identify "
                "which tasks genuinely require your involvement and which are better handled, "
                "or shared, with a home health aide, nurse, or therapist.\n\n"
                "## A simple test\n\n"
                "Ask: does this task require clinical training, or does it require someone who "
                "knows and loves this person? Wound care, medication titration, and physical "
                "therapy usually belong with trained professionals. Emotional support, daily "
                "routine, and advocacy usually belong with you.\n\n"
                "## It's okay to say 'that's not something I can do'\n\n"
                "Recognizing a task is outside your ability isn't failure — it's what keeps the "
                "person you're caring for safe."
            ),
            "quiz": [
                {
                    "question_text": "What's a useful test for deciding if a task should be yours or a professional's?",
                    "choices": [
                        "Whether it requires clinical training vs. knowing the person",
                        "Whether you have time that day",
                        "Whether a family member suggests it",
                    ],
                    "correct_index": 0,
                    "explanation": "Tasks requiring clinical training (wound care, medication titration) are generally better handled by trained professionals; tasks requiring personal knowledge of the individual are a natural fit for family caregivers.",
                },
                {
                    "question_text": "What does recognizing a task is outside your ability represent?",
                    "choices": [
                        "A failure as a caregiver",
                        "A way of keeping the person you care for safe",
                        "Something to hide from the care team",
                    ],
                    "correct_index": 1,
                    "explanation": "Acknowledging limits and bringing in professional help is part of responsible caregiving, not a shortcoming.",
                },
            ],
        },
        {
            "title": "Setting boundaries without guilt",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Boundaries protect the relationship\n\n"
                "A boundary might be a set time you're available for calls, tasks you've handed "
                "off to a sibling, or hours you protect for your own work or rest. Boundaries "
                "aren't about caring less — they're what makes caregiving sustainable over "
                "months or years instead of weeks.\n\n"
                "## Saying it clearly\n\n"
                "Try direct, unapologetic language: 'I can help with groceries on Sundays, but "
                "I can't take on weekday appointments too.' Vague boundaries get renegotiated in "
                "the moment; specific ones hold.\n\n"
                "## Expect pushback, and hold anyway\n\n"
                "The person you're caring for, or other family members, may push back on a new "
                "boundary at first. That's common and doesn't mean the boundary was wrong."
            ),
            "quiz": [
                {
                    "question_text": "Why do boundaries matter in caregiving?",
                    "choices": [
                        "They make caregiving sustainable over the long term",
                        "They show you care less about the person",
                        "They're only needed if the caregiver is being asked to do too little",
                    ],
                    "correct_index": 0,
                    "explanation": "Boundaries protect a caregiver's capacity so they can keep showing up over months or years, not just in an initial burst.",
                },
                {
                    "question_text": "What kind of boundary language tends to hold up best?",
                    "choices": [
                        "Vague and flexible, decided in the moment",
                        "Specific and stated clearly ahead of time",
                        "Left unsaid and hoped for",
                    ],
                    "correct_index": 1,
                    "explanation": "Specific, clearly stated boundaries are less likely to be renegotiated in a stressful moment than vague ones.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Understanding Your Role as a Family Caregiver",
            "source_name": "AARP Caregiving Resource Center (sample/seed content)",
            "url": "https://www.aarp.org/caregiving/basics/",
            "body_text": (
                "Family caregivers frequently take on tasks that go beyond what's realistic for "
                "one person to manage alone. A useful way to decide what belongs to you versus "
                "the broader care team is to ask whether a task requires clinical training — such "
                "as wound care or adjusting medication doses — or whether it requires someone who "
                "knows the person's history, preferences, and daily patterns. Clinical tasks are "
                "usually better handled by a trained professional; personal and relational tasks "
                "are a natural fit for family involvement.\n\n"
                "Recognizing when a task is outside your ability is not a failure. It is part of "
                "responsible caregiving, and it helps keep the person you are caring for safe."
            ),
        },
        {
            "title": "Setting Sustainable Boundaries as a Caregiver",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/caregiving/taking-care-yourself-tips-caregivers",
            "body_text": (
                "Boundaries are a normal and necessary part of long-term caregiving. A boundary "
                "might be a specific time window you're available for calls, a task you've handed "
                "off to another family member, or hours protected for rest or work. Boundaries do "
                "not mean caring less — they are what allows caregiving to continue over months "
                "or years rather than burning out in weeks.\n\n"
                "Clear, specific boundaries tend to hold up better than vague ones. Saying 'I can "
                "help with groceries on Sundays, but not weekday appointments' is easier to "
                "maintain than an open-ended offer to help 'whenever needed.' Expect some pushback "
                "when a new boundary is introduced — that reaction is common and does not mean the "
                "boundary was the wrong call."
            ),
        },
    ],
}
