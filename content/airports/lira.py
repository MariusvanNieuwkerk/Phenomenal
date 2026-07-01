"""Rome Ciampino (LIRA) — crew special airport (no OM-C chapter 14 briefing in current Part C)."""

DETAIL = {
    "category": "Cat C",
    "headline": "Rome GA · RWY 15/33 · slots/PPR · noise abatement · busy mixed traffic",
    "pdf_section": "LIRA — Rome Ciampino (verify IJet/Waypoint; no OM-C Ch.14 chapter in Part C)",
    "qualification": [
        "Confirm aerodrome category and qualification in IJet / Waypoint before accepting the trip.",
        "Self-brief with company aerodrome briefing and current Jeppesen charts.",
        "PF shall hold current AHQ.",
    ],
    "revalidation": [
        "Review NOTAMs, slots/PPR status, and noise procedures before every operation.",
    ],
    "limitations": [
        "Verify current AIP/NOTAM operating hours (typically 0600–2300 local — exceptions for state/emergency).",
        "Slots and PPR normally required — confirm with handler before dispatch.",
        "Night GA to Rome is often restricted to LIRF when LIRA is closed or unavailable.",
        "Follow published noise abatement SID/ICP when active (check ENAV SUP/NOTAM).",
        "Wet or contaminated runway — use performance data and company limits.",
    ],
    "threats": [
        "High traffic mix: scheduled commercial, military, and GA on a single runway.",
        "Terrain and obstacles east/southeast of the field — brief STAR/approach carefully.",
        "Short final to RWY 15 can be tight with noise tracks — stabilised approach discipline.",
        "Rome CTR/TMA complexity — expect vectors, speed control, and holding.",
        "Apron construction phases may affect parking, taxi routes, and TWY availability (check NOTAM).",
        "Summer heat → performance and brake cooling; winter low vis possible.",
    ],
    "overview": (
        "Rome Ciampino (LIRA/CIA) is the primary business-aviation airport for Rome, ~8 NM SE of the city. "
        "Single runway 15/33 (7226 ft, asphalt). Field elevation 427 ft. Tower 120.500, Ground 121.750, ATIS 122.425."
    ),
    "operational_general": [
        "Coordinate slots/PPR and ground handling early — peak season demand is high.",
        "Customs/immigration normally available within published airport hours.",
        "Jet A-1 available; confirm uplift and GPU with handler.",
        "If LIRA closed, at capacity, or outside hours — plan LIRF (Fiumicino) per company policy and NOTAM.",
        "Brief alternate parking/diversion options before departure.",
    ],
    "weather": [
        "Use Jeppesen/company minima for approach type flown.",
        "Check METAR/TAF and Rome area convective activity in summer.",
    ],
    "approaches": [
        {
            "name": "ILS CAT I RWY 15",
            "expanded": True,
            "procedure": [
                "Primary IFR approach — LOC/DME or ILS per current chart.",
                "Brief noise abatement constraints on departure/arrival when SUP active.",
            ],
        },
        {
            "name": "RNAV (GNSS) RWY 15 / 33",
            "procedure": [
                "RNAV approaches per Jeppesen — confirm RNP capability and chart validity.",
            ],
        },
        {
            "name": "VOR/DME",
            "procedure": [
                "Backup per published charts if GNSS degraded — brief navaid status in NOTAM.",
            ],
        },
    ],
    "departure": [
        "Use published SID/ICP including noise abatement tracks when required.",
        "Confirm runway in use and departure restrictions with Tower/Ground.",
        "Standardise FMS with current waypoint naming from EFB charts.",
    ],
    "ground": [
        "Follow marshaller/Ground instructions — apron layout may change during construction.",
        "PPR includes parking stand — confirm with handler before taxi.",
    ],
    "charts": [
        "Jeppesen airport briefing pages (GEN, ARR, DEP).",
        "Check ENAV website for active SUP affecting noise procedures.",
    ],
}
