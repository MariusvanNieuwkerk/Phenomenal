import os

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


def render_airplane_general():
    st.markdown("## Airplane General")
    st.caption("ATA 06 | Source: Phenom 300 POH (Section 6-01, Rev 13)")

    folder = "assets/airplane_general"

    with st.expander("**1. What this section is (and is not)**", expanded=True):
        st.markdown(
            """
Section 6-01 is a reference for:
- Aircraft basic data and dimensions
- Cockpit/cabin general layout and philosophy
- General arrangements and common references

For study purposes, this is most useful as a fast reference for **layout**, **locations**, and **where to find indications**.
"""
        )

    with st.expander("**2. POH extracts / synoptic pages**", expanded=False):
        _show_poh_images(folder, "poh_6-01_synoptic_", "POH pages detected as synoptic references (6-01)")
        st.markdown("_If this section includes avionics-specific pages, we can keep the focus on airframe/general references._")

