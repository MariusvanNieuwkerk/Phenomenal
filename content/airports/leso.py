"""OM-C 14-CAT-C-LESO — San Sebastián."""

DETAIL = {
    "category": "Cat C",
    "headline": "Mountain · steep RWY 04 (4.75°) · prefer RNP · prescribed circling tracks",
    "pdf_section": "OM-C 14-CAT-C-LESO",
    "qualification": [
        "PIC qualification required; SIC not required.",
        "Type-related qualification: yes.",
        "Self-briefing permitted.",
        "Ground training: yes — self-briefing from OM-C and Jeppesen prior to familiarisation flight.",
        "In-flight familiarisation: yes — any approach at LESO revalidates for 12 months.",
        "Qualification valid 12 months; if last flight > 12 months ago, repeat initial qualification.",
        "PF shall hold current AHQ.",
    ],
    "revalidation": [
        "Any approach at LESO revalidates qualification for 12 months.",
        "Familiarisation: low approach and go-around fulfils requirement — landing not required.",
        "Unqualified PIC as SIC to LESO-qualified commander: one approach/go-around or landing as PF/PM on revenue or non-revenue flight.",
        "Contact Dispatch Supervisor for familiarisation brief; form NTA-TRN-FCM-3104-FLT-TR-ALL.",
    ],
    "limitations": [
        "RWY 04: PAPI 4.75° = STEEP APPROACH — qualified crew, steep procedures, commercial performance only.",
        "Fractional Ops performance prohibited on steep approach.",
        "NO NIGHT CIRCLING to RWY 04. Landing RWY 04 DAY ONLY.",
        "Jeppesen circling minima/speeds NOT compatible with reduced protection areas — use OM-C 9.4 only.",
        "Circling RWY 04 NetJets minima: vis 5 km, ceiling 2400 ft, MDA 2350 ft (2335 ft), max 160 kt IAS.",
    ],
    "threats": [
        "High terrain surrounds the aerodrome.",
        "Steep circling to RWY 04 requires precise track and descent rate — early turn risks excessive RoD.",
        "Circling enters danger area LE(D)-8 — coordinate with TWR.",
        "Do not descend to VOR RWY 22 platform altitude when circling — maintain 2350 ft AMSL.",
    ],
    "overview": (
        "North-west Spain near the French border, ~14 NM southwest of Biarritz (LFBZ). "
        "High terrain surrounds the field. CAT-C requires previous real approach in VMC or approved simulator."
    ),
    "operational_general": [
        "Circuit: RWY 22 right-hand, RWY 04 left-hand (north/west).",
        "Preference: RNP straight-in to RWY 22 or RWY 04.",
        "VOR RWY 22 and circling RWY 04: backup only (equipment unserviceability or GPS jamming).",
    ],
    "weather": [
        "Arrival/departure: as per Jeppesen.",
        "Night approved except circling RWY 04 (see 9.4).",
    ],
    "approaches": [
        {
            "name": "9.2 Preferred — RNP RWY 22 and RWY 04",
            "expanded": True,
            "procedure": [
                "RWY 22: RNP Z/Y/X RWY 22 (charts 12-1, -2, -3) — straight-in as per Jeppesen.",
                "RWY 04: RNP A (chart 12-4) — straight-in as per Jeppesen.",
            ],
        },
        {
            "name": "9.3 Backup — VOR RWY 22",
            "procedure": ["Straight-in to RWY 22 as per Jeppesen chart 13-1."],
        },
        {
            "name": "9.4 Circling to RWY 04 (steep approach)",
            "warning": "Steep approach procedures mandatory. Fractional performance prohibited.",
            "minima": "Vis 5 km, ceiling 2400 ft, MDA 2350 ft (2335 ft), max 160 kt IAS.",
            "procedure": [
                "Based on 160 kt — lower speed reduces bank/RoD but keep published ground track for stabilised approach.",
                "From RNP Z/Y/X RWY 22: join at breakoff or downwind, then same procedure.",
                "Prior to approach: request TWR permission for danger area LE(D)-8; advise circling at 2350 ft AMSL.",
                "2350 ft is above VOR RWY 22 platform — do not descend to platform altitude.",
                "At D5.0 SSN (MAP): if visual for circling, turn right track 264°, maintain 2350 ft.",
                "Maintain 264° until ridge, then left downwind track 219°, maintain 2350 ft.",
                "Follow ridge to mast (~radial 335° from SSN, 1931 ft amsl), maintain 2350 ft.",
                "Left turn 25° AOB; when clear of mast/high ground, descend ~5.5° (1560 fpm at 160 kt).",
                "Max 160 kt, min Vref (steep) + 10 kt.",
                "Do NOT turn significantly earlier — excessive RoD needed to intercept 4.75° PAPI.",
                "Roll out on final ~1000 ft / 1.87 NM from threshold on 4.75° PAPI.",
                "Reduce RoD and speed for stabilised steep approach landing.",
            ],
            "caution": "Early turn before mast requires very high descent rate to stabilise on 4.75° PAPI.",
        },
    ],
    "departure": ["As per Jeppesen."],
    "ground": ["Refer to Jeppesen."],
    "charts": ["12-1/2/3 — RNP RWY 22", "12-4 — RNP A RWY 04", "13-1 — VOR RWY 22"],
}
