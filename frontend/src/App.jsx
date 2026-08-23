import React, { useEffect, useState } from "react";
import { Navigate, NavLink, Route, Routes, useLocation } from "react-router-dom";
import { useAuth } from "./auth/AuthContext.jsx";
import Logo from "./components/Logo.jsx";
import AboutPage from "./pages/marketing/AboutPage.jsx";
import FeaturesPage from "./pages/marketing/FeaturesPage.jsx";
import CoursesPage from "./pages/marketing/CoursesPage.jsx";
import FaqPage from "./pages/marketing/FaqPage.jsx";
import LandingPage from "./pages/marketing/LandingPage.jsx";
import LoginPage from "./pages/auth/LoginPage.jsx";
import SignupPage from "./pages/auth/SignupPage.jsx";
import ForgotPasswordPage from "./pages/auth/ForgotPasswordPage.jsx";
import ResetPasswordPage from "./pages/auth/ResetPasswordPage.jsx";
import TrackListPage from "./pages/app/tracks/TrackListPage.jsx";
import TrackDetailPage from "./pages/app/tracks/TrackDetailPage.jsx";
import CertificationPage from "./pages/app/certification/CertificationPage.jsx";
import CertificateViewPage from "./pages/app/certification/CertificateViewPage.jsx";
import ChatPage from "./pages/app/ChatPage.jsx";
import ChecklistPage from "./pages/app/ChecklistPage.jsx";
import MedicationsPage from "./pages/app/MedicationsPage.jsx";
import ProfilePage from "./pages/app/ProfilePage.jsx";

const PUBLIC_TABS = [
  { to: "/", label: "Home", end: true },
  { to: "/about", label: "About" },
  { to: "/features", label: "Features" },
  { to: "/courses", label: "Courses" },
  { to: "/faq", label: "FAQ" },
];

const APP_TABS = [
  { to: "/tracks", label: "Tracks" },
  { to: "/checklist", label: "Checklist" },
  { to: "/medications", label: "Medications" },
  { to: "/certification", label: "Certification" },
  { to: "/chat", label: "Chat" },
  { to: "/profile", label: "Profile" },
];

function RequireAuth({ children }) {
  const { token, loading } = useAuth();
  if (loading) return <div className="page-loading">Loading...</div>;
  if (!token) return <Navigate to="/" replace />;
  return children;
}

function NavTabs({ tabs }) {
  return (
    <nav className="nav-tabs">
      {tabs.map((tab) => (
        <NavLink
          key={tab.to}
          to={tab.to}
          end={tab.end}
          className={({ isActive }) => `nav-tab${isActive ? " nav-tab-active" : ""}`}
        >
          {tab.label}
        </NavLink>
      ))}
    </nav>
  );
}

function TopNav() {
  const { token, user, logout } = useAuth();
  const location = useLocation();
  const [menuOpen, setMenuOpen] = useState(false);

  // Predictable navigation: the logo always stays top-left and pinned; on
  // narrow screens the nav collapses behind a toggle instead of wrapping
  // across multiple rows, and closes automatically on every navigation.
  useEffect(() => {
    setMenuOpen(false);
  }, [location.pathname]);

  return (
    <header className="top-nav">
      <div className="top-nav-bar">
        <NavLink to={token ? "/tracks" : "/"} className="brand">
          <Logo className="brand-logo" aria-hidden="true" />
          Caregiver Training Hub
        </NavLink>

        <button
          type="button"
          className="nav-toggle"
          aria-label="Toggle navigation menu"
          aria-expanded={menuOpen}
          onClick={() => setMenuOpen((v) => !v)}
        >
          <span className="nav-toggle-bar" />
          <span className="nav-toggle-bar" />
          <span className="nav-toggle-bar" />
        </button>
      </div>

      <div className={`top-nav-collapse${menuOpen ? " top-nav-collapse-open" : ""}`}>
        <NavTabs tabs={token ? APP_TABS : PUBLIC_TABS} />

        <div className="top-nav-right">
          {user ? (
            <>
              <span className="user-badge">
                <span className="user-avatar">{user.display_name.charAt(0).toUpperCase()}</span>
                {user.display_name}
              </span>
              <button onClick={logout}>Log out</button>
            </>
          ) : (
            <>
              <NavLink to="/login" className="nav-login-link">
                Log in
              </NavLink>
              <NavLink to="/signup" className="nav-signup-btn">
                Sign up
              </NavLink>
            </>
          )}
        </div>
      </div>
    </header>
  );
}

function Footer() {
  return (
    <footer className="site-footer">
      Caregiver Training Hub &mdash; educational content only, not a substitute for professional
      medical advice.
    </footer>
  );
}

export default function App() {
  return (
    <>
      <TopNav />
      <main className="page">
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/features" element={<FeaturesPage />} />
          <Route path="/faq" element={<FaqPage />} />
          <Route path="/courses" element={<CoursesPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignupPage />} />
          <Route path="/forgot-password" element={<ForgotPasswordPage />} />
          <Route path="/reset-password" element={<ResetPasswordPage />} />
          <Route
            path="/certification"
            element={
              <RequireAuth>
                <CertificationPage />
              </RequireAuth>
            }
          />
          <Route
            path="/certification/:slug"
            element={
              <RequireAuth>
                <CertificateViewPage />
              </RequireAuth>
            }
          />
          <Route
            path="/tracks"
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
          <Route
            path="/checklist"
            element={
              <RequireAuth>
                <ChecklistPage />
              </RequireAuth>
            }
          />
          <Route
            path="/medications"
            element={
              <RequireAuth>
                <MedicationsPage />
              </RequireAuth>
            }
          />
          <Route
            path="/profile"
            element={
              <RequireAuth>
                <ProfilePage />
              </RequireAuth>
            }
          />
        </Routes>
      </main>
      <Footer />
    </>
  );
}
