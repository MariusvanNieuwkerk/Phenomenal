"""OM-C 14-CAT-C-EDFE — Frankfurt-Egelsbach."""

DETAIL = {
    "category": "Cat C",
    "headline": "Day only · RWY 26 arrivals · EDDF proximity · VFR/IFR cancel · powerlines on final",
    "pdf_section": "OM-C 14-CAT-C-EDFE",
    "qualification": [
        "PIC training required; SIC training not required.",
        "Type-related qualification: yes.",
        "Self-briefing permitted.",
        "Simulator training: yes, 12-month revalidation.",
        "PF shall hold current AHQ.",
        "Departure RWY 26: pilot flying shall be qualified EDFE PIC.",
        "PIC must not be designated 'INEXPERIENCED'.",
        "TCAS and EGPWS must be operative (no MEL).",
    ],
    "revalidation": [
        "Simulator training every 12 months.",
        "Ground training not required for revalidation.",
    ],
    "limitations": [
        "DAY ONLY operations.",
        "PROHIBITED: approaches to RWY 08.",
        "PROHIBITED: SLO, GA or fractional ops performance — commercial performance factors only.",
        "Arrivals: RWY 26 only (proximity to EDDF).",
        "Departures: RWY 08 and RWY 26 permitted.",
        "Arrival minima RWY 26: 8 km vis, 1900 ft ceiling (2300 ft QNH).",
        "Departure RWY 08 lower-vis procedure: 5 km vis when applicable.",
    ],
    "threats": [
        "Collision risk: no dedicated approach — LANGEN/Frankfurt App vectors to radar minimum then cancel IFR for visual final in Class E/G airspace.",
        "Uncontrolled traffic expected near EDFE — adhere to OM-A 8.3.1 VFR Policy.",
        "EDDF Class C/D airspace 3 NM from RWY 18 extended centreline — stepped descent and IFR cancel before Frankfurt zone lateral limit.",
        "RWY 26: railway and powerlines ~900 ft before displaced threshold (32 ft height, lit, balloon markers).",
        "APAPI 4.4° is only vertical guidance — follow APAPI to clear powerlines.",
        "Balked landing below 1500 ft routes into Frankfurt Class C airspace.",
    ],
    "overview": (
        "General aviation field 11 NM south of Frankfurt city, 5 NM south of Frankfurt-Main (EDDF). "
        "MSA within 25 NM of ARP is 4000 ft. Service by EGELSBACH INFORMATION (air-to-ground) "
        "and EGELSBACH APRON for startup/clearance. LANGEN INFORMATION provides FIS."
    ),
    "operational_general": [
        "NetJets tailored charts: 30-3-NJE (VFR departure), 39-10-NJE (visual approach RWY 26 via ASBAB).",
        "Required waypoints in FMS (max 160 KIAS): SPESA, PEKIG, ASBAB, DELTA, D3, YANKEE (Y).",
        "YANKEE within 0.3 NM of ASBAB.",
        "Standard VFR squawk in Germany: 7000.",
        "Webcam: http://www.egelsbach-airport.com",
    ],
    "weather": [
        "Cat B arrival: 8 km vis, 1900 ft ceiling.",
        "Cat B departure: 8 km vis*, 1900 ft ceiling (*RWY 08 lower-vis 5 km may apply).",
    ],
    "approaches": [
        {
            "name": "9.2 Arrival RWY 26 via PEKIG – ASBAB",
            "expanded": True,
            "minima": "DAY ONLY. Visibility 8 km, ceiling 1900 ft (2300 ft QNH).",
            "performance": (
                "PDCS as applicable. Restrict arrival weight to not exceed departure DP26 — "
                "balked landing scenario follows motorway to the south."
            ),
            "procedure": [
                "Request radar vectors to PEKIG with LANGEN — they know this routing.",
                "FMS route: PEKIG (3000 ft) – ASBAB (2100 ft / winter 2300 ft) – EDFE RWY 26.",
                "ASBAB is the MAP for this approach.",
                "Contact EGELSBACH INFORMATION; listening watch on secondary VHF no later than 10 min prior (AIP).",
                "LANGEN may vector to intercept final via ASBAB (course 265°).",
                "When EDDF on westerly arrivals (25L/C/R), expect routing to PEKIG via EDDF RNAV STAR (KERAX, SPESA, INBOS likely).",
                "ATC may require holding at CHA VOR (see EDDF 10-2 or EDFE 39-10-NJE).",
                "Cancel IFR prior to ASBAB (DFS instruction) — if not possible, follow missed approach.",
                "From ASBAB 2100 ft QNH (1700 ft AAL) descend to 1500 ft to enter RMZ at/below 1500 ft (5 NM from threshold).",
                "Reduce RoD, intercept and follow APAPI 4.4° — do NOT fly shallow glidepath (displaced threshold, powerlines, railway).",
                "At ASBAB RWY may not be in sight at 8 km minima — if clear of cloud and ground in sight, continue visual descent.",
                "VFR alternative: YANKEE (Y)-(VFR 1400')-RWY26.",
                "iPad VFR map with Roads and Airspace aids SA.",
            ],
            "missed": "See 9.3 Missed Approach RWY 26 (Jepp 39-10-NJE). Contingency: PDCS STRAIGHT and 26DP.",
        },
        {
            "name": "9.3 Missed approach RWY 26",
            "procedure": [
                "At ASBAB (7.7 NM from RWY): if unable to cancel IFR/VMC, or IFR cancel not confirmed — follow LANGEN/Frankfurt instructions.",
                "If no instructions: climb 4000 ft, left climbing turn (min 15° AOB, max 160 KIAS), inbound CHA VOR, inform LANGEN/Frankfurt App.",
                "Lost comm: left turn max 160 KIAS inbound CHA, climb 4000 ft, regain contact.",
                "Enter published holding per EDDF STAR/RNAV charts.",
            ],
        },
        {
            "name": "9.4 Balked landing RWY 26 after cancelling IFR",
            "procedure": [
                "Maintain VMC throughout.",
                "> 5 NM from threshold (at/above 1500 ft QNH): follow 9.3 missed approach — use FMS distance (no DME). Contact LANGEN/Frankfurt ASAP (enters Class C above 1500 ft).",
                "During final visual descent below 1500 ft: climb maintain 1400 ft, max 160 KIAS, route D3 – DELTA – FKS (1400'/K160-).",
                "Advise EGELSBACH INFO. For additional approach: remain with INFO, expect IFR regain at DELTA, routed to PEKIG/YANKEE.",
                "If no additional approach: remain with INFO, expect IFR regain with LANGEN for further climb passing DELTA.",
            ],
        },
    ],
    "departure": [
        "RWY 08 exit YANKEE: route Y (1400'/K160-); after Y if VMC climb 3400 ft MSL, coordinate with LANGEN or Frankfurt App. Y is compulsory reporting point.",
        "RWY 08 lower-vis (5 km, clear of cloud until IFR): EGELSBACH INFO relays LANGEN clearance, slot or release. IFR starts passing MRVA. Contingency: straight procedure only.",
        "RWY 26 exit DELTA: DAY ONLY, 8 km vis, 1900 ft ceiling, clear of cloud until IFR. PDCS 26DP.",
        "At 785 ft (400 AGL) turn left to D3; route D3 – DELTA – FKS, maintain 1400 ft max 160 KIAS. Avoid Erzhausen (noise). Stay west of A5 within 0.5 NM to avoid EDDF CTR.",
        "Consider listening watch EDDF TWR 118.780 or 119.905 MHz.",
        "See Jeppesen EDFE 30-3-NJE NetJets VFR Departure.",
    ],
    "ground": ["See Jeppesen for parking stands."],
    "charts": [
        "30-3-NJE — NetJets VFR departure.",
        "39-10-NJE — visual approach RWY 26 via ASBAB.",
        "39-2 — frequencies; 39-1A — LANGEN FIS.",
    ],
}
