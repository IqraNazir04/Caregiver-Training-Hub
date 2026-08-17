"""Seed content for the Legal & Financial Basics track.

Written as plausible, general educational guidance in the style of NIA/AARP materials for
demo/seed purposes — not scraped or verbatim from those sources, and not a substitute for advice
from a qualified elder law attorney or financial advisor. Replace with vetted, properly licensed
source text before any real-world use.
"""

TRACK = {
    "slug": "legal-financial-basics",
    "name": "Legal & Financial Basics",
    "theme": "family-logistics",
    "description": "An orientation to the legal and financial concepts caregivers commonly encounter — this is general education, not legal or financial advice.",
    "lessons": [
        {
            "title": "Key documents to know about",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Power of attorney\n\n"
                "A power of attorney is a legal document that lets someone else make financial or "
                "medical decisions on a person's behalf if they're unable to. It needs to be set "
                "up while the person can still legally consent — waiting until after a decline in "
                "capacity is often too late.\n\n"
                "## Advance directives and healthcare proxies\n\n"
                "These documents record someone's wishes about medical treatment and name who can "
                "make healthcare decisions if they can't speak for themselves. Having the "
                "conversation and documenting it early avoids guesswork during a crisis.\n\n"
                "## This is general education, not legal advice\n\n"
                "Requirements for these documents vary by location. An elder law attorney can set "
                "up documents that are actually valid and effective where the person lives — this "
                "lesson is meant to help you know what to ask about, not to replace that advice."
            ),
            "quiz": [
                {
                    "question_text": "When does a power of attorney need to be set up?",
                    "choices": [
                        "Any time, it doesn't matter",
                        "While the person can still legally consent",
                        "Only after they've lost capacity to decide",
                    ],
                    "correct_index": 1,
                    "explanation": "A power of attorney requires the person to have legal capacity to consent at the time it's created, so waiting too long can make it impossible to set up.",
                },
                {
                    "question_text": "Why is this lesson described as general education rather than legal advice?",
                    "choices": [
                        "Because legal requirements vary by location and a qualified attorney should be involved",
                        "Because the information isn't useful",
                        "Because legal documents aren't actually necessary",
                    ],
                    "correct_index": 0,
                    "explanation": "Legal requirements differ by jurisdiction, so this content is meant to inform what to ask an elder law attorney, not to replace their advice.",
                },
            ],
        },
        {
            "title": "Navigating benefits and financial support",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Start by identifying what category of support applies\n\n"
                "Benefits generally fall into a few buckets: health coverage (Medicare/Medicaid), "
                "disability-related benefits, veterans' benefits, and local Area Agency on Aging "
                "programs. Knowing which category applies narrows down where to actually look.\n\n"
                "## Keep records organized before you need them\n\n"
                "Applications for benefits typically require documentation — income, medical "
                "records, proof of relationship. Gathering these before you're in an urgent "
                "situation makes the application process much faster.\n\n"
                "## Free help exists — use it before paid help\n\n"
                "Area Agencies on Aging and benefits counselors (sometimes called SHIP counselors "
                "for Medicare questions) offer free guidance navigating these systems, and are a "
                "reasonable first stop before paying for private consultation."
            ),
            "quiz": [
                {
                    "question_text": "What's a useful first step in navigating caregiving-related benefits?",
                    "choices": [
                        "Applying to every program regardless of fit",
                        "Identifying which general category of support applies",
                        "Waiting until a financial emergency forces the issue",
                    ],
                    "correct_index": 1,
                    "explanation": "Narrowing down which category of benefit applies (health coverage, disability, veterans, local aging services) focuses the search significantly.",
                },
                {
                    "question_text": "What's a reasonable first stop for free help navigating benefits?",
                    "choices": [
                        "A private financial advisor only",
                        "Area Agencies on Aging or free benefits counselors",
                        "There's no free help available",
                    ],
                    "correct_index": 1,
                    "explanation": "Free resources like Area Agencies on Aging and SHIP counselors are designed specifically to help navigate these systems before paying for private help.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Understanding Power of Attorney and Advance Directives",
            "source_name": "National Institute on Aging (sample/seed content — general education, not legal advice)",
            "url": "https://www.nia.nih.gov/health/legal-and-financial-planning-people-alzheimers",
            "body_text": (
                "A power of attorney is a legal document allowing someone else to make financial "
                "or medical decisions on a person's behalf if they become unable to do so "
                "themselves. It must be established while the person still has the legal capacity "
                "to consent, since waiting until after a decline in capacity is often too late. "
                "Advance directives and healthcare proxy documents similarly record a person's "
                "medical treatment wishes and designate who can make healthcare decisions on their "
                "behalf.\n\n"
                "Requirements for these documents vary by location, and an elder law attorney "
                "should be consulted to ensure documents are valid and effective for where the "
                "person lives. This information is general education, not a substitute for legal "
                "advice."
            ),
        },
        {
            "title": "Navigating Caregiving Benefits and Financial Support",
            "source_name": "AARP Caregiving Resource Center (sample/seed content — general education, not financial advice)",
            "url": "https://www.aarp.org/caregiving/financial-legal/",
            "body_text": (
                "Benefits relevant to caregivers generally fall into a few categories: health "
                "coverage such as Medicare or Medicaid, disability-related benefits, veterans' "
                "benefits, and local Area Agency on Aging programs. Identifying which category "
                "applies narrows down where to look. Gathering documentation such as income "
                "records, medical records, and proof of relationship before an urgent situation "
                "arises makes the application process significantly faster when the time comes.\n\n"
                "Area Agencies on Aging and free benefits counselors, including SHIP counselors "
                "for Medicare-related questions, offer no-cost guidance navigating these systems "
                "and are a reasonable first stop before seeking paid financial advice."
            ),
        },
    ],
}
