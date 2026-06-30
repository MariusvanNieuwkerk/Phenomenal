"""OM-B Ch.2 normal procedures — preflight through landing (skimmed)."""

import streamlit as st

from content.render_helpers import source_footer
from study.sop_helpers import sop_checklist, sop_crew_table, sop_event_table, sop_flow, sop_md
from study.sop_styles import sop_note
from ui.theme import render_section_label


def render_general():
    render_section_label("0 · General operating (2.1)")
    with st.expander("**Automation — AP & FD callouts**", expanded=False):
        sop_crew_table([
            ("AP ON", "**'AUTOPILOT ON'**", "Select AP ON → **'AP GREEN'**"),
            ("AP OFF", "**'AUTOPILOT OFF'**", "Verify AP OFF"),
            ("FD mode change (AP ON)", "**'[XX] GREEN/WHITE'**", "Verify mode"),
            ("FD mode select (AP OFF)", "**'SELECT [XX]'**", "**'[XX] GREEN'**"),
            ("Set FD value", "**'SET [XXXX] FEET PER MIN'** / **'SET HEADING [XXX]'** / **'SET SPEED [XXX]'**", "Calls new value"),
            ("Alt / FL (AP ON)", "**'FL [XXX] SET'**", "**'CHECKED'**"),
            ("Alt / FL (AP OFF)", "—", "**'FL [XXX] SET'** → PF **'CHECKED'**"),
            ("MAA", "—", "**'[XXX] SET'** → PF **'CHECKED'**"),
            ("Direct To (AP ON)", "**'DIRECT TO [XXX]'**", "**'CONFIRMED'** → PF activates"),
            ("Direct To (AP OFF)", "—", "**'DIRECT TO [XXX]'** → PF **'CONFIRMED'**"),
            ("Speedbrake", "**'SPEEDBRAKE OPEN'** / **'CLOSED'**", "Verify MFD"),
        ])
        sop_note("info", "After nav/altitude changes PM ensures correct FD mode by exception (e.g. HDG after ATC deviation).")
        source_footer("om_b", "2.1.1 Automation")

    with st.expander("**CAS management**", expanded=False):
        sop_md("""
**Unexpected CAS**
1. Announce level + exact message — e.g. **'Warning ENG 1 FIRE'**
2. Other pilot: **'… confirmed'**
3. PM cancels warning where applicable
4. PF: memory items or checklist when workload allows

**Expected CAS** (start, test, normal switch): silent acknowledge.

**Checklists:** **'CLEAR'** only if **no CAS** displayed; otherwise summarise verbally.
""")
        source_footer("om_b", "2.1.2 CAS Management")


def render_preflight():
    render_section_label("1 · Pre-flight (2.2)")
    with st.expander("**Task allocation & planning**", expanded=True):
        sop_md("""
**First flight of day (FFOD)**
| Role | Tasks |
|------|-------|
| PF + PM | Check-in, documents, schedule, weather, special requirements, initial briefing |
| PF | Cockpit emergency equipment, cockpit prep & power-up, database validity |
| PM | Exterior inspection, cabin preparation |
| PIC | Aircraft docs, tech/appearance logs |

**Before every flight**
| Role | Tasks |
|------|-------|
| Both | Weather, NOTAMs, performance, fuel, limitations, primary EFB |
| PF | OFP/flight data, fuel & O₂ check, load sheet, AFL, **departure briefing**, FMS load |
| PM | Exterior / turnaround inspection, refuel monitor, catering, cabin, pax briefing |
| Commander | Sign documents, security check (Waypoint App) |

**Duplicate exterior inspection** — always by the pilot who did **not** do the main walk-around.
""")
        source_footer("om_b", "2.2.1 Task Allocation")

    with st.expander("**Exterior · cabin · refuel**", expanded=False):
        sop_md("""
**Exterior (AFM/POH checklist)**
- Show other pilot **3 ADS covers + 3 gear pins** before stowing
- **Duplicate check:** covers/pins out, doors secure, engine covers off, fuel caps, torque link, chocks, area clear

**Refuel**
- Over-wing refuel: **no pax on board**
- Pressure refuel: pax may remain per OM-A; SIGNS/OUTLET OFF/ON, main door OPEN

**Cabin prep (PM)** — emergency equipment, life jackets, FAK/AED, briefing cards, galley/toilet, cleanliness, iPads charged
""")
        source_footer("om_b", "2.2.2–2.2.4 Refuel · Cabin · Exterior")


