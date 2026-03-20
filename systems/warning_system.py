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


def render_warning_system():
    st.markdown("## Warning System (CAS and checks)")
    st.caption("ATA 31 | Source: Phenom 300 POH (Section 6-14, Rev 12)")

    folder = "assets/warning_system"

    with st.expander("**1. Overview**", expanded=True):
        st.markdown(
            """
This section focuses on the airplane’s alerting and warning philosophy:
- **CAS message display and prioritization**
- **Configuration warnings / checks** (e.g., takeoff configuration check)
- System test functions and cutouts (where applicable)

This module intentionally avoids detailed avionics functions (e.g., TAWS/TCAS pages), per your preference.
"""
        )

    with st.expander("**2. CAS messages (how to interpret quickly)**", expanded=False):
        st.markdown(
            """
Practical CAS scan technique:
- Identify **severity/level** first (what must be handled immediately vs monitored).
- Determine **system context** (which ATA/system is affected).
- Cross-check **synoptic/indications** to confirm the actual state.

Use the QRH/AFM for memory items and required actions.
"""
        )
        quick = [
            ("Level", "Treat level/priority as the urgency cue; then confirm with indications."),
            ("Context", "Tie the CAS to a system page (synoptic) when available."),
            ("Trend", "Monitor whether the message clears, latches, or escalates."),
        ]
        st.table(pd.DataFrame(quick, columns=["Focus", "What to do"]))

    with st.expander("**3. Takeoff configuration / stall warning controls**", expanded=False):
        st.markdown(
            """
Study items in this area typically include:
- What the **takeoff configuration check** verifies
- What conditions can trigger a takeoff configuration warning
- What the **stall warning cutout** does and when it is permitted/used
"""
        )

    with st.expander("**4. POH extracts**", expanded=False):
        _show_poh_images(folder, "poh_6-14_synoptic_", "POH synoptic pages (Warning System)")
        st.markdown("_If no synoptic images were detected automatically, we can extract additional POH pages for this section._")

