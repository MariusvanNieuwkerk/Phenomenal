"""OM-C 14-CAT-C-LIPB — Bolzano."""

DETAIL = {
    "category": "Cat C",
    "headline": "Alpine · VFR preferred · prescribed tracks · CAT B circle only · not in sim",
    "pdf_section": "OM-C 14-CAT-C-LIPB",
    "qualification": [
        "PIC and SIC LIPB qualifications required.",
        "LIPB NOT modelled in flight simulators — familiarisation flight required before operation.",
        "Online qualification test — certificate to lis-crewtraining@netjets.com and lis-flightdispatch@netjets.com.",
        "PF shall hold current AHQ.",
        "See OM-C section 4 for in-flight familiarisation syllabus.",
    ],
    "revalidation": [
        "Per OM-C revalidation schedule and online test requirements.",
    ],
    "limitations": [
        "DAY ONLY. Global 5000/6000 PROHIBITED.",
        "EGPWS and TCAS shall be operable.",
        "PROHIBITED: LOC DME RWY 01, RNP RWY 01, night operations.",
        "Authorised IFR: VOR A + circle-to-land with prescribed tracks (CAT B only).",
        "Preferred: VFR approach using VOR A initial guidance (CAT B and C) when weather/traffic permit.",
        "Deviation from OM-A 8.3.1 para 1 approved — VFR in preference to IFR when suitable.",
        "VFR arrivals from North via Brenner Pass or Reschen Pass PROHIBITED.",
        "Circle prescribed tracks: max 15 kt surface wind incl. gusts (NetJets).",
        "Critical manoeuvring speed — weight/flap must permit compliance.",
        "RNP initial climb and RNP transitions PROHIBITED.",
    ],
    "threats": [
        "Confusion: complicated IFR/VFR and prescribed tracks vary by category; NetJets VFR minima stricter than AIP.",
        "Collision: busy VFR/IFR valley thoroughfare; GA, helicopters, gliders; VFR traffic may be encountered during IFR.",
        "Combined ATZ/RMZ Class G — only one IFR arrival at a time but terrain masking makes separation impractical.",
        "CFIT: significant terrain; protracted VFR arrivals increase risk. EGPWS mandatory.",
        "OEI: valley south is safe escape toward Lake Garda / Villafranca (LIPX) 194°/66 NM.",
        "Unstable approaches: prescribed tracks and RWY 19 downwind with airport out of sight; displaced thresholds; PAPI 4.48°.",
        "EGPWS alerts possible from terrain spurs during approaches — see arrival sections.",
    ],
    "overview": (
        "Challenging mountain airport in Italian Alps near Austrian border, between Innsbruck and Verona. "
        "Preferred approach: VFR using VOR A to RWY 01 or 19. "
        "Pilot briefing: https://www.bolzanoairport.it/en/pilots-corner-en.htm"
    ),
    "operational_general": [
        "IFR departures preferred over VFR when suitable.",
        "VFR arrivals shall follow routings in this briefing.",
        "Latest VOR break-off for VFR via VOR A: RWY 01 at D10 OZE (D13 IBZ); RWY 19 at D6.5 OZE (D3.5 IBZ).",
        "PDCS 'STPT' performance: use full runway starter extension (grey 'Start point' on Jeppesen 10-9).",
        "Minima higher than Jeppesen 13-1 for NetJets VFR arrivals.",
    ],
    "weather": [
        "VFR RWY 01 via VOR A: vis 8 km, ceiling 8313 ft (9100 QNH) — preferred Cat B/C.",
        "VOR A circle prescribed tracks RWY 01: vis 5 km, ceiling 4133 ft (4920 QNH) — CAT B only, max 15 kt wind.",
        "VFR RWY 01 OZE U/S: vis 8 km, ceiling 11,713 ft (12,500 QNH).",
        "VFR RWY 19 via VOR A: vis 8 km, ceiling 8313 ft — preferred if RWY 01 not available.",
        "VOR A circle prescribed tracks RWY 19: vis 5 km, ceiling 4133 ft — CAT B only.",
        "IFR dep RWY 19: vis 5 km, ceiling 2700 ft (3487 QNH) — preferred.",
        "IFR dep RWY 01: vis 5 km, ceiling 2700 ft — 10-3B or 10-3C to OZE.",
        "VFR dep RWY 01/19: vis 8 km, ceiling 11,713 ft (12,500 QNH).",
    ],
    "approaches": [
        {
            "name": "Preferred — VFR RWY 01 using VOR A",
            "expanded": True,
            "minima": "DAY vis 8 km, ceiling 8313 ft (9100 QNH) — higher than Jeppesen 13-1.",
            "performance": "PDCS Arrival '01', balked landing Departure '01DP1'.",
            "procedure": [
                "Straight-in VFR using VOR A for initial descent — Cat B and Cat C.",
                "Break off VOR at D10 OZE (D13 IBZ) latest — excessive RoD inside this distance.",
            ],
        },
        {
            "name": "IFR backup — VOR A circle prescribed tracks RWY 01 (CAT B only)",
            "minima": "Vis 5 km, ceiling 4133 ft (4920 QNH). Max 15 kt wind incl. gusts.",
            "procedure": ["Charts 13-1, 19-10, 19-11 balked landing. Lower minima than VFR but CAT B only."],
        },
        {
            "name": "VFR RWY 19 using VOR A",
            "procedure": [
                "Approved Cat B and C; requires slow-speed manoeuvring.",
                "Break-off D6.5 OZE (D3.5 IBZ) for downwind positioning.",
                "Airport out of sight during downwind — brief carefully.",
            ],
        },
        {
            "name": "VOR A circle prescribed tracks RWY 19 (CAT B only)",
            "minima": "Vis 5 km, ceiling 4133 ft. Max 15 kt wind.",
            "procedure": ["Chart 19-12. Circling RWY 19 from LOC/DME or RNP prohibited."],
        },
        {
            "name": "Contingency — VOR OZE unserviceable",
            "minima": "Vis 8 km, ceiling 11,713 ft (12,500 QNH). Chart 19-1.",
        },
    ],
    "departure": [
        "IFR RWY 19 preferred: visual manoeuvre to OZE, IFR climb to FORER, SIDs from FORER — '19', '19DP2' or '19STPT'.",
        "IFR RWY 01: 10-3B (visual manoeuvre) or 10-3C (more limiting gradient/speed) to OZE, climb to FORER.",
        "VFR RWY 01/19 contingency if IFR unavailable (e.g. OZE U/S) — charts 19-1 through 19-3A.",
        "RNP initial climb and transitions prohibited.",
    ],
    "ground": [
        "Performance planning essential — check PDCS before commit.",
        "Only one IFR arrival at a time at airport — coordinate with traffic.",
    ],
    "charts": [
        "13-1 — VOR A.",
        "19-1 through 19-3A — VFR approaches/departures.",
        "19-10 / 19-11 / 19-12 — prescribed tracks and balked landing.",
        "10-3B/C/E — IFR departures.",
    ],
}
