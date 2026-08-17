import React from "react";

/**
 * Purely decorative margin graphic for wide pages: a standing caregiver with
 * an elderly person in a wheelchair, stacked vertically, same hand-drawn style
 * as AboutScene. Fixed-positioned so it never affects document flow or causes
 * overflow; hidden below a viewport-width breakpoint via .side-decor CSS.
 */

const OUTLINE = "rgba(24,20,40,0.1)";
const FACE_INK = "#2a2a35";

const TORSO_D =
  "M-32,88 C-34,81 -29,78 -22,78 L22,78 C29,78 34,81 32,88 C36,104 30,126 28,140 C27,144 24,147 19,147 L-19,147 C-24,147 -27,144 -28,140 C-30,126 -36,104 -32,88 Z";
const ARM_L_D =
  "M-32,84 C-39,84 -43,89 -43,96 L-43,150 C-43,159 -39,164 -32,164 C-27,164 -23,159 -23,150 L-23,94 C-23,87 -27,84 -32,84 Z";
const ARM_R_RAISED_D =
  "M30,80 C24,74 24,64 30,58 L44,44 C50,38 58,38 63,44 C68,49 68,56 63,61 L49,75 C46,82 38,86 32,86 Z";

function Caregiver() {
  return (
    <g transform="translate(80,90)">
      {/* legs */}
      <path d="M-26,142 L-3,142 L-7,206 C-7,211 -11,215 -16,215 C-21,215 -25,211 -25,206 Z" fill="#3f4c63" stroke={OUTLINE} strokeWidth={1.4} />
      <path d="M26,142 L3,142 L7,206 C7,211 11,215 16,215 C21,215 25,211 25,206 Z" fill="#3f4c63" stroke={OUTLINE} strokeWidth={1.4} />
      <rect x={-30} y={216} width={22} height={9} rx={4.5} fill="#292f3d" />
      <rect x={8} y={216} width={22} height={9} rx={4.5} fill="#292f3d" />

      {/* lowered arm */}
      <path d={ARM_L_D} fill="#f97316" stroke={OUTLINE} strokeWidth={1.2} />
      <circle cx={-33} cy={168} r={9.5} fill="#c98a5e" stroke={OUTLINE} strokeWidth={1} />

      {/* torso + raised arm */}
      <path d={TORSO_D} fill="#f97316" stroke={OUTLINE} strokeWidth={1.4} />
      <path d={ARM_R_RAISED_D} fill="#f97316" stroke={OUTLINE} strokeWidth={1.2} />
      <circle cx={62} cy={46} r={9.5} fill="#c98a5e" stroke={OUTLINE} strokeWidth={1} />

      {/* stethoscope */}
      <path d="M-12,80 q-7,22 6,30 q14,8 4,25" stroke="#f5f4f1" strokeWidth={3.4} fill="none" strokeLinecap="round" />
      <circle cx={0} cy={137} r={5} fill="#f5f4f1" stroke="#c1c3cc" />

      {/* clipboard */}
      <rect x={-46} y={128} width={16} height={20} rx={2.5} fill="white" stroke="#c1c3cc" strokeWidth={1.2} />
      <line x1={-43} y1={134} x2={-33} y2={134} stroke="#c1c3cc" strokeWidth={1.2} />
      <line x1={-43} y1={139} x2={-33} y2={139} stroke="#c1c3cc" strokeWidth={1.2} />

      {/* neck + head */}
      <rect x={-6} y={66} width={12} height={14} rx={4} fill="#c98a5e" />
      <circle cx={0} cy={52} r={19} fill="#c98a5e" stroke={OUTLINE} strokeWidth={1.2} />
      <path d="M-19,50 a19,19 0 0 1 38,-2" fill="#241d1a" />
      <ellipse cx={-6} cy={44} rx={6} ry={4.2} fill="white" opacity={0.2} />

      {/* face */}
      <ellipse cx={-6} cy={54} rx={1.9} ry={2.5} fill={FACE_INK} />
      <ellipse cx={7} cy={54} rx={1.9} ry={2.5} fill={FACE_INK} />
      <path d="M-9,62 Q0,68 9,62" stroke={FACE_INK} strokeWidth={1.3} fill="none" strokeLinecap="round" />
    </g>
  );
}

