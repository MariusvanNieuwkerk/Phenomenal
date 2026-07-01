"""Warning System — CAS, configuration checks, SWPS interface (ATA 31)."""

import pandas as pd
import streamlit as st

from content.render_helpers import back_to_top, cas_quick_reference, source_footer


def _table(rows: list[tuple], columns: list[str]):
    st.dataframe(pd.DataFrame(rows, columns=columns), hide_index=True, use_container_width=True)


def render_warning_system():
    st.markdown("## Warning System (CAS & checks)")
    st.caption("ATA 31 · Crew Alerting System · POH §6-14")

    with st.expander("**1. Big picture**", expanded=True):
        st.markdown(
            """
The **Crew Alerting System (CAS)** is your central warning display on the PFD.

| Level | Colour cue | Pilot response |
|-------|------------|----------------|
| **WARNING** | Red | Immediate action — memory item or QRH now |
| **CAUTION** | Amber | Prompt action — QRH when workload allows |
| **ADVISORY** | Cyan/white | Awareness — monitor, may not need immediate action |

**This module covers:** CAS philosophy, takeoff configuration check, stall-warning controls, and how SWPS/pusher alerts appear.

**Not here:** TAWS/TCAS pages (avionics-specific).
"""
        )

    with st.expander("**2. How to read a CAS message (scan technique)**", expanded=False):
        st.markdown(
            """
1. **Level** — WARNING vs CAUTION vs ADVISORY sets urgency.
2. **System** — which ATA/system is affected (hydraulics, gear, SWPS…).
3. **Indications** — confirm on synoptic / dedicated display (don't trust CAS alone).
4. **Trend** — clearing, latched, or escalating?

**SOP (unexpected CAS):** PF announces level + exact text → PM confirms → cancel audio if applicable → QRH.
"""
        )

    with st.expander("**3. Takeoff configuration check**", expanded=False):
        st.markdown(
            """
Before takeoff, the system verifies the aircraft is configured correctly (logic varies by phase).

**Typically monitored:**
- Flap position vs required takeoff setting
- Speedbrake / spoiler state
- Trim in takeoff range
- Parking brake released
- Other config items per POH

**If config is wrong:** aural/visual warning — do **not** take off until resolved.

**Link:** flap/gear warnings interact with **Landing Gear** (gear horn logic) and **Flight Controls** (flaps, spoilers).
"""
        )

    with st.expander("**4. Stall warning & SWPS (stick shaker / pusher)**", expanded=False):
        st.markdown(
            """
**SWPS** = Stall Warning and Protection System (see also **Flight Controls → SWPS**).

| Component | What it does |
|-----------|--------------|
| **Stick shaker** | Vibrates column before stall — time to recover |
| **Stick pusher** | Pushes column forward if AoA still too high |
| **PUSHER CUTOUT** | Inhibits pusher (memory item: inadvertent activation) |
| **STALL WARN CUTOUT** | Inhibits shaker — limited use per QRH |

**Icing:** WINGSTAB ON → **SWPS ICE SPEED** / higher stall speeds → **ICE SPEED RESET** only when ice is gone (see **Ice Protection**).

**Takeoff:** SWPS must be tested/serviceable — **SWPS UNTESTED** is a dispatch issue.
"""
        )

    with st.expander("**4b. Windshear detection (Handbook Ch 3.3)**", expanded=False):
        st.markdown(
            """
On-board **windshear detection** uses similar logic to stall warning (multiple inputs).

- Use as an **aid** alongside OM-B windshear cues and weather — not a sole go/no-go.
- **Safety first** — positive response to any warning.
- **AOA-based** alerts may show ~3 s then clear (like stall warning) — use experience and other cues.

_See **Flight Profiles** / OM-B for windshear recovery._
"""
        )

    with st.expander("**4c. EGPWS / TAWS (Handbook Ch 5.3)**", expanded=False):
        st.markdown(
            """
**Garmin EGPWS** looks ahead **45 s in turn**, **60 s straight** — often **more terrain alerts** than Honeywell-equipped types.

**Customised look-ahead (4 airports only)** — Lugano, Bolzano, Sion, Innsbruck: **50%** reduction (~23 s turn / 30 s straight). Enables reduced minima ops at LSZA after Load update.

**All other airports** — standard TAWS envelope.

**Crew action** — always follow **OM-A TAWS guidance**; make a **positive correction** regardless of perceived nuisance.

_See **Special Airports** for airport-specific notes (e.g. Lugano)._
"""
        )

    with st.expander("**4d. TCAS & transponder (Handbook Ch 5.4)**", expanded=False):
        st.markdown(
            """
**Ground TA/RA events** — transponder in **AUTO** on ground with faulty **radalt** (e.g. showing 1100 ft on ramp) can trigger **CLIMB** alerts.

**Fleet procedure**
1. **STBY** at power-up during system tests and FMS programming.
2. Select **AUTO** just before **taxi** (required for ALT reporting airborne — **ON** does not auto-switch to ALT).

**Oscillations > 1000 ft** — TCAS may command TA/RA; consider **STBY** if needed to avoid ATC interference.

**ADS-B OUT** — additional data exchange with ATC; brief accordingly.
"""
        )

    with st.expander("**5. Other common CAS (by system)**", expanded=False):
        st.markdown("Use the dedicated system page for full tables. Quick cross-reference:")
        _table(
            [
                ("Hydraulics", "HYD HI TEMP, HYD LO PRES, HYD SOV FAIL", "Systems → Hydraulics"),
                ("Landing gear", "LG LEVER DISAG, LG WOW SYS FAIL, ANTI-SKID FAIL", "Systems → Landing Gear"),
                ("Fire", "BAG SMK, E1(2) FIRE DET FAIL", "Systems → Fire Protection"),
                ("Flight controls", "FLAP FAIL, PTRIM FAIL, RUD GUST LOCKED", "Systems → Flight Controls"),
                ("AFCS", "AP FAIL, AP MISTRIM, STEEP FAIL", "Systems → Automatic Flight"),
                ("Pressurization", "CAB ALTITUDE HI, PRESN AUTO FAIL", "Systems → Air Management"),
            ],
            ["System", "Examples", "Where in Briefly"],
        )

    cas_quick_reference(
        [
            ("SWPS", "CAUTION", "PUSHER FAIL", "Pusher may not activate — fly conservative margins."),
            ("SWPS", "CAUTION", "PUSHER OFF", "Pusher inhibited — know why (cutout vs fault)."),
            ("SWPS", "CAUTION", "SWPS FAIL", "Protection degraded — QRH."),
            ("SWPS", "CAUTION", "SWPS FAULT", "Fault detected — verify before flight."),
            ("SWPS", "CAUTION", "SWPS UNTESTED", "Power-up test incomplete — resolve before dispatch."),
            ("SWPS", "ADVISORY", "SWPS ICE SPEED", "Anti-ice on — stall speeds increased."),
        ],
        title="6. CAS quick reference",
    )

    with st.expander("**7. Study checklist**", expanded=False):
        st.markdown(
            """
- [ ] Name the **three CAS levels** and colours.
- [ ] What does **takeoff config check** protect against?
- [ ] Difference between **shaker** and **pusher**.
- [ ] When is **PUSHER CUTOUT** a memory item?
- [ ] What does **SWPS ICE SPEED** mean?
- [ ] SOP flow for an **unexpected WARNING**.
"""
        )

    back_to_top()
    source_footer("poh", "§6-14 Warning System · QRH for memory items")