def render_predeparture():
    render_section_label("2 · Pre-departure (2.3)")
    with st.expander("**Cockpit preparation flow**", expanded=False):
        sop_flow(
            "Cockpit preparation (before electrical power)",
            "Before applying power — configure for safe power-up",
            pf=[
                "Emergency equipment check (barrier, goggles, flashlight, axe, PBE, extinguisher, life jackets, +emer lights FFOD)",
                "Circuit breakers IN (except MEL tie-wraps)",
                "Initial switch positions: BATT OFF, ELEC EMER out, BUS/GEN AUTO, BLEED/XBLEED AUTO, engines OFF, flaps match indication, park brake SET, etc.",
            ],
        )
        sop_note("info", "Match flap lever to observed position if not 0 — keep personnel clear when applying power.")
        source_footer("om_b", "2.3.4 Cockpit Preparation Flow")

    with st.expander("**Power-up flow & checklist**", expanded=False):
        sop_flow(
            "Power-up",
            "After cockpit prep complete — expedite if on batteries only",
            pf=["BATT 1 & 2 ON — verify ≥ **24 V** (replace if <19 V; GPU if <24 V)"],
            pm=[
                "Wait for BIT complete — **do not move aircraft 90 s** (AHRS alignment)",
                "GPU AS REQ — min **27 V** for battery charging",
                "+O₂ mask flow/mic test, O₂ pressure dispatch check",
                "+Test panel: FIRE, SMK DET, ANN, +trims, +MFD databases, transponder 2000 STBY",
            ],
        )
        sop_checklist("Power-up checklist", [
            "COCKPIT PREPARATION FLOW — COMPLETED",
            "BATT 1 & 2 — ON",
            "GPU — AS REQUIRED",
            "CVDR — TESTED",
            "O₂ SYSTEM — +TESTED / ___PSI",
            "+TEST PANEL — TESTED",
            "+TRIMS — TESTED & CENTRED",
        ], "Before flight guidance programming")
        sop_note("warn", "Do not tow/move during AHRS init (~60 s). GPU <27 V → BATT DISCHARGE CAS; may turn batteries OFF until start.")
        source_footer("om_b", "2.3.4.1 Power-Up")

    with st.expander("**Flight guidance & departure briefing**", expanded=False):
        sop_flow(
            "FMS programming",
            "GPU available or sufficient battery — else delay until after 1st engine start",
            pf=[
                "NetJets crew profile, flight plan insert (verify constraints ACFOG), OAT, LFE, weight planning",
                "AFCS panel: PF side, TO guidance, pitch trim green band, AAD when clearance received",
                "PFD set for departure; radar STBY (or after start if battery start)",
            ],
            pm=[
                "NAV/COM, altimeters ×3, V1/VR/V2/VFS bugs ON, transponder c/s & 2000 STBY",
                "Baro transition alert, TCAS test & mode, PFD (consider green needles backup)",
                "Press TO/GA",
            ],
        )
        sop_md("""
**Departure briefing (minimum)**
- SID / departure, **engine-failure plan**, threats
- AP/FD mode strategy, conventional nav backup
- Low level-off technique if applicable (flap overspeed, ROC)
- Noise abatement / level-off below 3000 ft if applicable
""")
        source_footer("om_b", "2.3.5–2.3.6 FMS · Departure Briefing")

    with st.expander("**Suggested avionics display setup**", expanded=False):
        sop_md("""
| Phase | PF PFD | MFD | PM PFD |
|-------|--------|-----|--------|
| Start / shutdown | SID | Elec status | Normal |
| Taxi out | SID | Safe taxi | Taxi chart |
| Departure | Chart | Flight plan map | Chart |
| Cruise | — | Flight plan map | — |
| Descent / approach | Arrival chart | Flight plan map | Arrival chart |
| Taxi in | — | Safe taxi | Taxi chart |

MFD changes must be briefed. PF controls MFD in flight.
""")
        source_footer("om_b", "2.3.7 Avionics Setup")


