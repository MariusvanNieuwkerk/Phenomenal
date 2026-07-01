"""Warning System — CAS, configuration checks, SWPS interface (ATA 31)."""

import streamlit as st

from content.render_helpers import back_to_top, cas_quick_reference, source_footer


def render_warning_system():
    st.markdown("## Warning System (CAS & checks)")
    st.caption("ATA 31 · Crew Alerting System · POH §6-14")

    with st.expander("**1. How it works**", expanded=True):
        st.markdown(
            """
The **Crew Alerting System (CAS)** is your central warning display on the PFD.

| Level | Colour cue | Pilot response |
|-------|------------|----------------|
| **WARNING** | Red | Immediate action — memory item or QRH now |
| **CAUTION** | Amber | Prompt action — QRH when workload allows |
| **ADVISORY** | Cyan/white | Awareness — monitor, may not need immediate action |

This page explains how to read CAS messages, the takeoff configuration check, and how **SWPS** / stick pusher alerts appear.

Windshear (Handbook Ch 3.3), EGPWS/TAWS (Ch 5.3), and TCAS/transponder (Ch 5.4) are covered in the Handbook and OM-A — not repeated here.
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

### Typically monitored:

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

    with st.expander("**5. Other common CAS (by system)**", expanded=False):
        st.markdown(
            """
Use the dedicated system page for full CAS tables. Quick cross-reference:

| System | Examples | Where in Briefly |
|--------|----------|------------------|
| Hydraulics | HYD HI TEMP, HYD LO PRES, HYD SOV FAIL | Systems → Hydraulics |
| Landing gear | LG LEVER DISAG, LG WOW SYS FAIL, ANTI-SKID FAIL | Systems → Landing Gear |
| Fire | BAG SMK, E1(2) FIRE DET FAIL | Systems → Fire Protection |
| Flight controls | FLAP FAIL, PTRIM FAIL, RUD GUST LOCKED | Systems → Flight Controls |
| AFCS | AP FAIL, AP MISTRIM, STEEP FAIL | Systems → Automatic Flight |
| Pressurization | CAB ALTITUDE HI, PRESN AUTO FAIL | Systems → Air Management |
"""
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

    back_to_top()
    source_footer("poh", "§6-14 Warning System · QRH for memory items")
