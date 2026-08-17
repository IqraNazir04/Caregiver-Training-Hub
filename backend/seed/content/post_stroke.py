"""Seed content for the Post-Stroke Recovery track.

Written as plausible caregiving guidance in the style of CDC/Mayo Clinic materials for demo/seed
purposes — not scraped or verbatim from those sources. Replace with vetted, properly licensed
source text before any real-world use.
"""

TRACK = {
    "slug": "post-stroke-recovery",
    "theme": "foundational",
    "name": "Post-Stroke Recovery",
    "description": "Support for caregivers helping a family member recover after a stroke, including warning signs, mobility, and daily routines.",
    "lessons": [
        {
            "title": "Recognizing a stroke (F.A.S.T.)",
            "estimated_minutes": 3,
            "body_markdown": (
                "## The F.A.S.T. test\n\n"
                "- **Face drooping** — does one side of the face droop or feel numb?\n"
                "- **Arm weakness** — is one arm weak or numb? Does it drift downward when raised?\n"
                "- **Speech difficulty** — is speech slurred, or hard to understand?\n"
                "- **Time to call 911** — if any of these signs are present, call emergency services immediately, "
                "even if the symptom goes away.\n\n"
                "## Why speed matters\n\n"
                "Stroke treatment is most effective within a narrow window after symptoms begin. Note "
                "the time symptoms started — this information helps emergency responders decide on "
                "treatment."
            ),
            "quiz": [
                {
                    "question_text": "What does the 'T' in F.A.S.T. stand for?",
                    "choices": [
                        "Talk to the person calmly",
                        "Time to call 911",
                        "Take their temperature",
                    ],
                    "correct_index": 1,
                    "explanation": "T stands for 'Time to call 911' — stroke is a time-critical emergency.",
                },
                {
                    "question_text": "If stroke symptoms appear and then go away after a few minutes, what should you do?",
                    "choices": [
                        "Wait to see if they come back before doing anything",
                        "Still call 911 right away",
                        "Have the person rest and check again in the morning",
                    ],
                    "correct_index": 1,
                    "explanation": "Even brief symptoms can indicate a serious event (such as a TIA) and warrant immediate emergency evaluation.",
                },
            ],
        },
        {
            "title": "Supporting mobility and daily routines",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Follow the therapy plan\n\n"
                "Stick to the exercises and mobility routines recommended by the physical or "
                "occupational therapist. Consistency matters more than intensity in early recovery.\n\n"
                "## Adapt the environment\n\n"
                "Clear walking paths, install grab bars, and consider a raised toilet seat or shower "
                "chair if balance or one-sided weakness is a concern.\n\n"
                "## Watch for fatigue and mood changes\n\n"
                "Fatigue and frustration are common after a stroke. Encourage rest breaks, and let the "
                "care team know about mood changes such as persistent sadness or withdrawal — "
                "post-stroke depression is common and treatable."
            ),
            "quiz": [
                {
                    "question_text": "What's most important in early post-stroke mobility recovery?",
                    "choices": [
                        "Pushing for maximum intensity in every session",
                        "Following the therapist's plan consistently",
                        "Skipping rest breaks to recover faster",
                    ],
                    "correct_index": 1,
                    "explanation": "Consistency with the prescribed therapy plan is generally more effective and safer than pushing intensity.",
                },
                {
                    "question_text": "What should a caregiver watch for that's a common but treatable issue after stroke?",
                    "choices": [
                        "Post-stroke depression",
                        "Improved appetite",
                        "Increased energy",
                    ],
                    "correct_index": 0,
                    "explanation": "Post-stroke depression is common and treatable — caregivers should flag persistent sadness or withdrawal to the care team.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Stroke Signs and Symptoms — F.A.S.T.",
            "source_name": "CDC (sample/seed content)",
            "url": "https://www.cdc.gov/stroke/signs_symptoms.htm",
            "body_text": (
                "Stroke is a medical emergency. Use the F.A.S.T. test to check for the most common "
                "signs: Face drooping on one side, Arm weakness or drift when raised, Speech that is "
                "slurred or hard to understand, and Time to call 911 immediately if any of these signs "
                "are present. Note the time symptoms first appeared, since this affects treatment "
                "options. Even if symptoms resolve on their own, the person should still be evaluated "
                "in an emergency setting right away, as this can indicate a transient ischemic attack "
                "(TIA) and a higher risk of a full stroke soon after."
            ),
        },
        {
            "title": "Stroke Rehabilitation and Recovery at Home",
            "source_name": "Mayo Clinic (sample/seed content)",
            "url": "https://www.mayoclinic.org/diseases-conditions/stroke/in-depth/stroke-rehabilitation",
            "body_text": (
                "Recovery after a stroke often involves physical, occupational, and speech therapy. "
                "Caregivers can support recovery by helping the person follow their therapist's home "
                "exercise plan consistently, rather than pushing for intensity beyond what's "
                "recommended. Home modifications such as grab bars, clear walking paths, and shower "
                "chairs reduce fall risk for someone with one-sided weakness or balance problems.\n\n"
                "Fatigue is common during recovery, so build in rest periods. Mood changes, including "
                "persistent sadness, irritability, or withdrawal from activities, can indicate "
                "post-stroke depression, which is common and responds well to treatment — caregivers "
                "should mention these changes to the person's care team."
            ),
        },
    ],
}
