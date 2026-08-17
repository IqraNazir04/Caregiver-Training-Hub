"""Seed content for the Coordinating Care Across Family Without Conflict track.

Written as plausible caregiving guidance in the style of AARP/NIA family-caregiving materials for
demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted, properly
licensed source text before any real-world use.
"""

TRACK = {
    "slug": "coordinating-family-care",
    "name": "Coordinating Care Across Family Without Conflict",
    "theme": "family-logistics",
    "description": "Set up systems so multiple family members can share caregiving duties without duplicated work or dropped balls.",
    "lessons": [
        {
            "title": "Setting up a shared system early",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Pick one place for shared information\n\n"
                "Medication logs, appointment notes, and to-do items scattered across texts, "
                "memory, and individual notebooks are how things get missed or duplicated. A "
                "single shared log — even a simple shared document — gives everyone the same "
                "source of truth.\n\n"
                "## Assign roles based on strengths and availability, not just family order\n\n"
                "The sibling who's good with paperwork isn't necessarily the one who lives "
                "closest. Splitting tasks by what each person can realistically and reliably do "
                "reduces resentment compared to assuming roles by birth order or proximity alone.\n\n"
                "## Revisit the system, don't just set it once\n\n"
                "What works when care needs are light may not hold up as they increase. A brief "
                "regular check-in on how the system is working keeps it from quietly breaking "
                "down."
            ),
            "quiz": [
                {
                    "question_text": "Why does scattering caregiving information across texts and memory cause problems?",
                    "choices": [
                        "It's how things get missed or duplicated",
                        "It's actually more efficient",
                        "It has no real downside",
                    ],
                    "correct_index": 0,
                    "explanation": "Without a single shared source of truth, tasks and information are easy to lose track of or duplicate.",
                },
                {
                    "question_text": "What's a better basis for assigning caregiving roles than birth order or proximity alone?",
                    "choices": [
                        "Each person's actual strengths and availability",
                        "Whoever complains the least",
                        "A strict rotation regardless of skill",
                    ],
                    "correct_index": 0,
                    "explanation": "Matching tasks to what each person can realistically and reliably do tends to reduce resentment and produce better outcomes.",
                },
            ],
        },
        {
            "title": "Handling conflict when it comes up",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Address process problems, not just people problems\n\n"
                "When something falls through, it's tempting to frame it as someone not caring "
                "enough. Often it's a process gap — no clear owner, no reminder system — that a "
                "process fix solves better than a difficult conversation about character.\n\n"
                "## Separate the caregiving relationship from old family dynamics\n\n"
                "Caregiving can resurface old sibling roles and rivalries. Naming that directly — "
                "'this feels like an old pattern, not really about the schedule' — can defuse a "
                "disagreement that's actually about something older.\n\n"
                "## When it's truly stuck, get outside help\n\n"
                "A family meeting facilitated by a social worker or care manager can help when "
                "conflict keeps recurring despite good-faith attempts to resolve it directly."
            ),
            "quiz": [
                {
                    "question_text": "When a caregiving task falls through, what's often the actual cause?",
                    "choices": [
                        "The person responsible doesn't care about the family member",
                        "A process gap, like no clear owner or reminder system",
                        "There's always a character flaw involved",
                    ],
                    "correct_index": 1,
                    "explanation": "Dropped tasks are often a sign of a process gap rather than a lack of care, and fixing the process is usually more effective than a conflict about character.",
                },
                {
                    "question_text": "What can help when caregiving conflict actually stems from old family dynamics?",
                    "choices": [
                        "Ignoring the pattern and hoping it resolves itself",
                        "Naming the pattern directly as separate from the current disagreement",
                        "Avoiding the topic permanently",
                    ],
                    "correct_index": 1,
                    "explanation": "Explicitly naming an old family pattern can help separate it from the immediate caregiving disagreement and make the real issue easier to address.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Building a Shared System for Family Caregiving",
            "source_name": "AARP Caregiving Resource Center (sample/seed content)",
            "url": "https://www.aarp.org/caregiving/family-caregiving/info-2017/sharing-caregiving-responsibilities.html",
            "body_text": (
                "When caregiving information is scattered across texts, memory, and individual "
                "notes, tasks are more likely to be missed or duplicated. A single shared log "
                "gives every family member involved the same source of truth. Assigning roles "
                "based on each person's actual strengths and availability, rather than birth order "
                "or proximity alone, tends to reduce resentment and produce a more sustainable "
                "arrangement.\n\n"
                "A system that works when care needs are light may not hold up as needs increase, "
                "so a brief, regular check-in on how the system is functioning helps catch quiet "
                "breakdowns before they become bigger problems."
            ),
        },
        {
            "title": "Resolving Family Conflict Around Caregiving",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/caregiving/what-do-when-you-caregiver",
            "body_text": (
                "When a caregiving task falls through, it's often a process gap — no clear owner, "
                "no reminder system — rather than a sign that someone doesn't care enough, and a "
                "process fix tends to resolve it better than a conflict about character. "
                "Caregiving can also resurface old sibling roles and rivalries; naming that "
                "pattern directly can help defuse a disagreement that's really about something "
                "older than the current schedule.\n\n"
                "When conflict keeps recurring despite good-faith attempts to resolve it directly, "
                "a family meeting facilitated by a social worker or care manager can help move "
                "things forward."
            ),
        },
    ],
}
