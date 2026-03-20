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
    for p in paths:
        _img(p, os.path.basename(p))


def render_fire_protection():
    st.markdown("## Fire Protection")
    st.caption("ATA 26 | Source: Phenom 300 POH (Section 6-06, Rev 6)")

    folder = "assets/fire_protection"

    with st.expander("**1. Overview**", expanded=True):
        st.markdown(
            """
The fire protection system provides:
- **Detection** (sensors/logic) for engine fire conditions.
- **Crew alerting** via CAS and panel indications.
- **Extinguishing capability** via dedicated fire bottles (per POH configuration).

The operational intent is rapid identification and a clear crew interface to isolate the affected engine and discharge extinguishing agent as required.
"""
        )

    with st.expander("**2. Controls & indications (crew interface)**", expanded=False):
        st.markdown(
            """
You interact with fire protection primarily through:
- The **engine fire protection control panel** (fire handles/buttons, discharge).
- **CAS messages** and associated annunciations.

Use the QRH/AFM procedures for specific actions.
"""
        )

    with st.expander("**3. System logic (conceptual)**", expanded=False):
        st.markdown(
            """
At a high level:
- **Detection** drives alerting.
- **Fire shutoff** isolates fuel/hydraulic/bleed paths per system design.
- **Extinguishing** provides agent discharge to the affected zone.

For studying: focus on what each crew action isolates (fuel, bleed, electrics/hydraulics as applicable) and what indications confirm the commanded state.
"""
        )

    with st.expander("**4. CAS messages (POH quick reference)**", expanded=False):
        rows = [
            ("WARNING", "BAG SMK", "Smoke detected in baggage compartment."),
            ("CAUTION", "E1 (2) FIRE DET FAIL", "Engine fire detection system has failed."),
            ("CAUTION", "E1 (2) FIREX FAIL", "Engine fire extinguisher system has failed."),
            ("CAUTION", "BAG SMK FAIL", "Two baggage compartment smoke detectors have failed."),
            ("CAUTION", "ENG FIREX DISCH", "Engine fire-extinguisher bottle has been discharged."),
            ("ADVISORY", "BAG SMK FAULT", "One baggage compartment smoke detector has failed."),
        ]
        st.table(pd.DataFrame(rows, columns=["Type", "Message", "Meaning"]))
        st.markdown("_Source: POH 6-06-35 (Rev 6)._")

    with st.expander("**5. POH extracts**", expanded=False):
        _show_poh_images(folder, "poh_6-06_synoptic_", "POH synoptic pages (Fire Protection)")
        st.markdown("_If no synoptic images were detected automatically, we can extract additional POH pages for this section._")

