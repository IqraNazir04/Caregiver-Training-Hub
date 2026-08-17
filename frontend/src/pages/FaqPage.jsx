import React from "react";

const FAQS = [
  {
    q: "Is this a substitute for medical advice?",
    a: "No. Lessons and chat answers are educational, not a diagnosis or treatment plan. Every chat response carries a disclaimer, and you should always confirm care decisions with the patient's doctor or care team.",
  },
  {
    q: "What happens if I ask about a possible emergency?",
    a: "Messages that sound emergency-adjacent are flagged in the chat with a clear warning to call 911 or seek emergency care immediately, and the interaction is logged for safety review. This is an early, lightweight version of a fuller symptom-triage feature we're building.",
  },
  {
    q: "Where does the lesson and chat content come from?",
    a: "Content is written to reflect guidance in the style of trusted sources such as the National Institute on Aging, the CDC, and Mayo Clinic. Chat answers cite the specific source document they're drawn from, so you can see where the information came from.",
  },
  {
    q: "Which conditions are covered right now?",
    a: "Three tracks are live today: Dementia & Alzheimer's care, post-stroke recovery, and diabetes management. More condition-specific tracks are planned.",
  },
  {
    q: "Is my account information private?",
    a: "Your account is protected by a password and used only to save your progress and chat history. We don't share your data with third parties.",
  },
  {
    q: "What's coming next?",
    a: "A daily care checklist generator, a medication interaction assistant, full symptom triage, voice-first mode, burnout check-ins, a family coordination board, and an appointment-prep tool — see the Features page for details on each.",
  },
];

export default function FaqPage() {
  return (
    <div className="static-page">
      <section className="static-hero">
        <h1>Frequently asked questions</h1>
        <p className="static-lede">
          Common questions about how Caregiver Training Hub works and what it can and can't do.
        </p>
      </section>

      <div className="faq-list">
        {FAQS.map((item) => (
          <details className="faq-item" key={item.q}>
            <summary>{item.q}</summary>
            <p>{item.a}</p>
          </details>
        ))}
      </div>
    </div>
  );
}
