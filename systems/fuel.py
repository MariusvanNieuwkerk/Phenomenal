import os

import pandas as pd
import streamlit as st
from PIL import Image


def _img(path: str, caption: str):
    if os.path.exists(path):
        st.image(Image.open(path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Missing image: `{path}`")


def render_fuel():
    st.markdown("## Fuel System")
    st.caption("ATA 28 | Source: Phenom 300 POH (Section 6-09, Rev 12)")

    folder = "assets/fuel"

    with st.expander("**1. System overview**", expanded=True):
        st.markdown(
            """
**Purpose**
- Store fuel and **continuously supply both engines** across the operating envelope.
- Provide **indication** and crew alerting (synoptic + CAS).

**Where fuel is stored**
- Two **integral wing tanks** (left & right), physically isolated from each other.

**Where to see it**
- Fuel parameters and synoptic → **MFD** (Fuel synoptic + Fuel Data)
- Messages → **both PFDs**

_Source: POH 6-09-00 (Original/Rev 6)._"""
        )

    with st.expander("**2. Controls (Fuel panel)**", expanded=False):
        st.markdown(
            """
**Fuel pump selector (per side)**
- **ON**: activates associated electric boost pump.
- **AUTO**: EFCU controls pump automatically (normal position).
- **OFF**: deactivates pump.

**Crossfeed knob (XFEED)**
- **LO1**: opens crossfeed **and turns on Pump 2** → both engines fed from **right** tank.
- **OFF**: crossfeed closed.
- **LO2**: opens crossfeed **and turns on Pump 1** → both engines fed from **left** tank.

**Operational note**
- Crossfeed operation **should not be performed during takeoff and landing**.

_Source: POH 6-09-05 (Original/Rev 7)._"""
        )
        _img(f"{folder}/fuel_control_panel.png", "Fuel control panel")

    with st.expander("**3. Tanks, ventilation, and indications**", expanded=False):
        st.markdown(
            """
**Tank structure (each wing)**
- **Main tank**, **surge tank**, and **collector tank**.
- The **collector tank** keeps pumps submerged to support a steady feed.

**Vent system**
- Designed to keep tank differential pressure within structural limits and prevent spillage during maneuvers/overfill events.
- Each tank vents through a **NACA inlet/outlet** on the lower wing surface (inboard of the wing tip).

**Quantity indication**
- **Capacitive** measurement, self-calibrated (no adjustment).
- Quantity signal is processed by a segregated **EFCU** channel for each tank.
  - Loss of one tank quantity indication also removes the **total** quantity indication.

**Fuel temperature**
- Measured in the **right collector tank**.
- Normal display range: **> -37°C (-34°F)** and **< 80°C (176°F)**.

_Source: POH 6-09-10 (Rev 12) + 6-09-05 (Rev 6)._"""
        )
        _img(f"{folder}/fuel_tanks_location.png", "Fuel tanks (location/structure)")

    with st.expander("**4. Engine fuel feed (normal and backup)**", expanded=False):
        st.markdown(
            """
**Independent feeds**
- Left and right engine feed systems are **independent**.
- Closing one engine fuel shutoff valve does **not** make fuel unavailable to the other engine.

**Pumps in each tank**
- **Ejector fuel pump** (primary): venturi/jet pump, **no moving parts**, driven by engine motive flow.
- **Scavenge jet pump**: maintains collector tank level (helps during uncoordinated maneuvers).
- **Electric boost pump**: used for **engine start**, **XFEED**, and **backup** when ejector feed is not sufficient.

**Automatic logic**
- With pump selector in **AUTO**, EFCU commands the electric boost pumps when required.

**Electrical power sources (asymmetric on purpose)**
- **DC Pump 1 (left)**: powered by the **Emergency Bus**.
- **DC Pump 2 (right)**: powered by **DC BUS 2**.

_Source: POH 6-09-10 (Rev 12)._"""
        )

    with st.expander("**5. Fuel shutoff (fire protection interface)**", expanded=False):
        st.markdown(
            """
**Fuel shutoff valves**
- Installed in each wing feed line to prevent hazardous fuel flow into fire zones.
- **Normally open**.
- Only the **fire shutoff pushbutton** commands them closed.

_Source: POH 6-09-10 (Rev 12)._"""
        )

    with st.expander("**6. CAS messages (quick meanings)**", expanded=False):
        rows = [
            ("FUEL 1 (2) LO LEVEL", "Low-level sensors: 140 kg (310 lb) remains in that tank."),
            ("FUEL 1 (2) LO PRES", "Low pressure to associated engine while engine is running."),
            ("FUEL 1 (2) SOV FAIL", "Mismatch between commanded and actual shutoff valve status."),
            ("FUEL IMBALANCE", "Imbalance ≥ 100 kg (220 lb); clears when reduced to 40 kg (88 lb)."),
            ("FUEL XFEED FAIL", "Mismatch between commanded and actual crossfeed valve status."),
            ("FUEL PUMP 1 (2) FAIL", "Mismatch between commanded/actual pump status or pump failure."),
            ("FUEL 1 (2) FEED FAULT", "Primary feed low pressure → DC pump activates."),
            ("DOOR REFUEL OPEN", "Refuel panel door open; must be closed before takeoff."),
            ("FUEL EQUAL", "With XFEED open: lateral fuel difference < 20 kg (44 lb)."),
        ]
        st.table(pd.DataFrame(rows, columns=["CAS message", "Meaning (summary)"]))
        st.markdown("_Source: POH 6-09-15 (Rev 8)._")

    with st.expander("**7. Synoptic (what you’ll see on the MFD)**", expanded=False):
        st.markdown(
            """
The fuel synoptic provides a quick visual of:
- Total fuel remaining / total used
- Left/right tank quantities
- Electric pump status (ON/OFF/FAILED)
- Crossfeed valve status (OPEN/CLOSED)

_Source: POH 6-09-05 (Rev 6/7)._"""
        )
        _img(f"{folder}/fuel_synoptic_mfd.png", "Fuel synoptic page (MFD)")

