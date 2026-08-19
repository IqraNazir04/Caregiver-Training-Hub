import React from "react";

/**
 * Purely decorative margin graphic for the Courses page: a stack of books
 * with a graduation cap, same hand-drawn style/palette as SideDecor. Reuses
 * the .side-decor wrapper classes (fixed positioning, breakpoint, flip).
 */

const OUTLINE = "rgba(24,20,40,0.12)";

function BookStack() {
  return (
    <g transform="translate(80,240)">
      {/* books, bottom to top */}
      <rect x={-46} y={20} width={92} height={20} rx={4} fill="#71737f" stroke={OUTLINE} strokeWidth={1.4} />
      <rect x={-42} y={22} width={84} height={4} fill="#8d8f99" />

      <rect x={-40} y={2} width={80} height={19} rx={4} fill="#f97316" stroke={OUTLINE} strokeWidth={1.4} />
      <rect x={-36} y={4} width={72} height={3.6} fill="#ffb877" />

      <rect x={-34} y={-16} width={68} height={19} rx={4} fill="#eab308" stroke={OUTLINE} strokeWidth={1.4} />
      <rect x={-30} y={-14} width={60} height={3.6} fill="#fde68a" />

      {/* graduation cap on top */}
      <g transform="translate(0,-30)">
        <path d="M0,-14 L46,0 L0,14 L-46,0 Z" fill="#3b3c45" stroke={OUTLINE} strokeWidth={1.2} />
        <rect x={-13} y={0} width={26} height={16} rx={3} fill="#53555f" />
        <circle cx={0} cy={8} r={3.2} fill="#eab308" />
        <path d="M38,-2 L46,0 L44,20" stroke="#3b3c45" strokeWidth={2} fill="none" strokeLinecap="round" />
        <circle cx={44} cy={22} r={3} fill="#eab308" />
      </g>
    </g>
  );
}

function CourseScene({ flip = false }) {
  return (
    <svg viewBox="0 0 160 420" width="100%" height="100%" style={flip ? { transform: "scaleX(-1)" } : undefined}>
      <ellipse cx={80} cy={280} rx={58} ry={12} fill="#71737f" opacity={0.15} />
      <BookStack />

      {/* small floating open book accent */}
      <g transform="translate(80,110)">
        <path
          d="M-30,-6 C-20,-14 -8,-14 0,-6 C8,-14 20,-14 30,-6 L30,10 C20,2 8,2 0,10 C-8,2 -20,2 -30,10 Z"
          fill="white"
          stroke="#c1c3cc"
          strokeWidth={1.6}
        />
        <line x1={0} y1={-6} x2={0} y2={10} stroke="#c1c3cc" strokeWidth={1.4} />
        <line x1={-20} y1={-4} x2={-8} y2={-2} stroke="#e8e4dd" strokeWidth={1.6} />
        <line x1={-20} y1={2} x2={-8} y2={4} stroke="#e8e4dd" strokeWidth={1.6} />
        <line x1={20} y1={-4} x2={8} y2={-2} stroke="#e8e4dd" strokeWidth={1.6} />
        <line x1={20} y1={2} x2={8} y2={4} stroke="#e8e4dd" strokeWidth={1.6} />
      </g>
    </svg>
  );
}

export function CourseSideDecorLeft(props) {
  return (
    <div className="side-decor side-decor-left" aria-hidden="true" {...props}>
      <CourseScene />
    </div>
  );
}

export function CourseSideDecorRight(props) {
  return (
    <div className="side-decor side-decor-right" aria-hidden="true" {...props}>
      <CourseScene flip />
    </div>
  );
}