def render_start_taxi_lineup():
    render_section_label("3 · Start · taxi · line-up (2.4–2.6)")
    with st.expander("**Before start — flow & checklist**", expanded=False):
        sop_flow(
            "Before start",
            "Both in cockpit, start clearance received",
            pf=[
                "PARK BRAKE ON, START/RUN, harness secure, phones OFF, SIGNS BELTS/ON",
                "ADS PROBES ON if OAT ≤10°C and icing",
            ],
            pm=[
                "MFD STATUS + ELEC split, harness, phones OFF",
                "Fuel matches required, doors closed",
            ],
        )
        sop_checklist("Before start checklist", [
            "FLIGHT LOG / RELEASE — COMPLETE",
            "PORTABLE EFB — PREPARED & SECURE",
            "+PINS AND COVERS — COUNTED & STOWED",
            "TORQUE LINK — A/R (CONNECTED or REMOVED FOR PUSHBACK)",
            "SIGNS — BELTS/ON",
            "FUEL — __ LBS / BALANCED",
            "PARKING BRAKE — ON",
            "ADS PROBES — A/R",
            "CAS — A/R",
        ])
        source_footer("om_b", "2.4.1.2 Before Start")

    with st.expander("**Engine start — callouts**", expanded=False):
        sop_crew_table([
            ("Cleared to start", "**'CLEAR LEFT'**", "**'CLEAR RIGHT'**"),
            ("Engine stabilised", "—", "**'START COMPLETE'**"),
        ], "**Start sequence:** LHS starts; monitor ITT/N1/N2 silently.")
        sop_md("""
**Technical notes**
- GPU start: **No. 2 first**, disconnect GPU before other engine
- FADEC auto-abort: no light-off 10 s, hot/hung start — manual abort if false start
- Tailwind **>10 kt** can extend start / raise ITT — prefer headwind/crosswind
- 2nd engine: **72% N2 jet blast** — visual check behind aircraft
""")
        source_footer("om_b", "2.4.1.3 Start Procedure")

    with st.expander("**After start — flow & checklist**", expanded=False):
        sop_flow(
            "After start",
            "Second engine started — PF may 'brief the glass'",
            pf=[
                "GPU disconnect verify",
                "ELEC EMER test (see explanation below)",
                "Stall test + test panel ICE PROT",
                "Flight controls checked",
                "CAS A/R, cabin secure",
            ],
            pm=[
                "A/C A/R",
                "Flap for T/O",
                "Heating & ice protection +TEST, then set for SAT (see explanation)",
                "Screens for taxi (only after ELEC EMER test complete)",
                "Transponder code & AUTO",
            ],
        )
        sop_checklist("After start checklist", [
            "GPU — DISCONNECTED (if used)",
            "ELEC EMER — TESTED",
            "STALL PROTECTION — TESTED",
            "FLIGHT CONTROLS — CHECKED",
            "ICE PROTECTION — +TESTED & A/R",
            "FLAPS — A/R",
            "PITCH TRIM — _._",
            "ALTIMETERS — QNH __ SET & X-CHECKED",
            "FLIGHT GUIDANCE — SET & CHECKED",
            "TRANSPONDER — CODE SET & AUTO",
            "CAS — A/R",
            "CABIN — SECURE",
        ])

        with st.expander("**Guide: ELEC EMER test (LHS / PF)**", expanded=False):
            sop_md("""
**What is it?**  
A brief test that the **emergency electrical configuration** works. You simulate an electrical emergency and verify the buses reconfigure correctly.

**Step 1 — press ELEC EMER IN**  
Check on the **ELEC synoptic** (MFD):
| Check | Expected |
|-------|----------|
| DC BUS 1 | Disconnected from EMER BUS |
| DC BUS 2 | Disconnected from CENTRAL BUS |
| HOT BUS 2 | Connected to EMER BUS |
| BATT 1 & 2 | Minimum **23.5 V** (allow voltage to stabilise) |

**Step 2 — press ELEC EMER OUT (normal)**  
Verify:
| Check | Expected |
|-------|----------|
| DC BUS 1 | Connected to EMER BUS |
| DC BUS 2 | Connected to CENTRAL BUS |
| HOT BUS 2 | Disconnected from EMER BUS |

**Why now?**  
ELEC EMER test must be **complete** before the PM changes the MFD display (e.g. for taxi) so you can see the bus configuration clearly.

**Do not confuse with:** leaving ELEC EMER **IN** to save battery before start — that is only during power-up without GPU, not this test.
""")
            source_footer("om_b", "2.4.1.4 After Start · ELEC EMER")

        with st.expander("**Guide: anti-ice — test & when to select ON**", expanded=False):
            sop_md("""
There are **two steps**: first **test**, then **set for today's conditions**.

---

### Part 1 — TEST (required FFOD / +TEST)

**PF (LHS) — test panel**
1. Move yoke aft and hold
2. **STALL PROT** test → aural **'STALL, STALL'** (4×), stick pusher on 3rd callout
3. **ICE PROT** test → CAS **ICE CONDITION** (may linger briefly, must clear)
   - Temporary **ICE DET FAIL** is acceptable — if it persists, consider ice detector failed

**PM (RHS) — heating & ice protection panel**
1. **ADS PROBES** → **AUTO** (was **ON** before start if OAT ≤10°C + icing — return to AUTO)
2. For the test, select **all ON**: **WSHLD 1 & 2**, **ENG 1 & 2**, **WINGSTAB** → **ON**
3. Check EICAS:
   - No **WSHLD 1(2) HTR FAIL**
   - After ~10 s: **A-I 1** and **A-I 2** (engine anti-ice active)
   - **A-I WINGSTB ARM** may appear briefly
4. Select all **OFF** again — test complete

---

### Part 2 — OPERATIONAL setup (after test, based on ground SAT)

| Outside temp (SAT) | WSHLD 1 & 2 | ENG 1 & 2 | WINGSTAB | ADS PROBES |
|--------------------|-------------|-----------|----------|------------|
| **5°C to 10°C** | OFF | **ON** | OFF | AUTO |
| **Below 5°C** | **ON** | **ON** | **ON** | AUTO |

**What each switch does**
| Switch | Function |
|--------|----------|
| **ENG 1 & 2** | Engine anti-ice — hot bleed air to engine inlet |
| **WINGSTAB** | Wing/stab anti-ice — prevents ice on wing and stabiliser |
| **WSHLD 1 & 2** | Windshield heat — clears/de-ices windshield |
| **ADS PROBES** | Pitot/static/probe heat — **AUTO** is normal; **ON** before start when cold + icing |

---

### When to select more ON — **icing conditions**

**Icing conditions** (OM-B): SAT ≤ **10°C** + visible moisture (fog, rain, snow, etc.),  
or SAT ≤ **10°C** on snow/ice-contaminated ramp/taxiway/runway.

Then typically:
- **Before start:** ADS PROBES **ON** (before start flow)
- **Taxi / departure:** Normal Checklist **Icing Conditions** — anti-ice per checklist
- **In flight in icing:** usually **ENG + WINGSTAB ON** (not SAT table alone)

**Rule of thumb:** SAT table = **baseline after start on the ground**. In actual icing conditions → follow **icing checklist** and select WINGSTAB (and WSHLD if needed) **ON**, even if SAT is 5–10°C.

**Note:** **A-I WINGSTB INHB** CAS may appear if you test outside the icing envelope — normal during ground test.
""")
            sop_note(
                "info",
                "If unsure about ground ice/contamination: see <strong>Cold Weather</strong> module "
                "and Normal Checklist <strong>Icing Conditions</strong> before line-up.",
            )
            source_footer("om_b", "2.4.1.4 After Start · Ice Protection · 2.24 Icing")

        source_footer("om_b", "2.4.1.4 After Start")

    with st.expander("**Taxi & line-up**", expanded=False):
        sop_crew_table([
            ("Cleared to taxi", "LDG/TAXI → TAXI", "**'CLEAR LEFT'** / **'CLEAR RIGHT'**"),
            ("Park brake release", "**'PARKING BRAKE OFF'**", "—"),
            ("Brake check", "**'CHECK YOUR BRAKES'**", "**'BRAKES CHECKED'**"),
        ])
        sop_flow(
            "Line-up",
            "Line-up clearance — both confirm runway clear",
            pf=["Runway for departure verified"],
            pm=[
                "Departure review complete (active lateral FD mode HDG/FMS)",
                "T/O CONFIG → **'TAKE-OFF OK'**",
                "Engine indications check, strobe ON, radar A/R, CAS A/R, pax advise",
                "LDG/TAXI → **LDG** when T/O clearance received",
            ],
        )
        sop_checklist("Line-up checklist", [
            "DEPARTURE REVIEW — COMPLETE",
            "T/O CONFIG — OK",
            "ENGINE INDICATIONS — CHECKED",
            "STROBE — ON",
            "CAS — A/R",
        ])
        sop_note("warn", "Avoid >20% N1 differential when lining up — can trigger TO RSV at TO/GA. Never taxi/brake on **POOR** surfaces.")
        source_footer("om_b", "2.5–2.6 Taxi · Line-Up")


