"""Seed content for the Mobility Assistance & Fall Prevention track.

Written as plausible caregiving guidance in the style of NIA/CDC fall-prevention materials for
demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted, properly
licensed source text before any real-world use.
"""

TRACK = {
    "slug": "mobility-fall-prevention",
    "name": "Mobility Assistance & Fall Prevention",
    "theme": "practical-skills",
    "description": "Practical techniques for helping someone move safely and reducing fall risk around the home.",
    "lessons": [
        {
            "title": "Assisting with safe movement",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Let them lead, support the rest\n\n"
                "Encourage the person to do as much of the movement as they safely can — this "
                "preserves strength and confidence over time. Support balance and provide backup, "
                "rather than lifting or moving them entirely.\n\n"
                "## Protect your own back\n\n"
                "Bend at your knees, not your waist, when assisting with transfers, and keep the "
                "person close to your body. If a transfer regularly feels physically unsafe for "
                "you to do alone, that's a sign to bring in equipment (a gait belt, transfer "
                "board) or additional help.\n\n"
                "## Use consistent verbal cues\n\n"
                "Simple, consistent phrases — 'ready, and stand' — help the person anticipate and "
                "participate in the movement instead of being surprised by it."
            ),
            "quiz": [
                {
                    "question_text": "Why encourage the person to do as much of a movement as they safely can?",
                    "choices": [
                        "It's faster for the caregiver",
                        "It preserves their strength and confidence over time",
                        "It's required by most care plans",
                    ],
                    "correct_index": 1,
                    "explanation": "Letting someone do what they safely can, rather than doing everything for them, helps maintain their mobility and confidence longer.",
                },
                {
                    "question_text": "What should a caregiver do to protect their own back during transfers?",
                    "choices": [
                        "Bend at the waist to get closer",
                        "Bend at the knees and keep the person close to their body",
                        "Lift as quickly as possible",
                    ],
                    "correct_index": 1,
                    "explanation": "Bending at the knees rather than the waist, and keeping the person close, reduces strain on the caregiver's back during a transfer.",
                },
            ],
        },
        {
            "title": "Reducing fall risk at home",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Clear the paths, not just the room\n\n"
                "Walk the actual routes used daily — bedroom to bathroom, chair to kitchen — and "
                "clear cords, rugs, and clutter specifically along those paths, not just general "
                "tidying.\n\n"
                "## Lighting matters more than it seems\n\n"
                "Falls often happen at night. Night-lights along the bedroom-to-bathroom path and "
                "easy-to-reach light switches reduce risk significantly.\n\n"
                "## Footwear and grab bars\n\n"
                "Non-slip, supportive footwear (not just socks or loose slippers) and grab bars "
                "near the toilet and shower address two of the most common fall locations in the "
                "home."
            ),
            "quiz": [
                {
                    "question_text": "What's a more effective approach to reducing fall risk than general tidying?",
                    "choices": [
                        "Clearing the specific paths used daily, like bedroom to bathroom",
                        "Rearranging furniture every week",
                        "Removing all furniture from the home",
                    ],
                    "correct_index": 0,
                    "explanation": "Walking and clearing the actual daily-use paths targets where falls are most likely to happen, more effectively than general cleanup.",
                },
                {
                    "question_text": "Where are grab bars most commonly recommended?",
                    "choices": [
                        "In the kitchen only",
                        "Near the toilet and shower",
                        "By the front door only",
                    ],
                    "correct_index": 1,
                    "explanation": "The bathroom — especially near the toilet and shower — is one of the most common locations for falls, making grab bars there particularly valuable.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Assisting with Safe Movement and Transfers",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/safety/fall-prevention-older-adults",
            "body_text": (
                "When assisting someone with movement, encouraging them to do as much of the "
                "movement as they can safely manage helps preserve their strength and confidence "
                "over time, with the caregiver supporting balance rather than lifting them "
                "entirely. Caregivers should bend at the knees rather than the waist during "
                "transfers and keep the person close to their body to protect their own back. If a "
                "transfer regularly feels physically unsafe to do alone, that's a signal to bring "
                "in equipment such as a gait belt or transfer board, or additional help.\n\n"
                "Simple, consistent verbal cues before a movement — such as a short countdown — "
                "help the person anticipate and actively participate rather than being caught off "
                "guard."
            ),
        },
        {
            "title": "Reducing Fall Risk in the Home",
            "source_name": "CDC STEADI Initiative (sample/seed content)",
            "url": "https://www.cdc.gov/steadi/patient-materials/index.html",
            "body_text": (
                "Falls are more effectively prevented by clearing the specific paths used daily — "
                "such as bedroom to bathroom — of cords, rugs, and clutter, rather than general "
                "tidying alone. Since many falls happen at night, night-lights along frequently "
                "used paths and easily reachable light switches meaningfully reduce risk.\n\n"
                "Non-slip, supportive footwear rather than loose slippers or socks, along with "
                "grab bars near the toilet and shower, address two of the most common fall "
                "scenarios in the home."
            ),
        },
    ],
}
