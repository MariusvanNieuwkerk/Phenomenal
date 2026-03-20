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


def render_oxygen():
    st.markdown("## Oxygen")
    st.caption("ATA 35 | Source: Phenom 300 POH (Section 6-13, Rev 14)")

    folder = "assets/oxygen"

    with st.expander("**1. Overview**", expanded=True):
        st.markdown(
            """
The oxygen system provides supplemental oxygen to:
- **Flight crew** via dedicated crew masks, and
- **Passengers** via passenger oxygen masks (deployment per system design/procedures).

Study goal: know **where to see oxygen quantity/pressure**, how masks are selected/used, and the major operational modes.
"""
        )

    with st.expander("**2. Controls & indications**", expanded=False):
        st.markdown(
            """
Primary references in the POH:
- **Oxygen control panel** (crew interface)
- **Mask stowage boxes** and mask operating modes
- **MFD synoptic page** for system status/quantity indication
"""
        )
        _show_poh_images(folder, "poh_6-13_synoptic_", "POH synoptic pages (Oxygen)")

    with st.expander("**3. Crew masks (operational concepts)**", expanded=False):
        st.markdown(
            """
For flight crew masks, focus on:
- Selecting the correct operating mode for the situation
- Establishing communication while on oxygen
- Ensuring oxygen flow and mask fit are correct

Use the POH/QRH for the exact steps and limitations for the specific mask type installed.
"""
        )

    with st.expander("**4. Passenger oxygen (operational concepts)**", expanded=False):
        st.markdown(
            """
For passenger oxygen, focus on:
- How/when masks are made available or deployed
- How passengers should be briefed for correct mask use

In training, tie this back to cabin altitude events and associated procedures.
"""
        )

    with st.expander("**5. Quick lookup (study prompts)**", expanded=False):
        prompts = [
            ("Where to look", "MFD oxygen synoptic + panel indication for quantity/pressure (per POH)."),
            ("Mask use", "Know crew mask modes and how to maintain comms on oxygen."),
            ("Briefing", "Passenger briefing essentials (fit, pull to start flow, normal breathing)."),
        ]
        st.table(pd.DataFrame(prompts, columns=["Topic", "What to know"]))

    with st.expander("**6. CAS messages (POH quick reference)**", expanded=False):
        rows = [
            ("CAUTION", "OXY LO PRES", "Oxygen cylinder pressure is below dispatch safety limit, pressure sensor failed, or OXYGEN SUPPLY handle is pulled."),
            ("CAUTION", "PAX OXY NO PRES", "Passenger masks not deployed in a cabin depressurization condition (availability depends on configuration)."),
            ("ADVISORY", "OXY SW NOT AUTO", "SUPPLY CONTROL knob not in PAX AUTO position."),
        ]
        st.table(pd.DataFrame(rows, columns=["Type", "Message", "Meaning"]))
        st.markdown("_Source: POH 6-13-20 (Original)._")

