import React, { useEffect, useRef, useState } from "react";
import { useParams } from "react-router-dom";
import { api } from "../api/client.js";
import { useAuth } from "../auth/AuthContext.jsx";

function renderInline(text, keyPrefix) {
  return text.split(/(\*\*.+?\*\*|\*.+?\*)/g).map((part, i) => {
    if (part.startsWith("**") && part.endsWith("**")) {
      return <strong key={`${keyPrefix}-${i}`}>{part.slice(2, -2)}</strong>;
    }
    if (part.startsWith("*") && part.endsWith("*")) {
      return <em key={`${keyPrefix}-${i}`}>{part.slice(1, -1)}</em>;
    }
    return part;
  });
}

function renderChatMarkdown(text) {
  const blocks = [];
  let list = null;

  text.split("\n").forEach((rawLine) => {
    const line = rawLine.trim();
    if (!line) {
      return;
    }
    const bullet = line.match(/^[-*]\s+(.*)/);
    if (bullet) {
      if (!list) {
        list = { type: "ul", items: [] };
        blocks.push(list);
      }
      list.items.push(bullet[1]);
      return;
    }
    list = null;
    if (line.startsWith("## ")) {
      blocks.push({ type: "h4", text: line.slice(3) });
    } else {
      blocks.push({ type: "p", text: line });
    }
  });

  return blocks.map((block, i) => {
    if (block.type === "ul") {
      return (
        <ul key={i}>
          {block.items.map((item, j) => (
            <li key={j}>{renderInline(item, `${i}-${j}`)}</li>
          ))}
        </ul>
      );
    }
    if (block.type === "h4") {
      return <h4 key={i}>{renderInline(block.text, `${i}`)}</h4>;
    }
    return <p key={i}>{renderInline(block.text, `${i}`)}</p>;
  });
}

export default function ChatPage() {
  const { slug } = useParams();
  const { token } = useAuth();
  const [sessionId, setSessionId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [sending, setSending] = useState(false);
  const [error, setError] = useState("");
  const bottomRef = useRef(null);

  useEffect(() => {
    api
      .createChatSession(token, slug || null)
      .then((session) => setSessionId(session.id))
      .catch((err) => setError(err.message));
  }, [token, slug]);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
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
      <h1>{slug ? `Chat: ${slug.replace(/-/g, " ")}` : "General caregiving chat"}</h1>
      <div className="chat-messages">
        {messages.map((m, i) => (
          <div key={i} className={`chat-bubble chat-bubble-${m.role}`}>
            {m.role === "assistant" ? (
              <div className="chat-markdown">{renderChatMarkdown(m.content)}</div>
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
