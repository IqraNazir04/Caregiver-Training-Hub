import React from "react";

/**
 * Flat-illustration hero graphic for the About page: a caregiver mid-explanation,
 * addressing a small seated group — one listener in a wheelchair. Hand-drawn SVG
 * (no external image assets), matching the site's grey/yellow/orange palette and
 * the bezier-silhouette style used in CaregivingScene.
 */

const OUTLINE = "rgba(24,20,40,0.1)";
const FACE_INK = "#2a2a35";

const TORSO_D =
  "M-32,88 C-34,81 -29,78 -22,78 L22,78 C29,78 34,81 32,88 C36,104 30,126 28,140 C27,144 24,147 19,147 L-19,147 C-24,147 -27,144 -28,140 C-30,126 -36,104 -32,88 Z";
const ARM_L_D =
  "M-32,84 C-39,84 -43,89 -43,96 L-43,150 C-43,159 -39,164 -32,164 C-27,164 -23,159 -23,150 L-23,94 C-23,87 -27,84 -32,84 Z";
const ARM_R_RAISED_D =
  "M30,80 C24,74 24,64 30,58 L44,44 C50,38 58,38 63,44 C68,49 68,56 63,61 L49,75 C46,82 38,86 32,86 Z";

function Caregiver({ cx }) {
  return (
    <g transform={`translate(${cx},0)`}>
      {/* legs */}
      <path d="M-26,142 L-3,142 L-7,206 C-7,211 -11,215 -16,215 C-21,215 -25,211 -25,206 Z" fill="#3f4c63" stroke={OUTLINE} strokeWidth={1.4} />
      <path d="M26,142 L3,142 L7,206 C7,211 11,215 16,215 C21,215 25,211 25,206 Z" fill="#3f4c63" stroke={OUTLINE} strokeWidth={1.4} />
      <rect x={-30} y={216} width={22} height={9} rx={4.5} fill="#292f3d" />
      <rect x={8} y={216} width={22} height={9} rx={4.5} fill="#292f3d" />

      {/* lowered (left) arm */}
      <path d={ARM_L_D} fill="#f97316" stroke={OUTLINE} strokeWidth={1.2} />
      <circle cx={-33} cy={168} r={9.5} fill="#c98a5e" stroke={OUTLINE} strokeWidth={1} />

      {/* torso + raised arm (explaining gesture) */}
      <path d={TORSO_D} fill="#f97316" stroke={OUTLINE} strokeWidth={1.4} />
      <path d={ARM_R_RAISED_D} fill="#f97316" stroke={OUTLINE} strokeWidth={1.2} />
      <circle cx={62} cy={46} r={9.5} fill="#c98a5e" stroke={OUTLINE} strokeWidth={1} />

      {/* stethoscope */}
      <path
        d="M-12,80 q-7,22 6,30 q14,8 4,25"
        stroke="#f5f4f1"
        strokeWidth={3.4}
        fill="none"
        strokeLinecap="round"
      />
      <circle cx={0} cy={137} r={5} fill="#f5f4f1" stroke="#c1c3cc" />

      {/* clipboard in lowered hand */}
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

function SeatedListener({ cx, shirt, hair, faceRight = false }) {
  const s = faceRight ? 1 : -1;
  return (
    <g transform={`translate(${cx},0) scale(${s},1)`}>
      {/* chair */}
      <rect x={-30} y={150} width={60} height={10} rx={4} fill="#e9e9ed" />
      <rect x={-26} y={158} width={8} height={40} rx={2} fill="#c1c3cc" />
      <rect x={18} y={158} width={8} height={40} rx={2} fill="#c1c3cc" />
      <rect x={16} y={70} width={10} height={82} rx={4} fill="#e9e9ed" />

      {/* legs, seated */}
      <rect x={-22} y={148} width={16} height={12} rx={4} fill="#586178" />
      <rect x={4} y={148} width={16} height={12} rx={4} fill="#586178" />
      <rect x={-24} y={158} width={18} height={34} rx={5} fill="#586178" />
      <rect x={4} y={158} width={22} height={30} rx={5} fill="#3d4353" />

      {/* torso */}
      <path
        d="M-24,96 C-26,90 -21,86 -14,86 L18,86 C25,86 29,91 27,98 C29,112 25,132 23,144 C22,148 18,150 13,150 L-18,150 C-22,150 -25,147 -25,143 C-27,130 -22,108 -24,96 Z"
        fill={shirt}
        stroke={OUTLINE}
        strokeWidth={1.3}
      />

      {/* far arm resting */}
      <rect x={16} y={98} width={12} height={44} rx={6} fill={shirt} stroke={OUTLINE} strokeWidth={1} />
      {/* near arm resting on chair */}
      <rect x={-30} y={100} width={12} height={40} rx={6} fill={shirt} stroke={OUTLINE} strokeWidth={1} />
      <circle cx={-24} cy={143} r={7.5} fill="#e8b48c" stroke={OUTLINE} strokeWidth={1} />

      {/* neck + head */}
      <rect x={-6} y={68} width={12} height={13} rx={4} fill="#e8b48c" />
      <circle cx={0} cy={56} r={18} fill="#e8b48c" stroke={OUTLINE} strokeWidth={1.2} />
      {hair}

      {/* face */}
      <ellipse cx={-6} cy={58} rx={1.8} ry={2.3} fill={FACE_INK} />
      <ellipse cx={6} cy={58} rx={1.8} ry={2.3} fill={FACE_INK} />
      <path d="M-7,65 Q0,68 7,65" stroke={FACE_INK} strokeWidth={1.2} fill="none" strokeLinecap="round" opacity={0.7} />
    </g>
  );
}

function WheelchairListener({ cx }) {
  return (
    <g transform={`translate(${cx},0)`}>
      {/* wheels */}
      <circle cx={0} cy={210} r={30} fill="none" stroke="#71737f" strokeWidth={4} />
      <circle cx={0} cy={210} r={4} fill="#71737f" />
      <circle cx={-34} cy={222} r={9} fill="none" stroke="#71737f" strokeWidth={3} />
      {/* frame + seat */}
      <rect x={-22} y={150} width={44} height={10} rx={4} fill="#c1c3cc" />
      <rect x={14} y={104} width={8} height={70} rx={3} fill="#c1c3cc" />
      <line x1={22} y1={110} x2={40} y2={150} stroke="#71737f" strokeWidth={3.4} strokeLinecap="round" />

      {/* legs + feet */}
      <rect x={-16} y={150} width={13} height={30} rx={5} fill="#586178" />
      <rect x={2} y={150} width={13} height={30} rx={5} fill="#586178" />
      <rect x={-20} y={178} width={20} height={9} rx={4} fill="#292f3d" />
      <rect x={-2} y={178} width={20} height={9} rx={4} fill="#292f3d" />

      {/* torso */}
      <path
        d="M-22,96 C-24,90 -19,86 -12,86 L16,86 C23,86 27,91 25,98 C27,112 23,134 21,144 C20,148 16,150 11,150 L-16,150 C-20,150 -23,147 -23,143 C-25,130 -20,108 -22,96 Z"
        fill="#c1c3cc"
        stroke={OUTLINE}
        strokeWidth={1.3}
      />

      {/* arms resting on wheels */}
      <rect x={-30} y={104} width={12} height={42} rx={6} fill="#c1c3cc" stroke={OUTLINE} strokeWidth={1} />
      <circle cx={-24} cy={148} r={7.5} fill="#f0c9a0" stroke={OUTLINE} strokeWidth={1} />
      <rect x={14} y={104} width={12} height={42} rx={6} fill="#c1c3cc" stroke={OUTLINE} strokeWidth={1} />

      {/* neck + head */}
      <rect x={-6} y={68} width={12} height={13} rx={4} fill="#f0c9a0" />
      <circle cx={0} cy={56} r={18} fill="#f0c9a0" stroke={OUTLINE} strokeWidth={1.2} />
      <path d="M-18,54 a18,19 0 0 1 36,0" fill="#cfcfd8" />

      {/* face */}
      <ellipse cx={-6} cy={58} rx={1.8} ry={2.3} fill={FACE_INK} />
      <ellipse cx={6} cy={58} rx={1.8} ry={2.3} fill={FACE_INK} />
    </g>
  );
}

export default function AboutScene(props) {
  return (
    <svg viewBox="0 0 760 300" {...props}>
      {/* ground */}
      <ellipse cx={380} cy={272} rx={340} ry={20} fill="#fff4ec" />

      {/* soft plant accents */}
      <g transform="translate(70,0)">
        <rect x={-5} y={200} width={10} height={56} rx={4} fill="#8a6a4a" />
        <circle cx={0} cy={186} r={26} fill="#ffe3cc" />
        <circle cx={-14} cy={196} r={20} fill="#ffb877" opacity={0.85} />
      </g>
      <g transform="translate(690,0)">
        <rect x={-5} y={200} width={10} height={56} rx={4} fill="#8a6a4a" />
        <circle cx={0} cy={186} r={26} fill="#ffe3cc" />
        <circle cx={14} cy={196} r={20} fill="#ffb877" opacity={0.85} />
      </g>

      <ellipse cx={380} cy={268} rx={280} ry={14} fill="#71737f" opacity={0.18} />

      <SeatedListener cx={150} shirt="#c1c3cc" hair={<path d="M-18,52 a18,19 0 0 1 36,0" fill="#cfcfd8" />} faceRight />
      <SeatedListener
        cx={240}
        shirt="#fcd34d"
        hair={
          <>
            <path d="M-18,50 a18,18 0 0 1 36,0 Z" fill="#4a3626" />
            <circle cx={0} cy={30} r={5.5} fill="#4a3626" />
          </>
        }
        faceRight
      />

      <Caregiver cx={400} />

      <SeatedListener
        cx={560}
        shirt="#f97316"
        hair={<path d="M-18,50 a18,18 0 0 1 36,-1" fill="#241d1a" />}
      />

      <WheelchairListener cx={670} />
    </svg>
  );
}
