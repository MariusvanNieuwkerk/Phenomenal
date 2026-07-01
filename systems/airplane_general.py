"""Airplane General — dimensions, layout, walkaround reference (ATA 06)."""

import os

import streamlit as st
from PIL import Image

from content.render_helpers import back_to_top, source_footer


def _img(path: str, caption: str):
    if os.path.exists(path):
        st.image(Image.open(path), caption=caption, use_container_width=True)


def _show_poh_images(folder: str, startswith: str, title: str):
    paths = []
    if os.path.isdir(folder):
        for name in os.listdir(folder):
            if name.lower().endswith(".png") and name.startswith(startswith):
                paths.append(os.path.join(folder, name))
    paths.sort()
    if not paths:
        st.info("No POH images found for this section yet.")
        return
    st.markdown(f"**{title}**")
    cols = st.columns(2, gap="medium")
    for i, p in enumerate(paths):
        with cols[i % 2]:
            _img(p, os.path.basename(p))


_WALK_FOLDER = "assets/walkaround"


def _walk_imgs(*prefixes: str):
    """Show handbook walkround photos (extracted from Handbook Ch 2.1)."""
    if not os.path.isdir(_WALK_FOLDER):
        return
    paths: list[str] = []
    for prefix in prefixes:
        for name in sorted(os.listdir(_WALK_FOLDER)):
            if name.startswith(prefix) and name.lower().endswith((".jpeg", ".jpg", ".png")):
                paths.append(os.path.join(_WALK_FOLDER, name))
    paths = sorted(set(paths))
    if not paths:
        return
    cols = st.columns(2, gap="medium")
    for i, p in enumerate(paths):
        with cols[i % 2]:
            _img(p, os.path.basename(p).replace("_", " ").replace(".jpeg", ""))


