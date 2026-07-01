"""OM-C 14-CAT-C-LSZA — Lugano."""

DETAIL = {
    "category": "Cat C",
    "headline": "Alpine lake · Qual A–D · circling RWY 19 · IGS RWY 01 CE-680A · level-bust hotspot",
    "pdf_section": "OM-C 14-CAT-C-LSZA",
    "qualification": [
        "Qual A: day only, high minima — online briefing + test (all fleet crew); sim training for Qual A PICs.",
        "Qual B: RWY 19 day/night lower minima — PIC 12-month validity.",
        "Qual B2: Qual B extended 12–24 months — +500 ft ceiling, +1000 m visibility.",
        "Qual C: IGS RWY 01 — CE-680A only, 12-month validity.",
        "Qual C2: Qual C extended 12–24 months — increased minima.",
        "Qual D: RWY 19 night departure lower minima.",
        "Qual A SIC can act as PM for Qual B/B2/C/C2/D operations.",
        "Recency: within further 12 months fly 3× IFR approaches as PF or PM to retain Qual B/C; else full re-qualification.",
        "PF shall hold current AHQ for all operations.",
        "Qual B/B2 equipment: EGPWS, radio altimeter, VOR, transponder, TCAS, FMS, all PFD/MFD with TAWS terrain, 2 GPS or 2 DME.",
        "Night landing RWY 19: RWY lead-in lighting system (RLLS) must be operative.",
    ],
    "revalidation": [
        "Qual A PIC: online briefing every 12 months, online test every 24 months; validity 24 months from initial.",
        "Qual B/C: 12 months from initial; B2/C2 at 12–24 months with increased minima.",
        "Qual D: 24 months validity.",
        "SIC: online briefing and test only.",
    ],
    "limitations": [
        "VFR takeoff prohibited.",
        "RWY 01 landing: IFR visual approach only for Qual A/B (section 9.6). IGS RWY 01 = Qual C/C2, CE-680A only.",
        "Limit thrust reversers above idle to safety/exceptional cases (noise abatement).",
        "Level-bust hotspot on Jeppesen 10-2B — ODINA 8L, LEGLO 5P, EKLIB 5P hide cleared descent levels.",
    ],
    "threats": [
        "Mountains north of CTR to 7300 ft; south to 4100 ft.",
        "Late descent clearance — prepare PINIK hold.",
        "Level violations on STAR transitions — see operational_general.",
        "Circling RWY 19 FOXTROT/CHARLIE procedures terrain-critical.",
        "CAT C RWY 19: speed limits on Jeppesen 11-2/11-3 determine minima tier.",
    ],
    "overview": (
        "South edge of Italian Alps, 2.2 NM west of Lugano, north of Lake Ceresio. "
        "Special procedures combine airport and NetJets authorisations."
    ),
    "operational_general": [
        "NetJets tailored charts (CO tab): 10-7 (engine fail RWY 01 VMC), 10-7A (engine fail RWY 19 IMC/VMC), 10-7B (missed apch circling CHARLIE RWY 19).",
        "LEGLO 5P / EKLIB 5P: min level = transition level from D29.0 BRL until PINIK, then 6000 ft.",
        "ODINA 8L: min level = transition level from LUGAN until D20.0 MMP, then 6000 ft.",
        "Expect late handover to Lugano — brief PINIK hold.",
    ],
    "weather": [
        "RWY 19 Qual A Cat B: DAY ceiling 3100 ft, vis 5 km.",
        "RWY 19 Qual A Cat C (speed limits met): DAY ceiling 3100 ft, vis 5 km.",
        "RWY 19 Qual A Cat C (speed limits not met): DAY ceiling 5100 ft, vis 8 km.",
        "RWY 01 Qual A: DAY ceiling 5100 ft, vis 8 km — visual approach only.",
        "RWY 19 Qual B: ceiling 1700 ft, vis 3 km day / 5 km night.",
        "RWY 19 Qual B2: ceiling 2200 ft, vis 4 km day / 6 km night.",
        "RWY 01 Qual C/C2: IGS per Jeppesen 11-1 (C2: +500 ft / +1000 m).",
        "Dep RWY 01 Qual A: DAY ceiling 4100 ft, vis 5 km.",
        "Dep RWY 19 Qual A: DAY ceiling 2100 ft, vis 3000 m.",
        "Dep RWY 19 Qual D: day/night vis 400 m, no ceiling required.",
    ],
    "approaches": [
        {
            "name": "RWY 19 — Qual A circling (CAT B) — LOC RWY 01",
            "expanded": True,
            "procedure": [
                "CAT B normally performs LOC RWY 01 for circling RWY 19 (section 9.2).",
                "CAT C: see section 9.4 Category C Aircraft — Approach RWY 19.",
            ],
        },
        {
            "name": "RWY 19 — Qual B/B2 circling (CAT B)",
            "procedure": [
                "Lower minima including night — section 9.3 circling FOXTROT/CHARLIE procedures.",
                "Use tailored 10-7B for missed approach circling CHARLIE RWY 19.",
            ],
        },
        {
            "name": "RWY 01 — IFR visual approach (Qual A/B)",
            "procedure": ["Only visual approach permitted for Qual A/B — section 9.6."],
        },
        {
            "name": "RWY 01 — IGS (Qual C/C2, CE-680A only)",
            "procedure": ["Jeppesen chart 11-1 per Qual C or C2 minima."],
        },
    ],
    "departure": [
        "RWY 01: DAY ONLY, ceiling 4100 ft, vis 5 km — PDCS 01DP4.",
        "Maintain visual ground contact until LUGAN (overhead); LUGAN SID restriction at or above 5000 ft.",
        "Contingency RWY 01: Jeppesen (NetJets) 10-7 and 01DP4 — VMC until outbound on ILU LOC.",
        "CANE2U SID RWY 01: comply INITIAL CLIMB on Jepp 10-3B; remain on published track to LUGAN before left turn to CANNE.",
        "Do NOT turn left to CANNE before LUGAN and 5000 ft — terrain hotspot.",
        "RWY 19 Qual D: night/low vis departure possible but lower max takeoff mass on PDCS.",
        "Qual D may use Qual A procedures/minima (section 10.3) for higher takeoff mass.",
    ],
    "ground": ["Noise: limit reverse thrust above idle."],
    "charts": [
        "10-7 / 10-7A / 10-7B — NetJets contingencies (CO tab).",
        "10-2B — STAR level-bust caution.",
        "11-1 — IGS RWY 01.",
        "19-10 / 19-11 — circling procedures.",
    ],
}
