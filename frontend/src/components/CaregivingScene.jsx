import React from "react";

/**
 * Flat-illustration hero graphic: a family member and a healthcare worker
 * supporting an elderly person outside a nursing home, with trees framing
 * the scene. Hand-drawn SVG (no external image assets), built with bezier
 * body silhouettes, soft gradient sheens, and a blurred ground shadow for
 * depth. Colors mirror the site's grey/yellow/orange CSS custom properties
 * as literal hex values (SVG presentation attributes don't reliably
 * resolve var() across browsers).
 */

const TORSO_D =
  "M-38,104 C-40,96 -34,92 -26,92 L26,92 C34,92 40,96 38,104 C42,122 36,148 33,164 C32,169 28,172 22,172 L-22,172 C-28,172 -32,169 -33,164 C-36,148 -42,122 -38,104 Z";
const ARM_L_D =
  "M-38,98 C-46,98 -50,104 -50,112 L-50,180 C-50,190 -46,196 -38,196 C-32,196 -28,190 -28,180 L-28,110 C-28,102 -32,98 -38,98 Z";
const ARM_R_D =
  "M38,98 C46,98 50,104 50,112 L50,180 C50,190 46,196 38,196 C32,196 28,190 28,180 L28,110 C28,102 32,98 38,98 Z";
const LEG_L_D = "M-30,168 L-4,168 L-9,240 C-9,246 -13,250 -19,250 C-25,250 -29,246 -29,240 Z";
const LEG_R_D = "M30,168 L4,168 L9,240 C9,246 13,250 19,250 C25,250 29,246 29,240 Z";
const SHOE_L_D =
  "M-34,254 C-34,247 -29,244 -22,244 L-8,244 C-2,244 2,248 2,254 C2,260 -3,263 -10,263 L-30,263 C-33,263 -35,259 -34,254 Z";
const SHOE_R_D =
  "M34,254 C34,247 29,244 22,244 L8,244 C2,244 -2,248 -2,254 C-2,260 3,263 10,263 L30,263 C33,263 35,259 34,254 Z";

const OUTLINE = "rgba(24,20,40,0.1)";
const FACE_INK = "#2a2a35";

function Person({ id, shirt, shirtDark, pants, skin, hair, accessory }) {
  return (
    <g>
      {/* legs + shoes */}
      <path d={LEG_L_D} fill={pants} stroke={OUTLINE} strokeWidth={1.4} />
      <path d={LEG_R_D} fill={pants} stroke={OUTLINE} strokeWidth={1.4} />
      <path d={SHOE_L_D} fill="#33313f" stroke={OUTLINE} strokeWidth={1.4} />
      <path d={SHOE_R_D} fill="#33313f" stroke={OUTLINE} strokeWidth={1.4} />

      {/* arms + hands */}
      <path d={ARM_L_D} fill={shirt} stroke={OUTLINE} strokeWidth={1.4} />
      <path d={ARM_R_D} fill={shirt} stroke={OUTLINE} strokeWidth={1.4} />
      <rect x={-49} y={183} width={20} height={10} rx={5} fill={shirtDark} />
      <rect x={29} y={183} width={20} height={10} rx={5} fill={shirtDark} />
      <circle cx={-39} cy={200} r={11} fill={skin} stroke={OUTLINE} strokeWidth={1.2} />
      <circle cx={39} cy={200} r={11} fill={skin} stroke={OUTLINE} strokeWidth={1.2} />

      {/* torso + sheen + collar */}
      <path d={TORSO_D} fill={shirt} stroke={OUTLINE} strokeWidth={1.4} />
      <path d={TORSO_D} fill={`url(#sheen-${id})`} />
      <path
        d="M-13,93 L0,106 L13,93"
        stroke={shirtDark}
        strokeWidth={3}
        fill="none"
        strokeLinecap="round"
        strokeLinejoin="round"
      />

      {/* neck + head */}
      <rect x={-7} y={80} width={14} height={16} rx={5} fill={skin} />
      <ellipse cx={-22} cy={64} rx={3.6} ry={6} fill={skin} stroke={OUTLINE} strokeWidth={1} />
      <ellipse cx={22} cy={64} rx={3.6} ry={6} fill={skin} stroke={OUTLINE} strokeWidth={1} />
      <circle cx={0} cy={62} r={22} fill={skin} stroke={OUTLINE} strokeWidth={1.2} />
      <ellipse cx={-7} cy={52} rx={7} ry={5} fill="white" opacity={0.22} />
      {hair}

      {/* face */}
      <path d="M-14,55 Q-9,51 -4,54" stroke={FACE_INK} strokeWidth={1.8} fill="none" strokeLinecap="round" />
      <path d="M14,55 Q9,51 4,54" stroke={FACE_INK} strokeWidth={1.8} fill="none" strokeLinecap="round" />
      <ellipse cx={-8} cy={63} rx={2.2} ry={2.9} fill={FACE_INK} />
      <ellipse cx={8} cy={63} rx={2.2} ry={2.9} fill={FACE_INK} />
      <path d="M0,63 C-1.4,66 -1.4,68.5 0,70" stroke={FACE_INK} strokeWidth={1.4} fill="none" strokeLinecap="round" opacity={0.5} />
      <ellipse cx={-15} cy={71} rx={6} ry={3.6} fill="#f2a29a" opacity={0.4} />
      <ellipse cx={15} cy={71} rx={6} ry={3.6} fill="#f2a29a" opacity={0.4} />
      <path
        d="M-10,71 Q0,82 10,71 Q0,77 -10,71 Z"
        fill="white"
        stroke={FACE_INK}
        strokeWidth={1.4}
        strokeLinejoin="round"
      />

      {accessory}
    </g>
  );
}

