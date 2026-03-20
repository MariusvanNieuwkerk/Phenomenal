import os

import pandas as pd
import streamlit as st
from PIL import Image


def _img(path: str, caption: str):
    if os.path.exists(path):
        st.image(Image.open(path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Missing image: `{path}`")


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


def render_air_management():
    st.markdown("## Air Management System (Bleed, ECS, Pressurization)")
    st.caption("ATA 21 | Source: Phenom 300 POH (Section 6-02, Rev 6)")

    folder = "assets/air_management"
    press_folder = "assets/pressurization"

    with st.expander("**1. Overview (scope and architecture)**", expanded=True):
        st.markdown(
            """
The Air Management System combines:

- **Pneumatic (bleed) system**: provides pressurized air from the engines.
- **Environmental Control System (ECS)**: conditions air for the cabin (temperature and distribution).
- **Pressurization**: controls cabin altitude, cabin rate, and differential pressure.

Operationally, most “air” topics on the airplane connect back to two questions:
- **Do we have a good bleed supply?**
- **Is the outflow valve being controlled correctly?**
"""
        )
        _img(f"{press_folder}/pneumatic_system_schematic.png", "Bleed / pneumatic overview (PRSOV, XBV, supply)")

    with st.expander("**2. Controls & indications (what you touch / what you monitor)**", expanded=False):
        st.markdown(
            """
**Primary crew interfaces**
- **Air Conditioning Control Panel** (temperature / distribution / conditioning functions).
- **Pressurization and Pneumatic Control Panel** (pressurization mode, dump, bleed, crossbleed).

**Primary displays**
- **MFD synoptic pages** (air management overview and system state).
- **Cabin pressure indication** (cabin altitude / rate / differential pressure).
"""
        )
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            _img(f"{press_folder}/pressurization_pneumatic_panel.png", "Pressurization & pneumatic control panel")
        with c2:
            _img(f"{press_folder}/pressure_indication_mfd.png", "Cabin pressure indication (MFD example)")

        _show_poh_images(folder, "poh_6-02_synoptic_", "POH synoptic pages (Air Management)")

    with st.expander("**3. Pneumatic (bleed) system (what it supplies)**", expanded=False):
        st.markdown(
            """
**What bleed air is used for**
- **Cabin conditioning and pressurization** (via ECS).
- **Wing/stabilizer anti-ice** (thermal).

**Key elements**
- **PRSOV (per engine)**: regulates bleed pressure and provides shutoff.
- **XBV (Cross Bleed Valve)**: interconnect capability between sides when required.

**Practical monitoring**
- If multiple “air” functions degrade together (pressurization, temperature control, anti-ice), suspect **bleed supply** first.
"""
        )

    with st.expander("**4. ECS / temperature control (what you should expect)**", expanded=False):
        st.markdown(
            """
The ECS conditions bleed air so the cabin receives:
- correct **temperature** (temperature control system),
- correct **flow distribution** (ducting/zone distribution),
- stable operation across flight phases.

Operational cues:
- If the cabin temperature is slow to respond, verify panel settings and confirm there is no broader **bleed limitation**.
"""
        )

    with st.expander("**5. Pressurization (conceptual model)**", expanded=False):
        st.markdown(
            """
Pressurization is controlled by **air in vs air out**.

**Air in (supply)**
- Engine bleed air (conditioned by ECS).

**Air out (control)**
- Cabin pressure is controlled primarily by positioning the **Outflow Valve (OFV)**.

**Effect of OFV position**
- **Close OFV** → less air escapes → cabin pressure increases (cabin altitude decreases).
- **Open OFV** → more air escapes → cabin pressure decreases (cabin altitude increases).

The CPCS provides automatic OFV control to maintain cabin altitude, cabin rate, and differential pressure within limits.
"""
        )
        _img(f"{press_folder}/cpcs_schematic.png", "CPCS schematic (pressurization control)")

    with st.expander("**6. Operating goal by phase (what the system is trying to do)**", expanded=False):
        phases = [
            ("On the ground", "Keep cabin near ambient; prevent unintended differential pressure."),
            ("Takeoff / climb", "Schedule cabin altitude and rate within comfort and structural limits."),
            ("Cruise", "Maintain stable cabin altitude and protect differential pressure limits."),
            ("Descent / landing", "Schedule cabin descent toward landing field reference so doors open normally."),
        ]
        st.table(pd.DataFrame(phases, columns=["Phase", "Goal"]))
        st.markdown(
            """
**Landing field reference**
- The automatic schedule depends on having a correct destination reference (typically from the FMS or via manual entry).
"""
        )

    with st.expander("**7. Operational interpretation (common patterns)**", expanded=False):
        patterns = [
            ("CAB ALTITUDE HI", "Cabin altitude is increasing; common drivers include insufficient bleed supply or OFV too open."),
            ("PRESN AUTO FAIL", "Automatic pressurization is unavailable; manual control may be required."),
            ("CAB DELTA-P FAIL", "Differential pressure limit exceeded (high or low); structural protection condition."),
            ("BLEED FAIL / LEAK / OVERTEMP", "Typically indicates an upstream pneumatic/bleed issue impacting multiple air functions."),
        ]
        st.table(pd.DataFrame(patterns, columns=["Cue", "Operational meaning"]))
        st.markdown("_Source reference: POH 6-02 (controls/indications, CAS messages)._")

