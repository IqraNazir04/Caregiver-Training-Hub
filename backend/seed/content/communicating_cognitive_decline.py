"""Seed content for the Communicating with Cognitive Decline track.

Written as plausible caregiving guidance in the style of NIA/Alzheimer's Association materials
for demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted,
properly licensed source text before any real-world use.
"""

TRACK = {
    "slug": "communicating-cognitive-decline",
    "name": "Communicating with Cognitive Decline",
    "theme": "communication-behavior",
    "description": "Ongoing communication strategies for a loved one experiencing memory loss or cognitive decline, beyond a single conversation.",
    "lessons": [
        {
            "title": "Adjusting how you communicate over time",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Meet them at their current level, not the past one\n\n"
                "Communication needs change as cognitive decline progresses. A strategy that "
                "worked six months ago — longer conversations, more complex choices — may need to "
                "be simplified further. Reassess periodically rather than assuming what worked "
                "before still works now.\n\n"
                "## Offer choices, not open questions\n\n"
                "'What do you want to wear?' can be overwhelming. 'The blue shirt or the green "
                "one?' is easier to answer and preserves a sense of control without requiring "
                "open-ended recall.\n\n"
                "## Nonverbal communication carries more weight over time\n\n"
                "As verbal understanding becomes harder, tone of voice, facial expression, and "
                "touch (when welcomed) carry more of the message than the specific words used."
            ),
            "quiz": [
                {
                    "question_text": "Why is it important to reassess communication strategies periodically?",
                    "choices": [
                        "Communication needs can change as cognitive decline progresses",
                        "It's required documentation for care plans",
                        "Strategies should change every day regardless of need",
                    ],
                    "correct_index": 0,
                    "explanation": "What worked at an earlier stage may become too complex later on, so strategies benefit from periodic reassessment rather than staying fixed.",
                },
                {
                    "question_text": "Why do limited-choice questions ('the blue or the green shirt?') often work better than open questions?",
                    "choices": [
                        "They're faster to ask",
                        "They're easier to answer and still preserve a sense of control",
                        "They avoid the need for any response at all",
                    ],
                    "correct_index": 1,
                    "explanation": "A limited choice reduces the cognitive load of an open-ended question while still letting the person make a real decision.",
                },
            ],
        },
        {
            "title": "Staying connected as words become harder",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Enter their reality instead of correcting it\n\n"
                "If someone asks for a parent who has passed away, redirecting gently ('tell me "
                "about her') is often kinder and more effective than repeatedly explaining the "
                "loss, which can cause them to re-experience grief each time.\n\n"
                "## Use familiar routines as communication anchors\n\n"
                "Music, old photos, and familiar routines can open connection even when "
                "conversation itself has become difficult, tapping into memory that's preserved "
                "differently than recent recall.\n\n"
                "## Presence still matters when words don't land\n\n"
                "Sitting with someone, holding a hand, or simply being present communicates care "
                "even in advanced stages where verbal exchange is very limited."
            ),
            "quiz": [
                {
                    "question_text": "If someone asks for a deceased parent, what's often the kinder approach?",
                    "choices": [
                        "Repeatedly explaining that the parent has passed away",
                        "Gently redirecting, like asking them to talk about that person",
                        "Ignoring the question entirely",
                    ],
                    "correct_index": 1,
                    "explanation": "Gently redirecting avoids causing the person to re-experience grief repeatedly, which can happen if the loss is re-explained each time it's asked about.",
                },
                {
                    "question_text": "What can serve as a communication anchor when conversation becomes difficult?",
                    "choices": [
                        "Music, old photos, and familiar routines",
                        "Complex new topics to keep them engaged",
                        "Correcting factual errors in what they say",
                    ],
                    "correct_index": 0,
                    "explanation": "Familiar, sensory, and routine-based connections can open communication in ways that direct conversation may no longer support.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Adjusting Communication as Cognitive Decline Progresses",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/alzheimers-caregiving/tips-communicating-person-alzheimers-disease",
            "body_text": (
                "Communication needs change as cognitive decline progresses, and a strategy that "
                "worked at an earlier stage may need to be simplified over time rather than "
                "assumed to still be effective. Offering a limited choice, such as between two "
                "specific items, is often easier to answer than an open-ended question and still "
                "preserves a sense of control.\n\n"
                "As verbal understanding becomes more difficult, nonverbal communication — tone of "
                "voice, facial expression, and welcomed touch — carries an increasing share of the "
                "message relative to the specific words used."
            ),
        },
        {
            "title": "Staying Connected Through Memory Loss",
            "source_name": "Alzheimer's Association (sample/seed content)",
            "url": "https://www.alz.org/help-support/caregiving/daily-care/communications",
            "body_text": (
                "When someone with memory loss asks for a person who has passed away, gently "
                "redirecting the conversation is often kinder than repeatedly explaining the loss, "
                "which can cause the person to re-experience grief each time. Familiar routines, "
                "music, and old photographs can open connection even when direct conversation has "
                "become difficult, tapping into memory that is often preserved differently than "
                "recent recall.\n\n"
                "In more advanced stages, simple presence — sitting together, holding a hand — "
                "continues to communicate care even when verbal exchange is very limited."
            ),
        },
    ],
}
