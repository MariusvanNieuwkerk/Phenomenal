import os

import streamlit as st
from PIL import Image

from content.render_helpers import back_to_top, cas_quick_reference, source_footer


def _img(path: str, caption: str):
    if os.path.exists(path):
        st.image(Image.open(path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Missing image: `{path}`")


def render_powerplant():
    st.markdown("## Powerplant (PW535E engines)")
    st.caption("ATA 71 | Source: Phenom 300 POH (Section 6-05, Rev 12)")

    folder = "assets/powerplant"

    with st.expander("**0. Big picture**", expanded=True):
        st.markdown(
            """
**Two PW535E turbofans** on the rear fuselage. Each engine has a **dual-channel FADEC** that schedules fuel
and protects limits — you set **thrust lever** position; FADEC delivers the matching N1 within ratings.

| FADEC input | What it does |
|-------------|--------------|
| **Thrust lever** | Selects rating (IDLE → TO/GA → MAX) |
| **ENG START/STOP** | Start, run, or shutdown sequence |
| **ENG IGNITION** | When igniters fire (AUTO = normal) |
| **Takeoff dataset (MFD)** | OAT + ATR → correct T/O thrust |

**What each engine drives** — follow links for detail:
- Bleed → **Air Management** · **Ice Protection**
- Hydraulic pump → **Hydraulics**
- Generator → **Electrics**

**Where to look**
- Parameters → **MFD engine page**
- Warnings → **both PFDs**
- Procedures → **SOP** (start/T/O) · **Profiles** (EFATO/OEI) · **Memory Items** (fire/abnormal start)

**Study focus:** understand **FADEC start logic** and **MFD indications**; use other sections for step-by-step flows.
"""
        )
        c1, c2 = st.columns(2)
        with c1:
            _img(f"{folder}/pw535e_engine_overview.png", "PW535E engine (external overview)")
        with c2:
            _img(f"{folder}/pw535e_engine_cutaway.png", "PW535E engine (cutaway overview)")

    with st.expander("**1. Controls & MFD indications**", expanded=False):
        st.markdown(
            """
**Thrust levers (per engine)**

| Detent | Rating |
|--------|--------|
| **MAX** | Maximum |
| **TO/GA** | Takeoff / go-around |
| **CON / CLB** | Max continuous / climb |
| **MAX CRZ** | Cruise |
| **IDLE** | Ground & flight idle |

Positions between detents = intermediate thrust. **TO/GA button** on thrust quadrant → **Automatic Flight**.

**ENG START/STOP knob**

| Position | Use |
|----------|-----|
| **RUN** | Normal |
| **START** | Momentary — begins start (TLA at **IDLE**) |
| **STOP** | Shutdown command — TLA must reach **IDLE within 5 s** or FADEC ignores |

**ENG IGNITION switch**

| Position | Use |
|----------|-----|
| **AUTO** | Normal — FADEC controls igniters |
| **ON** | Continuous ignition (per QRH — heavy rain, turbulence, icing) |
| **OFF** | Dry motoring only |

**Fire / fuel shutoff** → **Fire Protection** & **Memory Items** (*E1(2) FIRE*).

**Line-up:** avoid **>20% N1 differential** — can trigger **TO RSV** at TO/GA (*SOP*).

---

**MFD engine page — what to scan**

| Indication | Normal | Watch for |
|------------|--------|-----------|
| **N1** | Green | Red = limit; **FAIL** = uncommanded flameout |
| **N2** | Green | Red = limit; primary cue **during start** |
| **ITT** | Green | Yellow on ground = high start temp; Red = limit |
| **Oil pres / temp** | Green | Yellow = caution; Red = limit |
| **Fuel flow** | — | Asymmetric thrust check |
| **Thrust mode** | CRZ / CLB / CON / TO / GA | **RSV** suffix when ATR active |
| **ATR** | Green = armed, White = enabled | Blank = not selected |
| **Anti-ice N1 bug** | Yellow minimum N1 | Wing/stab A/I ON + gear down, or single engine/bleed |

Red **FIRE** on ITT dial → engine fire memory item.

_Source: POH 6-05-05 (Rev 12)._"""
        )
        c1, c2 = st.columns(2)
        with c1:
            _img(f"{folder}/poh_6-05_engine_control_panel_p473.png", "Engine control panel (POH 6-05-05)")
        with c2:
            _img(f"{folder}/poh_6-05_mfd_engine_indications_p474.png", "MFD engine page layout (POH 6-05-05)")

    with st.expander("**2. Start & shutdown**", expanded=False):
        st.markdown(
            """
**FADEC start sequence (ground)**
1. Starter spins engine → **N2** rises
2. FADEC commands fuel + ignition → **ITT** rises
3. Engine stabilises at idle → starter disengages

**Pilot actions** — callouts and flows → **SOP → Engine start**.
**Abnormal start** → memory item *ENGINE ABNORMAL START* (knob to **STOP**).

**FADEC auto-abort (ground only)**

| Condition | Trigger |
|-----------|---------|
| No light-off | ITT not rising significantly **10 s** after fuel on |
| Hot start | ITT exceeds steady-state limit by half the transient margin |
| Hung start | Idle not reached within **60 s** after fuel commanded |
| High ITT | Ground abort at **720°C** |

Manual abort at any time: knob to **STOP**.

**In-flight start / relight**
- FADEC **disables auto-abort** — pilot decides whether to continue or abort.
- **Auto-relight:** igniters on flameout (knob not on STOP) until **N2 < 40%**.

**Dry motoring** — IGNITION **OFF**, knob **START**; count time against starter limits (*Monitoring* below).

**Normal shutdown** — TLA **IDLE** → knob **STOP**.

**Emergency shutdown** — **FIRE SHUTOFF** pushbutton → **Fire Protection**.
"""
        )
        _img(f"{folder}/poh_6-05_ground_starting_p491.png", "Ground starting logic (POH 6-05-20)")

    with st.expander("**3. Takeoff dataset & ATR**", expanded=False):
        st.markdown(
            """
**Before every takeoff — enter dataset on MFD**
1. **SYSTEM** → **ENG SET**
2. Enter **OAT**, select **ATR ON** or **ATR OFF**
3. **ACCEPT**

Missing data → **ENG NO TO DATA** (advisory).

**ATR (Automatic Thrust Reserve)**
- Extra thrust if an engine fails **at or after V1** during T/O or go-around.
- When active: **ATR** indication changes, thrust mode shows **RSV**; ECS bleed from that engine may close.

**Thrust lever detents → FADEC modes**

| Detent | Mode | Time limit (typical) |
|--------|------|----------------------|
| **TO/GA** | TO or GA | 5 min (T/O) |
| **CON / CLB** | MCT / climb | Continuous |
| **MAX CRZ** | Cruise | Continuous |

Anti-ice ON reduces available thrust — watch the **minimum N1 bug** on MFD.
"""
        )
        c1, c2 = st.columns(2)
        with c1:
            _img(f"{folder}/takeoff_dataset_menu_mfd.png", "Takeoff dataset menu (MFD)")
        with c2:
            _img(f"{folder}/poh_6-05_atr_logic_p497.png", "ATR logic (POH 6-05-30)")

    with st.expander("**4. Monitoring (N1 · N2 · ITT · oil)**", expanded=False):
        st.markdown(
            """
**What each parameter tells you**

| Param | Role | When it matters most |
|-------|------|----------------------|
| **N1** | Fan speed ≈ thrust | Takeoff (**"THRUST SET"**), cruise thrust changes |
| **N2** | Core speed | **Engine start** — monitor silently with ITT |
| **ITT** | Turbine temp | **Start** — primary limit cue; FADEC protects in flight |
| **Oil pres / temp** | Lubrication health | Any phase — trend + colour |

**FADEC limiting** — if a limit is approached, FADEC reduces fuel (you may not get requested thrust).
Full AFM limits → **Limitations → Engine Limits (PW535E)**.

**Start & starter limits (keep in head)**

| Item | Value |
|------|-------|
| FADEC ground abort ITT | **720°C** |
| Auto-relight until | **N2 < 40%** |
| Starter motoring 1 / 2 | **60 s** each |
| Starter motoring 3 / 4 | **15 min / 30 min** |
| Min oil temp for start | **-40°C** |

**Oil system (operational)**
- Lubricates main bearings and accessory gearbox.
- **Preflight:** check **sightglass** on each engine (*Airplane General* walkaround).
- **In flight:** watch oil pres/temp colours on MFD — CAS messages → **§5 below**.

**Engine failure in flight** → **Profiles** (EFATO / cruise OEI / OEI approach) — not repeated here.

**Icing & thrust** — engine anti-ice and **TT0 probe** → **Ice Protection**.
"""
        )

    cas_quick_reference(
        [
            ("Fire", "WARNING", "E1 (2) FIRE", "Memory item — IDLE, STOP, SHUTOFF; bottle if fire persists."),
            ("Engine", "WARNING", "E1 (2) FAIL", "Uncommanded shutdown — fly aircraft; QRH; see Profiles for OEI."),
            ("Oil", "CAUTION", "E1 (2) OIL LO PRES", "Reduce thrust on affected engine; land ASAP."),
            ("Control", "CAUTION", "E1 (2) CTRL FAULT", "Thrust modulation degraded or slow — avoid rapid lever moves."),
            ("FADEC", "CAUTION", "E1 (2) FADEC FAULT", "One channel not communicating — remaining channel may control."),
            ("Engine", "CAUTION", "E1 (2) CHIP DETECTED", "Metal in oil system — maintenance required."),
            ("Filters", "ADVISORY", "E1 (2) FUEL IMP BYP", "Fuel filter restriction increasing."),
            ("Filters", "ADVISORY", "E1 (2) OIL IMP BYP", "Oil filter restriction increasing."),
            ("TT0 probe", "CAUTION", "E1 (2) TT0 HTR FAIL", "TT0 heater failed — monitor thrust in icing."),
            ("TT0 probe", "ADVISORY", "E1 (2) TT0 PROBE ICE", "Ice on TT0 probe — possible thrust loss; see Ice Protection."),
            ("Performance", "ADVISORY", "ENG NO TO DATA", "Enter OAT + ATR on MFD before takeoff."),
            ("Limits", "CAUTION", "ENG EXCEEDANCE", "In-flight limit exceedance logged — maintenance follow-up."),
        ],
        title="5. CAS quick reference",
    )

    back_to_top()
    source_footer("poh", "§6-05 Powerplant · SOP Ch 2 start · Profiles EFATO/OEI")
