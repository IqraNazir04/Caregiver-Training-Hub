const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

async function request(path, { method = "GET", body, token, form, formData } = {}) {
  const headers = {};
  if (token) headers["Authorization"] = `Bearer ${token}`;

  let payload = body;
  if (formData) {
    payload = formData; // let the browser set the multipart Content-Type + boundary
  } else if (form) {
    payload = new URLSearchParams(body);
    headers["Content-Type"] = "application/x-www-form-urlencoded";
  } else if (body !== undefined) {
    headers["Content-Type"] = "application/json";
    payload = JSON.stringify(body);
  }

  const response = await fetch(`${API_URL}${path}`, { method, headers, body: payload });

  if (!response.ok) {
    let detail = response.statusText;
    try {
      const errorBody = await response.json();
      detail = errorBody.detail || detail;
    } catch {
      // ignore JSON parse failure, fall back to statusText
    }
    throw new Error(typeof detail === "string" ? detail : JSON.stringify(detail));
  }

  if (response.status === 204) return null;
  return response.json();
}

export const api = {
  signup: (email, password, displayName) =>
    request("/auth/signup", {
      method: "POST",
      body: { email, password, display_name: displayName },
    }),
  login: (email, password) =>
    request("/auth/login", {
      method: "POST",
      form: true,
      body: { username: email, password },
    }),
  me: (token) => request("/auth/me", { token }),
  updateSelectedTracks: (token, selectedTracks) =>
    request("/auth/me", { method: "PATCH", token, body: { selected_tracks: selectedTracks } }),

  listTracks: (token) => request("/tracks", { token }),
  listPublicTracks: () => request("/tracks/public"),
  getTrack: (token, slug) => request(`/tracks/${slug}`, { token }),
  getLesson: (token, slug, lessonId) => request(`/tracks/${slug}/lessons/${lessonId}`, { token }),
  submitQuiz: (token, slug, lessonId, answers) =>
    request(`/tracks/${slug}/lessons/${lessonId}/quiz/submit`, {
      method: "POST",
      token,
      body: { answers },
    }),

  createChatSession: (token, trackSlug) =>
    request("/chat/sessions", { method: "POST", token, body: { track_slug: trackSlug } }),
  listMessages: (token, sessionId) => request(`/chat/sessions/${sessionId}/messages`, { token }),
  sendMessage: (token, sessionId, content) =>
    request(`/chat/sessions/${sessionId}/messages`, {
      method: "POST",
      token,
      body: { content },
    }),

  generateChecklist: (token, trackSlugs, medications) =>
    request("/checklist/generate", {
      method: "POST",
      token,
      body: { track_slugs: trackSlugs, medications },
    }),

  listMedications: (token) => request("/medications", { token }),
  addMedication: (token, medication) =>
    request("/medications", { method: "POST", token, body: medication }),
  deleteMedication: (token, id) => request(`/medications/${id}`, { method: "DELETE", token }),
  scanMedicationPhoto: (token, file) => {
    const formData = new FormData();
    formData.append("file", file);
    return request("/medications/scan", { method: "POST", token, formData });
  },
  checkMedicationInteractions: (token) =>
    request("/medications/check-interactions", { method: "POST", token }),
};
