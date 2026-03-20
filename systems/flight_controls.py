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


def render_flight_controls():
    st.markdown("## Flight Controls")
    st.caption("ATA 27 | Source: Phenom 300 POH (Section 6-07, Rev 8)")

    folder = "assets/flight_controls"

    with st.expander("**1. Overview (what’s included)**", expanded=True):
        st.markdown(
            """
The Flight Control System includes primary and secondary flight control systems and their associated components.

**Primary flight controls**
- **Ailerons** (roll)
- **Elevators** (pitch)
- **Rudder** (yaw)

**Cockpit controls**
- Control wheels provide roll and pitch control; rudder pedals provide yaw control.
- Controls are duplicated and mechanically interconnected; either pilot station can control the primary surfaces.
- Ailerons, elevators, and rudder are driven by **conventional control cables** to the bellcranks.

**AFCS interaction**
- The Automatic Flight Control System can command primary control surfaces through **electromechanical servo actuators** interfacing with the flight control system.

**Secondary flight controls**
- **Aileron and rudder trim tabs**
- **Elevator tab and movable horizontal stabilizer surface**
- **Flaps**
- **Spoilers** (electrically commanded, hydraulically actuated)

_Source: POH 6-07-00 (Rev 8), Introduction._
"""
        )

    with st.expander("**2. Controls & indications (high level)**", expanded=False):
        st.markdown(
            """
Key controls and indications referenced in the POH include:
- Control wheel / control column functions
- Flap selector lever and flap indication
- Trim panel and trim indication
- Speedbrake control and spoiler/speedbrake indications (MFD)
"""
        )

    with st.expander("**3. Normal use (what you should expect)**", expanded=False):
        st.markdown(
            """
Practical expectations in normal operation:
- Flap and trim indications provide immediate confirmation of commanded position.
- Trim changes should be reflected on the trim indicator and in handling response.
- Speedbrake use should be verified by indication (avoid “blind” deployment).
"""
        )

    with st.expander("**4. Quick lookup (study prompts)**", expanded=False):
        prompts = [
            ("Trim", "Where is trim commanded, and how do you verify it? What are the limits and protections?"),
            ("Flaps", "What is the normal callout/sequence for flap changes? Where do you see confirmation?"),
            ("Speedbrake", "What are the operational constraints and typical use cases?"),
        ]
        st.table(pd.DataFrame(prompts, columns=["Topic", "Key questions"]))

    with st.expander("**5. CAS messages (POH quick reference)**", expanded=False):
        rows = [
            ("CAUTION", "FLAP FAIL", "Flap control system is inoperative or jammed; flaps cannot move."),
            ("CAUTION", "GND SPLR FAIL", "Loss of ground spoilers function (spoilers failed to extend or unavailable as ground spoilers)."),
            ("CAUTION", "PTRIM BKP FAIL", "Pitch trim backup function is no longer available."),
            ("CAUTION", "PTRIM NML FAIL", "Pitch trim normal function is no longer available."),
            ("CAUTION", "RUD GUST LOCKED", "Rudder gust lock is not retracted."),
            ("CAUTION", "RUD OVERBOOST", "Spring-loaded rudder booster uncommanded actuation."),
        ]
        st.table(pd.DataFrame(rows, columns=["Type", "Message", "Meaning"]))
        st.markdown("_Source: POH 6-07-35 (Rev 9)._")

    with st.expander("**6. POH extracts**", expanded=False):
        _show_poh_images(folder, "poh_6-07_synoptic_", "POH synoptic pages (Flight Controls)")
        st.markdown("_If no synoptic images were detected automatically, we can extract additional POH pages for this section._")