def render_takeoff_climb_cruise():
    render_section_label("4 · Takeoff · climb · cruise (2.7–2.9)")
    with st.expander("**Normal takeoff — OM-B callouts (2.7.1)**", expanded=False):
        sop_crew_table([
            ("T/O clearance, checklists done", "Thrust TO/GA", "N1 = target → **'THRUST SET'**"),
            ("Airspeeds alive", "—", "Verify IAS"),
            ("60 kt", "**'60'**", "**'CHECKED'**"),
            ("V1", "**'V1'**", "—"),
            ("VR", "**'ROTATE'**", "—"),
            ("Airborne", "Verify + rate → **'GEAR UP'**", "**'POSITIVE RATE'** → gear UP, FLC **150**"),
            ("", "Verify FLC/150", "**'FLC GREEN/PINK, SPEED 150'** → **'GEAR UP'**"),
            ("1000 ft AAL", "**'1000 FEET'** → thrust ≤CLB → **'FLAP ZERO'**", "**'XXX'** → **'FLAP ZERO'** → **'YD GREEN'**"),
            ("3000 ft / NADP", "Speed **225 KIAS**", "Verify speed set"),
            ("Transition altitude", "**'SET STANDARD'**", "**'STANDARD SET AND BLUE'**"),
        ])
        sop_md("""
**Technique**
- Rotate ~**15°** initially; max **20°** after gear up (V2+10 to 150 kt)
- Flap 2 T/O: pause at flap 1 before flap 0
- Below 1000 ft: only essential lever/switch moves
- Min AP engage: **600 ft AAL** (1000 ft OEI) · Avoid MAX detent (TO RSV, ECS off risk)
- Gear/flap overspeed: stay FLC, bug ≤**170 kt** (160 flap 2) until flap 0 loop complete
""")
        source_footer("om_b", "2.7.1 Normal Take-off")

    with st.expander("**RTO & EFATO — callouts (abnormal)**", expanded=False):
        sop_crew_table([
            ("Abort decision", "**'STOP STOP'**", "Confirm spoilers · ATC *'[Callsign] Stopping'*"),
        ], "**RTO criteria:** <60 kt any failure · 60 kt–V1 fire, thrust loss, directional control, red CAS.")
        sop_event_table([
            ("Engine failure at V1", "Continue · **'ROTATE'** (Flap1 10.5° / Flap2 8°)"),
            ("Positive rate", "PM **'POSITIVE RATE'** · PF **'GEAR UP'** · FLC V2, low bank"),
            ("Climb", "**V2** (max V2+10)"),
            ("1000 ft", "Consider AP (YD OFF)"),
            ("Acceleration", "V_FS → CON, disengage low bank, V2+10, Flap 0"),
        ], "**EFATO**")
        source_footer("om_b", "Flight Profiles · RTO · EFATO")

    with st.expander("**After take-off checklist & climb**", expanded=False):
        sop_checklist("After take-off / go-around checklist", [
            "LANDING GEAR — UP",
            "FLAP — 0",
            "YAW DAMPER — GREEN",
            "ALTIMETERS — STD SET & BLUE",
        ], "First level-off or suitable point during initial departure")
        sop_flow(
            "Climb flow",
            "Passing FL100 or transition altitude, whichever higher",
            pm=[
                "LDG/TAXI OFF",
                "Pressurisation checked (cabin alt, rate, delta-P green, no AMS CAS)",
                "WSHLD heat ON, COM 2 121.5, RVSM check if applicable",
            ],
        )
        sop_checklist("Climb checklist", [
            "PRESSURISATION — CHECKED",
            "WINDSHIELD HEAT — ON",
        ])
        sop_md("**Climb profile:** **225 KIAS** to ~29,600 ft → **M0.60** · Max thrust CON/CLB.")
        source_footer("om_b", "2.7.1.5 · 2.8 Climb")

    with st.expander("**Crosswind · wet · noise abatement**", expanded=False):
        sop_md("""
| Topic | Key limit / note |
|-------|------------------|
| Crosswind T/O | Max demonstrated **25 kt** · Static T/O max **18 kt** |
| Wet runway | No special technique |
| NADP 1/2 | Standard profile meets ICAO Doc 8168 |
| Level-off ≤3000 ft | After 1000 ft: ~65% N1, ~10° pitch; min thrust reduction **400 ft AAL** |
""")
        source_footer("om_b", "2.7.2–2.7.5")

    with st.expander("**Cruise flow (2.9.1)**", expanded=False):
        sop_flow(
            "Cruise flow",
            "Top of climb — repeat periodically in cruise",
            pf=["Thrust set — reduce to MAX CRUISE or below within **5 min** of CON/CLB"],
            pm=[
                "Primary altimeters within **200 ft** (RVSM)",
                "Pressurisation check",
                "Fuel check & FOB SYNC on GTC if needed",
                "TCAS mode for best SA",
            ],
        )
        source_footer("om_b", "2.9 Cruise")


