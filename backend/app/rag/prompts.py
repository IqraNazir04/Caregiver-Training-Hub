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
