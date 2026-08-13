import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client.js";
import { useAuth } from "../auth/AuthContext.jsx";

function Lesson({ track, lesson }) {
  const { token } = useAuth();
  const [expanded, setExpanded] = useState(false);
  const [answers, setAnswers] = useState(() => lesson.quiz_questions.map(() => null));
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const selectAnswer = (questionIndex, choiceIndex) => {
    setAnswers((prev) => {
      const next = [...prev];
      next[questionIndex] = choiceIndex;
      return next;
    });
  };

  const submitQuiz = async () => {
    setError("");
    if (answers.some((a) => a === null)) {
      setError("Answer every question before submitting.");
      return;
    }
    try {
      const res = await api.submitQuiz(token, track.slug, lesson.id, answers);
      setResult(res);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="lesson-card">
      <button className="lesson-toggle" onClick={() => setExpanded((v) => !v)}>
        {expanded ? "▾" : "▸"} {lesson.title} ({lesson.estimated_minutes} min)
      </button>
      {expanded && (
        <div className="lesson-body">
          <div className="lesson-markdown">
            {lesson.body_markdown.split("\n").map((line, i) => (
              <p key={i}>{line}</p>
            ))}
          </div>

          <h3>Quick check</h3>
          {lesson.quiz_questions.map((q, qi) => (
            <div key={q.id} className="quiz-question">
              <p>{q.question_text}</p>
              {q.choices.map((choice, ci) => (
                <label key={ci} className="quiz-choice">
                  <input
                    type="radio"
                    name={`q-${q.id}`}
                    checked={answers[qi] === ci}
                    onChange={() => selectAnswer(qi, ci)}
                  />
                  {choice}
                </label>
              ))}
              {result && (
                <p className={result.results[qi].correct ? "quiz-correct" : "quiz-incorrect"}>
                  {result.results[qi].correct ? "Correct. " : "Not quite. "}
                  {result.results[qi].explanation}
                </p>
              )}
            </div>
          ))}
          {error && <p className="error-text">{error}</p>}
          {result ? (
            <p className="quiz-score">
              Score: {result.score} / {result.total}
            </p>
          ) : (
            <button onClick={submitQuiz}>Submit quiz</button>
          )}
        </div>
      )}
    </div>
  );
}

export default function TrackDetailPage() {
  const { slug } = useParams();
  const { token } = useAuth();
  const [track, setTrack] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    api.getTrack(token, slug).then(setTrack).catch((err) => setError(err.message));
  }, [token, slug]);

  if (error) return <p className="error-text">{error}</p>;
  if (!track) return <p>Loading...</p>;

  return (
    <div>
      <h1>{track.name}</h1>
      <p>{track.description}</p>
      <Link to={`/tracks/${track.slug}/chat`} className="chat-cta">
        Chat about {track.name}
      </Link>
      <div className="lesson-list">
        {track.lessons.map((lesson) => (
          <Lesson key={lesson.id} track={track} lesson={lesson} />
        ))}
      </div>
    </div>
  );
}
