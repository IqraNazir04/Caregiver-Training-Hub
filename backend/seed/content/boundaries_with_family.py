"""Seed content for the Setting Boundaries with Other Family Members track.

Written as plausible caregiving guidance in the style of AARP/NIA family-caregiving materials for
demo/seed purposes — not scraped or verbatim from those sources. Replace with vetted, properly
licensed source text before any real-world use.
"""

TRACK = {
    "slug": "boundaries-with-family",
    "name": "Setting Boundaries with Other Family Members",
    "theme": "communication-behavior",
    "description": "Navigate disagreements and uneven effort with siblings and other relatives involved (or not involved) in caregiving.",
    "lessons": [
        {
            "title": "Naming the imbalance without a blow-up",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Uneven effort is common, not a personal insult\n\n"
                "One family member often ends up doing more, especially if they live closer or "
                "have a more flexible schedule. Naming the imbalance factually — not as a moral "
                "failing — makes the conversation easier for everyone to engage with.\n\n"
                "## Ask for specific help, not general support\n\n"
                "'I need help' is easy to agree with and easy to forget. 'Can you handle Tuesday "
                "pharmacy pickups' is a request someone can actually say yes or no to and follow "
                "through on.\n\n"
                "## Put it in writing when it's contentious\n\n"
                "A shared document or group chat for who's doing what removes ambiguity and gives "
                "everyone the same reference point, reducing 'I thought you were handling that' "
                "moments."
            ),
            "quiz": [
                {
                    "question_text": "What's a more effective request than a general 'I need help'?",
                    "choices": [
                        "A specific, assignable task like handling a particular weekly errand",
                        "A vague statement repeated more emphatically",
                        "No request — waiting for others to notice",
                    ],
                    "correct_index": 0,
                    "explanation": "Specific requests are easier for someone to actually say yes or no to and follow through on than vague appeals for general support.",
                },
                {
                    "question_text": "Why frame an uneven caregiving effort as a factual imbalance rather than a moral failing?",
                    "choices": [
                        "It's easier for everyone to engage with productively",
                        "It avoids the topic being discussed at all",
                        "It makes the other person feel worse, which is the goal",
                    ],
                    "correct_index": 0,
                    "explanation": "A factual framing tends to open a conversation rather than trigger defensiveness that shuts it down.",
                },
            ],
        },
        {
            "title": "Handling disagreement about care decisions",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Separate 'different opinion' from 'not involved enough to weigh in'\n\n"
                "A sibling who visits rarely but has strong opinions about care decisions can be a "
                "source of friction. It's reasonable to welcome input while noting that day-to-day "
                "decisions need to be made by whoever is actually present and informed.\n\n"
                "## Regular updates reduce out-of-the-blue conflict\n\n"
                "A short, regular update (even a brief text) to less-involved family members "
                "prevents decisions from feeling sudden or exclusionary when they do get "
                "involved.\n\n"
                "## Some conflicts need a neutral third party\n\n"
                "A social worker, care manager, or family mediator can help when disagreements "
                "about care decisions become a pattern rather than a one-time disagreement."
            ),
            "quiz": [
                {
                    "question_text": "How can regular updates help with less-involved family members?",
                    "choices": [
                        "They prevent decisions from feeling sudden or exclusionary",
                        "They're legally required",
                        "They eliminate the need for any future conversation",
                    ],
                    "correct_index": 0,
                    "explanation": "Consistent updates keep everyone informed so major decisions don't come as a surprise, which reduces friction.",
                },
                {
                    "question_text": "When might a neutral third party, like a care manager or mediator, be helpful?",
                    "choices": [
                        "Never — family disagreements should stay private",
                        "When disagreements about care decisions become a recurring pattern",
                        "Only for legal disputes",
                    ],
                    "correct_index": 1,
                    "explanation": "A neutral third party can be valuable when conflict over care decisions is a repeated pattern rather than a single disagreement.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Addressing Uneven Caregiving Effort Among Siblings",
            "source_name": "AARP Caregiving Resource Center (sample/seed content)",
            "url": "https://www.aarp.org/caregiving/family-caregiving/info-2017/sharing-caregiving-responsibilities.html",
            "body_text": (
                "It's common for one family member to end up doing more caregiving, often simply "
                "because of proximity or schedule flexibility. Naming this imbalance factually, "
                "rather than as a moral failing, tends to make the conversation easier for "
                "everyone to engage with productively. Specific, assignable requests — such as "
                "handling a particular weekly task — are easier for another family member to "
                "commit to and follow through on than a general appeal for more help.\n\n"
                "A shared document or group chat tracking who is handling what can reduce "
                "ambiguity and prevent 'I thought you were handling that' situations."
            ),
        },
        {
            "title": "Navigating Disagreement About Care Decisions",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/caregiving/what-do-when-you-caregiver",
            "body_text": (
                "Family members who are less involved day-to-day may still have strong opinions "
                "about care decisions, which can create friction. It's reasonable to welcome their "
                "input while noting that day-to-day decisions need to be made by whoever is "
                "actually present and informed. Regular, even brief, updates to less-involved "
                "family members help prevent decisions from feeling sudden or exclusionary.\n\n"
                "When disagreement about care decisions becomes a recurring pattern rather than a "
                "one-time conflict, a neutral third party — such as a social worker, care manager, "
                "or family mediator — can help the family work through it."
            ),
        },
    ],
}
