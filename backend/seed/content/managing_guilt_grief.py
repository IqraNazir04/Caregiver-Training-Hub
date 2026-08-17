"""Seed content for the Managing Guilt, Grief & Resentment track.

Written as plausible caregiving guidance in the style of NIA/family-caregiver-alliance materials
for demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted,
properly licensed source text before any real-world use.
"""

TRACK = {
    "slug": "managing-guilt-grief-resentment",
    "name": "Managing Guilt, Grief & Resentment",
    "theme": "emotional-mental-load",
    "description": "These emotions are a normal part of caregiving, not a sign you're doing it wrong — here's how to work with them.",
    "lessons": [
        {
            "title": "Why these feelings show up, and why that's normal",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Guilt often comes from an impossible standard\n\n"
                "Caregiver guilt frequently comes from measuring yourself against an idealized, "
                "unlimited version of care that no real person could sustain. Noticing the "
                "standard you're holding yourself to is often more useful than trying to silence "
                "the guilt directly.\n\n"
                "## Grief can start before a loss\n\n"
                "Grieving the gradual loss of who someone was — their personality, their "
                "independence, the relationship as it used to be — is real grief, even while "
                "they're still alive. It's sometimes called anticipatory grief, and it doesn't "
                "mean you've given up on them.\n\n"
                "## Resentment doesn't cancel out love\n\n"
                "Feeling resentful about the demands of caregiving, sometimes toward the person "
                "you're caring for, doesn't mean you don't love them. Both feelings can be true "
                "at once."
            ),
            "quiz": [
                {
                    "question_text": "What often drives caregiver guilt?",
                    "choices": [
                        "Measuring yourself against an unsustainable, idealized standard of care",
                        "Not caring enough about the person",
                        "Guilt has no identifiable cause",
                    ],
                    "correct_index": 0,
                    "explanation": "Guilt often stems from an impossibly high internal standard rather than an accurate reflection of how caregiving is actually going.",
                },
                {
                    "question_text": "What is anticipatory grief?",
                    "choices": [
                        "Grief that only happens after someone has died",
                        "Grieving a gradual loss — like personality or independence — while the person is still alive",
                        "A sign that the caregiver has given up",
                    ],
                    "correct_index": 1,
                    "explanation": "Anticipatory grief is a real and common experience of mourning ongoing losses while the person is still living.",
                },
            ],
        },
        {
            "title": "Working with these feelings instead of against them",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Naming it reduces its power\n\n"
                "Saying 'I feel resentful right now' — even just to yourself — tends to reduce the "
                "shame spiral that comes from feeling like you shouldn't feel that way at all.\n\n"
                "## Separate the feeling from the action\n\n"
                "Feeling something and acting on it are different. You can feel intense frustration "
                "and still choose a calm response — the feeling isn't the problem, and having it "
                "doesn't make you a bad caregiver.\n\n"
                "## These feelings are a sign to get support, not to hide\n\n"
                "Persistent guilt, grief, or resentment are common enough that support groups and "
                "counselors who specialize in caregiving exist specifically for this. Reaching out "
                "is a response to a normal experience, not an admission of failure."
            ),
            "quiz": [
                {
                    "question_text": "What effect does naming a difficult feeling (even privately) tend to have?",
                    "choices": [
                        "It makes the feeling worse",
                        "It tends to reduce the shame spiral of feeling like you shouldn't feel that way",
                        "It has no effect",
                    ],
                    "correct_index": 1,
                    "explanation": "Acknowledging a feeling directly often reduces the additional layer of shame that comes from suppressing or denying it.",
                },
                {
                    "question_text": "What's true about feeling something difficult versus acting on it?",
                    "choices": [
                        "They're the same thing — feeling it means you'll act on it",
                        "They're different — you can feel frustration and still choose a calm response",
                        "Feelings should always be suppressed",
                    ],
                    "correct_index": 1,
                    "explanation": "Having a difficult feeling doesn't determine the response — the two are separable, and having the feeling doesn't make someone a bad caregiver.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Understanding Caregiver Guilt and Anticipatory Grief",
            "source_name": "Family Caregiver Alliance (sample/seed content)",
            "url": "https://www.caregiver.org/resource/caregiver-guilt/",
            "body_text": (
                "Caregiver guilt frequently stems from measuring oneself against an idealized, "
                "unlimited standard of care that no real person could sustain — noticing that "
                "standard is often more useful than trying to suppress the guilt directly. "
                "Grieving the gradual loss of who someone was, including their personality or "
                "independence, is a real form of grief even while they are still alive. This is "
                "sometimes called anticipatory grief, and experiencing it does not mean a "
                "caregiver has given up on the person.\n\n"
                "Resentment about the demands of caregiving, including resentment sometimes "
                "directed at the person receiving care, does not cancel out love for that person. "
                "Both feelings can coexist."
            ),
        },
        {
            "title": "Working with Difficult Caregiving Emotions",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/caregiving/taking-care-yourself-tips-caregivers",
            "body_text": (
                "Naming a difficult feeling, even privately, tends to reduce the additional shame "
                "that comes from believing the feeling itself is wrong to have. Feeling something "
                "and acting on it are separate — a caregiver can feel intense frustration and "
                "still choose a calm response, and having the feeling does not make someone a bad "
                "caregiver.\n\n"
                "Persistent guilt, grief, or resentment are common enough among caregivers that "
                "support groups and counselors specializing in caregiving exist specifically to "
                "help with them. Seeking that support is a response to a normal experience, not an "
                "admission of failure."
            ),
        },
    ],
}
