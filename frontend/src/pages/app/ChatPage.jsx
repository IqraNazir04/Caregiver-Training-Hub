import React, { useEffect, useRef, useState } from "react";
import { useParams } from "react-router-dom";
import { api } from "../../api/client.js";
import { useAuth } from "../../auth/AuthContext.jsx";
import { renderMarkdown } from "../../markdown.jsx";
import { ChatGraphic } from "../../components/PageGraphics.jsx";
import { useSeo } from "../../hooks/useSeo.js";

export default function ChatPage() {
  const { slug } = useParams();
  const { token } = useAuth();
  const [sessionId, setSessionId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [sending, setSending] = useState(false);
  const [error, setError] = useState("");
  const bottomRef = useRef(null);

  useSeo({ title: slug ? `Chat: ${slug.replace(/-/g, " ")}` : "Chat", noindex: true });

  useEffect(() => {
    api
      .createChatSession(token, slug || null)
      .then((session) => setSessionId(session.id))
      .catch((err) => setError(err.message));
  }, [token, slug]);

  useEffect(() => {
    if (messages.length > 0) {
      bottomRef.current?.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages]);

  const send = async (e) => {
    e.preventDefault();
    if (!input.trim() || !sessionId) return;
    const content = input;
    setInput("");
    setError("");
    setMessages((prev) => [...prev, { role: "user", content }]);
    setSending(true);
    try {
      const reply = await api.sendMessage(token, sessionId, content);
      setMessages((prev) => [...prev, reply]);
    } catch (err) {
      setError(err.message);
    } finally {
      setSending(false);
    }
  };

  return (
    <div className="chat-page">
      <div className="page-header page-header-compact">
        <ChatGraphic className="page-header-graphic" aria-hidden="true" />
        <div className="page-header-text">
          <h1>{slug ? `Chat: ${slug.replace(/-/g, " ")}` : "General caregiving chat"}</h1>
        </div>
      </div>
      <div className="chat-messages">
        {messages.map((m, i) => (
          <div key={i} className={`chat-bubble chat-bubble-${m.role}`}>
            {m.role === "assistant" ? (
              <div className="chat-markdown">{renderMarkdown(m.content)}</div>
            ) : (
              <p>{m.content}</p>
            )}
            {m.role === "assistant" && (
              <>
                {m.is_flagged && (
                  <div className="emergency-banner">
                    This sounds urgent. If this is an emergency, call 911 now.
                  </div>
                )}
                {m.citations && m.citations.length > 0 && (
                  <details className="citations">
                    <summary>Sources ({m.citations.length})</summary>
                    <ul>
                      {m.citations.map((c) => (
                        <li key={c.source_document_id}>
                          <strong>{c.title}</strong>
                          <p>{c.snippet}</p>
                        </li>
                      ))}
                    </ul>
                  </details>
                )}
                <p className="disclaimer">{m.disclaimer}</p>
              </>
            )}
          </div>
        ))}
        <div ref={bottomRef} />
      </div>
      {error && <p className="error-text">{error}</p>}
      <form className="chat-input" onSubmit={send}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a caregiving question..."
          disabled={!sessionId || sending}
        />
        <button type="submit" disabled={!sessionId || sending}>
          {sending ? "Sending..." : "Send"}
        </button>
      </form>
    </div>
  );
}
