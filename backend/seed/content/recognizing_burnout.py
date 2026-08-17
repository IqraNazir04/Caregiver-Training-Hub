"""Seed content for the Recognizing Caregiver Burnout Early track.

Written as plausible caregiving guidance in the style of NIA/AARP caregiver-wellbeing materials
for demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted,
properly licensed source text before any real-world use.
"""

TRACK = {
    "slug": "recognizing-caregiver-burnout",
    "name": "Recognizing Caregiver Burnout Early",
    "theme": "emotional-mental-load",
    "description": "Learn the early signs of caregiver burnout before it becomes a crisis, and what to do when you notice them.",
    "lessons": [
        {
            "title": "Early signs, before the crisis point",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Burnout builds gradually\n\n"
                "By the time exhaustion feels undeniable, burnout has usually been building for "
                "months. Early signs are quieter: losing interest in things you used to enjoy, "
                "increased irritability, trouble sleeping even when tired, or feeling constantly "
                "behind no matter how much you do.\n\n"
                "## Physical symptoms count too\n\n"
                "Frequent headaches, getting sick more often, changes in appetite, or new aches "
                "and tension are the body's way of signaling chronic stress, even when the mind "
                "hasn't caught up to naming it.\n\n"
                "## A useful check-in question\n\n"
                "'If a friend described feeling the way I feel right now, what would I tell them?' "
                "often surfaces what's being minimized in your own situation."
            ),
            "quiz": [
                {
                    "question_text": "What's true about how caregiver burnout typically develops?",
                    "choices": [
                        "It appears suddenly with no warning signs",
                        "It usually builds gradually over months before feeling undeniable",
                        "It only affects people who aren't trying hard enough",
                    ],
                    "correct_index": 1,
                    "explanation": "Burnout tends to build gradually, with quieter early signs that are easy to dismiss before it reaches a crisis point.",
                },
                {
                    "question_text": "Which of these can be an early physical sign of caregiver burnout?",
                    "choices": [
                        "Frequent headaches or getting sick more often",
                        "Only feeling tired after a long day of physical labor",
                        "Physical symptoms are unrelated to caregiving stress",
                    ],
                    "correct_index": 0,
                    "explanation": "Chronic stress often shows up physically — headaches, frequent illness, appetite changes — before it's consciously recognized as burnout.",
                },
            ],
        },
        {
            "title": "What to do when you notice the signs",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Don't wait for a bigger crisis to act\n\n"
                "Early signs are the easiest point to intervene. Waiting until burnout is severe "
                "makes recovery slower and increases the risk to both the caregiver and the "
                "person being cared for.\n\n"
                "## Small changes are still real changes\n\n"
                "You don't need to overhaul your whole life to respond to burnout. Even one "
                "recurring break, one task handed off, or one honest conversation about capacity "
                "can meaningfully shift the trajectory.\n\n"
                "## Tell someone, even briefly\n\n"
                "Naming what you're experiencing out loud — to a friend, a doctor, a support "
                "group — breaks the isolation that lets burnout deepen unnoticed."
            ),
            "quiz": [
                {
                    "question_text": "Why is it better to act on early signs of burnout rather than wait?",
                    "choices": [
                        "Early signs are the easiest point to intervene, before recovery becomes harder",
                        "Nothing can be done regardless of timing",
                        "Waiting has no effect either way",
                    ],
                    "correct_index": 0,
                    "explanation": "Addressing burnout early is generally easier and more effective than waiting until it becomes severe.",
                },
                {
                    "question_text": "What's a reasonable first step when noticing signs of burnout?",
                    "choices": [
                        "A complete overhaul of your entire schedule",
                        "One small change, like a recurring break or handing off one task",
                        "Waiting until things get worse to see if it resolves itself",
                    ],
                    "correct_index": 1,
                    "explanation": "Small, concrete changes are more sustainable and achievable than an all-at-once overhaul, and they can still meaningfully help.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Recognizing the Early Signs of Caregiver Burnout",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/caregiving/taking-care-yourself-tips-caregivers",
            "body_text": (
                "Caregiver burnout typically builds gradually rather than appearing suddenly. "
                "Early signs are often quiet and easy to dismiss: losing interest in previously "
                "enjoyed activities, increased irritability, trouble sleeping despite being tired, "
                "or a persistent feeling of being behind no matter how much gets done. Physical "
                "symptoms — frequent headaches, getting sick more often, or changes in appetite — "
                "are also common signals of chronic stress, sometimes appearing before it's "
                "consciously recognized as burnout."
            ),
        },
        {
            "title": "Responding to Burnout Before It Becomes a Crisis",
            "source_name": "AARP Caregiving Resource Center (sample/seed content)",
            "url": "https://www.aarp.org/caregiving/life-balance/info-2017/caregiver-burnout.html",
            "body_text": (
                "Early signs of burnout represent the easiest point to intervene — waiting until "
                "burnout becomes severe tends to make recovery slower and increases risk for both "
                "the caregiver and the person receiving care. Small, concrete changes, such as a "
                "recurring break, handing off a single task, or an honest conversation about "
                "capacity, can meaningfully shift the trajectory without requiring a complete "
                "overhaul.\n\n"
                "Naming what's being experienced out loud, even briefly, to a friend, doctor, or "
                "support group helps break the isolation that allows burnout to deepen unnoticed."
            ),
        },
    ],
}