def render_arrival_descent():
    render_section_label("5 · Arrival · descent · approach prep (2.10–2.12)")
    with st.expander("**Arrival preparation & descent**", expanded=False):
        sop_md("""
**Arrival briefing (before descent)**
- Approach type, minima, MAP, **landing flap** (Flap 3 preferred; FULL for steep/anti-ice bleed)
- FMS approach loaded early (GPS/SBAS availability affects selectable procedures)
- Config gates (**latest** points), stabilised plan, threats
- V_AP wind correction: +½ headwind + gusts, max V_REF+20
""")
        sop_flow(
            "Descent flow",
            "Before leaving cruise altitude",
            pf=[
                "SIGNS BELTS/ON",
                "LFE set, landing speed bugs ON (V_AP, V_REF, V_AC, V_FS)",
                "Flight guidance: PROC, NAVAIDs, BARO MIN, baro transition alert",
                "Arrival briefing complete",
            ],
            pm=["PFD set A/R"],
        )
        sop_checklist("Descent checklist", [
            "LFE — SET",
            "FLIGHT GUIDANCE — SET & CHECKED",
            "ARRIVAL BRIEFING — COMPLETE",
            "SIGNS / OUTLET — BELTS/ON",
        ])
        sop_md("**Descent profile:** M0.75 above 35,600 ft → **250 kt** to 1500 ft · Holding normal speed **170 KIAS**.")
        sop_note("info", "Holding icing: min **150 kt** WHSAIS ON / **165 kt** if inhibited.")
        source_footer("om_b", "2.10–2.11 Arrival · Descent")

    with st.expander("**Approach flow & technical gates (2.12)**", expanded=False):
        sop_flow(
            "Approach flow",
            "Passing FL100 or cleared to altitude in descent — whichever first",
            pf=["Altimeters SET QNH when cleared"],
            pm=[
                "WSHLD 1&2 A/R (OFF on final unless needed)",
                "LDG/TAXI TAXI",
                "NAVAIDS set & checked (green ident on PFD)",
                "CABIN secure",
                "Altimeters cross-check",
            ],
        )
        sop_checklist("Approach checklist", [
            "WINDSHIELD HEAT — A/R",
            "CABIN — SECURE",
            "ALTIMETERS — QNH ___ SET & BLUE",
        ])
        sop_md("""
**Manoeuvring speeds (min before final)**
| Flaps | Min IAS |
|-------|---------|
| 0 | 150 kt |
| 1 | 140 kt |
| 2/3/Full | V_REF + 10 |

**Flap/gear:** 10 kt buffer below limits · bypassing detent → pause at intermediate.

**V_AP / V_REF:** Bug to V_REF+10 (+ wind correction) · at MINIMUMS/Continue → bug to **V_REF** · threshold **50 ft @ V_REF**.

**Automation notes**
- Circling after ILS: set up as LOC, AAD to circling altitude
- RNAV: suitable map display · LNAV+V vs LNAV (VS if no +V)
- Approach plate on PM EFB or PFD · NAVAIDs auto-tune — PM verifies by exception
""")
        source_footer("om_b", "2.12 Approach General")


