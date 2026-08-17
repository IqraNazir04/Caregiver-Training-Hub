"""Seed content for the Nutrition & Meal Planning track.

Written as plausible caregiving guidance in the style of NIA/Academy of Nutrition and Dietetics
materials for demo/seed purposes — not scraped or verbatim from those sources. Replace with
vetted, properly licensed source text before any real-world use.
"""

TRACK = {
    "slug": "nutrition-meal-planning",
    "name": "Nutrition & Meal Planning",
    "theme": "practical-skills",
    "description": "Practical approaches to feeding a care recipient well, including common eating challenges and simple meal planning.",
    "lessons": [
        {
            "title": "Common eating challenges and what helps",
            "estimated_minutes": 5,
            "body_markdown": (
                "## Reduced appetite is common, not always a crisis\n\n"
                "Illness, medication side effects, and reduced activity all lower appetite. Small, "
                "frequent, nutrient-dense meals often work better than three large meals when "
                "appetite is low.\n\n"
                "## Chewing and swallowing changes\n\n"
                "Coughing during meals, taking a long time to eat, or avoiding certain textures "
                "can signal swallowing difficulty. This is worth mentioning to a doctor — softer "
                "textures or thickened liquids may be recommended, and it shouldn't be managed by "
                "guesswork alone.\n\n"
                "## Make mealtime easier, not just the food\n\n"
                "Adaptive utensils, non-slip plates, and a calm, unhurried setting can matter as "
                "much as what's actually being served."
            ),
            "quiz": [
                {
                    "question_text": "What often works better than three large meals when appetite is low?",
                    "choices": [
                        "Skipping meals until hunger returns",
                        "Small, frequent, nutrient-dense meals",
                        "One very large meal per day",
                    ],
                    "correct_index": 1,
                    "explanation": "Smaller, more frequent meals are often easier to manage and more effective than large meals when someone's appetite is reduced.",
                },
                {
                    "question_text": "What should prompt a conversation with a doctor rather than guesswork at home?",
                    "choices": [
                        "A preference for one food over another",
                        "Coughing during meals or a long time spent chewing",
                        "Eating slightly less than usual on one day",
                    ],
                    "correct_index": 1,
                    "explanation": "Coughing during meals or unusually prolonged chewing can signal a swallowing difficulty that needs a professional evaluation, not home guesswork.",
                },
            ],
        },
        {
            "title": "Simple, sustainable meal planning",
            "estimated_minutes": 4,
            "body_markdown": (
                "## Plan around a rotation, not new recipes daily\n\n"
                "A rotation of 7-10 meals the person reliably eats and tolerates well is more "
                "sustainable than planning something new every day. Variety still matters, but it "
                "doesn't need to be constant.\n\n"
                "## Batch what you can\n\n"
                "Cooking proteins or grains in larger batches and portioning them for the week "
                "reduces daily decision-making and effort, especially on harder days.\n\n"
                "## Loop in a dietitian for specific conditions\n\n"
                "Diabetes, kidney disease, and swallowing difficulties all have specific dietary "
                "considerations. A registered dietitian can tailor a plan rather than relying on "
                "general nutrition advice alone."
            ),
            "quiz": [
                {
                    "question_text": "What's a more sustainable meal-planning approach than a new recipe every day?",
                    "choices": [
                        "A rotation of reliable meals the person tolerates well",
                        "Ordering delivery every night",
                        "Skipping meal planning entirely",
                    ],
                    "correct_index": 0,
                    "explanation": "A manageable rotation reduces daily decision-making while still allowing for some variety.",
                },
                {
                    "question_text": "When should a registered dietitian be brought in?",
                    "choices": [
                        "Only if the caregiver enjoys cooking",
                        "For specific conditions like diabetes or kidney disease that have particular dietary needs",
                        "Dietitians aren't relevant to caregiving",
                    ],
                    "correct_index": 1,
                    "explanation": "Conditions like diabetes, kidney disease, or swallowing difficulties benefit from a dietitian's tailored guidance rather than general advice.",
                },
            ],
        },
    ],
    "source_documents": [
        {
            "title": "Managing Appetite and Eating Challenges",
            "source_name": "National Institute on Aging (sample/seed content)",
            "url": "https://www.nia.nih.gov/health/healthy-eating-nutrition-tips-older-adults",
            "body_text": (
                "Reduced appetite is a common effect of illness, medication side effects, and "
                "lower activity levels. Small, frequent, nutrient-dense meals often work better "
                "than three large meals when appetite is low. Signs such as coughing during meals, "
                "taking an unusually long time to eat, or avoiding certain textures can indicate a "
                "swallowing difficulty and should be raised with a doctor rather than managed by "
                "guesswork, since softer textures or thickened liquids may be recommended.\n\n"
                "Making mealtime itself easier — through adaptive utensils, non-slip plates, and an "
                "unhurried, calm setting — can matter as much as the food being served."
            ),
        },
        {
            "title": "Sustainable Meal Planning for Caregivers",
            "source_name": "Academy of Nutrition and Dietetics (sample/seed content)",
            "url": "https://www.eatright.org/health/wellness/caregiving",
            "body_text": (
                "A rotation of seven to ten meals that a care recipient reliably eats and "
                "tolerates well tends to be more sustainable for caregivers than planning a new "
                "recipe every day, while still allowing for some variety. Batch-cooking proteins "
                "or grains and portioning them for the week reduces daily decision-making and "
                "effort.\n\n"
                "For conditions with specific dietary considerations, such as diabetes, kidney "
                "disease, or swallowing difficulties, a registered dietitian can build a tailored "
                "plan rather than relying on general nutrition guidance alone."
            ),
        },
    ],
}
