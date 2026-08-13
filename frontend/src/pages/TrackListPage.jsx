import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api/client.js";
import { useAuth } from "../auth/AuthContext.jsx";

export default function TrackListPage() {
  const { token } = useAuth();
  const [tracks, setTracks] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    api.listTracks(token).then(setTracks).catch((err) => setError(err.message));
  }, [token]);

  if (error) return <p className="error-text">{error}</p>;
  if (!tracks) return <p>Loading tracks...</p>;

  return (
    <div>
      <h1>Learning tracks</h1>
      <p>
        Pick a condition to learn about, or{" "}
        <Link to="/chat">start a general chat</Link>.
      </p>
      <div className="track-grid">
        {tracks.map((track) => (
          <Link key={track.id} to={`/tracks/${track.slug}`} className="track-card">
            <h2>{track.name}</h2>
            <p>{track.description}</p>
          </Link>
        ))}
      </div>
    </div>
  );
}
