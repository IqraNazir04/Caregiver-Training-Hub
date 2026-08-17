import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api/client.js";
import { useAuth } from "../auth/AuthContext.jsx";
import { THEMES } from "../themes.js";

export default function ProfilePage() {
  const { token, user, logout, updateSelectedTracks } = useAuth();
  const [tracks, setTracks] = useState([]);
  const [selectedSlugs, setSelectedSlugs] = useState([]);
  const [saving, setSaving] = useState(false);
  const [saved, setSaved] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    api
      .listTracks(token)
      .then(setTracks)
      .catch(() => setTracks([]));
  }, [token]);

  useEffect(() => {
    if (user) setSelectedSlugs(user.selected_tracks || []);
  }, [user]);

  if (!user) return <p>Loading...</p>;

  const toggleTrack = (slug) => {
    setSaved(false);
    setSelectedSlugs((prev) => (prev.includes(slug) ? prev.filter((s) => s !== slug) : [...prev, slug]));
  };

  const isDirty =
    selectedSlugs.length !== (user.selected_tracks || []).length ||
    selectedSlugs.some((s) => !(user.selected_tracks || []).includes(s));

  const saveTopics = async () => {
    setError("");
    setSaving(true);
    try {
      await updateSelectedTracks(selectedSlugs);
      setSaved(true);
    } catch (err) {
      setError(err.message);
    } finally {
      setSaving(false);
    }
  };

  return (
    <div>
      <h1>Your profile</h1>
      <div className="profile-card">
        <div className="profile-avatar">{user.display_name.charAt(0).toUpperCase()}</div>
        <div>
          <h2>{user.display_name}</h2>
          <p className="profile-email">{user.email}</p>
        </div>
      </div>

      <div className="profile-topics">
        <h2 className="profile-section-title">What are you caring for?</h2>
        <p className="profile-section-hint">
          Pick any topics that apply — this is just to help you find relevant tracks faster.
        </p>
        {THEMES.map((theme) => {
          const themeTracks = tracks.filter((t) => t.theme === theme.key);
          if (themeTracks.length === 0) return null;
          return (
            <div className="topic-select" key={theme.key}>
              <span className="topic-select-label">{theme.title}</span>
              <div className="topic-tabs">
                {themeTracks.map((track) => (
                  <button
                    key={track.slug}
                    type="button"
                    className={`topic-tab${selectedSlugs.includes(track.slug) ? " topic-tab-active" : ""}`}
                    onClick={() => toggleTrack(track.slug)}
                    aria-pressed={selectedSlugs.includes(track.slug)}
                  >
                    {track.name}
                  </button>
                ))}
              </div>
            </div>
          );
        })}

        {error && <p className="error-text">{error}</p>}
        <div className="profile-topics-save">
          <button onClick={saveTopics} disabled={!isDirty || saving}>
            {saving ? "Saving..." : "Save changes"}
          </button>
          {saved && !isDirty && <span className="profile-saved-note">Saved</span>}
        </div>
      </div>

      <div className="profile-actions">
        <Link to="/tracks" className="landing-btn landing-btn-primary">
          Go to your tracks
        </Link>
        <Link to="/chat" className="landing-btn landing-btn-secondary">
          Start a chat
        </Link>
        <button onClick={logout}>Log out</button>
      </div>
    </div>
  );
}
