import React from "react";

/**
 * Small hand-drawn badge illustrations for authenticated app page headers —
 * a soft colored circle backdrop with a simple flat icon-illustration on top,
 * matching the site's grey/yellow/orange palette and bezier-illustration style
 * used elsewhere (CaregivingScene, AboutScene).
 */

const OUTLINE = "rgba(24,20,40,0.12)";

export function MedicationGraphic(props) {
  return (
    <svg viewBox="0 0 96 96" {...props}>
      <circle cx={48} cy={48} r={44} fill="#fff4ec" />
      <rect x={30} y={38} width={24} height={34} rx={7} fill="white" stroke="#ffb877" strokeWidth={2} />
      <rect x={30} y={38} width={24} height={11} rx={5} fill="#f97316" />
      <line x1={34} y1={58} x2={50} y2={58} stroke="#ffe3cc" strokeWidth={2} />
      <line x1={34} y1={64} x2={50} y2={64} stroke="#ffe3cc" strokeWidth={2} />
      <g transform="translate(63,52) rotate(35)">
        <rect x={-9} y={-5} width={18} height={10} rx={5} fill="#eab308" stroke={OUTLINE} strokeWidth={1} />
        <path d="M-9,0 H9" stroke="white" strokeWidth={1.4} />
      </g>
      <g transform="translate(66,66) rotate(-15)">
        <rect x={-7} y={-4} width={14} height={8} rx={4} fill="#c1c3cc" stroke={OUTLINE} strokeWidth={1} />
        <path d="M-7,0 H7" stroke="white" strokeWidth={1.2} />
      </g>
    </svg>
  );
}

export function CertificationGraphic(props) {
  return (
    <svg viewBox="0 0 96 96" {...props}>
      <circle cx={48} cy={48} r={44} fill="#fffbea" />
      <path d="M38,52 L30,80 L48,72 L66,80 L58,52 Z" fill="#f97316" stroke={OUTLINE} strokeWidth={1.4} />
      <circle cx={48} cy={42} r={22} fill="#eab308" stroke={OUTLINE} strokeWidth={1.6} />
      <circle cx={48} cy={42} r={15} fill="#fcd34d" />
      <path
        d="M40,42 L46,48 L57,35"
        stroke="white"
        strokeWidth={3.2}
        fill="none"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}

export function ChatGraphic(props) {
  return (
    <svg viewBox="0 0 96 96" {...props}>
      <circle cx={48} cy={48} r={44} fill="#fffbea" />
      <path
        d="M26,34 h44 a6,6 0 0 1 6,6 v22 a6,6 0 0 1 -6,6 h-28 l-12,11 v-11 h-4 a6,6 0 0 1 -6,-6 v-22 a6,6 0 0 1 6,-6 Z"
        fill="white"
        stroke="#c1c3cc"
        strokeWidth={2}
      />
      <circle cx={40} cy={51} r={3.4} fill="#eab308" />
      <circle cx={51} cy={51} r={3.4} fill="#f97316" />
      <circle cx={62} cy={51} r={3.4} fill="#71737f" />
    </svg>
  );
}

export function ProfileGraphic(props) {
  return (
    <svg viewBox="0 0 96 96" {...props}>
      <circle cx={48} cy={48} r={44} fill="#f5f5f7" />
      <path d="M18,82 C18,63 31,54 48,54 C65,54 78,63 78,82 Z" fill="#c1c3cc" stroke={OUTLINE} strokeWidth={1.4} />
      <circle cx={48} cy={38} r={19} fill="#e8b48c" stroke={OUTLINE} strokeWidth={1.4} />
      <path d="M29,36 a19,19 0 0 1 38,0 Z" fill="#3b2a1f" />
      <ellipse cx={41} cy={40} rx={6} ry={4.4} fill="white" opacity={0.22} />
    </svg>
  );
}

export function ChecklistGraphic(props) {
  return (
    <svg viewBox="0 0 96 96" {...props}>
      <circle cx={48} cy={48} r={44} fill="#fff4ec" />
      <rect x={28} y={26} width={40} height={52} rx={6} fill="white" stroke="#ffb877" strokeWidth={2} />
      <rect x={38} y={22} width={20} height={10} rx={3} fill="#71737f" />
      <rect x={41} y={25} width={14} height={4} rx={2} fill="#f5f5f7" />

      <rect x={35} y={40} width={9} height={9} rx={2.5} fill="#fef3c7" stroke="#eab308" strokeWidth={1.4} />
      <path d="M37,44.3 L39.4,46.6 L43,41.5" stroke="#a16207" strokeWidth={1.6} fill="none" strokeLinecap="round" strokeLinejoin="round" />
      <line x1={49} y1={44} x2={61} y2={44} stroke="#e8e4dd" strokeWidth={2.2} />

      <rect x={35} y={54} width={9} height={9} rx={2.5} fill="#ffe3cc" stroke="#f97316" strokeWidth={1.4} />
      <path d="M37,58.3 L39.4,60.6 L43,55.5" stroke="#c2410c" strokeWidth={1.6} fill="none" strokeLinecap="round" strokeLinejoin="round" />
      <line x1={49} y1={58} x2={61} y2={58} stroke="#e8e4dd" strokeWidth={2.2} />

      <rect x={35} y={68} width={9} height={9} rx={2.5} fill="#f5f5f7" stroke="#c1c3cc" strokeWidth={1.4} />
      <line x1={49} y1={72} x2={58} y2={72} stroke="#e8e4dd" strokeWidth={2.2} />
    </svg>
  );
}
