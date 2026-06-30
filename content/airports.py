"""Category C and special airport reference data from OM-C Chapter 14."""

BRIEFING_STRUCTURE = [
    "Qualification requirements",
    "Initial qualification requirements",
    "Revalidation requirements",
    "In-flight familiarisation syllabus",
    "Limitations / Miscellaneous",
    "Weather / Airport limitations",
    "Overview",
    "Operational procedures — General",
    "Arrival procedures",
    "Departure procedures",
    "Ground procedures",
    "Miscellaneous",
    "Charts / Pictures / Other",
    "Changes since the last revision",
]

CATEGORY_C_AIRPORTS = [
    {"icao": "EDFE", "name": "Frankfurt-Egelsbach", "tags": ["Europe"]},
    {"icao": "EGLC", "name": "London City", "tags": ["Europe", "Steep approach", "Short runway"]},
    {"icao": "ENAT", "name": "Alta", "tags": ["Arctic", "Mountain", "Cold weather"]},
    {"icao": "ENSB", "name": "Longyearbyen / Svalbard", "tags": ["Arctic", "Remote"]},
    {"icao": "ENTC", "name": "Tromsø / Langnes", "tags": ["Arctic", "Northern Norway"]},
    {"icao": "LESO", "name": "San Sebastián", "tags": ["Europe", "Terrain"]},
    {"icao": "LFKC", "name": "Calvi / St Catherine", "tags": ["Europe", "Terrain"]},
    {"icao": "LFLB", "name": "Chambéry / Aix-les-Bains", "tags": ["Europe", "Alpine", "Terrain"]},
    {"icao": "LFLP", "name": "Annecy / Meythet", "tags": ["Europe", "Alpine", "Terrain"]},
    {"icao": "LFTZ", "name": "La Môle", "tags": ["Europe", "Coastal"]},
    {"icao": "LICG", "name": "Pantelleria", "tags": ["Europe", "Island"]},
    {"icao": "LICR", "name": "Reggio Calabria", "tags": ["Europe", "Terrain"]},
    {"icao": "LIMG", "name": "Albenga / Riviera", "tags": ["Europe", "Terrain"]},
    {"icao": "LIPB", "name": "Bolzano", "tags": ["Europe", "Alpine", "Terrain"]},
    {"icao": "LOWI", "name": "Innsbruck", "tags": ["Europe", "Alpine", "Terrain", "Special"]},
    {"icao": "LPMA", "name": "Madeira", "tags": ["Europe", "Island", "Terrain"]},
    {"icao": "LSGS", "name": "Sion", "tags": ["Europe", "Alpine", "Terrain"]},
    {"icao": "LSZA", "name": "Lugano", "tags": ["Europe", "Alpine", "Terrain"]},
    {"icao": "LSZS", "name": "Samedan / St Moritz", "tags": ["Europe", "Alpine", "High elevation"]},
    {"icao": "LTAS", "name": "Zonguldak / Çaycuma", "tags": ["Europe", "Terrain"]},
    {"icao": "LTFG", "name": "Alanya / Gazipaşa", "tags": ["Europe", "Coastal"]},
    {"icao": "VNKT", "name": "Kathmandu / Tribhuvan", "tags": ["Himalaya", "High elevation", "Special"]},
    {"icao": "VQPR", "name": "Paro", "tags": ["Himalaya", "Special", "Terrain"]},
]

