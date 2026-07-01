"""OM-C 14-CAT-C-LSGS — Sion."""

DETAIL = {
    "category": "Cat C",
    "headline": "Swiss Alps · IGS RWY 25 · Qual A/B · circle/visual RWY 07 · arrestor cables",
    "pdf_section": "OM-C 14-CAT-C-LSGS",
    "qualification": [
        "PIC: simulator training + online briefing. SIC: online briefing.",
        "Type-related: Qual A yes, Qual B yes.",
        "Self-briefing: OM-C review.",
        "Qual A: IGS RWY 25, VFR approaches, IFR departures — PIC or SIC may be PF.",
        "Qual B: additionally circle/visual RWY 07 — PIC must hold Qual B and fly as PF; SIC Qual A PM only.",
        "All pilots: Sion Type A online qualification including online test.",
        "Qual B: simulator syllabus for circle/visual RWY 07.",
    ],
    "revalidation": [
        "Ground training and simulator training every 12 months (Qual A and B).",
    ],
    "limitations": [
        "Only arrivals/departures in this brief are authorised.",
        "VFR prohibited when LSGS military areas active.",
        "IGS RWY 25 + circle RWY 07: Qual B, CAT B only, max 125 kt, DAY ONLY, EGPWS required.",
        "IGS RWY 25 + visual RWY 07: Qual B, Challenger 350 + CAT B, max 135 kt, DAY ONLY.",
        "RNP RWY 25 (AR): prohibited for NetJets.",
        "Do not use military PAPIs — civilian PAPIs ~650 ft from threshold at 4°.",
        "Civil aircraft prohibited from trampling arrestor cables.",
        "PF shall hold current AHQ.",
    ],
    "crew_assignment": [
        "Only Qual B PICs trained EFATO and circle/visual RWY 07 as PF in simulator.",
        "Circle/visual RWY 07 best flown from LHS.",
        "Brief crew assignments fully before execution.",
    ],
    "threats": [
        "CFIT: valley airport, MSA 17,900 ft south, terrain within 10 NM to 11,500 ft.",
        "EGPWS hotspot 1: visual transition IGS to RWY 25 — early alignment, overshoot, hospital avoidance, 6° to 4° PAPI change.",
        "EGPWS hotspot 2: turning final circle RWY 07 — use tailored chart 11-1A.",
        "Loss of control: high platform altitudes increase TAS/groundspeed/turn radius; low-speed manoeuvring on go-around and circle.",
        "Mid-air: mixed military/civilian, GA, helicopters, parachuting to 15,000 ft, hang-gliding, Class E — TCAS and visual lookout.",
        "Runway incursion: very short taxiway to active runway, GA on grass runway, military traffic.",
        "Runway excursion: 6° IGS to 4° PAPI at D7; visual align after D6.0 SIO avoiding hospital and south terrain.",
        "Arrestor cables during MIL activity — confirm lowered before approach/departure.",
        "Qual B below Qual A minima: max landing mass limited to RWY 25 IMC max dry takeoff mass (25DP5) for balked landing.",
    ],
    "overview": (
        "Mountain airport in Swiss Alps at 1582 ft elevation. Terrain rises above 11,500 ft within 10 NM. "
        "Mixed military and civilian operations."
    ),
    "operational_general": [
        "Arrestor cables may be in use during MIL activity — normally lowered for civilian use; confirm with ATC.",
        "During MIL activity check SID climb profile notes on Jeppesen.",
        "High platform on approach — configure with care, respect flap/slat altitude limits.",
        "Qual B may use Qual A performance if DAY ONLY and Qual A minima assured.",
    ],
    "weather": [
        "IGS RWY 25 Qual A: ceiling 6500 ft, MDA 8000 ft, vis 8 km DAY.",
        "IGS RWY 25 Qual B: DA per Jeppesen, vis 5 km, NIGHT approved.",
        "VFR RWY 25: ceiling 15,500 ft, vis 8 km DAY.",
        "Circle/visual RWY 07: ceiling 6500 ft, vis 8 km DAY ONLY (Qual B).",
        "VFR RWY 07: ceiling 16,400 ft, vis 8 km DAY.",
        "IFR dep RWY 25 Qual A: ceiling 6500 ft, vis 8 km DAY.",
        "IFR dep RWY 25 Qual B: vis 550 m NIGHT contingency.",
        "IFR dep RWY 07: ceiling 6500 ft, vis 8 km DAY ONLY.",
        "Actual minima may be higher due to mass and OAT.",
    ],
    "approaches": [
        {
            "name": "9.2 IGS RWY 25",
            "expanded": True,
            "minima": "See section 6 table. Qual B: missed approach climb gradient determines DA — check PDCS.",
            "procedure": [
                "Missed approach per Jeppesen 11-1.",
                "Balked landing RWY 25: NetJets chart 10-7.",
                "Note 6° IGS to 4° visual at D7 ISI.",
                "Visual approach inset on 11-1: avoid overflying hospital, keep hospital to right.",
            ],
            "caution": (
                "Honeywell FMS: first MAP point may show spurious right turn to 063° — procedure flies correctly once activated; "
                "monitor closely, revert to conventional SIO VOR nav if turn begins."
            ),
        },
        {
            "name": "9.3 VFR approach RWY 25",
            "warning": "Only when IGS RWY 25 or SIO VOR unavailable. PROHIBITED when MIL areas active.",
            "minima": "Ceiling 15,500 ft, vis 8 km DAY.",
            "procedure": [
                "Verify VMC and visual references throughout.",
                "Vectors or self-position track GS603 to MASAB 17,000 ft; cancel IFR no later than MASAB.",
                "Use 11-1 vertical speed vs groundspeed table; FMS vertical path as reference.",
                "Fly route E-E1-E2 at or above 3000 ft (waypoints in brief).",
                "Avoid hospital, proceed visual to land RWY 25.",
                "Missed approach per 11-1 — do not follow IGS back course outbound.",
                "D10.8 ISI = D10.0 SIO; D23.3 ISI = D22.5 SIO.",
            ],
        },
        {
            "name": "9.4 IGS RWY 25 + circle to land RWY 07 (CAT B, Qual B)",
            "warning": "Visual manoeuvre. Max 125 KIAS. EGPWS required. PF must be Qual B PIC with sim training. LHS recommended.",
            "minima": "Ceiling 6500 ft, vis 8 km DAY. NetJets minima on tailored 11-1A more restrictive than standard.",
            "procedure": [
                "Follow NetJets tailored chart 11-1A lateral/vertical guidance.",
                "Perform IGS to NetJets circle minima on 11-1A; missed approach per 11-1 if needed at that point.",
                "When visual assured: circle to land RWY 07 — RNAV visual guidance per 11-1A.",
                "Re-check waypoint insertion by both crew — RAIM deviation risks off-course in mountains.",
                "Landing weight may need restriction to stay within max speeds.",
            ],
        },
        {
            "name": "9.5 IGS RWY 25 + visual approach RWY 07 (CL350 + CAT B, Qual B)",
            "procedure": [
                "Same lateral/vertical as circle procedure; max 135 KIAS.",
                "Perform IGS to visual approach minima per tailored 11-1B.",
                "When visual assured: visual approach RWY 07 per 11-1B.",
            ],
        },
    ],
    "departure": [
        "IFR RWY 25: charts 10-3A/E/C/G, NetJets 10-7, 25DP4/5.",
        "IFR RWY 07: NetJets 19-11, 07DP4 — DAY ONLY.",
        "VFR RWY 25: ceiling 16,400 ft, vis 8 km DAY.",
        "VFR RWY 07: see brief 07DP4.",
        "Non-standard flap retraction for time-limited takeoff thrust aircraft on go-around/missed.",
        "Missed approach/go-around: max gradient climb to MSA for terrain clearance.",
    ],
    "ground": [
        "Arrestor cables — confirm lowered; do not taxi over cables.",
        "Short taxiway to active runway — runway incursion risk.",
    ],
    "charts": [
        "11-1 / 11-1A / 11-1B — NetJets IGS and circle/visual RWY 07.",
        "19-11 — departures RWY 07 / balked circle.",
        "10-7 — balked landing RWY 25.",
        "25DP4/5, 07DP4 — PDCS.",
    ],
}
