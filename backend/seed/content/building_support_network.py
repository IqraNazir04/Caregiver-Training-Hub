"""Seed content for the Building a Support Network track.

Written as plausible caregiving guidance in the style of NIA/AARP caregiver-support materials for
demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted, properly
licensed source text before any real-world use.
"""

TRACK = {
    "slug": "building-support-network",
    "name": "Building a Support Network",
    "theme": "emotional-mental-load",
    "description": "Practical ways to build a real support network and get comfortable asking for help before you're in crisis.",
    "lessons": [
        {
            "title": "Why asking for help is harder than it sounds",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Vague offers rarely turn into real help\n\n"
                "'Let me know if you need anything' is well-meaning but easy to let slide — for "
                "both sides. Converting a vague offer into a specific ask ('could you sit with mom "
                "Thursday afternoon') is what actually gets help scheduled.\n\n"
                "## Asking isn't a failure\n\n"
                "Many caregivers treat needing help as evidence they're not managing well enough. "
                "In reality, sustainable caregiving almost always involves other people — treating "
                "asking as normal, not a last resort, makes it easier to do before you're "
                "desperate.\n\n"
                "## Different people can offer different things\n\n"
                "One friend might be great for an hour of company, another for a specific errand, "
                "another just for venting to. You don't need one person to do everything."
            ),
            "quiz": [
                {
                    "question_text": "Why does 'let me know if you need anything' rarely turn into real help?",
                    "choices": [
                        "People don't mean it",
                        "It's vague and easy to let slide on both sides — a specific ask works better",
                        "It's rude to accept such offers",
                    ],
                    "correct_index": 1,
                    "explanation": "A specific, concrete request is much more likely to become real, scheduled help than an open-ended offer.",
                },
                {
                    "question_text": "What's a healthier way to think about needing help as a caregiver?",
                    "choices": [
                        "As evidence of failing at caregiving",
                        "As a normal part of sustainable caregiving, not a last resort",
                        "As something to avoid at all costs",
                    ],
                    "correct_index": 1,
                    "explanation": "Treating help as a normal part of caregiving — rather than a sign of failure — makes it easier to ask before reaching a crisis point.",
                },
            ],
        },
        {
            "title": "Where support actually comes from",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Support groups offer something friends and family can't\n\n"
                "People who are also caregiving understand specifics that even well-meaning "
                "friends may not — the exhaustion, the guilt, the particular logistics. In-person "
                "or online caregiver support groups can be a source of both practical tips and "
                "emotional relief.\n\n"
                "## Professional support has a place too\n\n"
                "A therapist or counselor isn't only for crisis moments — many caregivers benefit "
                "from ongoing support even when things are 'manageable,' the same way regular "
                "maintenance prevents bigger problems later.\n\n"
                "## Local resources are often underused\n\n"
                "Area Agencies on Aging, disease-specific organizations, and religious or "
                "community centers often have caregiver-specific resources — respite programs, "
                "support groups, transportation help — that go unused simply because caregivers "
                "don't know to look."
            ),
            "quiz": [
                {
                    "question_text": "What can caregiver support groups offer that friends and family sometimes can't?",
                    "choices": [
                        "Financial assistance",
                        "Understanding of caregiving-specific exhaustion, guilt, and logistics",
                        "Nothing meaningfully different",
                    ],
                    "correct_index": 1,
                    "explanation": "Other caregivers often understand the specific realities of caregiving in a way that even supportive friends and family may not.",
                },
                {
                    "question_text": "What's a reason to consider professional support even when things feel 'manageable'?",
                    "choices": [
                        "Ongoing support can help the way regular maintenance prevents bigger problems",
                        "Therapy is only useful during an active crisis",
                        "It's not relevant for caregivers",
                    ],
                    "correct_index": 0,
                    "explanation": "Ongoing professional support can be valuable proactively, not just as a crisis response.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Turning Offers of Help into Real Support",
            "source_name": "AARP Caregiving Resource Center (sample/seed content)",
            "url": "https://www.aarp.org/caregiving/life-balance/info-2017/asking-for-help.html",
            "body_text": (
                "Vague offers of help, like 'let me know if you need anything,' are easy to let "
                "slide on both sides. Converting a vague offer into a specific request — such as "
                "asking someone to sit with a care recipient for a set time — is what actually "
                "results in scheduled help. Many caregivers treat needing help as evidence they "
                "aren't managing well enough, but sustainable caregiving almost always involves "
                "other people, and treating asking as normal rather than a last resort makes it "
                "easier to do before reaching a crisis point."
            ),
        },
        {
            "title": "Finding Caregiver Support Beyond Friends and Family",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/caregiving/what-do-when-you-caregiver",
            "body_text": (
                "Other caregivers often understand the specific exhaustion, guilt, and logistics "
                "of caregiving in ways that even supportive friends and family may not, making "
                "in-person or online caregiver support groups valuable for both practical tips and "
                "emotional relief. Professional counseling isn't only useful during a crisis — many "
                "caregivers benefit from ongoing support even when things feel manageable.\n\n"
                "Local resources such as Area Agencies on Aging, disease-specific organizations, "
                "and community or religious centers often offer caregiver-specific resources, "
                "including respite programs and transportation help, that go unused simply because "
                "caregivers don't know to look for them."
            ),
        },
    ],
}
