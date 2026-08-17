"""Seed content for the Basic First Aid for Caregivers track.

Written as plausible caregiving guidance in the style of Red Cross/CDC first aid materials for
demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted, properly
licensed source text before any real-world use.
"""

TRACK = {
    "slug": "basic-first-aid-caregivers",
    "name": "Basic First Aid for Caregivers",
    "theme": "practical-skills",
    "description": "Core first aid skills for common at-home incidents — falls, cuts, and choking — while you're waiting for or deciding on further care.",
    "lessons": [
        {
            "title": "Responding to falls and minor injuries",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Don't rush to move someone after a fall\n\n"
                "Check for pain, especially in the hip, wrist, or head, before helping someone up. "
                "Moving too quickly after a fall can turn a minor injury into a serious one if "
                "there's a fracture.\n\n"
                "## Basic wound care\n\n"
                "Clean a minor cut with water, apply gentle pressure with a clean cloth to stop "
                "bleeding, and cover with a bandage. Seek care if bleeding doesn't slow after 10 "
                "minutes of steady pressure, or if the wound is deep, gaping, or from a dirty "
                "object.\n\n"
                "## When a fall needs more than first aid\n\n"
                "Head injury with confusion, loss of consciousness, an obviously deformed limb, or "
                "inability to bear weight after a fall are signs to seek medical evaluation, not "
                "just first aid."
            ),
            "quiz": [
                {
                    "question_text": "What should you check before helping someone up after a fall?",
                    "choices": [
                        "Whether anyone saw them fall",
                        "Pain, especially in the hip, wrist, or head",
                        "How long they were on the ground",
                    ],
                    "correct_index": 1,
                    "explanation": "Checking for pain in these areas first helps avoid worsening a possible fracture by moving someone too quickly.",
                },
                {
                    "question_text": "What's a sign a fall needs medical evaluation beyond first aid?",
                    "choices": [
                        "A small bruise",
                        "Inability to bear weight or a deformed limb",
                        "Feeling embarrassed about falling",
                    ],
                    "correct_index": 1,
                    "explanation": "Inability to bear weight or an obviously deformed limb suggests a possible fracture that needs medical evaluation.",
                },
            ],
        },
        {
            "title": "Choking and when to act fast",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Recognize true choking\n\n"
                "A person who can cough, speak, or breathe is getting some air — encourage "
                "coughing and don't intervene forcefully. A person who cannot cough, speak, or "
                "breathe, or who is making high-pitched sounds, needs immediate action.\n\n"
                "## Abdominal thrusts, if trained\n\n"
                "If you're trained in abdominal thrusts (the Heimlich maneuver), this is the time "
                "to use them. If you're not trained, call 911 immediately and follow the "
                "dispatcher's instructions.\n\n"
                "## After any real choking episode\n\n"
                "Even after an object is dislodged, seek a medical evaluation — internal injury "
                "or a partial obstruction can remain even once someone can breathe and talk again."
            ),
            "quiz": [
                {
                    "question_text": "How can you tell the difference between true choking and a person who is coughing but breathing?",
                    "choices": [
                        "True choking means they can't cough, speak, or breathe",
                        "Any coughing means you should start abdominal thrusts",
                        "Choking always causes loss of consciousness first",
                    ],
                    "correct_index": 0,
                    "explanation": "If someone can still cough, speak, or breathe, they are getting air and should be encouraged to keep coughing rather than receiving forceful intervention.",
                },
                {
                    "question_text": "What should happen after a real choking episode is resolved?",
                    "choices": [
                        "Nothing further is needed once they can breathe again",
                        "Seek a medical evaluation even after the object is dislodged",
                        "Wait a week to see if symptoms return",
                    ],
                    "correct_index": 1,
                    "explanation": "A medical evaluation after a real choking episode can catch internal injury or a remaining partial obstruction that isn't obvious once breathing resumes.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "First Aid Basics for Falls and Minor Wounds",
            "source_name": "American Red Cross (sample/seed content)",
            "url": "https://www.redcross.org/take-a-class/first-aid",
            "body_text": (
                "After a fall, check for pain — especially in the hip, wrist, or head — before "
                "helping someone up, since moving too quickly can worsen a possible fracture. For "
                "minor cuts, clean with water, apply gentle steady pressure with a clean cloth to "
                "control bleeding, and cover with a bandage. Seek medical care if bleeding doesn't "
                "slow after about 10 minutes of pressure, or if the wound is deep, gaping, or came "
                "from a dirty object.\n\n"
                "Signs that a fall needs medical evaluation beyond basic first aid include head "
                "injury with confusion, loss of consciousness, an obviously deformed limb, or "
                "inability to bear weight."
            ),
        },
        {
            "title": "Responding to a Choking Emergency",
            "source_name": "CDC (sample/seed content)",
            "url": "https://www.cdc.gov/aging/caregiving/index.html",
            "body_text": (
                "A person who can still cough, speak, or breathe is getting some air and should be "
                "encouraged to keep coughing rather than receiving forceful intervention. Someone "
                "who cannot cough, speak, or breathe, or who is making high-pitched sounds, needs "
                "immediate action — abdominal thrusts if you are trained, or an immediate call to "
                "911 with the dispatcher's guidance if you are not.\n\n"
                "Even after a choking episode resolves and the person can breathe and talk again, "
                "a medical evaluation is still recommended, since internal injury or a partial "
                "obstruction can remain."
            ),
        },
    ],
}
