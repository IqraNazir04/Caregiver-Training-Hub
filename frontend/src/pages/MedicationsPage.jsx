import React, { useEffect, useState } from "react";
import { api } from "../api/client.js";
import { useAuth } from "../auth/AuthContext.jsx";
import { renderMarkdown } from "../markdown.jsx";
import { MedicationGraphic } from "../components/PageGraphics.jsx";
import { useSeo } from "../hooks/useSeo.js";

export default function MedicationsPage() {
  const { token } = useAuth();
  useSeo({ title: "Medication Assistant", noindex: true });
  const [medications, setMedications] = useState(null);
  const [name, setName] = useState("");
  const [dosage, setDosage] = useState("");
  const [scheduleNote, setScheduleNote] = useState("");
  const [saving, setSaving] = useState(false);
  const [scanning, setScanning] = useState(false);
  const [error, setError] = useState("");

  const [interactionResult, setInteractionResult] = useState(null);
  const [checking, setChecking] = useState(false);
  const [checkError, setCheckError] = useState("");

  const load = () => {
    api
      .listMedications(token)
      .then(setMedications)
      .catch((err) => setError(err.message));
  };

  useEffect(load, [token]);

  const resetForm = () => {
    setName("");
    setDosage("");
    setScheduleNote("");
  };

  const addMedication = async (e) => {
    e.preventDefault();
    if (!name.trim()) {
      setError("Enter a medication name.");
      return;
    }
    setError("");
    setSaving(true);
    try {
      await api.addMedication(token, { name: name.trim(), dosage: dosage.trim(), schedule_note: scheduleNote.trim() });
      resetForm();
      load();
    } catch (err) {
      setError(err.message);
    } finally {
      setSaving(false);
    }
  };

  const removeMedication = async (id) => {
    try {
      await api.deleteMedication(token, id);
      load();
    } catch (err) {
      setError(err.message);
    }
  };

  const scanPhoto = async (e) => {
    const file = e.target.files?.[0];
    e.target.value = "";
    if (!file) return;
    setError("");
    setScanning(true);
    try {
      const scanned = await api.scanMedicationPhoto(token, file);
      setName(scanned.name);
      setDosage(scanned.dosage);
      setScheduleNote(scanned.schedule_note);
      if (!scanned.name) {
        setError("Couldn't read a medication name from that photo — try a clearer shot, or enter it manually below.");
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setScanning(false);
    }
  };

  const checkInteractions = async () => {
    setCheckError("");
    setChecking(true);
    setInteractionResult(null);
    try {
      const res = await api.checkMedicationInteractions(token);
      setInteractionResult(res);
    } catch (err) {
      setCheckError(err.message);
    } finally {
      setChecking(false);
    }
  };

  if (!medications) return <p>Loading medications...</p>;

  return (
    <div>
      <div className="page-header">
        <MedicationGraphic className="page-header-graphic" aria-hidden="true" />
        <div className="page-header-text">
          <h1>Medication assistant</h1>
          <p>
            Keep a list of medications, scan a label photo to add one quickly, and get a general
            interaction/duplicate-therapy check — always confirm with a pharmacist or doctor before acting
            on it.
          </p>
        </div>
      </div>

      <div className="medication-list">
        {medications.length === 0 ? (
          <p className="cert-empty-hint">No medications added yet.</p>
        ) : (
          medications.map((m) => (
            <div className="medication-item" key={m.id}>
              <div>
                <strong>{m.name}</strong>
                {m.dosage && <span className="medication-dosage"> — {m.dosage}</span>}
                {m.schedule_note && <p className="medication-schedule-note">{m.schedule_note}</p>}
              </div>
              <button onClick={() => removeMedication(m.id)}>Remove</button>
            </div>
          ))
        )}
      </div>

      <form className="checklist-form" onSubmit={addMedication}>
        <label className="checklist-med-label">
          Scan a label photo (optional)
          <input type="file" accept="image/jpeg,image/png,image/webp,image/gif" onChange={scanPhoto} disabled={scanning} />
        </label>
        {scanning && <p>Reading the label...</p>}

        <label className="checklist-med-label">
          Medication name
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Metformin" />
        </label>
        <label className="checklist-med-label">
          Dosage
          <input type="text" value={dosage} onChange={(e) => setDosage(e.target.value)} placeholder="500mg" />
        </label>
        <label className="checklist-med-label">
          Schedule note
          <input
            type="text"
            value={scheduleNote}
            onChange={(e) => setScheduleNote(e.target.value)}
            placeholder="Twice daily with food"
          />
        </label>

        {error && <p className="error-text">{error}</p>}
        <button type="submit" disabled={saving}>
          {saving ? "Saving..." : "Add medication"}
        </button>
      </form>

      <div className="checklist-actions">
        <button onClick={checkInteractions} disabled={checking || medications.length === 0}>
          {checking ? "Checking..." : "Check for interactions"}
        </button>
      </div>
      {checkError && <p className="error-text">{checkError}</p>}

      {interactionResult && (
        <div className="checklist-result medication-interaction-result">
          <div className="chat-markdown">{renderMarkdown(interactionResult.content)}</div>
          <p className="medication-disclaimer">{interactionResult.disclaimer}</p>
        </div>
      )}
    </div>
  );
}
