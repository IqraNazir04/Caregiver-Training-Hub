import React, { useEffect, useState } from "react";
import { api } from "../api/client.js";
import { useAuth } from "../auth/AuthContext.jsx";
import { renderMarkdown } from "../markdown.jsx";
import { THEMES } from "../themes.js";
import { ChecklistGraphic } from "../components/PageGraphics.jsx";
import { useSeo } from "../hooks/useSeo.js";

export default function ChecklistPage() {
  const { token, user } = useAuth();
  const [tracks, setTracks] = useState([]);
  const [selectedSlugs, setSelectedSlugs] = useState([]);
  const [medicationsText, setMedicationsText] = useState("");
  const [result, setResult] = useState(null);
  const [generating, setGenerating] = useState(false);
  const [error, setError] = useState("");

  useSeo({ title: "Daily Care Checklist", noindex: true });

  useEffect(() => {
    api
      .listTracks(token)
      .then(setTracks)
      .catch(() => setTracks([]));
  }, [token]);

  useEffect(() => {
    if (user) setSelectedSlugs(user.selected_tracks || []);
  }, [user]);

  const toggleTrack = (slug) => {
    setSelectedSlugs((prev) => (prev.includes(slug) ? prev.filter((s) => s !== slug) : [...prev, slug]));
  };

  const generate = async (e) => {
    e.preventDefault();
    if (selectedSlugs.length === 0) {
      setError("Pick at least one condition to build a checklist for.");
      return;
    }
    setError("");
    setGenerating(true);
    setResult(null);
    const medications = medicationsText
      .split("\n")
      .map((m) => m.trim())
      .filter(Boolean);
    try {
      const res = await api.generateChecklist(token, selectedSlugs, medications);
      setResult(res);
    } catch (err) {
      setError(err.message);
    } finally {
      setGenerating(false);
    }
  };

  return (
    <div>
      <div className="page-header">
        <ChecklistGraphic className="page-header-graphic" aria-hidden="true" />
        <div className="page-header-text">
          <h1>Daily care checklist</h1>
          <p>
            Pick the conditions you're caring for and list any medications, and get a personalized daily
            checklist — medication timing, vitals to watch, and red-flag symptoms — grounded in your
            tracks' source material.
          </p>
        </div>
      </div>

      <form className="checklist-form no-print" onSubmit={generate}>
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

        <label className="checklist-med-label">
          Medications (one per line, optional)
          <textarea
            className="checklist-med-input"
            rows={4}
            value={medicationsText}
            onChange={(e) => setMedicationsText(e.target.value)}
            placeholder={"Metformin\nLisinopril"}
          />
        </label>

        {error && <p className="error-text">{error}</p>}
        <button type="submit" disabled={generating}>
          {generating ? "Generating..." : "Generate checklist"}
        </button>
      </form>

      {result && (
        <div className="checklist-result">
          <div className="chat-markdown">{renderMarkdown(result.content)}</div>
          {result.citations.length > 0 && (
            <details className="citations">
              <summary>Sources ({result.citations.length})</summary>
              <ul>
                {result.citations.map((c) => (
                  <li key={c.source_document_id}>
                    <strong>{c.title}</strong>
                    <p>{c.snippet}</p>
                  </li>
                ))}
              </ul>
            </details>
          )}
          <p className="disclaimer">{result.disclaimer}</p>
          <div className="checklist-actions no-print">
            <button onClick={() => window.print()}>Print checklist</button>
          </div>
        </div>
      )}
    </div>
  );
}
