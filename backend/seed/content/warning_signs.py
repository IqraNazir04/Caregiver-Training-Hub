"""Seed content for the Recognizing Warning Signs track.

Written as plausible caregiving guidance in the style of CDC/Mayo Clinic caregiving materials for
demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted, properly
licensed source text before any real-world use.
"""

TRACK = {
    "slug": "recognizing-warning-signs",
    "name": "Recognizing Warning Signs — Doctor vs. ER",
    "theme": "practical-skills",
    "description": "Learn to tell the difference between symptoms that can wait for a doctor's appointment and ones that need emergency care now.",
    "lessons": [
        {
            "title": "Sorting symptoms into 'watch,' 'call,' and 'go'",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Watch: monitor at home\n\n"
                "Mild, stable symptoms that match a known condition — a slightly elevated "
                "temperature with no other symptoms, mild fatigue — can often be watched for a "
                "day, with a plan for what would prompt escalation.\n\n"
                "## Call: reach out within 24-48 hours\n\n"
                "New or worsening symptoms that aren't immediately dangerous — a new rash, "
                "increasing confusion without other red flags, a wound that looks slower to heal "
                "— usually warrant a call to the doctor within a day or two rather than a wait-"
                "and-see approach.\n\n"
                "## Go: emergency care now\n\n"
                "Sudden severe pain, difficulty breathing, sudden confusion or weakness on one "
                "side, chest pain, or any sudden dramatic change from baseline means emergency "
                "care, not a phone call first."
            ),
            "quiz": [
                {
                    "question_text": "Which of these fits the 'call within 24-48 hours' category rather than emergency care?",
                    "choices": [
                        "Sudden weakness on one side of the body",
                        "A new rash or a wound that seems slower to heal",
                        "Chest pain with difficulty breathing",
                    ],
                    "correct_index": 1,
                    "explanation": "A new rash or a slow-healing wound is a signal worth reporting soon, but it's not an immediate emergency the way sudden weakness or chest pain is.",
                },
                {
                    "question_text": "What generally distinguishes a 'go now' symptom from a 'call' symptom?",
                    "choices": [
                        "How long the person has had the underlying condition",
                        "Whether it's a sudden, severe, or dramatic change from baseline",
                        "Whether it happens during business hours",
                    ],
                    "correct_index": 1,
                    "explanation": "Sudden, severe changes — especially involving breathing, consciousness, or one-sided weakness — point toward emergency care rather than a scheduled call.",
                },
            ],
        },
        {
            "title": "What to have ready when you do call",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Note when it started and what changed\n\n"
                "'Since when' and 'compared to what' are the two most useful pieces of "
                "information for a triage nurse or doctor. Note the timing and exactly what's "
                "different from the person's normal baseline.\n\n"
                "## Have vitals ready if you can take them\n\n"
                "Temperature, and if available, blood pressure or oxygen level, help the person on "
                "the other end of the call assess urgency faster than a general description alone.\n\n"
                "## Don't downplay it to sound less dramatic\n\n"
                "Caregivers sometimes soften how a symptom is described to avoid sounding "
                "alarmist. Describe it plainly — the person triaging the call needs accurate "
                "information, not a filtered version."
            ),
            "quiz": [
                {
                    "question_text": "What two pieces of information are most useful when describing a new symptom?",
                    "choices": [
                        "The person's full medical history and insurance details",
                        "When it started and what's different from their normal baseline",
                        "How the caregiver feels about the situation",
                    ],
                    "correct_index": 1,
                    "explanation": "Onset timing and what's changed from baseline give a triage nurse or doctor the clearest picture, faster than a general description.",
                },
                {
                    "question_text": "Why is it important not to downplay a symptom when describing it?",
                    "choices": [
                        "It's against the law to exaggerate or minimize symptoms",
                        "Accurate information helps the person triaging assess urgency correctly",
                        "Doctors prefer dramatic descriptions",
                    ],
                    "correct_index": 1,
                    "explanation": "Softening a description to avoid sounding alarmist can cause a genuinely urgent situation to be under-triaged.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "When to Call the Doctor vs. Seek Emergency Care",
            "source_name": "CDC (sample/seed content)",
            "url": "https://www.cdc.gov/aging/caregiving/index.html",
            "body_text": (
                "Symptoms generally fall into three categories for a caregiver to sort through: "
                "mild and stable symptoms that can be watched at home for a short period, new or "
                "worsening symptoms that aren't immediately dangerous but warrant a call to the "
                "doctor within a day or two, and sudden, severe changes — such as difficulty "
                "breathing, chest pain, sudden confusion, or weakness on one side of the body — "
                "that require emergency care right away rather than a phone call first.\n\n"
                "The key distinguishing factor for emergency symptoms is a sudden, dramatic change "
                "from the person's normal baseline, rather than a gradual or mild shift."
            ),
        },
        {
            "title": "What to Have Ready Before You Call",
            "source_name": "Mayo Clinic (sample/seed content)",
            "url": "https://www.mayoclinic.org/healthy-lifestyle/caregivers/in-depth/caregiving/art-20044989",
            "body_text": (
                "When calling a doctor's office or triage line about a new symptom, the most "
                "useful information is when the symptom started and how it differs from the "
                "person's normal baseline. If available, basic vitals such as temperature, blood "
                "pressure, or oxygen level help the person on the other end assess urgency more "
                "quickly than a general description alone.\n\n"
                "Caregivers sometimes unintentionally soften how they describe a symptom to avoid "
                "sounding alarmist. Describing symptoms plainly and specifically, without "
                "minimizing them, helps ensure the situation is triaged accurately."
            ),
        },
    ],
}
