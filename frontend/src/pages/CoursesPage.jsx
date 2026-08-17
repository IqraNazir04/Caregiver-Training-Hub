import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api/client.js";
import { useAuth } from "../auth/AuthContext.jsx";
import { THEMES } from "../themes.js";

function CourseCard({ track, loggedIn }) {
  return (
    <Link to={loggedIn ? `/tracks/${track.slug}` : "/signup"} className="track-card">
      <h2>{track.name}</h2>
      <p>{track.description}</p>
      {track.lesson_count > 0 && (
        <span className="course-lesson-count">
          {track.lesson_count} lesson{track.lesson_count === 1 ? "" : "s"}
        </span>
      )}
    </Link>
  );
}

export default function CoursesPage() {
  const { token } = useAuth();
  const [tracks, setTracks] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    api.listPublicTracks().then(setTracks).catch((err) => setError(err.message));
  }, []);

  if (error) return <p className="error-text">{error}</p>;
  if (!tracks) return <p>Loading courses...</p>;

  return (
    <div className="static-page">
      <section className="static-hero">
        <h1>Courses</h1>
        <p className="static-lede">
          Every course is a short, condition-specific learning track — a few 3-5 minute lessons plus a quiz,
          grounded in real caregiving guidance. Browse what's available, then sign up to start tracking your
          progress and chat about any course.
        </p>
      </section>

      <div className="theme-list">
        {THEMES.map((theme) => {
          const themeTracks = tracks.filter((t) => t.theme === theme.key);
          if (themeTracks.length === 0 && theme.plannedTitles.length === 0) return null;

          return (
            <section className="theme-section" key={theme.key}>
              <div className="theme-header">
                <h2>{theme.title}</h2>
                <p>{theme.description}</p>
              </div>
              <div className="track-grid">
                {themeTracks.map((track) => (
                  <CourseCard key={track.id} track={track} loggedIn={!!token} />
                ))}
                {theme.plannedTitles.map((title) => (
                  <div className="track-card track-card-soon" key={title}>
                    <span className="status-badge status-soon">Coming soon</span>
                    <h2>{title}</h2>
                  </div>
                ))}
              </div>
            </section>
          );
        })}
      </div>

      <section className="static-cta">
        <h2>Ready to start learning?</h2>
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
