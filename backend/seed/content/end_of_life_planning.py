"""Seed content for the End-of-Life Conversations & Planning track.

Written as plausible caregiving guidance in the style of NIA/National Hospice and Palliative Care
Organization materials for demo/seed purposes — not scraped or verbatim from those sources.
Replace with vetted, properly licensed source text before any real-world use.
"""

TRACK = {
    "slug": "end-of-life-planning",
    "name": "End-of-Life Conversations & Planning",
    "theme": "family-logistics",
    "description": "Approaching end-of-life conversations and planning with care — for both practical clarity and peace of mind.",
    "lessons": [
        {
            "title": "Starting the conversation",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Earlier is easier than later\n\n"
                "These conversations are almost always easier before a crisis forces them, when "
                "there's room to talk without an urgent decision pressing down on the "
                "conversation. Waiting for the 'right moment' often means it never happens until "
                "it's forced.\n\n"
                "## Ask about values before specifics\n\n"
                "'What matters most to you if things get harder' opens more honest conversation "
                "than jumping straight to specific medical scenarios. Values often make the "
                "specific decisions clearer later.\n\n"
                "## It's normal for this to feel hard\n\n"
                "Discomfort talking about death doesn't mean you're doing it wrong. Starting "
                "small — even a single honest conversation — matters more than having a perfect, "
                "comprehensive discussion all at once."
            ),
            "quiz": [
                {
                    "question_text": "Why are end-of-life conversations generally easier earlier rather than later?",
                    "choices": [
                        "There's room to talk without an urgent decision forcing the pace",
                        "They're actually easier during a medical crisis",
                        "Timing doesn't matter",
                    ],
                    "correct_index": 0,
                    "explanation": "Having the conversation before a crisis allows for a calmer, more thoughtful discussion rather than one made under acute pressure.",
                },
                {
                    "question_text": "What's a good way to open an end-of-life conversation?",
                    "choices": [
                        "Jumping straight into specific medical scenarios",
                        "Asking about what matters most to the person if things get harder",
                        "Avoiding the topic entirely until forced",
                    ],
                    "correct_index": 1,
                    "explanation": "Starting with values tends to open a more honest conversation and makes specific decisions easier to navigate later.",
                },
            ],
        },
        {
            "title": "Turning the conversation into a plan",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Document what's discussed\n\n"
                "A conversation that isn't written down can be hard to recall accurately, "
                "especially under stress later. Advance directives and healthcare proxy documents "
                "translate the conversation into something the care team can actually act on.\n\n"
                "## Hospice and palliative care are not the same thing\n\n"
                "Palliative care focuses on comfort and can happen alongside curative treatment at "
                "any stage of illness. Hospice specifically supports comfort-focused care when "
                "curative treatment is no longer the goal. Knowing the difference helps these "
                "options come up as choices, not just a last resort.\n\n"
                "## Revisit the plan, don't treat it as permanent\n\n"
                "Wishes can change as circumstances change. Treating the plan as something to "
                "revisit periodically, not a one-time document, keeps it aligned with what the "
                "person actually wants over time."
            ),
            "quiz": [
                {
                    "question_text": "Why document end-of-life wishes rather than relying on a remembered conversation?",
                    "choices": [
                        "A conversation that isn't written down can be hard to recall accurately under stress later",
                        "Documentation isn't actually useful",
                        "It's only needed for legal reasons, not medical ones",
                    ],
                    "correct_index": 0,
                    "explanation": "Written documents like advance directives give the care team something concrete to act on, rather than relying on memory during a stressful moment.",
                },
                {
                    "question_text": "What's a key difference between palliative care and hospice?",
                    "choices": [
                        "They're the same thing with different names",
                        "Palliative care can happen alongside curative treatment; hospice is for when curative treatment is no longer the goal",
                        "Hospice is only for a specific illness",
                    ],
                    "correct_index": 1,
                    "explanation": "Palliative care focuses on comfort at any stage of illness, including alongside treatment, while hospice specifically supports comfort-focused care once curative treatment is no longer being pursued.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Starting End-of-Life Conversations Early",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/end-life/advance-care-planning-healthcare-directives",
            "body_text": (
                "End-of-life conversations are almost always easier when they happen before a "
                "crisis forces them, allowing room to talk without an urgent decision pressing "
                "down on the discussion. Asking about what matters most to a person if things get "
                "harder, rather than starting with specific medical scenarios, tends to open a "
                "more honest conversation and makes later decisions clearer, since they can be "
                "grounded in expressed values.\n\n"
                "Discomfort discussing these topics is common and doesn't mean it's being done "
                "wrong — starting with even one honest conversation matters more than attempting a "
                "perfect, comprehensive discussion all at once."
            ),
        },
        {
            "title": "From Conversation to Plan: Documentation, Palliative Care, and Hospice",
            "source_name": "National Hospice and Palliative Care Organization (sample/seed content)",
            "url": "https://www.nhpco.org/patients-and-caregivers/",
            "body_text": (
                "A conversation about end-of-life wishes that isn't documented can be difficult to "
                "recall accurately under stress later. Advance directives and healthcare proxy "
                "documents translate the conversation into something a care team can act on "
                "directly. Palliative care focuses on comfort and can be provided alongside "
                "curative treatment at any stage of illness, while hospice specifically supports "
                "comfort-focused care once curative treatment is no longer the goal — "
                "understanding this distinction helps both options be considered as genuine "
                "choices rather than a last resort.\n\n"
                "Because wishes can change as circumstances change, a plan benefits from being "
                "revisited periodically rather than treated as a single, permanent document."
            ),
        },
    ],
}