AIRPORT_DETAILS = {
    "EGLC": {
        "category": "Cat C",
        "headline": "Steep approach · short runway · noise-sensitive · level-bust hotspot",
        "qualification": [
            "PIC: EGLC PIC incl. Steep Approach PF + AHQ required.",
            "SIC: EGLC SIC qualification required.",
            "Type-related qualification: yes.",
            "Self-briefing: not permitted for initial qualification.",
        ],
        "limitations": [
            "Steep approach approved aircraft and qualified crew only.",
            "Steep approach procedures and performance shall be used.",
            "Fractional Ops performance is prohibited.",
            "See OM-A 8.3.28.3, OM-D steep approach sections.",
        ],
        "crew_assignment": [
            "PF for approach: current AHQ + Steep Approach PF.",
            "PM for approach: minimum Steep Approach PM qualification.",
            "PF for takeoff: at PIC discretion; must hold current AHQ.",
        ],
        "overview": (
            "Busy civil airport in East London. Category C due to steep approach training. "
            "Short runway, close obstacles, possible magnetic anomalies, and strict noise monitoring."
        ),
        "weather": "Refer to OM-C arrival section and Jeppesen for minima by approach type.",
        "departure": [
            "Short runway — consider static takeoff.",
            "Noise abatement takeoff required; noise monitoring in effect.",
            "Level-bust hotspot — follow OM-B low level-off procedures.",
        ],
        "ground": [
            "Apron space limited — marshaller required for all apron movements and engine starts.",
            "Magnetic anomalies near RWY structure and Jet Centre apron — use slew mode or face East at holding point M.",
            "Resolve any HDG discrepancy before departure.",
            "APU time limits apply — consider GPU (see Jeppesen).",
        ],
        "pdf_section": "OM-C 14 · EGLC (London City)",
    },
    "LOWI": {
        "category": "Cat C",
        "headline": "Alpine valley · circling · terrain · strict qualification",
        "qualification": [
            "PIC and SIC LOWI qualifications required.",
            "Simulator and ground training per OM-C revalidation schedule.",
        ],
        "limitations": [
            "Circling and visual manoeuvres require increased attention to terrain.",
            "Wind and weather limits per OM-C and Jeppesen — check current briefing.",
            "Performance and balked landing considerations critical in valley environment.",
        ],
        "overview": (
            "Innsbruck sits in an Alpine valley with demanding approaches, often requiring "
            "specific training and careful energy management."
        ),
        "departure": ["Follow Jeppesen SID and OM-C departure procedures.", "Terrain-aware climb and noise procedures."],
        "arrival": ["Brief circling options and increased minima where applicable.", "Stabilised approach gates per OM-B profiles."],
        "pdf_section": "OM-C 14 · LOWI (Innsbruck)",
    },
    "LPMA": {
        "category": "Cat C",
        "headline": "Island · offset approach · winds · go-around considerations",
        "qualification": ["LPMA PIC/SIC qualifications per OM-C.", "Self-briefing validity per OM-C tables."],
        "limitations": [
            "Unique approach geometry over water and elevated runway.",
            "Wind limits and visual references critical.",
        ],
        "overview": "Madeira (Funchal) requires specific familiarisation due to approach complexity and wind sensitivity.",
        "departure": ["Short runway considerations.", "Wind shear awareness."],
        "arrival": ["Brief offset approach and missed approach procedure.", "Stabilised approach mandatory."],
        "pdf_section": "OM-C 14 · LPMA (Madeira)",
    },
    "LIPB": {
        "category": "Cat C",
        "headline": "Alpine · short runway · performance critical",
        "qualification": ["LIPB qualifications per OM-C.", "Extended briefing in OM-C (large chapter)."],
        "limitations": ["Performance-limited field.", "Terrain and weather constraints."],
        "overview": "Bolzano is a high-workload alpine airfield with detailed OM-C briefing material.",
        "pdf_section": "OM-C 14 · LIPB (Bolzano)",
    },
    "ENAT": {
        "category": "Cat C",
        "headline": "Arctic · mountain · cold weather · circling restrictions",
        "qualification": ["ENAT PIC/SIC per OM-C.", "Mountain airport briefing required."],
        "limitations": [
            "Circling at night prohibited (OM-A 8.1.3.6.4).",
            "Circle-to-land and Visual LNAV: increased minima 2070 ft ceiling, 5 km vis, DAY ONLY.",
            "RWY 11 landing: max 15 kt wind from 180°–220° mag (NetJets windshear restriction).",
            "Circle / Visual LNAV: max 40 kt (terrain and turbulence mitigation).",
        ],
        "overview": (
            "Alta is above the Arctic Circle in northern Norway. Short daylight in winter, "
            "severe cold, and significant terrain influence on approaches."
        ),
        "weather": "RWY 11 preferred for landing; RWY 29 preferred for takeoff. Multiple RNP and conventional options — see OM-C tables.",
        "pdf_section": "OM-C 14 · ENAT (Alta)",
    },
    "VQPR": {
        "category": "Cat C",
        "headline": "Himalaya · very demanding · strict qualification",
        "qualification": ["VQPR qualifications mandatory for PIC/SIC.", "No substitute for full OM-C briefing."],
        "limitations": ["Only authorised crews.", "Strict weather and performance limits."],
        "overview": "Paro is one of the most demanding airports in the NetJets network — full OM-C briefing mandatory.",
        "pdf_section": "OM-C 14 · VQPR (Paro)",
    },
    "VNKT": {
        "category": "Cat C",
        "headline": "High elevation · Himalayan terrain",
        "qualification": ["VNKT qualifications per OM-C."],
        "overview": "Kathmandu Tribhuvan requires specific training due to terrain and elevation.",
        "pdf_section": "OM-C 14 · VNKT (Kathmandu)",
    },
}