def render_airplane_general():
    st.markdown("## Airplane General")
    st.caption("ATA 06 · Layout & reference data · POH §6-01 · Handbook Ch 2.1 walkround")

    folder = "assets/airplane_general"

    with st.expander("**1. What this section is for**", expanded=False):
        st.markdown(
            """
Use **Airplane General** as a fast reference for:

- **Dimensions** — wingspan, length (taxi clearances)
- **Door locations** — pax, baggage, servicing
- **Cockpit layout** — where to find indications and controls
- **Walkaround** — step-by-step exterior inspection with handbook photos

For systems knowledge, use the dedicated **Systems** pages.
"""
        )

    with st.expander("**2. Key dimensions (study reference)**", expanded=False):
        st.markdown(
            """
| Item | Approximate value |
|------|-------------------|
| **Wingspan** | ~16.2 m (52 ft 2 in) |
| **Length** | ~15.9 m (52 ft 2 in) |
| **Height (tail)** | ~5.1 m (16 ft 9 in) |
| **Wheelbase** | Main gear spacing per POH diagram |

**Taxi turns:** see **Landing Gear → Turning radius** for steering limits.

_Verify exact figures on your POH §6-01 for exam/sim._
"""
        )

    with st.expander("**3. External walkround guide (Handbook Ch 2.1)**", expanded=True):
        st.markdown(
            """
**Authority:** AFM External Inspection Checklist + **Handbook Ch 2.1** (photos below).

**Route:** stand **left of the main door** → walk **toward the nose** → continue **clockwise** around the aircraft → finish at the **main door**.

### Golden rules

- All doors/panels: **fully open OR fully locked** — never ambiguous.
- Overall: any **damage**, contamination (ice/frost/snow), or abnormal condition → resolve before flight.
- **POH** is master for latest checklist revision.

### Order of checks

1. External lights (first flight of the day)
2. Emergency lighting (batteries OFF)
3. Exterior walkround (item list below)
4. Main door
"""
        )

        with st.expander("**3a. External lights check (Ch 2.1.1)**", expanded=False):
            st.markdown(
                """
**First flight of the day** — verify from outside:

| Light | Location / behaviour |
|-------|----------------------|
| **Navigation** | Red (port), green (starboard), 2× white aft near wing tips |
| **Beacon** | Tail — auto ON when either engine start knob → RUN |
| **Taxi / landing** | 4 belly lights — all 4 **dim** for taxi; centre two **bright** when landing selected |
| **Strobe / anti-collision** | Upper and lower fuselage |
| **Wing inspection** | **Left side only** — sole **halogen** bulb (rest are LED) |

→ Light logic: **Electrics** · Callouts: **SOP** pre-flight flows.
"""
            )
            _walk_imgs("handbook_2_1_", "handbook_2_2_")

        with st.expander("**3b. Emergency lighting check (Ch 2.1.2)**", expanded=False):
            st.markdown(
                """
Test with **batteries OFF** — confirms emergency lights run on their own supply.

### Check

- Main aisle lights (red, forward of exits)
- Overhead lights and **EXIT** signs
- Main door exit sign
- Main stair lights
- Emergency exit egress lights

**After check** — turn all lights **OFF** (especially on battery power).

### Troubleshooting

- Flickering or lights ON in ARM → weak/low emergency battery.
- Charge with GPU or in flight **≥ 45 min**, then retest.
- Avoid using EMER lights for paperwork after BATT OFF (known battery drain issue).
"""
            )
            _walk_imgs("handbook_2_3_", "handbook_2_4_")

        with st.expander("**3c. Nose & forward fuselage (Ch 2.1.3 — start)**", expanded=False):
            st.markdown(
                """
| Item | What to check |
|------|----------------|
| **IASP (port)** | Condition, no obstruction; stow cover in **left nose baggage box** |
| **Oxygen blow-out disc** | **Green disc** in place; O₂ pressure gauge in left nose baggage if needed |
| **Ice detector** | Condition |
| **Antennas (nose underside)** | No damage |
| **Nose landing gear** | Tyre (wear/cuts), strut extension normal for weight, bay condition |
| **NLG safety pin** | **Removed** (flag can hide inside bay — look carefully) |
| **Steering torque link** | **Connected & secured** if not towing; extra clip locked |
| **Fwd LH baggage door** | Locked when not in use / loading complete |
| **Radome** | Condition |
| **Fwd RH baggage door** | Locked |
| **Standby pitot** | Condition, no obstruction |
| **Refuelling panel** | **Closed** |
| **Landing / taxi lights** | Condition |
"""
            )
            st.caption("NLG steering: towing adapter only fits with steering disconnected.")
            _walk_imgs("handbook_2_5_", "handbook_2_6_", "handbook_2_7_", "handbook_2_8_")

        with st.expander("**3d. Right wing, engine & MLG (Ch 2.1.3 — right side)**", expanded=False):
            st.markdown(
                """
| Item | What to check |
|------|----------------|
| **Engine fan** | Blades condition, free to turn |
| **S/GEN air inlets** | Clear |
| **Fuselage air intake** | Condition |
| **Fuel drains / dump valves** | No leaks (fleet: drain check often omitted — high utilisation) |
| **MLG doors, wheels, brakes, tyres** | Condition; **2 brake wear pins** per wheel — change when pin **flush** with housing |
| **MLG safety pin** | **Removed** |
| **Fuel cap** | Closed and locked |
| **Fuel tank vent** | No obstruction |
| **Nav / strobe lights** | Condition |
| **Right wing LE, winglet** | Condition (contamination, damage) |
| **Right aileron, spoilers, flap** | Condition; aileron **free** |
| **Static dischargers** | Count & condition — min **1 per control surface**, **≥ 8 total** (MEL G-CDL-5) |
| **Battery access door** | Secured |
| **Toilet servicing door** | Secure → **Cabin & IFE** |
| **Oil level** | Check |
| **Cowlings** | Latched |
| **Drain masts, exhausts** | Clear |
| **Heat exchanger exhaust** | Clear |
"""
            )
            _walk_imgs("handbook_2_9_", "handbook_2_10_", "handbook_2_11_", "handbook_2_12_", "handbook_2_13_")

        with st.expander("**3e. Tail & empennage (Ch 2.1.3 — aft)**", expanded=False):
            st.markdown(
                """
| Item | What to check |
|------|----------------|
| **Vertical stabilizer, pylon** | Condition |
| **Rudder, yaw trim tab** | Condition; rudder static dischargers |
| **Horizontal stabilizer, elevator, pitch trim** | Condition; elevator static dischargers |
| **Tail antennas** | Condition |
| **Ventral rudder** | Condition |
| **Aft baggage bay** | Secure |
| **Left engine (aft view)** | Pylon, cowlings latched, exhausts clear, drains, oil |
| **Air exhausts** | No obstructions |
"""
            )
            _walk_imgs("handbook_2_14_", "handbook_2_15_", "handbook_2_16_")

        with st.expander("**3f. Left aft fuselage — hydraulics & GPU (Ch 2.1.3)**", expanded=False):
            st.markdown(
                """
| Item | What to check |
|------|----------------|
| **DC power receptacle** | Condition |
| **Hydraulic access — upper door** | Lines, connections, **red chip detectors** OK; door closed |
| **Hydraulic access — lower door** | Reservoir sight gauge — blue fluid mark in **green dispatch range** |

### If fluid level doubtful

- Full check per **POH 5-30**.
- Depressurise parking brake (pump T-handle to zero) only with aircraft **chocked** — chocks stay until after **first engine start**.
- Low fluid + brake release can raise indicated level — interpret carefully.

→ **Hydraulics** system page · **Landing Gear** brakes.
"""
            )
            _walk_imgs("handbook_2_17_")

        with st.expander("**3g. Left wing back to main door (Ch 2.1.3 — finish)**", expanded=False):
            st.markdown(
                """
| Item | What to check |
|------|----------------|
| **Left flap, spoilers, aileron** | Condition; aileron **free** |
| **Roll trim tab** | Condition |
| **Nav / strobe lights** | Condition |
| **Left winglet & LE** | Condition |
| **Fuel cap & vent** | Closed / clear |
| **MLG (port)** | Doors, wheels, brakes, tyres — same as starboard |
"""
            )
            _walk_imgs("handbook_2_18_")

        with st.expander("**3h. Main door (Ch 2.1.4)**", expanded=False):
            st.markdown(
                """
### Main door

- Condition, ease of movement
- Door lights / exit signage (after emergency lighting check)
- Seals and locking indication

→ Interior cabin prep: **Cabin & IFE** · **SOP** flows.
"""
            )

        st.markdown("---")
        st.markdown(
            """
### Study checklist

- [ ] I know the walkround **direction** (left of door → nose → clockwise → door)
- [ ] NLG & MLG **safety pins removed**
- [ ] **Steering torque link** connected when not towing
- [ ] **Brake wear pins** — when flush, maintenance required
- [ ] **Static dischargers** — MEL minimums
- [ ] **Hydraulic** reservoir in green range
- [ ] Doors/panels **open or locked**, never in-between

_Full handbook PDF with original layout → **Documents → Handbook Phenom 300** Ch 2.1._
"""
        )

    with st.expander("**4. Cockpit orientation**", expanded=False):
        st.markdown(
            """
### Left to right (concept)

- **PFD** — flight instruments, FD command bars, CAS messages
- **MFD** — synoptics, maps, checklists
- **GTC** — FMS / system setup touch controller

**Pedestal** — thrust levers, flap lever, speedbrake, parking brake T-handle, trim

**Overhead** — electrics, bleeds, pressurization, ice protection, lights

Match POH §6-01 cockpit layout diagrams for exact naming.
"""
        )

    with st.expander("**5. POH synoptic pages**", expanded=False):
        _show_poh_images(folder, "poh_6-01_synoptic_", "POH pages (6-01)")

    back_to_top()
    source_footer("poh", "§6-01 Airplane General · Handbook Ch 2.1")
