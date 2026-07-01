"""OM-C 14-CAT-C-EGLC — London City."""

DETAIL = {
    "category": "Cat C",
    "headline": "Steep approach · short runway · magnetic anomalies · level-bust hotspot · noise-sensitive",
    "pdf_section": "OM-C 14-CAT-C-EGLC",
    "qualification": [
        "PIC: EGLC PIC qualification required — includes Steep Approach PF and current AHQ.",
        "SIC: EGLC SIC qualification required.",
        "Type-related qualification: yes.",
        "Self-briefing: not permitted for initial qualification.",
        "Ground training: yes for initial and revalidation.",
        "Simulator training: yes — EMB-505, BD-100, BD-700 every 6 months; remaining fleets every 12 months.",
        "In-flight familiarisation: not applicable.",
        "Flight training: not required.",
    ],
    "revalidation": [
        "Ground training + self-briefing every 12 months.",
        "Simulator training: 6 months (EMB-505, BD-100, BD-700) or 12 months (other fleets).",
    ],
    "limitations": [
        "Steep approach approved aircraft and qualified crew only.",
        "Steep approach procedures and performance shall be used on every approach.",
        "Fractional Ops performance is prohibited.",
        "See OM-A 8.3.28.3 Steep Approach Operations, OM-D 2.1.1.5.6 and OM-D 2.1.3.4.6.",
        "Nominated diversion to EGLC is prohibited — customer/crew preference diversions only via Dispatch or Duty Manager.",
        "Runway operations only when DRY, or WET with small water patches not exceeding 3 mm depth.",
        "Prohibited when runway is contaminated: ice/slush > 3 mm, dry snow > 10 mm, or friction worse than 'medium' (unless AFM permits).",
    ],
    "crew_assignment": [
        "BD-700: LHS shall be PF for takeoff and landing.",
        "Other fleets: PF for takeoff at PIC discretion; PF must hold current AHQ.",
        "PF for approach: current AHQ + Steep Approach PF qualification.",
        "PM for approach: minimum Steep Approach PM qualification.",
    ],
    "threats": [
        "Close-in buildings and obstacles — steep approach required.",
        "Possible low-level turbulence and windshear in strong winds.",
        "Short final sector — unstable approach risk, especially on visual steep descent.",
        "Magnetic anomalies at RWY 27 holding point M and Jet Centre apron.",
        "Level-bust hotspot — follow OM-B low level-off procedures.",
        "Noise monitoring — strict abatement procedures.",
    ],
    "overview": (
        "Busy civil airport in East London. Category C because steep approach training is mandatory. "
        "Short runway, close obstacles, possible magnetic anomalies, and strict noise monitoring. "
        "Refer to Jeppesen Airport Briefing pages 40-1P through 40-1P2 for additional information."
    ),
    "operational_general": [
        "Airport surrounded by close-in buildings — steep approach geometry required.",
        "Expect possible low-level turbulence and windshear in strong winds.",
        "Under normal conditions conduct ILS/LOC approach (section 9.2).",
        "Visual approach only when ILS/LOC unavailable by NOTAM or AIP Supplement.",
    ],
    "weather": [
        "Arrival minima: refer to section 9 and Jeppesen by approach type.",
        "Departure: as per Jeppesen.",
        "EMB-505 max crosswind landing 28 kt; max tailwind landing 5 kt.",
        "CE-560XLS: 24 kt crosswind / 0 kt tailwind landing.",
        "CE-680A: 30 kt crosswind / 5 kt tailwind landing.",
        "BD-100 / CL-600: 20 kt crosswind / 0 kt tailwind landing.",
        "BD-700: 15 kt crosswind / 0 kt tailwind landing.",
        "EGLC normally reduces tailwind to zero; slight TWC (Southerly) up to 5 kt acceptable per OM-B/AFM when performance permits.",
        "Max wind for taxiing: 50 kt all fleets.",
        "Max crosswind takeoff: as per OM-B.",
    ],
    "approaches": [
        {
            "name": "9.2 ILS/LOC approaches (normal)",
            "expanded": True,
            "minima": "As per Jeppesen.",
            "performance": "Steep approach performance shall be used. Check tailwind carefully — adhere to fleet-specific/AFM tailwind limitations.",
            "procedure": [
                "As per Jeppesen.",
                "Steep approach procedures shall be used.",
            ],
            "caution": (
                "ODLEG transition does not connect directly to ILS 09 — distance from ODLEG to localiser is less than 1.9 NM. "
                "Careful planning and monitoring of flight director modes required."
            ),
        },
        {
            "name": "9.3 Visual approach (contingency only)",
            "warning": (
                "Visual approach only when ILS/LOC not available (NOTAM/AIP Supplement for unserviceable navaids). "
                "In all other conditions conduct ILS/LOC."
            ),
            "minima": "Ceiling 2000 ft, visibility 6 km. PAPI must be operative.",
            "performance": "Steep approach performance shall be used. Check tailwind per AFM.",
            "procedure": [
                "Refer to chart 49-10 VISUAL APPROACH PROFILE (CAT A, B & C) — in TAXI tab on iPad FD Pro (not APP tab).",
                "ATC may commence visual from 2000 ft (not 1500/1600 ft on Jepp 49-10) — traffic flow with Thames Radar and noise abatement (~3.4 NM from threshold).",
                "Distances on chart based on DME which may be unavailable — use speed/RoD tables on ILS chart.",
                "Configure early; smooth but positive attitude for final descent to avoid being high.",
                "Hold required visual references before final visual descent.",
                "Be prepared to go around — errors in visual steep descent entry/maintenance are common.",
            ],
            "missed": [
                "EGLC may provide specific missed approach instructions on visual approach.",
                "RWY 27: follow ILS/LOC published missed approach; if ILSR unavailable use LON DME (Jepp 41-2).",
                "RWY 09: climb straight ahead (track 092°) to 2000 ft, follow ATC; expect handoff to Thames Radar (Director).",
            ],
        },
    ],
    "departure": [
        "As per Jeppesen.",
        "Short runway — consider static takeoff.",
        "Noise abatement takeoff required — noise monitoring in effect.",
        "Level-bust hotspot — follow OM-B low level-off procedures.",
    ],
    "ground": [
        "Apron very limited — marshaller required for all apron movements and engine starts.",
        "Magnetic anomalies: ferrous material in RWY structure and metallic items at Jet Centre apron.",
        "Threat most apparent at RWY 27 holding point M (especially facing North) and Jet Centre apron.",
        "Use slew mode if able, or face East instead of North at holding point M.",
        "Resolve any HDG discrepancy before departure.",
        "APU time limitations — see Jepps 40-4; consider GPU.",
    ],
    "charts": [
        "Jeppesen 40-1P through 40-1P2 — airport briefing.",
        "49-10 — visual approach profile (TAXI tab on FD Pro).",
        "41-2 — RWY 27 missed approach with LON DME.",
    ],
}
