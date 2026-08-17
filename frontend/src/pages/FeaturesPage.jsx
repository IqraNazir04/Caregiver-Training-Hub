import React from "react";
import { Link } from "react-router-dom";
import { SideDecorLeft, SideDecorRight } from "../components/SideDecor.jsx";
import {
  BookIcon,
  CalendarIcon,
  ChatIcon,
  ChecklistIcon,
  HeartIcon,
  MicIcon,
  PillIcon,
  ShieldIcon,
  UsersIcon,
} from "../components/icons.jsx";

const FEATURES = [
  {
    icon: BookIcon,
    color: "grey",
    title: "Condition-specific learning tracks",
    body: "Short 3-5 minute lessons and quizzes for Dementia & Alzheimer's care, post-stroke recovery, and diabetes management, with more tracks planned.",
    available: true,
  },
  {
    icon: ChatIcon,
    color: "yellow",
    title: "AI chat, grounded in real guidance",
    body: "Ask questions scoped to a track and get answers with inline citations back to the source material, plus a clear medical disclaimer on every response.",
    available: true,
  },
  {
    icon: ChecklistIcon,
    color: "orange",
    title: "Daily care checklist generator",
    body: "Enter a patient's conditions and medications to get a personalized daily routine — medication timing, vitals to watch, and condition-specific red-flag symptoms.",
    available: false,
  },
  {
    icon: PillIcon,
    color: "grey",
    title: "Medication interaction & schedule assistant",
    body: "Photo-scan prescription bottles to build a medication schedule, flag dangerous interactions or duplicate therapies, and get reminders.",
    available: false,
  },
  {
    icon: ShieldIcon,
    color: "yellow",
    title: "Symptom triage with escalation tiers",
    body: "Three-tier guidance — monitor, call the doctor within 24-48h, or seek emergency care now — mirroring clinical triage protocols, with next steps for each tier.",
    available: false,
  },
  {
    icon: MicIcon,
    color: "orange",
    title: "Voice-first mode",
    body: "A hands-free assistant for when you're mid-task — changing a bandage, holding a patient — so you can ask a question out loud instead of typing.",
    available: false,
  },
  {
    icon: HeartIcon,
    color: "grey",
    title: "Burnout & respite support",
    body: "A short weekly check-in to track caregiver stress, surfacing local respite care resources and support groups when you need a break.",
    available: false,
  },
  {
    icon: UsersIcon,
    color: "yellow",
    title: "Family care coordination board",
    body: "A shared log for families splitting caregiving duties — who gave medication when, doctor's notes, upcoming appointments — visible to everyone involved.",
    available: false,
  },
  {
    icon: CalendarIcon,
    color: "orange",
    title: "Appointment prep tool",
    body: "Describe recent changes or concerns and get help drafting questions for the doctor, so nothing gets forgotten in a rushed 10-minute visit.",
    available: false,
  },
];

export default function FeaturesPage() {
  return (
    <div className="static-page">
      <SideDecorLeft />
      <SideDecorRight />
      <section className="static-hero">
        <h1>Features</h1>
        <p className="static-lede">
          Two pieces are live today — learning tracks and grounded AI chat. Everything else below
          is on the roadmap.
        </p>
      </section>

      <div className="features-grid">
        {FEATURES.map((f) => (
          <div className="feature-tile" key={f.title}>
            <div className={`feature-icon feature-icon-${f.color}`}>
              <f.icon />
            </div>
            <span className={`status-badge ${f.available ? "status-available" : "status-soon"}`}>
              {f.available ? "Available now" : "Coming soon"}
            </span>
            <h3>{f.title}</h3>
            <p>{f.body}</p>
          </div>
        ))}
      </div>

      <section className="static-cta">
        <h2>Start with what's live today</h2>
        <div className="landing-actions">
          <Link to="/signup" className="landing-btn landing-btn-primary">
            Sign up
          </Link>
          <Link to="/login" className="landing-btn landing-btn-secondary">
            Log in
          </Link>
        </div>
      </section>
    </div>
  );
}
