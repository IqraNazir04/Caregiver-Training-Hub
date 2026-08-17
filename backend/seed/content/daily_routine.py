"""Seed content for the Building a Daily Care Routine track.

Written as plausible caregiving guidance in the style of NIA/AARP caregiving materials for
demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted, properly
licensed source text before any real-world use.
"""

TRACK = {
    "slug": "building-daily-care-routine",
    "name": "Building a Daily Care Routine",
    "theme": "foundational",
    "description": "Design a daily routine that covers what needs to happen without depending on willpower alone — and adjust it as needs change.",
    "lessons": [
        {
            "title": "Designing a routine that actually sticks",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Anchor to existing habits\n\n"
                "Attach new care tasks to things that already happen reliably — medications "
                "after breakfast, a mobility check before bed. Routines built around existing "
                "anchors survive chaotic days better than routines that need to be remembered "
                "from scratch.\n\n"
                "## Write it down somewhere visible\n\n"
                "A routine that only exists in your head disappears on your worst days, which "
                "are exactly the days you need it most. A simple written or printed checklist on "
                "the fridge outperforms a mental list.\n\n"
                "## Build in slack\n\n"
                "A routine scheduled down to the minute breaks the first time something runs "
                "long. Leave buffer time between tasks, especially around medications and "
                "appointments."
            ),
            "quiz": [
                {
                    "question_text": "Why does anchoring new tasks to existing habits help?",
                    "choices": [
                        "It requires less willpower than remembering tasks from scratch",
                        "It makes the routine look more official",
                        "It's required by most care plans",
                    ],
                    "correct_index": 0,
                    "explanation": "Attaching a new task to something that already happens reliably (like a meal) makes it far more likely to happen consistently, especially on hard days.",
                },
                {
                    "question_text": "What's a risk of scheduling a routine down to the minute?",
                    "choices": [
                        "It becomes too easy to follow",
                        "It breaks the first time something runs long",
                        "It requires too much paperwork",
                    ],
                    "correct_index": 1,
                    "explanation": "Tight schedules with no buffer tend to fall apart quickly since caregiving rarely goes exactly to plan.",
                },
            ],
        },
        {
            "title": "Adjusting the routine as needs change",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Revisit on a schedule, not just in a crisis\n\n"
                "Set a recurring check-in — weekly or monthly — to ask whether the routine still "
                "fits. Needs shift gradually, and it's easy to keep running an outdated routine "
                "until something forces a change.\n\n"
                "## Watch for routine tasks that have become harder\n\n"
                "A task that used to take five minutes and now takes twenty is a signal, not just "
                "an inconvenience — it may mean it's time to bring in additional help for that "
                "specific task.\n\n"
                "## Keep the routine realistic for you, too\n\n"
                "A routine that only accounts for the care recipient's needs and none of the "
                "caregiver's capacity will eventually fail. Build in your own meals, rest, and "
                "breaks as part of the routine, not an afterthought."
            ),
            "quiz": [
                {
                    "question_text": "Why schedule regular check-ins on the routine instead of only changing it during a crisis?",
                    "choices": [
                        "Needs shift gradually and are easy to miss otherwise",
                        "It's required by insurance",
                        "It gives the caregiver something to do",
                    ],
                    "correct_index": 0,
                    "explanation": "Gradual changes in needs are easy to miss without a regular check-in, leading to a routine that's quietly out of date.",
                },
                {
                    "question_text": "What should a sustainable daily routine account for?",
                    "choices": [
                        "Only the care recipient's medical needs",
                        "Only the family's schedule",
                        "Both the care recipient's needs and the caregiver's own capacity",
                    ],
                    "correct_index": 2,
                    "explanation": "A routine that ignores the caregiver's own rest and needs tends to break down over time.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Creating a Caregiving Routine That Lasts",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/caregiving/what-do-when-you-caregiver",
            "body_text": (
                "Care routines are more likely to stick when they're attached to habits that "
                "already happen reliably, such as giving medication after breakfast or doing a "
                "mobility check before bed. A routine that exists only in a caregiver's memory "
                "tends to disappear on the most difficult days — exactly when it's needed most — "
                "so writing it down somewhere visible, such as a printed checklist, is more "
                "reliable than a mental list.\n\n"
                "Routines that are scheduled too tightly, without buffer time between tasks, tend "
                "to break down the first time something runs long. Building in slack, especially "
                "around medications and appointments, makes a routine more resilient."
            ),
        },
        {
            "title": "Revisiting the Care Plan as Needs Change",
            "source_name": "AARP Caregiving Resource Center (sample/seed content)",
            "url": "https://www.aarp.org/caregiving/basics/",
            "body_text": (
                "Care needs tend to shift gradually rather than all at once, which makes it easy "
                "to keep following an outdated routine. Setting a recurring check-in — weekly or "
                "monthly — to review whether the current routine still fits helps catch these "
                "changes early. A task that used to take a few minutes and now takes much longer "
                "is a signal that it may be time to bring in additional help for that task "
                "specifically.\n\n"
                "A sustainable routine also needs to account for the caregiver's own capacity, "
                "including meals, rest, and breaks, not only the care recipient's needs. Routines "
                "that ignore the caregiver's own needs tend to fail over time."
            ),
        },
    ],
}