function WheelchairElder() {
  return (
    <g transform="translate(80,470)">
      {/* wheels */}
      <circle cx={0} cy={62} r={34} fill="none" stroke="#71737f" strokeWidth={4.5} />
      <circle cx={0} cy={62} r={4} fill="#71737f" />
      <circle cx={-38} cy={76} r={10} fill="none" stroke="#71737f" strokeWidth={3} />

      {/* frame + seat */}
      <rect x={-24} y={-6} width={48} height={11} rx={4} fill="#c1c3cc" />
      <rect x={16} y={-56} width={9} height={72} rx={3.5} fill="#c1c3cc" />
      <line x1={25} y1={-50} x2={44} y2={-6} stroke="#71737f" strokeWidth={3.6} strokeLinecap="round" />

      {/* legs + feet */}
      <rect x={-18} y={-6} width={15} height={32} rx={5.5} fill="#586178" />
      <rect x={3} y={-6} width={15} height={32} rx={5.5} fill="#586178" />
      <rect x={-22} y={24} width={22} height={10} rx={4.5} fill="#292f3d" />
      <rect x={-2} y={24} width={22} height={10} rx={4.5} fill="#292f3d" />

      {/* torso */}
      <path
        d="M-24,-60 C-26,-67 -21,-71 -14,-71 L18,-71 C25,-71 29,-66 27,-59 C29,-45 25,-23 23,-13 C22,-9 18,-7 13,-7 L-18,-7 C-22,-7 -25,-10 -25,-14 C-27,-27 -22,-49 -24,-60 Z"
        fill="#c1c3cc"
        stroke={OUTLINE}
        strokeWidth={1.4}
      />

      {/* arms resting on wheels */}
      <rect x={-33} y={-52} width={13} height={46} rx={6.5} fill="#c1c3cc" stroke={OUTLINE} strokeWidth={1} />
      <circle cx={-26} cy={-8} r={8} fill="#f0c9a0" stroke={OUTLINE} strokeWidth={1} />
      <rect x={16} y={-52} width={13} height={46} rx={6.5} fill="#c1c3cc" stroke={OUTLINE} strokeWidth={1} />

      {/* neck + head */}
      <rect x={-7} y={-88} width={14} height={15} rx={4.5} fill="#f0c9a0" />
      <circle cx={0} cy={-101} r={20} fill="#f0c9a0" stroke={OUTLINE} strokeWidth={1.3} />
      <path d="M-20,-103 a20,21 0 0 1 40,0" fill="#cfcfd8" />

      {/* face */}
      <ellipse cx={-6.5} cy={-99} rx={2} ry={2.5} fill={FACE_INK} />
      <ellipse cx={6.5} cy={-99} rx={2} ry={2.5} fill={FACE_INK} />
      <path d="M-8,-91 Q0,-87 8,-91" stroke={FACE_INK} strokeWidth={1.3} fill="none" strokeLinecap="round" opacity={0.7} />
    </g>
  );
}

function SideScene({ flip = false }) {
  return (
    <svg viewBox="0 0 160 610" width="100%" height="100%" style={flip ? { transform: "scaleX(-1)" } : undefined}>
      <ellipse cx={80} cy={582} rx={62} ry={12} fill="#71737f" opacity={0.15} />
      <Caregiver />
      <WheelchairElder />
    </svg>
  );
}

export function SideDecorLeft(props) {
  return (
    <div className="side-decor side-decor-left" aria-hidden="true" {...props}>
      <SideScene />
    </div>
  );
}

export function SideDecorRight(props) {
  return (
    <div className="side-decor side-decor-right" aria-hidden="true" {...props}>
      <SideScene flip />
    </div>
  );
}
