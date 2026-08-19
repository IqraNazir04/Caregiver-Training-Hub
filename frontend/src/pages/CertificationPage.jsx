import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api/client.js";
import { useAuth } from "../auth/AuthContext.jsx";
import { CertificationGraphic } from "../components/PageGraphics.jsx";
import { useSeo } from "../hooks/useSeo.js";

function isComplete(track) {
  return track.lesson_count > 0 && track.completed_count === track.lesson_count;
}

export default function CertificationPage() {
  const { token } = useAuth();
  const [tracks, setTracks] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    api.listTracks(token).then(setTracks).catch((err) => setError(err.message));
  }, [token]);

  useSeo({ title: "Certification", noindex: true });

  if (error) return <p className="error-text">{error}</p>;
  if (!tracks) return <p>Loading certification status...</p>;

  const earned = tracks.filter(isComplete);
  const inProgress = tracks.filter((t) => !isComplete(t) && t.completed_count > 0);

  return (
    <div>
      <div className="page-header">
        <CertificationGraphic className="page-header-graphic" aria-hidden="true" />
        <div className="page-header-text">
          <h1>Certification</h1>
          <p>
            Finish every lesson in a course to earn a certificate of completion, based on your actual quiz
            activity — free anytime you complete a course.
          </p>
        </div>
      </div>

      <section className="theme-section">
        <div className="theme-header">
          <h2>Earned certificates ({earned.length})</h2>
        </div>
        {earned.length === 0 ? (
          <p className="cert-empty-hint">
            You haven't completed a course yet. Finish every lesson in a course to earn your first
            certificate — see your <Link to="/tracks">courses</Link>.
          </p>
        ) : (
          <div className="track-grid">
            {earned.map((t) => (
              <Link key={t.id} to={`/certification/${t.slug}`} className="track-card cert-card-earned">
                <span className="status-badge status-available">Certified</span>
                <h2>{t.name}</h2>
                <p>{t.description}</p>
              </Link>
            ))}
          </div>
        )}
      </section>

      {inProgress.length > 0 && (
        <section className="theme-section">
          <div className="theme-header">
            <h2>In progress</h2>
          </div>
          <div className="track-grid">
            {inProgress.map((t) => {
              const pct = Math.round((t.completed_count / t.lesson_count) * 100);
              return (
                <Link key={t.id} to={`/tracks/${t.slug}`} className="track-card">
                  <h2>{t.name}</h2>
                  <div className="track-progress">
                    <div className="track-progress-bar">
                      <div className="track-progress-fill" style={{ width: `${pct}%` }} />
                    </div>
                    <span className="track-progress-label">
                      {t.completed_count} of {t.lesson_count} lessons complete
                    </span>
                  </div>
                </Link>
              );
            })}
          </div>
        </section>
      )}
    </div>
  );
}