def render_landing_shutdown():
    render_section_label("8 · Landing · taxi-in · shutdown (2.20–2.23)")
    with st.expander("**Before landing & landing callouts**", expanded=False):
        sop_flow(
            "Before landing flow",
            "First configuration change by PF",
            pf=["FUEL XFEED OFF"],
            pm=["Gear DN, landing flap, LDG/TAXI LDG when landing clearance"],
        )
        sop_crew_table([
            ("Before landing (PF)", "AP/YD disconnect ≥195 ft AGL (220 OEI)", "Verify AP/YD off"),
            ("Cleared to land", "—", "LDG/TAXI LDG"),
            ("Before touchdown", "—", "Verify YD OFF"),
            ("After touchdown", "—", "Verify spoilers · **'60'** at 60 kt"),
        ])
        sop_checklist("Before landing checklist", [
            "LANDING GEAR — DOWN",
            "FLAPS — A/R",
            "CAS — A/R",
        ], "Complete before stabilised approach point")
        sop_md("""
**Landing technique**
- Preferred flap **3** (FULL for steep / anti-ice bleed management)
- Crosswind max **28 kt** — de-crab per AFM
- Wet: positive landing, firm nosewheel down, moderate-firm brakes (don't pump)
- Rollout: non-essential actions only below **60 kt**
""")
        source_footer("om_b", "2.20 Landing")

    with st.expander("**After landing · shutdown · securing**", expanded=False):
        sop_flow(
            "After landing",
            "Runway vacated — no unnecessary switches on runway",
            pm=["Flap 0", "Ice protection A/R (OFF if not needed)", "LDG/TAXI TAXI", "Strobe OFF after vacated"],
        )
        sop_checklist("After landing checklist", ["STROBE — OFF", "FLAPS — 0"])
        sop_flow(
            "Shutdown",
            "Final parking, parking brake SET — recommend **2 min** idle before shutdown",
            pf=["Thrust idle, park brake SET"],
            pm=["STATUS on MFD, monitor spool-down & hyd pressure, transponder 2000 STBY"],
        )
        sop_md("""
**Shutdown (LHS):** heating/ice OFF → START/STOP STOP → SIGNS OFF/ON → exterior lights OFF → EMER lights OFF → BATT as required (min **24 V**)

**Securing:** chocks → park brake OFF → O₂ cut-out → gust lock → lights OFF → BATT OFF → emer door pin → torque link disconnected → ADS/pitot covers
""")
        sop_checklist("Shutdown checklist", [
            "PARKING BRAKE — ON",
            "HEATING & ICE PROTECTION — OFF",
            "SIGNS OUTLET — OFF/ON",
            "EXTERIOR LIGHTS — OFF",
            "EMER LIGHTS — OFF",
        ])
        sop_checklist("Securing checklist", [
            "PARKING BRAKE — OFF (chocks in place)",
            "O₂ BOTTLE — CUT-OUT",
            "GUST LOCK PIN — INSTALLED",
            "LIGHTS — OFF",
            "BATT 1 & 2 — OFF",
            "EMERGENCY DOOR PIN — INSTALLED",
            "TORQUE LINK — DISCONNECTED",
        ])
        sop_note("info", "Oil service: **10–20 min** after shutdown only. Batteries removal below **-10°C** if no GPU — coordinate maintenance.")
        source_footer("om_b", "2.21–2.23 After Landing · Shutdown · Securing")
