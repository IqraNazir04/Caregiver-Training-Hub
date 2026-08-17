"""Seed content for the De-escalating Agitation or Confusion track.

Written as plausible caregiving guidance in the style of NIA/Alzheimer's Association materials
for demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted,
properly licensed source text before any real-world use.
"""

TRACK = {
    "slug": "deescalating-agitation-confusion",
    "name": "De-escalating Agitation or Confusion",
    "theme": "communication-behavior",
    "description": "Techniques for calming moments of agitation or confusion, especially relevant for dementia and mental health caregiving.",
    "lessons": [
        {
            "title": "Understanding what's behind the behavior",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Agitation is usually communication\n\n"
                "Agitation often signals an unmet need — pain, hunger, fatigue, overstimulation, "
                "or confusion about surroundings — rather than defiance. Looking for the trigger "
                "is more productive than responding to the behavior alone.\n\n"
                "## Rule out the physical first\n\n"
                "Before assuming a behavioral or emotional cause, check for physical discomfort: "
                "pain, a full bladder, hunger, or being too hot or cold are common and fixable "
                "triggers that are easy to miss.\n\n"
                "## Your calm is contagious — so is your tension\n\n"
                "People in a confused or agitated state often pick up on a caregiver's tone and "
                "body language even when they can't follow the words. Slowing down your own "
                "breathing and voice can de-escalate a moment before you say anything specific."
            ),
            "quiz": [
                {
                    "question_text": "What does agitated behavior often signal?",
                    "choices": [
                        "Deliberate defiance",
                        "An unmet need such as pain, hunger, or overstimulation",
                        "Nothing meaningful — it's random",
                    ],
                    "correct_index": 1,
                    "explanation": "Agitation is frequently a form of communication about an unmet need rather than intentional defiance.",
                },
                {
                    "question_text": "What should be checked first when agitation appears?",
                    "choices": [
                        "Physical causes like pain, hunger, or needing the bathroom",
                        "Whether the TV is too loud",
                        "The weather forecast",
                    ],
                    "correct_index": 0,
                    "explanation": "Physical discomfort is a common and often overlooked trigger that's worth ruling out before assuming an emotional or behavioral cause.",
                },
            ],
        },
        {
            "title": "In-the-moment de-escalation",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Don't argue with the reality they're experiencing\n\n"
                "Correcting someone mid-agitation ('that's not true,' 'you're wrong') tends to "
                "escalate, not calm. Validate the emotion first — 'that sounds frustrating' — "
                "before addressing the facts, if at all.\n\n"
                "## Reduce stimulation\n\n"
                "Turn down noise, dim harsh lighting, and reduce the number of people or "
                "activities happening at once. A simpler environment is often calming on its own.\n\n"
                "## Redirect instead of confronting\n\n"
                "Shifting attention to a different activity or topic is often more effective than "
                "continuing to address the source of agitation directly, especially with cognitive "
                "decline."
            ),
            "quiz": [
                {
                    "question_text": "What tends to escalate agitation rather than calm it?",
                    "choices": [
                        "Validating the person's emotion first",
                        "Arguing or correcting facts mid-agitation",
                        "Reducing background noise",
                    ],
                    "correct_index": 1,
                    "explanation": "Correcting or arguing during an agitated moment tends to increase distress rather than resolve it.",
                },
                {
                    "question_text": "What's often more effective than continuing to confront the source of agitation directly?",
                    "choices": [
                        "Redirecting attention to a different activity",
                        "Repeating the same correction more firmly",
                        "Leaving the room without explanation",
                    ],
                    "correct_index": 0,
                    "explanation": "Redirecting to a different activity or topic often de-escalates more effectively than continued direct confrontation, especially with cognitive decline.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Understanding the Causes of Agitation",
            "source_name": "Alzheimer's Association (sample/seed content)",
            "url": "https://www.alz.org/help-support/caregiving/stages-behaviors/agitation-anxiety",
            "body_text": (
                "Agitated behavior often communicates an unmet need — such as pain, hunger, "
                "fatigue, overstimulation, or confusion about surroundings — rather than "
                "deliberate defiance. Before assuming a behavioral or emotional cause, it's worth "
                "checking for physical discomfort, since pain, a full bladder, hunger, or being too "
                "hot or cold are common and easily overlooked triggers.\n\n"
                "A caregiver's own tone and body language are often picked up by someone in a "
                "confused or agitated state even when the words aren't fully understood. Slowing "
                "down one's own breathing and voice can help de-escalate a moment before any "
                "specific words are exchanged."
            ),
        },
        {
            "title": "De-escalation Techniques in the Moment",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/alzheimers-caregiving/managing-personality-and-behavior-changes-alzheimers",
            "body_text": (
                "Correcting or arguing with someone during an agitated moment tends to escalate "
                "distress rather than resolve it. Validating the emotion first, before addressing "
                "the underlying facts if at all, is generally more effective. Reducing "
                "environmental stimulation — turning down noise, dimming harsh lighting, and "
                "limiting the number of people or activities happening at once — can also have a "
                "calming effect on its own.\n\n"
                "Redirecting attention to a different activity or topic is often more effective "
                "than continuing to address the source of agitation directly, particularly for "
                "someone experiencing cognitive decline."
            ),
        },
    ],
}
