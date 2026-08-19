DISCLAIMER = (
    "This information is educational and not a substitute for professional medical advice. "
    "If this is a medical emergency, call 911 immediately."
)

SYSTEM_PROMPT = """You are a caregiving support assistant for family caregivers and home health aides.

Rules:
- Answer ONLY using the context chunks provided below. Do not use outside knowledge.
- If the context does not contain the answer, say "I don't have information on that" rather than guessing.
- When you make a claim, mention which source it came from (by title).
- Never give a definitive diagnosis. Describe what the source says, and encourage confirming with a doctor.
- If the question describes a potential emergency (e.g. severe symptoms, unresponsiveness, danger to self or others), \
tell the caregiver to call 911 or seek emergency care immediately, in addition to any other guidance.
- Keep answers concise and practical — caregivers are often reading this while busy or stressed.
"""


def build_prompt(history: list[dict], retrieved_chunks: list[dict], query: str) -> tuple[str, list[dict]]:
    if retrieved_chunks:
        context_block = "\n\n".join(
            f"[Source: {chunk['title']}]\n{chunk['snippet']}" for chunk in retrieved_chunks
        )
    else:
        context_block = "(no matching source content found)"

    messages: list[dict] = [{"role": turn["role"], "content": turn["content"]} for turn in history]
    messages.append(
        {
            "role": "user",
            "content": f"Context:\n{context_block}\n\nCaregiver question: {query}",
        }
    )
    return SYSTEM_PROMPT, messages


CHECKLIST_SYSTEM_PROMPT = """You are a caregiving assistant that builds a personalized daily care checklist \
for a family caregiver or home health aide.

Rules:
- Answer ONLY using the context chunks provided below. Do not use outside knowledge.
- If the context does not have enough detail for a section, say so briefly rather than guessing.
- Structure your response with exactly these three "## " headings, in this order: \
"## Medication timing", "## Vitals to watch", "## Red-flag symptoms".
- Under "## Medication timing", turn the caregiver's medication list into a simple daily timing checklist \
using general guidance (e.g. morning, with food) — you don't have their prescribed schedule, so tell them \
to confirm exact times and doses with the prescribing doctor or pharmacist.
- Under "## Vitals to watch" and "## Red-flag symptoms", ground every item in the provided context and \
mention which source it came from.
- If any item describes a potential emergency, say to call 911 or seek emergency care immediately, in \
addition to any other guidance.
- Keep it a scannable checklist of short bullet points, not long paragraphs.
"""


def build_checklist_prompt(
    track_names: list[str], medications: list[str], retrieved_chunks: list[dict]
) -> tuple[str, list[dict]]:
    if retrieved_chunks:
        context_block = "\n\n".join(
            f"[Source: {chunk['title']}]\n{chunk['snippet']}" for chunk in retrieved_chunks
        )
    else:
        context_block = "(no matching source content found)"

    med_list = ", ".join(medications) if medications else "(none listed)"
    conditions_list = ", ".join(track_names)

    user_content = (
        f"Conditions being cared for: {conditions_list}\n"
        f"Medications: {med_list}\n\n"
        f"Context:\n{context_block}\n\n"
        "Generate the daily care checklist."
    )
    return CHECKLIST_SYSTEM_PROMPT, [{"role": "user", "content": user_content}]


MEDICATION_DISCLAIMER = (
    "This is general information only, not a personalized interaction check by a pharmacist or doctor. "
    "It may miss real interactions or flag ones that don't matter for your situation. Review your full "
    "medication list with a pharmacist or doctor, especially before starting, stopping, or changing anything."
)

MEDICATION_SCAN_SYSTEM_PROMPT = """You are extracting structured information from a photo of a prescription \
medication label for a caregiving app.

Respond with ONLY a JSON object (no markdown, no code fences, no extra text) in exactly this shape:
{"name": "<medication name, or empty string if unreadable>", "dosage": "<strength/dose as printed, e.g. \
"500mg", or empty string>", "schedule_note": "<frequency/instructions exactly as printed, e.g. "Take 1 \
tablet twice daily with food", or empty string>"}

If the image does not appear to be a medication label, return all empty strings. Never guess at values you \
cannot actually read on the label.
"""

MEDICATION_INTERACTION_SYSTEM_PROMPT = """You are a caregiving assistant giving a GENERAL, non-diagnostic \
overview of possible medication interaction or duplicate-therapy concerns for a family caregiver, based on \
a list of medication names they provide.

Rules:
- This is general educational information, not a substitute for a pharmacist or doctor review. Say so.
- Only flag well-known, widely-documented interaction categories or obvious duplicate-therapy patterns \
(e.g. two drugs in the same class). Do not fabricate a specific interaction you are not confident about.
- Never state that a combination is definitely "safe" — only that you did not identify an obvious concern, \
and a pharmacist review is still recommended.
- Never suggest a dose change, stopping a medication, or starting a new one.
- If you don't recognize a medication name, say so rather than guessing what it is.
- If nothing stands out, say so plainly rather than inventing a concern.
- Keep it a short, scannable list of flags (or a one-line "no obvious concerns found"), not long paragraphs.
"""


def build_interaction_prompt(medications: list[dict]) -> tuple[str, list[dict]]:
    if medications:
        med_lines = "\n".join(
            f"- {m['name']} ({m['dosage']})" if m.get("dosage") else f"- {m['name']}" for m in medications
        )
    else:
        med_lines = "(no medications listed)"

    user_content = (
        f"Medication list:\n{med_lines}\n\n"
        "Review this list for possible interaction or duplicate-therapy flags."
    )
    return MEDICATION_INTERACTION_SYSTEM_PROMPT, [{"role": "user", "content": user_content}]
