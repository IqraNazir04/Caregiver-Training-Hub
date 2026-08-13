import React from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import { useAuth } from "./auth/AuthContext.jsx";
import ChatPage from "./pages/ChatPage.jsx";
import LoginPage from "./pages/LoginPage.jsx";
import SignupPage from "./pages/SignupPage.jsx";
import TrackDetailPage from "./pages/TrackDetailPage.jsx";
import TrackListPage from "./pages/TrackListPage.jsx";

function RequireAuth({ children }) {
  const { token, loading } = useAuth();
  if (loading) return <div className="page-loading">Loading...</div>;
  if (!token) return <Navigate to="/login" replace />;
  return children;
}

function TopNav() {
  const { user, logout } = useAuth();
  if (!user) return null;
  return (
    <header className="top-nav">
      <a href="/" className="brand">
        Caregiver Training Hub
      </a>
      <div className="top-nav-right">
        <span>{user.display_name}</span>
        <button onClick={logout}>Log out</button>
      </div>
    </header>
  );
}

export default function App() {
  return (
    <>
      <TopNav />
      <main className="page">
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignupPage />} />
          <Route
            path="/"
            element={
              <RequireAuth>
                <TrackListPage />
              </RequireAuth>
            }
          />
          <Route
            path="/tracks/:slug"
            element={
              <RequireAuth>
                <TrackDetailPage />
              </RequireAuth>
            }
          />
          <Route
            path="/tracks/:slug/chat"
            element={
              <RequireAuth>
                <ChatPage />
              </RequireAuth>
            }
          />
          <Route
            path="/chat"
            element={
              <RequireAuth>
                <ChatPage />
              </RequireAuth>
            }
          />
        </Routes>
      </main>
    </>
  );
}
