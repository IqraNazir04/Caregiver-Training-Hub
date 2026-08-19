import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client.js";
import { useAuth } from "../auth/AuthContext.jsx";
import { useSeo } from "../hooks/useSeo.js";

export default function CertificateViewPage() {
  const { slug } = useParams();
  const { token, user } = useAuth();
  const [track, setTrack] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    api.getTrack(token, slug).then(setTrack).catch((err) => setError(err.message));
  }, [token, slug]);

  useSeo({ title: track ? `${track.name} Certificate` : "Certificate", noindex: true });

  if (error) return <p className="error-text">{error}</p>;
  if (!track || !user) return <p>Loading certificate...</p>;

  const isComplete = track.lesson_count > 0 && track.completed_count === track.lesson_count;

  if (!isComplete) {
    return (
      <div>
        <h1>Certificate not yet earned</h1>
        <p>
          You've completed {track.completed_count} of {track.lesson_count} lessons in {track.name}. Finish
          the remaining lessons to unlock this certificate.
        </p>
        <Link to={`/tracks/${track.slug}`} className="landing-btn landing-btn-primary">
          Continue the course
        </Link>
      </div>
    );
  }

  const completionDate = track.lessons
    .map((l) => l.completed_at)
    .filter(Boolean)
    .sort()
    .pop();

  const formattedDate = completionDate
    ? new Date(completionDate).toLocaleDateString(undefined, { year: "numeric", month: "long", day: "numeric" })
    : "";

  return (
    <div>
      <div className="certificate">
        <div className="certificate-border">
          <p className="certificate-eyebrow">Certificate of Completion</p>
          <h1 className="certificate-name">{user.display_name}</h1>
          <p className="certificate-body">has successfully completed the course</p>
          <h2 className="certificate-track">{track.name}</h2>
          {formattedDate && <p className="certificate-date">Completed {formattedDate}</p>}
          <p className="certificate-footer">Caregiver Training Hub</p>
        </div>
      </div>
      <div className="certificate-actions no-print">
        <button onClick={() => window.print()}>Print certificate</button>
        <Link to="/certification" className="landing-btn landing-btn-secondary">
          Back to certification
        </Link>
      </div>
    </div>
  );
}
