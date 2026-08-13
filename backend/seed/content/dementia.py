"""Seed content for the Dementia & Alzheimer's Care track.

Written as plausible caregiving guidance in the style of NIA/CDC/Mayo Clinic materials for
demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted,
properly licensed source text before any real-world use.
"""

TRACK = {
    "slug": "dementia-alzheimers-care",
    "name": "Dementia & Alzheimer's Care",
    "description": "Practical guidance for caregivers supporting someone with dementia or Alzheimer's disease, including communication strategies and safety at home.",
    "lessons": [
        {
            "title": "Communicating with someone with dementia",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Keep it simple\n\n"
                "Use short, clear sentences and ask one question at a time. Give the person extra "
                "time to respond before repeating or rephrasing.\n\n"
                "## Reduce distractions\n\n"
                "Turn off the TV or radio during conversations. Face the person and keep eye contact "
                "so they can pick up on your tone and expression.\n\n"
                "## Avoid arguing or correcting\n\n"
                "If the person is confused about time, place, or people, avoid direct confrontation. "
                "Gently redirect the conversation instead of insisting on the 'correct' facts — this "
                "reduces agitation for both of you."
            ),
            "quiz": [
                {
                    "question_text": "What's the best way to phrase questions when talking with someone with dementia?",
                    "choices": [
                        "Ask several questions at once so they can pick which to answer",
                        "Ask one short, simple question at a time",
                        "Avoid asking questions entirely",
                    ],
                    "correct_index": 1,
                    "explanation": "One simple question at a time reduces confusion and gives the person a clear, manageable prompt to respond to.",
                },
                {
                    "question_text": "If the person insists something happened that you know isn't true, what should you generally do?",
                    "choices": [
                        "Correct them firmly so they understand the facts",
                        "Gently redirect the conversation rather than argue",
                        "Ignore them and leave the room",
                    ],
                    "correct_index": 1,
                    "explanation": "Arguing or insisting on facts often increases agitation; gentle redirection is calmer and more effective.",
                },
            ],
        },
        {
            "title": "Making the home safer",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Reduce fall risks\n\n"
                "Remove loose rugs, add grab bars in the bathroom, and make sure hallways and stairs "
                "are well lit, including at night.\n\n"
                "## Secure hazards\n\n"
                "Lock away medications, cleaning supplies, and sharp tools. Consider stove knob covers "
                "or an automatic shut-off if wandering into the kitchen unsupervised is a risk.\n\n"
                "## Plan for wandering\n\n"
                "Some people with dementia wander and can become disoriented even in familiar places. "
                "Consider door alarms, a medical ID bracelet, and sharing a recent photo with neighbors."
            ),
            "quiz": [
                {
                    "question_text": "Which of these is a recommended home-safety change for a fall-risk caregiving environment?",
                    "choices": [
                        "Leave loose rugs to soften trip impacts",
                        "Add grab bars in the bathroom and improve lighting",
                        "Keep hallways dimly lit to avoid overstimulation",
                    ],
                    "correct_index": 1,
                    "explanation": "Grab bars and good lighting directly reduce fall risk; loose rugs and dim hallways increase it.",
                },
                {
                    "question_text": "What is a reasonable precaution if wandering is a concern?",
                    "choices": [
                        "A medical ID bracelet and door alarms",
                        "Removing all clocks and calendars from the home",
                        "Keeping every door unlocked for easy exit in an emergency",
                    ],
                    "correct_index": 0,
                    "explanation": "ID bracelets and door alarms help caregivers respond quickly if wandering occurs and help others identify the person if found alone.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Communicating with a Person with Alzheimer's Disease",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/alzheimers-caregiving",
            "body_text": (
                "When talking with a person who has Alzheimer's disease, speak slowly and clearly, "
                "using short, simple sentences. Ask one question at a time and allow extra time for a "
                "response before repeating the question. Turn off competing noise, such as the TV or "
                "radio, and make sure you have the person's attention before speaking.\n\n"
                "Avoid quizzing the person on names or facts, and avoid correcting or arguing about "
                "things they misremember. Instead, respond to the emotion behind what they're saying "
                "and gently redirect the conversation to a different topic or activity if they seem "
                "distressed or confused."
            ),
        },
        {
            "title": "Home Safety for People with Alzheimer's Disease",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/home-safety-alzheimers-disease",
            "body_text": (
                "People with Alzheimer's disease can become confused about their surroundings, which "
                "raises the risk of falls and accidents. Remove tripping hazards like loose rugs and "
                "clutter, install grab bars near the toilet and in the shower, and keep frequently used "
                "rooms well lit, including night-lights in hallways and bathrooms.\n\n"
                "Store medications, cleaning products, and sharp objects out of reach or in locked "
                "cabinets. If the person tends to wander, consider door and window alarms, keep a "
                "current photo on hand, and enroll in a wandering-response program if one is available "
                "in your area. A medical ID bracelet listing the diagnosis and an emergency contact can "
                "help if the person is found away from home."
            ),
        },
    ],
}
