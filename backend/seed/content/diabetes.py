"""Seed content for the Diabetes Management track.

Written as plausible caregiving guidance in the style of CDC/Mayo Clinic materials for demo/seed
purposes — not scraped or verbatim from those sources. Replace with vetted, properly licensed
source text before any real-world use.
"""

TRACK = {
    "slug": "diabetes-management",
    "theme": "foundational",
    "name": "Diabetes Management",
    "description": "Guidance for caregivers helping someone manage diabetes day to day, including blood sugar monitoring and recognizing highs and lows.",
    "lessons": [
        {
            "title": "Recognizing high and low blood sugar",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Low blood sugar (hypoglycemia)\n\n"
                "Signs include shakiness, sweating, confusion, irritability, and dizziness. If the "
                "person is conscious and able to swallow, give a fast-acting sugar source (juice, "
                "glucose tablets) and recheck blood sugar in 15 minutes.\n\n"
                "## High blood sugar (hyperglycemia)\n\n"
                "Signs include excessive thirst, frequent urination, fatigue, and blurred vision. "
                "Persistent high readings should be reported to the person's care team, along with any "
                "changes in diet, activity, or medication.\n\n"
                "## When to seek emergency care\n\n"
                "If the person is confused, unresponsive, or unable to keep food or liquid down, or if "
                "blood sugar readings are extremely high or low and not improving, seek emergency care "
                "right away."
            ),
            "quiz": [
                {
                    "question_text": "What's an appropriate first response to signs of low blood sugar in a conscious person?",
                    "choices": [
                        "Give a fast-acting sugar source and recheck in 15 minutes",
                        "Have them skip their next meal",
                        "Give them an extra dose of insulin immediately",
                    ],
                    "correct_index": 0,
                    "explanation": "A fast-acting sugar source raises blood sugar quickly; rechecking confirms whether it's back in a safe range.",
                },
                {
                    "question_text": "Which combination of signs should prompt emergency care rather than home management?",
                    "choices": [
                        "Mild thirst and tiredness",
                        "Confusion or unresponsiveness with an extreme blood sugar reading",
                        "Slightly blurred vision after a long day",
                    ],
                    "correct_index": 1,
                    "explanation": "Confusion, unresponsiveness, or extreme readings that aren't improving are signs of a possible emergency.",
                },
            ],
        },
        {
            "title": "Building a daily medication and meal routine",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Consistency helps\n\n"
                "Try to keep meal times, medication times, and activity levels consistent day to day — "
                "this makes blood sugar patterns easier to track and manage.\n\n"
                "## Track patterns, not just single readings\n\n"
                "A single high or low reading matters less than a pattern over several days. Keep a log "
                "of readings alongside meals, activity, and medication timing to share with the care "
                "team.\n\n"
                "## Coordinate with the care team on changes\n\n"
                "Don't adjust medication doses without guidance from the prescribing provider, even if "
                "patterns seem to suggest a change is needed — report the pattern and let them decide."
            ),
            "quiz": [
                {
                    "question_text": "Why is it useful to log blood sugar readings alongside meals and activity?",
                    "choices": [
                        "It has no real benefit beyond a single reading",
                        "It helps identify patterns to share with the care team",
                        "It replaces the need for medication entirely",
                    ],
                    "correct_index": 1,
                    "explanation": "Patterns over time are more informative than isolated readings and help the care team make decisions.",
                },
                {
                    "question_text": "If readings suggest a medication dose might need to change, what should a caregiver do?",
                    "choices": [
                        "Adjust the dose based on their own judgment",
                        "Stop the medication until the next appointment",
                        "Report the pattern to the prescribing provider before changing anything",
                    ],
                    "correct_index": 2,
                    "explanation": "Medication changes should be guided by the prescribing provider, not made independently by a caregiver.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Recognizing and Treating Low and High Blood Sugar",
            "source_name": "CDC (sample/seed content)",
            "url": "https://www.cdc.gov/diabetes/managing/low-high-blood-sugar.html",
            "body_text": (
                "Low blood sugar (hypoglycemia) can cause shakiness, sweating, confusion, irritability, "
                "and dizziness. If the person is conscious and able to swallow safely, give 15 grams of "
                "a fast-acting carbohydrate, such as juice or glucose tablets, and recheck blood sugar "
                "after 15 minutes, repeating if still low.\n\n"
                "High blood sugar (hyperglycemia) often causes excessive thirst, frequent urination, "
                "fatigue, and blurred vision. Persistent high readings should be discussed with the "
                "person's care team. Seek emergency care immediately if the person becomes confused or "
                "unresponsive, cannot keep liquids down, or has an extremely high or low reading that "
                "isn't improving with usual treatment."
            ),
        },
        {
            "title": "Everyday Diabetes Management for Caregivers",
            "source_name": "Mayo Clinic (sample/seed content)",
            "url": "https://www.mayoclinic.org/diseases-conditions/diabetes/in-depth/diabetes-management",
            "body_text": (
                "Keeping meal times, medication schedules, and activity levels consistent from day to "
                "day makes blood sugar easier to predict and manage. A single unusual reading is less "
                "important than a pattern across several days — keeping a simple log of readings, "
                "meals, and activity helps the care team spot trends.\n\n"
                "Medication doses should only be changed by the prescribing provider. If readings "
                "suggest a change might be needed, caregivers should share the pattern with the care "
                "team rather than adjusting doses independently."
            ),
        },
    ],
}
