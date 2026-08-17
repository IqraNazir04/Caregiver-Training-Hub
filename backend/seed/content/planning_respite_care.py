"""Seed content for the Planning for Respite Care track.

Written as plausible caregiving guidance in the style of NIA/ARCH National Respite Network
materials for demo/seed purposes — not scraped or verbatim from those sources. Replace with
vetted, properly licensed source text before any real-world use.
"""

TRACK = {
    "slug": "planning-respite-care",
    "name": "Planning for Respite Care",
    "theme": "family-logistics",
    "description": "What respite care actually is, the different forms it takes, and how to set it up before you're desperate for a break.",
    "lessons": [
        {
            "title": "What respite care actually covers",
            "estimated_minutes": 4,
            "body_markdown": (
                "## More than one form\n\n"
                "Respite care ranges from a few hours of in-home help to overnight stays at an "
                "adult day program or short-term stays at a care facility. It's not one specific "
                "service — it's a category, and the right form depends on how much time is needed "
                "and what care the person requires while you're away.\n\n"
                "## It's not just for emergencies\n\n"
                "Respite care is often thought of as a last resort, but planned, regular respite — "
                "even a few hours weekly or monthly — helps prevent the exhaustion that leads to a "
                "crisis in the first place.\n\n"
                "## Cost varies, and so does what's covered\n\n"
                "Some respite care is covered by Medicaid waivers, veterans' benefits, or "
                "nonprofit programs; other options are private-pay. It's worth checking multiple "
                "sources rather than assuming it's unaffordable before actually looking."
            ),
            "quiz": [
                {
                    "question_text": "What's true about respite care?",
                    "choices": [
                        "It's a single specific service everyone accesses the same way",
                        "It's a category covering several forms, from in-home hours to short facility stays",
                        "It's only available in emergencies",
                    ],
                    "correct_index": 1,
                    "explanation": "Respite care spans a range of formats, and the right one depends on the specific situation and needs.",
                },
                {
                    "question_text": "Why is planned, regular respite valuable, not just emergency respite?",
                    "choices": [
                        "It helps prevent the exhaustion that leads to a crisis in the first place",
                        "It's required by law",
                        "It has no advantage over emergency-only respite",
                    ],
                    "correct_index": 0,
                    "explanation": "Using respite proactively, rather than only after burnout, helps prevent reaching a crisis point at all.",
                },
            ],
        },
        {
            "title": "Setting it up before you need it urgently",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Research before you're desperate\n\n"
                "Finding and vetting respite options takes time — waitlists, paperwork, and "
                "eligibility checks aren't things you want to start during an acute crisis. "
                "Identifying a few options in advance means you're not starting from zero when "
                "you actually need it.\n\n"
                "## Prepare the person you care for, too\n\n"
                "A trial run with a new caregiver or a short stay, done in a low-stakes moment "
                "rather than the first time being an emergency, helps the person you're caring "
                "for adjust and gives you a chance to evaluate the fit.\n\n"
                "## Write down what a substitute caregiver needs to know\n\n"
                "Medication schedule, routines, preferences, and warning signs — written down "
                "clearly — mean respite care can actually go smoothly instead of creating new "
                "stress for everyone involved."
            ),
            "quiz": [
                {
                    "question_text": "Why research respite care options before an urgent need arises?",
                    "choices": [
                        "Waitlists and paperwork take time that's hard to find during a crisis",
                        "It's not actually necessary to plan ahead",
                        "Respite care doesn't require any setup",
                    ],
                    "correct_index": 0,
                    "explanation": "Researching and setting up respite care in advance avoids the added stress of starting the process during an acute crisis.",
                },
                {
                    "question_text": "Why do a trial run of respite care before it's urgently needed?",
                    "choices": [
                        "It helps the care recipient adjust and lets the caregiver evaluate fit in a low-stakes moment",
                        "Trial runs are required by respite providers",
                        "It has no real benefit",
                    ],
                    "correct_index": 0,
                    "explanation": "A low-stakes trial run helps both the care recipient and caregiver get comfortable with the arrangement before it's needed under pressure.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Understanding the Different Forms of Respite Care",
            "source_name": "ARCH National Respite Network (sample/seed content)",
            "url": "https://archrespite.org/respite-locator",
            "body_text": (
                "Respite care is a category rather than a single service, ranging from a few hours "
                "of in-home help to overnight stays at an adult day program or short-term stays at "
                "a care facility, with the right form depending on the amount of time needed and "
                "the level of care required. While often thought of as a last resort, planned and "
                "regular respite — even a few hours weekly or monthly — helps prevent the "
                "exhaustion that can lead to a crisis in the first place.\n\n"
                "Cost and coverage vary: some respite care is covered through Medicaid waivers, "
                "veterans' benefits, or nonprofit programs, while other options are private-pay, so "
                "it's worth checking multiple sources rather than assuming it's unaffordable."
            ),
        },
        {
            "title": "Preparing for Respite Care Before You Need It",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/caregiving/what-do-when-you-caregiver",
            "body_text": (
                "Finding and vetting respite care options takes time — waitlists, paperwork, and "
                "eligibility checks aren't things to start during an acute crisis, so identifying "
                "options in advance avoids starting from zero when respite is actually needed. A "
                "trial run with a new caregiver or a short stay, done during a low-stakes moment "
                "rather than as a first-time emergency, helps the care recipient adjust and lets "
                "the caregiver evaluate whether it's a good fit.\n\n"
                "Writing down the medication schedule, routines, preferences, and warning signs for "
                "a substitute caregiver helps respite care go smoothly rather than creating "
                "additional stress."
            ),
        },
    ],
}
