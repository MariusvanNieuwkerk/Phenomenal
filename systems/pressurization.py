import os

import pandas as pd
import streamlit as st
from PIL import Image


def _img(path: str, caption: str):
    if os.path.exists(path):
        st.image(Image.open(path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Missing image: `{path}`")


def render_pressurization():
    st.markdown("## Pressurization (Air Management)")
    st.caption("ATA 21 | Source: Phenom 300 POH (Section 6-02, Rev 6)")

    folder = "assets/pressurization"

    with st.expander("**1. What feeds pressurization (big picture)**", expanded=True):
        st.markdown(
            """
Pressurization is part of the **Air Management System**.

**Bleed / pneumatic basics**
- Two independent engine **bleed air circuits** supply:
  - **ECS** (environmental control / pressurization & conditioning)
  - **Wing & horizontal stabilizer anti-ice**
- Circuits can be interconnected via the **Cross Bleed Valve (XBV)** when required.
- Each side uses a **Pressure Regulating Shutoff Valve (PRSOV)** to regulate bleed pressure and provide firewall shutoff capability.

_Source: POH 6-02-10 (Rev 6/7)._"""
        )
        _img(f"{folder}/pneumatic_system_schematic.png", "Pneumatic system schematic (bleed, PRSOV, XBV)")

    with st.expander("**2. Controls & indications (where you touch/see it)**", expanded=False):
        st.markdown(
            """
**Primary crew interface**
- **Pressurization and Pneumatic Control Panel** (mode selection, dump, bleed, xbleed).

**Primary display**
- **Cabin pressure indications on the MFD** (cabin altitude, cabin rate, differential pressure, landing field elevation).

_Source: POH 6-02-05 (Original/Rev 6)._"""
        )
        c1, c2 = st.columns(2)
        with c1:
            _img(f"{folder}/pressurization_pneumatic_panel.png", "Pressurization & pneumatic control panel")
        with c2:
            _img(f"{folder}/pressure_indication_mfd.png", "Cabin pressure indication (MFD example)")

    with st.expander("**3. CPCS overview (components & functions)**", expanded=False):
        st.markdown(
            """
**Cabin Pressure Control System (CPCS)**
- Provides automatic pressurization control for safety and comfort.
- Normal operation is **AUTO** (manual is for abnormal use).

**Main components**
- **ECMU** (Electronic Control and Monitoring Unit) with **two independent channels**
- **Outflow Valve (OFV)** (auto or manual modulation of cabin exhaust)
- **Negative Relief Valve (NRV)** and **Positive Relief Valve (PRV)** (mechanical relief protection)

**Key functions**
- Cabin altitude limiting
- Decompression prevention (leaks)
- **DUMP** function (rapid depressurization)
- Automatic control of cabin pressure / rate / differential pressure
- Manual control capability (with protections/limits)

_Source: POH 6-02-20 (Rev 6)._"""
        )
        _img(f"{folder}/cpcs_schematic.png", "CPCS schematic")

    with st.expander("**4. Automatic vs Manual mode (what changes)**", expanded=False):
        st.markdown(
            """
**AUTO (normal)**
- CPCS controls cabin exhaust for ground / takeoff / climb / descent / taxi with no dedicated crew inputs.
- Requires **Landing Field Elevation (LFE)**:
  - Provided automatically via **FMS**, or
  - Entered manually through the **MFD**.

**MAN (abnormal)**
- Selected by MODE switch to **MAN**.
- Crew uses CABIN ALT switch **UP / DN** to command OFV open/close.
- Manual channel includes **altitude limiting** so commands don’t drive the cabin to unsafe conditions.

_Source: POH 6-02-20 (Rev 6)._"""
        )

    with st.expander("**5. Key numbers (quick lookup)**", expanded=False):
        st.markdown(
            """
**Cabin altitude high warning**
- Triggers at **10,000 ft cabin altitude** (standard configuration), with special logic for high-field operations.

**Differential pressure**
- Normal indication range centers below **9.5 psid**.
- A differential pressure fail condition is associated with **> 9.5 psid** or **< -0.3 psid**.

**Ceiling capability (system design point)**
- System described for airplane ceiling up to **45,000 ft** (cabin altitude approx **6,640 ft** at that altitude).

_Source: POH 6-02-20 + 6-02-25 (Rev 6/5)._"""
        )

    with st.expander("**6. Common CAS messages (meaning)**", expanded=False):
        rows = [
            ("CAB ALTITUDE HI", "Cabin altitude ≥ 10,000 ft."),
            ("PRESN AUTO FAIL", "Loss of automatic pressurization mode."),
            ("CAB DELTA-P FAIL", "Cabin differential pressure too high (> 9.5 psid) or too low (< -0.3 psid)."),
            ("BLEED 1 (2) FAIL", "Bleed failure detected; bleed no longer available."),
            ("BLEED 1 (2) LEAK", "Leak detected in associated bleed line."),
            ("BLEED 1 (2) OVERPRES", "Bleed overpressure condition in manifold."),
            ("DUCT 1 (2) OVERTEMP", "Overheat detected in associated bleed line."),
            ("XBLEED FAIL", "Crossbleed failure; not responding to commands."),
            ("EBAY OVHT", "Electronic bay temperature above 70°C (158°F)."),
        ]
        st.table(pd.DataFrame(rows, columns=["CAS message", "Meaning (summary)"]))
        st.markdown("_Source: POH 6-02-25 (Rev 5)._")

    with st.expander("**7. Diagram cheat sheet**", expanded=False):
        c1, c2 = st.columns(2)
        with c1:
            _img(f"{folder}/cpcs_schematic.png", "CPCS schematic (pressurization control)")
        with c2:
            _img(f"{folder}/pneumatic_system_schematic.png", "Pneumatic system (bleed supply)")
        _img(f"{folder}/tcs_schematic.png", "Temperature Control System (context)")

