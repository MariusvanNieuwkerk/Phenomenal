"""OM-C 14-CAT-C-LSZS — Samedan / St Moritz."""

DETAIL = {
    "category": "Cat C",
    "headline": "Highest airport in Europe · DAY ONLY · VFR preferred · AFIS · narrow RWY",
    "pdf_section": "OM-C 14-CAT-C-LSZS",
    "qualification": [
        "PIC: simulator training + online test — tracked on ATMS / Waypoint 'My Currency'.",
        "SIC: online test only — NOT tracked on ATMS/My Currency.",
        "Validity 12 months per OM-A 5.4.1.2.10.",
        "Simulator training can waive 24-month landing recency when NAA-approved sim used.",
        "Type-related qualification: no. Self-briefing: yes.",
        "PF shall hold current AHQ.",
    ],
    "revalidation": [
        "Online test every 12 months (PIC and SIC).",
        "Simulator training every 12 months (PICs only).",
    ],
    "limitations": [
        "All operations DAY ONLY (VFR preferred and IFR).",
        "IFR: mandatory RAIM requirements for non-SBAS aircraft (see OM-C appendix).",
        "Only approaches listed in section 6 and 9 are authorised.",
        "Narrow runway — performance and PDCS landing/balked landing checks mandatory.",
    ],
    "threats": [
        "CFIT: highest airport in Europe (5600 ft AMSL), terrain close both sides, MSA very high.",
        "EGPWS alerts final RWY 03: obstacle caution (antenna), sink rate, terrain caution (hill on short final).",
        "RWY excursion: late manoeuvring RWY 03, non-standard PAPI 5° left of centreline, no approach/runway lights.",
        "Mid-air: Class E/G, extensive GA, AFIS no traffic display, heliport/hospital rotary, gliders summer, no transponder gliders near Zernez.",
        "Loss of control: turbulence/windshear, high density altitude, increased turn radius.",
        "Runway incursion: short narrow taxiway, no taxi lighting.",
        "LS(R)-11 / LS(R)-11A military areas — can block ALL arrivals if crossing clearance unavailable.",
    ],
    "overview": (
        "Engadin Airport, 5 km from St Moritz at 5600 ft AMSL — highest in Europe. "
        "AFIS only. Tourist Alpine region with demanding performance requirements."
    ),
    "operational_general": [
        "VFR Class E: 8 km vis, 1000 ft vertical and 1500 m horizontal from cloud.",
        "PDCS used for landing AND balked landing — settings per arrival section.",
        "Non-IRS aircraft: Phenom 300, Citation XLS, Citation Latitude.",
        "IRS aircraft: Challenger 350, Falcon 2000EX, Global 5000/6000.",
        "Confirm LS(R)-11 / LS(R)-11A status with Samedan Info before cancel IFR.",
        "IFR holds nearby: PELAD, GUGSA, RONAG.",
        "Expect Zurich ATC routing to LSZS overhead descending FL160.",
    ],
    "weather": [
        "VFR RWY 03 via MALOJ: 8 km vis; BKN/OVC 10,400 ft AAL or FEW/SCT 2200 ft AAL.",
        "VFR RWY 21 via ZERNZ: same cloud rules.",
        "IFR visual + RNP guidance RWY 03: 5000 m vis, 5800 ft AAL, DA per Jeppesen + 50 ft.",
        "RNP RWY 21: 5000 m vis, DA per Jeppesen + 50 ft; 15° offset, high ceiling for stable approach.",
        "CAT C may use CDFA to IFR minima on chart 12-1.",
        "Dep VFR RWY 03/21: same cloud rules as arrivals.",
        "Dep IFR SID RONAG 1E RWY 03: 2000 m vis (IRS: no ceiling; non-IRS: 2000 ft AAL).",
        "Dep IFR SID RONAG 1V: 5000 m vis, 4400 ft AAL.",
        "Dep IFR SID PELAD RWY 21: 2000 m vis (IRS: no ceiling; non-IRS: 2000 ft AAL).",
        "Dep IFR SID PELAD 1V: 5000 m vis, 5100 ft AAL.",
    ],
    "approaches": [
        {
            "name": "9.2.1 VFR approach RWY 03 via MALOJ (preferred)",
            "expanded": True,
            "minima": "DAY ONLY. 8 km vis. BKN/OVC 10,400 ft AAL or FEW/SCT 2200 ft AAL. Pilot assessment: approach, RWY and missed approach clear of cloud.",
            "performance": (
                "PDCS Arrival LSZS RWY 03 + Departure 03DP4 for balked landing. "
                "Max landing mass = lower of landing perf (FLDTA option) and balked landing perf (DRY RWY in options regardless of actual state)."
            ),
            "procedure": [
                "IFR to overhead FL160; check LS(R)-11/11A — coordinate MIL crossing if active.",
                "Overhead: identify valley/airport; confirm whole valley MALOJ–ZERNZ clear; cancel IFR if VMC for approach and missed approach.",
                "Descend 12,000 ft AMSL, straight-in via MALOJ for RWY 03.",
                "Downwind: extend until abeam MALOJ; may lose visual contact with airport.",
                "Final: left descending turn (min 1000 fpm recommended).",
                "Point W at 2 NM final — FIZ edge; hill on centreline — pass LEFT of hill for offset final.",
                "Stable approach criteria by 300 ft AAL.",
                "Missed/balked: visual manoeuvring; initial PDCS OEI route, then visual to ZERNZ, out-climb valley to 12,000 ft.",
            ],
        },
        {
            "name": "9.2.2 VFR approach RWY 21 via ZERNZ",
            "procedure": [
                "Same IFR overhead and LS(R) checks as RWY 03.",
                "Descend 12,000 ft, straight-in via ZERNZ for RWY 21.",
                "Downwind abeam ZERNZ; left turn final 1000–1500 fpm.",
                "Point E at 2 NM final.",
                "Missed/balked: PDCS OEI then visual to MALOJ, out-climb to 12,000 ft.",
            ],
        },
        {
            "name": "9.3 IFR visual with RNP guidance RWY 03",
            "minima": "5000 m vis, 5800 ft AAL ceiling, DA per Jeppesen + 50 ft.",
            "procedure": ["Charts 19-10. PDCS Arrival 03 / Departure 03DP5."],
        },
        {
            "name": "9.3 RNP RWY 21",
            "minima": "5000 m vis, DA per Jeppesen + 50 ft. High ceiling requirement for 15° offset stable approach.",
            "procedure": ["Charts 12-1 / 12-1A. CAT C authorised CDFA to charted minima."],
        },
    ],
    "departure": [
        "VFR RWY 03: PDCS 03DP4; same cloud clearance as arrival.",
        "VFR RWY 21: 21DP2.",
        "IFR RWY 03 SID RONAG 1E/1V — see weather table.",
        "IFR RWY 21 SID PELAD 1W/1V — see weather table.",
        "Cold temperature correction tables apply to IFR procedures — see appendix.",
        "RAIM prediction checks required for non-SBAS IFR — see appendix.",
    ],
    "ground": [
        "AFIS only — no traffic sequencing.",
        "Short narrow taxi to runway.",
    ],
    "charts": [
        "19-1 / 19-1A / 19-11 — VFR approaches.",
        "19-10 — IFR visual RNP RWY 03.",
        "12-1 / 12-1A — RNP RWY 21.",
        "10-3A/C — IFR SIDs.",
    ],
}
