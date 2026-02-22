import os

import pandas as pd
import streamlit as st
from PIL import Image


def _img(path: str, caption: str):
    if os.path.exists(path):
        st.image(Image.open(path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Missing image: `{path}`")


def render_powerplant():
    st.markdown("## Powerplant (PW535E engines)")
    st.caption("ATA 71 | Source: Phenom 300 POH (Section 6-05, Rev 12)")

    folder = "assets/powerplant"

    with st.expander("**1. Engine overview (what you’re flying behind)**", expanded=True):
        st.markdown(
            """
**Configuration**
- Two rear-fuselage-mounted **Pratt & Whitney PW535E** turbofan engines.
- Two-spool architecture (LP & HP rotors), annular reverse-flow combustor.
- Controlled by a **dual-channel FADEC** (reduced workload, protections, and automated logic).

**Where to see it**
- Engine indications and alerts are displayed on the **MFD**.

_Source: POH 6-05-00 (Rev 12)._"""
        )
        c1, c2 = st.columns(2)
        with c1:
            _img(f"{folder}/pw535e_engine_overview.png", "PW535E engine (external overview)")
        with c2:
            _img(f"{folder}/pw535e_engine_cutaway.png", "PW535E engine (cutaway overview)")

    with st.expander("**2. Starting & ignition (high-level logic)**", expanded=False):
        st.markdown(
            """
**Starting system**
- Uses the **starter/generator** mounted on the accessory gearbox (AGB).
- FADEC provides automatic control of:
  - Fuel scheduling
  - Bleed valve position
  - Ignition
  - Start protections (on ground)

**Normal setup**
- ENG IGNITION switch in **AUTO** (FADEC controls igniters).

**Ground start (concept)**
- With thrust lever at IDLE, momentary START on ENG START/STOP initiates the sequence.
- FADEC monitors acceleration and **ITT** to protect the engine.

**FADEC aborts a ground start if** (examples)
- No light-up (ITT doesn’t rise significantly within ~10 s after fuel on)
- Hot start detected
- Hung start (time to reach idle exceeds ~60 s after fuel is commanded)

_Source: POH 6-05-20 (Original)._"""
        )

    with st.expander("**3. Engine fuel system (major components)**", expanded=False):
        st.markdown(
            """
**Main elements you’ll see referenced**
- **Fuel Metering Unit (FMU)** (metering, shutoff, motive flow, etc.)
- Integrated fuel manifold & nozzles (primary/secondary)
- **FOHE** (Fuel/Oil Heat Exchanger): heats fuel (anti-freeze) and manages oil temperature
- Fuel filter (with impending bypass and bypass indications)
- Fuel flow meter (FFT)

**Safety behaviors**
- FFT line failure protection: FADEC closes internal valves upstream to prevent fuel escape after starvation-induced shutdown.

_Source: POH 6-05-10 (Rev 6)._"""
        )
        _img(f"{folder}/engine_fuel_system_schematic.png", "Engine fuel system schematic")

    with st.expander("**4. Lubrication (what matters operationally)**", expanded=False):
        st.markdown(
            """
**Purpose**
- Lubricates and cools main shaft bearings and the accessory gearbox.

**Oil quantity**
- Each engine has an oil tank with **sightglass** indication.

**Key components (examples)**
- Oil tank, pressure/scavenge pumps, filters and bypass logic, FOHE, sensors.

_Source: POH 6-05-15 (Rev 6)._"""
        )

    with st.expander("**5. Thrust ratings / takeoff dataset (crew interaction)**", expanded=False):
        st.markdown(
            """
**FADEC-managed ratings**
- FADEC controls thrust ratings automatically based on conditions and selected modes.

**Takeoff dataset**
- Crew enters OAT and selects ATR option via the MFD takeoff dataset menu.

_Source: POH 6-05-30 (Rev 12)._"""
        )
        _img(f"{folder}/takeoff_dataset_menu_mfd.png", "Takeoff dataset menu (MFD)")

    with st.expander("**6. Protections (what the FADEC will do)**", expanded=False):
        st.markdown(
            """
**Overspeed/overtemp limiting**
- FADEC limits by reducing fuel flow when limits are exceeded (examples below).

**Key thresholds (from POH)**
- N1 limiting starts above **100%**.
- N2 limiting starts above **101%**.
- ITT limiting:
  - Above **700°C** during engine start
  - Above **765°C** otherwise
- On-ground start is aborted if ITT reaches **720°C** (to reduce damage risk).

**TT0 probe heating (icing)**
- TT0 probe heater is automatically used to prevent thrust loss in icing.

_Source: POH 6-05-30 (Rev 12)._"""
        )

    with st.expander("**7. CAS messages (quick meanings)**", expanded=False):
        rows = [
            ("E1 (2) FIRE", "Engine 1 (2) fire condition detected."),
            ("E1 (2) OIL LO PRES", "Engine 1 (2) oil pressure is low."),
            ("E1 (2) CTRL FAULT", "Thrust modulation may be degraded or respond slowly."),
            ("E1 (2) FAIL", "Uncommanded engine shutdown occurred."),
            ("E1 (2) FUEL IMP BYP", "Fuel filter impending bypass."),
            ("E1 (2) OIL IMP BYP", "Oil filter impending bypass."),
            ("E1 (2) CHIP DETECTED", "Chip detected in engine system."),
            ("E1 (2) FADEC FAULT", "Avionics not receiving data from one FADEC channel."),
            ("E1 (2) TT0 HTR FAIL", "TT0 sensor heating failed."),
            ("E1 (2) TT0 PROBE ICE", "TT0 heating turned off due to ice crystal formation."),
            ("ENG NO TO DATA", "Takeoff data not entered successfully."),
            ("ENG EXCEEDANCE", "In-flight engine limit exceedance detected."),
        ]
        st.table(pd.DataFrame(rows, columns=["CAS message", "Meaning (summary)"]))
        st.markdown("_Source: POH 6-05-35 (Rev 6)._")

