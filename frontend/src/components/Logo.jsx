import React from "react";

/**
 * Brand mark: a caregiver supporting an elderly person, with a small family
 * accent (heart), on the site's grey/yellow/orange gradient badge — same
 * flat-illustration style as CaregivingScene/AboutScene, simplified to read
 * clearly at small nav-bar sizes.
 */
export default function Logo(props) {
  return (
    <svg viewBox="0 0 64 64" {...props}>
      <defs>
        <linearGradient id="logo-badge" x1="0" y1="1" x2="1" y2="0">
          <stop offset="0" stopColor="#f97316" />
          <stop offset="1" stopColor="#eab308" />
        </linearGradient>
      </defs>

      <rect width="64" height="64" rx="16" fill="url(#logo-badge)" />

      {/* family/care accent */}
      <path
        d="M32 15.5c-1.7-2.1-4.9-2.1-6.3-0.2-1.3 1.8-0.8 3.9 1.1 5.6L32 25l5.2-4.1c1.9-1.7 2.4-3.8 1.1-5.6-1.4-1.9-4.6-1.9-6.3 0.2Z"
        fill="white"
      />

      {/* elderly person (back), with a cane to read clearly as elderly */}
      <circle cx="42" cy="30" r="6" fill="white" />
      <path
        d="M42 38c-6.3 0-11.1 4-11.9 11-0.2 1.6 1 3 2.6 3h18.6c1.6 0 2.8-1.4 2.6-3-0.8-7-5.6-11-11.9-11Z"
        fill="white"
      />

      {/* caregiver (front, supporting) */}
      <circle cx="24" cy="33" r="7.6" fill="white" />
      <path
        d="M24 42.5c-8.1 0-14.2 5.2-15.1 14-0.2 1.8 1.2 3.5 3 3.5h24.2c1.8 0 3.2-1.7 3-3.5-0.9-8.8-7-14-15.1-14Z"
        fill="white"
      />
    </svg>
  );
}
