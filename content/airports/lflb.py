"""OM-C 14-CAT-C-LFLB — Chambéry / Aix-les-Bains."""

DETAIL = {
    "category": "Cat C",
    "headline": "Alpine N-S valley · RWY 18 vs VPT 36 · RNP Z balked landing critical · French when AFIS closed",
    "pdf_section": "OM-C 14-CAT-C-LFLB",
    "qualification": [
        "PIC: LFLB qualification for RWY 18 VMC departure to join RWY 36 SID (Training Dept risk assessment).",
        "PF shall hold current AHQ.",
        "Self-briefing per OM-C schedule.",
    ],
    "limitations": [
        "Mountain airport — terrain 5200 ft within 4 NM, 6200 ft 7 NM east.",
        "VPT RWY 36: DAY ONLY, 5 km visibility (NTA limitation).",
        "RNP Z RWY 18: BALKED LANDING PERFORMANCE LIMITING — confirm planning and before approach.",
        "RNP Y RWY 18 (AR): PROHIBITED (no NTA RNP AR approval).",
        "Night circling to RWY 36 PROHIBITED.",
        "When ATC closed: one crew member must speak French (AFIS English unavailable, Class G). French speaker should be PM.",
        "PAPI RWY 18 at 4.46° (not 4.5 on Jepp 10-9) — check AFM supplement; not a 'steep approach' but apply 4.46° limitations.",
        "PAPI RWY 36 at 4.0° — prohibited beyond 5 NM.",
    ],
    "threats": [
        "CFIT: mountainous terrain, low-speed/low-altitude manoeuvring on balked landing/go-around.",
        "Confusion: some approaches/missed approaches not flyable by all fleets — know contingencies.",
        "Collision: busy GA/commercial/helicopter traffic; RWY 18 arrivals vs RWY 36/18 departures crossing paths.",
        "Turbulence/windshear: N/NW winds — shear on LOC 18 final; downdrafts RWY 36 short final.",
        "S/SW winds — rotors around CH locator.",
        "W wind or CB at 'La Dent du Chat' — gusts 20–50 kt, crosswind.",
        "RNP Z RWY 18 balked landing terrain-critical in climbout.",
    ],
    "overview": (
        "Chambéry in an N-S Alpine valley. High terrain very close on both sides. "
        "Straight-in approaches only to RWY 18; RWY 36 requires VPT after instrument approach to RWY 18."
    ),
    "operational_general": [
        "Strict compliance with published max IAS, min bank angles, min climb gradient.",
        "NetJets tailored charts (CO tab): 10-7 (RWY 18 VMC dep to join RWY 36 SIDs), 10-7A (special RWY 36), 10-7B (engine failure RWY 18 RNAV SIDs).",
        "Preferred approach: ILS/LOC Z (traffic flow and Geneva airspace). Delays if requesting other approaches — extra fuel.",
        "ILS/LOC Z/Y and RNP Z missed approaches require RNAV1 — procedure retrievable from FMS.",
    ],
    "weather": [
        "RWY 18 arrivals: ILS/LOC Z night approved; RNP Z night approved (balked landing limiting); LPV available.",
        "RWY 18 alternate arrival (contingency): vis 8 km, ceiling 6000 ft.",
        "RWY 36 VPT from ILS/LOC or RNP Z 18: DAY ONLY, vis 5 km.",
        "RWY 18 VMC dep to join RWY 36 SIDs: vis 5 km, ceiling 3000 ft — DAY ONLY for VMC departure.",
        "RWY 18 IMC/night RNAV SIDs: per Jeppesen (lowest RVR 400 m).",
        "RWY 36 all SIDs: night approved, per Jeppesen.",
        "Alternate dep RWY 18/36 (LOC/DME INOP, NDB INOP, Class G): vis 8 km, ceiling 6000 ft.",
    ],
    "approaches": [
        {
            "name": "9.2 ILS/LOC (Z/Y) approach RWY 18",
            "expanded": True,
            "minima": (
                "Derived from Jeppesen 11-2A/B/C tables using IAS and missed approach climb gradient "
                "(to 5000 ft with 20° turn degradation). Check PDCS and table in OM-C section 9.2."
            ),
            "procedure": ["As per Jeppesen. Preferred approach when traffic/airspace permit."],
            "caution": "Glideslope/PAPI 4.46° — configure and energy management accordingly.",
        },
        {
            "name": "9.3 RNP Z RWY 18",
            "warning": (
                "BALKED LANDING PERFORMANCE LIMITING. Do not plan or fly unless balked landing assured. "
                "Terrain proximity in climbout critical."
            ),
            "procedure": [
                "Confirm balked landing in pre-flight planning AND before approach.",
                "Night approved but performance check mandatory.",
            ],
        },
        {
            "name": "9.4 VPT RWY 36",
            "minima": "DAY ONLY. Visibility 5 km. From ILS/LOC (Z/Y) RWY 18 or RNP Z RWY 18.",
            "procedure": [
                "Visual prescribed tracks procedure — chart 19-10.",
                "Night circling to RWY 36 prohibited.",
            ],
        },
        {
            "name": "Contingency arrivals RWY 18",
            "procedure": [
                "CY LOC & GS INOP, NDB CH INOP, ATC not avail — see section 9.4 alternate arrival procedures.",
                "Vis 8 km, ceiling 6000 ft.",
            ],
        },
    ],
    "departure": [
        "RWY 18 VMC departure to join RWY 36 conventional SIDs: Qual A PIC, vis 5 km, ceiling 3000 ft, chart 10-7, 18DP5.",
        "RWY 18 IMC/night RNAV SIDs: charts 10-3 series, 10-7B engine failure procedure.",
        "RWY 36 SIDs: night approved, 36DP2, 10-7A contingency.",
        "When ATC closed and Class G: French-speaking crew member required; alternate procedures in brief.",
        "Contingency departures depend on aircraft position — brief all options.",
    ],
    "ground": ["When ATC closed, French language requirement for AFIS coordination."],
    "charts": [
        "10-7 / 10-7A / 10-7B — NetJets tailored (CO tab).",
        "11-2A/B/C — ILS/LOC minima tables.",
        "12-1 — RNP Z RWY 18.",
        "19-10 — VPT RWY 36.",
    ],
}