function Tree({ cx, flip = false }) {
  const s = flip ? -1 : 1;
  return (
    <g transform={`translate(${cx},0)`}>
      <rect x={-8} y={192} width={16} height={82} rx={6} fill="#8a6a4a" />
      <circle cx={14 * s} cy={158} r={30} fill="#ffe3cc" />
      <circle cx={-16 * s} cy={150} r={34} fill="#ffb877" />
      <circle cx={2} cy={128} r={36} fill="#fbbf4a" />
      <circle cx={-10 * s} cy={140} r={22} fill="#f97316" opacity={0.85} />
    </g>
  );
}

export default function CaregivingScene(props) {
  return (
    <svg viewBox="0 0 700 300" {...props}>
      <defs>
        <filter id="groundBlur" x="-30%" y="-60%" width="160%" height="220%">
          <feGaussianBlur stdDeviation="6" />
        </filter>
        {["family", "elderly", "health"].map((id) => (
          <linearGradient key={id} id={`sheen-${id}`} x1="0" y1="0" x2="0" y2="1">
            <stop offset="0" stopColor="#ffffff" stopOpacity="0.3" />
            <stop offset="1" stopColor="#ffffff" stopOpacity="0" />
          </linearGradient>
        ))}
      </defs>

      {/* ground */}
      <rect x={0} y={268} width={700} height={32} fill="#fff4ec" />

      {/* trees framing the scene */}
      <Tree cx={82} />
      <Tree cx={618} flip />

      {/* nursing home building */}
      <g>
        <path d="M242,112 L350,54 L458,112 Z" fill="#c1c3cc" stroke="rgba(24,20,40,0.08)" strokeWidth={1.4} />
        <rect x={250} y={110} width={200} height={160} fill="#f8f7f4" stroke="rgba(24,20,40,0.08)" strokeWidth={1.4} />
        <rect x={250} y={110} width={200} height={10} fill="#e9e9ed" />
        {/* signage plaque */}
        <rect x={318} y={122} width={64} height={22} rx={11} fill="white" stroke="#e9e9ed" strokeWidth={1.5} />
        <path
          d="M350.6,133.3a2.9,2.9 0 0 0-4.1,0l-0.5,0.5-0.5-0.5a2.9,2.9 0 0 0-4.1,4.1l0.5,0.5 4.1,4.1 4.1-4.1 0.5-0.5a2.9,2.9 0 0 0 0-4.1z"
          fill="#f97316"
        />
        <circle cx={362} cy={133} r={2.2} fill="#fcd34d" />
        <circle cx={368} cy={133} r={2.2} fill="#ffb877" />
        {/* windows */}
        <g>
          <rect x={268} y={166} width={34} height={34} rx={3} fill="#fef3c7" stroke="#e3d9b8" strokeWidth={1.5} />
          <line x1={285} y1={166} x2={285} y2={200} stroke="#e3d9b8" strokeWidth={1.5} />
          <line x1={268} y1={183} x2={302} y2={183} stroke="#e3d9b8" strokeWidth={1.5} />
        </g>
        <g>
          <rect x={398} y={166} width={34} height={34} rx={3} fill="#fef3c7" stroke="#e3d9b8" strokeWidth={1.5} />
          <line x1={415} y1={166} x2={415} y2={200} stroke="#e3d9b8" strokeWidth={1.5} />
          <line x1={398} y1={183} x2={432} y2={183} stroke="#e3d9b8" strokeWidth={1.5} />
        </g>
        <g>
          <rect x={268} y={216} width={30} height={30} rx={3} fill="#ffe3cc" stroke="#f0c7a0" strokeWidth={1.5} />
          <line x1={283} y1={216} x2={283} y2={246} stroke="#f0c7a0" strokeWidth={1.5} />
          <line x1={268} y1={231} x2={298} y2={231} stroke="#f0c7a0" strokeWidth={1.5} />
        </g>
        <g>
          <rect x={402} y={216} width={30} height={30} rx={3} fill="#ffe3cc" stroke="#f0c7a0" strokeWidth={1.5} />
          <line x1={417} y1={216} x2={417} y2={246} stroke="#f0c7a0" strokeWidth={1.5} />
          <line x1={402} y1={231} x2={432} y2={231} stroke="#f0c7a0" strokeWidth={1.5} />
        </g>
        {/* low hedges at the base */}
        <circle cx={256} cy={266} r={16} fill="#ffb877" opacity={0.8} />
        <circle cx={444} cy={266} r={16} fill="#ffb877" opacity={0.8} />
      </g>

      <ellipse cx={350} cy={278} rx={260} ry={16} fill="#71737f" opacity={0.25} filter="url(#groundBlur)" />

      {/* small "care" glow above the group */}
      <circle cx={350} cy={30} r={19} fill="#fffbea" />
      <path
        d="M354.1 23.9a4 4 0 0 0-5.7 0l-0.8 0.8-0.8-0.8a4 4 0 0 0-5.7 5.7l0.8 0.8 5.7 5.7 5.7-5.7 0.8-0.8a4 4 0 0 0 0-5.7z"
        fill="#f97316"
      />

      {/* family member */}
      <g transform="translate(200,0)">
        <Person
          id="family"
          shirt="#eab308"
          shirtDark="#a16207"
          pants="#586178"
          skin="#e8b48c"
          hair={
            <>
              <path d="M-24,61 a24,24 0 0 1 48,0 Z" fill="#3b2a1f" />
              <circle cx={0} cy={33} r={7} fill="#3b2a1f" />
            </>
          }
        />
      </g>

      {/* elderly person: gray hair, glasses, cane */}
      <g transform="translate(350,0)">
        <Person
          id="elderly"
          shirt="#c1c3cc"
          shirtDark="#71737f"
          pants="#6b6f80"
          skin="#f0c9a0"
          hair={<path d="M-22,60 a22,23 0 0 1 44,0" fill="#cfcfd8" />}
          accessory={
            <>
              <g stroke="#4a4d5e" strokeWidth={2} fill="none">
                <circle cx={-8} cy={63} r={8.5} />
                <circle cx={8} cy={63} r={8.5} />
              </g>
              <path
                d="M45,200 C45,240 45,260 45,278 M45,200 q11,-9 3,-18"
                stroke="#8a6a4a"
                strokeWidth={4}
                fill="none"
                strokeLinecap="round"
              />
            </>
          }
        />
      </g>

      {/* healthcare worker: stethoscope + badge */}
      <g transform="translate(500,0)">
        <Person
          id="health"
          shirt="#f97316"
          shirtDark="#c2410c"
          pants="#3f4c63"
          skin="#c98a5e"
          hair={<path d="M-24,60 a24,22 0 0 1 48,-2" fill="#241d1a" />}
          accessory={
            <>
              <path
                d="M-14,94 q-8,26 8,36 q17,10 5,30"
                stroke="#f5f4f1"
                strokeWidth={4}
                fill="none"
                strokeLinecap="round"
              />
              <circle cx={0} cy={160} r={6} fill="#f5f4f1" stroke="#c1c3cc" />
              <rect x={-32} y={118} width={15} height={15} rx={3} fill="white" />
              <path
                d="M-24.5,121.5 v8 M-28.5,125.5 h8"
                stroke="#c2410c"
                strokeWidth={2}
                strokeLinecap="round"
              />
            </>
          }
        />
      </g>
    </svg>
  );
}
