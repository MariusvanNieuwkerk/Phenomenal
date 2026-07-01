"""OM-C 14-CAT-C-LOWI — Innsbruck."""

DETAIL = {
    "category": "Cat C",
    "headline": "Alpine valley · NetJets chart 11-01 · RWY 26 preferred · Foehn · CTOT",
    "pdf_section": "OM-C 14-CAT-C-LOWI",
    "qualification": [
        "PIC and SIC LOWI qualifications required.",
        "Type-related qualification: no.",
        "Self-briefing: yes — every flight.",
        "Ground training: 12-month revalidation.",
        "Simulator training: 12-month revalidation.",
        "In-flight familiarisation: not applicable.",
    ],
    "revalidation": [
        "Ground training and simulator training every 12 months.",
        "Self-briefing required every flight.",
    ],
    "limitations": [
        "PF/PM assignment at PIC discretion — some manoeuvres (e.g. TELFS emergency) only trained as PF by PICs in simulator.",
        "Jeppesen 11-1 and 11-2 (installed EFB) replaced by NetJets tailored 11-01 (portable EFB only).",
        "11-1 on installed EFB may aid SA; primary reference must be 11-01 on portable EFB.",
        "Tailored charts do not appear on installed EFB — portable EFB essential.",
        "NetJets LOC DME EAST (11-1) and Special LOC DME EAST (11-2) prohibited.",
        "RNP E RWY 26: LPV required; LNAV/VNAV and LNAV prohibited.",
        "Visual approach RWY 26: DAY ONLY.",
        "MOGTI 1X and RTT 3X special performance RNAV departures prohibited.",
        "PF shall hold current AHQ.",
    ],
    "crew_assignment": [
        "Consider simulator training history when assigning PF/PM — TELFS and circling manoeuvres may only have been flown by PIC as PF in sim.",
    ],
    "threats": [
        "Rapidly changing weather, especially winter. Very busy ski weekends — slot restrictions.",
        "Foehn when LIPB QNH ≥ 6 hPa above LOWI: wind 100–180°, 15–25 kt, gusts 30–50 kt.",
        "Foehn windshear/turbulence south of city and over Inn river short of RWY 08 below 5000 ft.",
        "Foehn RWY 08: severe downdrafts south of city on balked landing — route visually north of city first.",
        "Marginal weather arrivals may get CTOT at departure — contact Supervisor +43 5 1703 6610 if incorrectly excluded.",
        "Cold temperature corrections: MRVA by ATC; all other corrections pilot responsibility.",
        "CFIT and performance critical in valley environment.",
    ],
    "overview": (
        "Mountain airport in the Inn valley (East-West), Western Austria. Ski season weekends are very busy. "
        "Expect ATC slot restrictions and tight coordination. "
        "Forecast: +43 5 1703 4643; Tower: +43 5 1703 6612; webcam: www.innsbruck-airport.com"
    ),
    "operational_general": [
        "Preferred landing runway: RWY 26. Preferred takeoff runway: RWY 08.",
        "Actual minima may be higher due to mass, OAT — check specific arrival and Jeppesen/PDCS.",
        "Arrival CTOTs may apply when weather marginal — monitor and comply.",
        "Slot adherence: monitor TWR 15 min before CTOT; advise able to comply or need extension/delay.",
        "Check ATIS early for runway in use vs planned SID.",
        "ATC expects full-length backtrack — no need to request.",
        "Inbound traffic: may be asked if able to depart within 3 min before holding point.",
    ],
    "weather": [
        "RWY 26 NetJets LOC DME EAST: DA 2900 ft (1006 ft) / vis 2800 m (Cat B) or 3700 m (contingency) — NIGHT approved.",
        "RWY 26 RNP E LPV: DA 3300 ft (1406 ft) / vis 1500 m (Cat B) or 2400 m (contingency) — LPV only.",
        "RWY 26 Visual: vis 10 km, ceiling 9100 ft — DAY ONLY.",
        "RWY 08 RNP Visual V: MDA 7100 ft (5193 ft) / vis 5000 m, ceiling 5200 ft — DAY ONLY.",
        "RWY 08 NetJets LOC DME to circling: MDA 3700 ft (1793 ft) / vis 3000 m (Cat B) or 5000 m (Cat C).",
        "RWY 08 departures RTT 2Q/3J SIDs: RVR 150 m — NIGHT approved.",
        "RWY 26 MOGTI 1R: ceiling 1300 ft, vis 1500 m — NIGHT, medium takeoff mass.",
        "RWY 26 increased mass departure: ceiling 3000 ft, vis 8 km — DAY ONLY, highest mass.",
    ],
    "approaches": [
        {
            "name": "9.2.1 RWY 26 — NetJets LOC DME EAST (chart 11-01)",
            "expanded": True,
            "minima": (
                "Night approved. NetJets lower minima than standard LOC DME EAST (11-1 prohibited). "
                "Lowest: DA 2900 ft (1006 ft) / Cat B 2800 m, Cat C 3700 m — requires 6% missed approach climb gradient. "
                "Cloud ceiling at or above minima required."
            ),
            "procedure": [
                "Primary reference: Jeppesen (NetJets) chart 11-01 on portable iPad EFB.",
                "Installed EFB 11-1 may aid SA — identical except missing NetJets lower minima and OEV DME vs altitude refs.",
                "Missed approach identical on both charts — 11-1 may be referenced for missed approach.",
            ],
            "missed": "Balked: chart 11-01A (requires OEV and OEJ serviceable) or 9.4 visual circuit after balked landing.",
        },
        {
            "name": "9.2.2 RWY 26 — RNP E (LPV) chart 12-2",
            "minima": "LPV aircraft only. Lowest DA 3300 ft (1406 ft) / Cat B 1500 m, Cat C 2400 m — requires 7.1% missed approach gradient.",
            "procedure": ["As per Jeppesen 12-2."],
            "missed": "11-01A (OEV/OEJ serviceable) or visual circuit 9.4.",
        },
        {
            "name": "9.3.1 RWY 08 — RNP Visual V (chart 12-1)",
            "warning": "FOEHN: expect RWY 08 in use; severe downdrafts south of city on balked landing.",
            "minima": "DAY ONLY. MDA 7100 ft (5193 ft), vis 5000 m, ceiling 5200 ft. Ceilometer at WI814 — ATC can provide ceiling.",
            "procedure": [
                "Sequence missed approach in FMS for guidance in visual segment after MAP at WI814.",
            ],
            "missed": "Chart 10-3 RWY 08 initial departure, 10-7 engine failure RWY 08, or 9.4 visual circuit.",
        },
        {
            "name": "9.3.2 RWY 08 — NetJets LOC DME EAST to circling",
            "minima": "MDA 3700 ft (1793 ft) / vis 3000 m (Cat B) or 5000 m (Cat C). Charts 11-01 and 19-10.",
            "procedure": ["See OM-C section 9.3.2 for circling guidance and FOEHN cautions."],
        },
        {
            "name": "9.5 Visual approach",
            "minima": "Vis 10 km, ceiling 9100 ft (RWY 26 DAY ONLY per table; RWY 08 see brief).",
            "procedure": ["Refer to OM-C 9.5 and Jeppesen for visual approach procedures."],
        },
    ],
    "departure": [
        "RWY 08 preferred. RTT 2Q/3J: RVR 150 m night approved — charts 10-3L/K, 08DP4/5.",
        "KPT 5J, ADILO 2J, BRENO 2J: charts 10-3F/E, 08DP4.",
        "Visual departure RWY 08: vis 10 km, ceiling 9100 ft — DAY ONLY.",
        "RWY 26 MOGTI 1R: ceiling 1300 ft, vis 1500 m — night, medium mass, 26DP8.",
        "RWY 26 MOGTI 3H/BRENO 3H/RTT 1R/4H: ceiling 2100–2000 ft, vis 5000 m.",
        "RWY 26 increased mass: ceiling 3000 ft, vis 8 km — DAY ONLY, 26DP6, highest mass.",
        "Unable to depart on stated runway: advise ATC at startup with estimate and required SID (ATC prefers KPT5J when need RWY 08 and 26 in use).",
    ],
    "ground": [
        "Pushback vs stand procedures — see OM-C section 11.",
        "Line-up: ATC expects backtrack for full length.",
    ],
    "charts": [
        "11-01 / 11-01A — NetJets LOC DME EAST and balked landing (portable EFB).",
        "12-1 — RNP Visual V RWY 08.",
        "12-2 — RNP E LPV RWY 26.",
        "19-10 — circling RWY 08.",
        "10-3 / 10-7 — departures and engine failure RWY 08.",
    ],
}
