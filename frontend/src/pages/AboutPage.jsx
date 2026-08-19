import React from "react";
import { Link } from "react-router-dom";
import AboutScene from "../components/AboutScene.jsx";
import { BookIcon, ChatIcon, ShieldIcon } from "../components/icons.jsx";
import { useSeo } from "../hooks/useSeo.js";

const STEPS = [
  {
    icon: BookIcon,
    title: "Pick a track",
    body: "Choose from 22 short courses — Dementia & Alzheimer's, diabetes, post-stroke recovery, medication safety, communication, burnout, and more — and work through lessons and quizzes at your own pace.",
  },
  {
    icon: ChatIcon,
    title: "Ask questions anytime",
    body: "Chat scoped to that track for fast, grounded answers with citations back to the source material, whenever a question comes up.",
  },
  {
    icon: ShieldIcon,
    title: "Stay safe by design",
    body: "Every answer carries a clear disclaimer, and messages that sound emergency-adjacent are flagged so you're reminded to call 911 or your care team.",
  },
];

export default function AboutPage() {
  useSeo({
    title: "About",
    description:
      "Why Caregiver Training Hub exists: trustworthy, bite-sized caregiving education plus an AI chat you can ask anything, for family caregivers and home health aides with no formal training.",
  });

  return (
    <div className="static-page">
      <section className="static-hero">
        <h1>About Caregiver Training Hub</h1>
        <p className="static-lede">
          Most caregiving falls to family members and home health aides with no formal training —
          learning wound care, medication schedules, and warning signs on the fly, usually in the
          middle of a stressful moment. This is a place to get that knowledge in small pieces,
          plus a chat you can ask anything, without wading through a hundred-page pamphlet.
        </p>
        <div className="hero-illustration hero-illustration-about" aria-hidden="true">
          <AboutScene />
        </div>
        <p className="hero-illustration-caption">
          Training that meets caregivers where the questions actually come up.
        </p>
      </section>

      <section className="static-section">
        <h2>How it works</h2>
        <div className="steps-grid">
          {STEPS.map((step, i) => (
            <div className="step-card" key={step.title}>
              <div className="step-number">{i + 1}</div>
              <div className="feature-icon feature-icon-grey">
                <step.icon />
              </div>
              <h3>{step.title}</h3>
              <p>{step.body}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="static-section">
        <h2>A trust layer, not just answers</h2>
        <p>
          Lesson content and chat answers are written to reflect guidance in the style of trusted
          sources like the National Institute on Aging, the CDC, and Mayo Clinic — with citations
          shown alongside every chat answer so you can see where it came from, not just take our
          word for it. Nothing here replaces your doctor or care team; it's meant to help you ask
          better questions and recognize when something needs their attention.
        </p>
      </section>

      <section className="static-cta">
        <h2>Ready to get started?</h2>
        <div className="landing-actions">
          <Link to="/signup" className="landing-btn landing-btn-primary">
            Create a free account
          </Link>
          <Link to="/features" className="landing-btn landing-btn-secondary">
            See what's included
          </Link>
        </div>
      </section>
    </div>
  );
}
