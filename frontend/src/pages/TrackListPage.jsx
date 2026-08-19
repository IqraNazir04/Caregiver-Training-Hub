import React, { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api/client.js";
import { useAuth } from "../auth/AuthContext.jsx";
import { useSeo } from "../hooks/useSeo.js";
import { THEMES } from "../themes.js";

function TrackCard({ track, recommended }) {
  const pct = track.lesson_count > 0 ? Math.round((track.completed_count / track.lesson_count) * 100) : 0;
  return (
    <Link to={`/tracks/${track.slug}`} className="track-card">
      {recommended && <span className="status-badge status-available">Matches your topics</span>}
      <h2>{track.name}</h2>
      <p>{track.description}</p>
      {track.lesson_count > 0 && (
        <div className="track-progress">
          <div className="track-progress-bar">
            <div className="track-progress-fill" style={{ width: `${pct}%` }} />
          </div>
          <span className="track-progress-label">
            {track.completed_count} of {track.lesson_count} lessons complete
          </span>
        </div>
      )}
    </Link>
  );
}

export default function TrackListPage() {
  const { token, user } = useAuth();
  const [tracks, setTracks] = useState(null);
  const [error, setError] = useState("");
  const [query, setQuery] = useState("");

  useEffect(() => {
    api.listTracks(token).then(setTracks).catch((err) => setError(err.message));
  }, [token]);

  useSeo({ title: "Your Tracks", noindex: true });

  const themeByKey = useMemo(() => Object.fromEntries(THEMES.map((t) => [t.key, t])), []);

  if (error) return <p className="error-text">{error}</p>;
  if (!tracks) return <p>Loading tracks...</p>;

  const q = query.trim().toLowerCase();
  const matchesQuery = (track) => {
    if (!q) return true;
    const theme = themeByKey[track.theme];
    const haystack = `${track.name} ${track.description} ${theme ? theme.title : ""}`.toLowerCase();
    return haystack.includes(q);
  };

  const selectedSlugs = new Set(user?.selected_tracks || []);
  const recommended = tracks.filter((t) => selectedSlugs.has(t.slug) && matchesQuery(t));
  const visibleTracks = tracks.filter(matchesQuery);

  return (
    <div>
      <h1>Learning tracks</h1>
      <p>
        Pick a topic to learn about, or <Link to="/chat">start a general chat</Link>.
      </p>

      <input
        type="search"
        className="track-search"
        placeholder="Search tracks by keyword (e.g. medication, grief, mobility)..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        aria-label="Search learning tracks"
      />

      {recommended.length > 0 && (
        <section className="theme-section">
          <div className="theme-header">
            <h2>Recommended for you</h2>
            <p>
              Based on what you told us you're caring for on your <Link to="/profile">profile</Link> — update it
              anytime.
            </p>
          </div>
          <div className="track-grid">
            {recommended.map((track) => (
              <TrackCard key={`rec-${track.id}`} track={track} recommended />
            ))}
          </div>
        </section>
      )}

      <div className="theme-list">
        {THEMES.map((theme) => {
          const themeTracks = tracks.filter((t) => t.theme === theme.key && matchesQuery(t));
          const showPlanned = !q;
          if (themeTracks.length === 0 && (!showPlanned || theme.plannedTitles.length === 0)) return null;

          return (
            <section className="theme-section" key={theme.key}>
              <div className="theme-header">
                <h2>{theme.title}</h2>
                <p>{theme.description}</p>
              </div>
              <div className="track-grid">
                {themeTracks.map((track) => (
                  <TrackCard key={track.id} track={track} recommended={selectedSlugs.has(track.slug)} />
                ))}
                {showPlanned &&
                  theme.plannedTitles.map((title) => (
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

      {q && visibleTracks.length === 0 && (
        <p className="track-search-empty">No tracks match "{query}". Try a different keyword.</p>
      )}
    </div>
  );
}
