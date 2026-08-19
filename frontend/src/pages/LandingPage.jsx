import React from "react";
import { Link, Navigate } from "react-router-dom";
import { useAuth } from "../auth/AuthContext.jsx";
import CaregivingScene from "../components/CaregivingScene.jsx";
import { BookIcon, ChatIcon, ShieldIcon } from "../components/icons.jsx";
import { useSeo } from "../hooks/useSeo.js";

export default function LandingPage() {
  const { token, loading } = useAuth();

  useSeo({
    description:
      "Bite-sized microlearning and AI chat support for family caregivers and home health aides caring for elderly or chronically ill loved ones. Free to start.",
  });

  if (!loading && token) {
    return <Navigate to="/tracks" replace />;
  }

  return (
    <div className="landing">
      <section className="landing-hero">
        <div className="hero-text">
          <h1>Caregiver Training Hub</h1>
          <p className="landing-tagline">
            Bite-sized microlearning and AI chat support for family caregivers and home health
            aides caring for elderly or chronically ill loved ones.
          </p>
          <div className="landing-actions">
            <Link to="/login" className="landing-btn landing-btn-primary">
              Log in
            </Link>
            <Link to="/signup" className="landing-btn landing-btn-secondary">
              Sign up
            </Link>
          </div>
        </div>

        <div className="hero-illustration" aria-hidden="true">
          <CaregivingScene />
        </div>
        <p className="hero-illustration-caption">
          Real support looks like a team — family, caregiver, and healthcare provider, together.
        </p>
      </section>

      <section className="landing-about">
        <h2>What you'll find here</h2>
        <div className="landing-features">
          <div className="landing-feature">
            <div className="feature-icon feature-icon-grey">
              <BookIcon />
            </div>
            <h3>Condition-specific tracks</h3>
            <p>
              Short 3-5 minute lessons and quizzes for Dementia &amp; Alzheimer's care,
              post-stroke recovery, and diabetes management, with more tracks planned.
            </p>
          </div>
          <div className="landing-feature">
            <div className="feature-icon feature-icon-yellow">
              <ChatIcon />
            </div>
            <h3>AI chat, grounded in real guidance</h3>
            <p>
              Ask questions and get answers scoped to your chosen track, with inline citations
              back to the source material — not a black box.
            </p>
          </div>
          <div className="landing-feature">
            <div className="feature-icon feature-icon-orange">
              <ShieldIcon />
            </div>
            <h3>Built with safety in mind</h3>
            <p>
              Every chat response carries a clear disclaimer, and messages that sound
              emergency-adjacent are flagged so you're reminded to call 911 or your care team.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
