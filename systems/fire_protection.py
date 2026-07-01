"""Fire Protection — detection, shutoff, extinguishing (ATA 26)."""

import os

import streamlit as st
from PIL import Image

from content.render_helpers import back_to_top, cas_quick_reference, source_footer


def _img(path: str, caption: str):
    if os.path.exists(path):
        st.image(Image.open(path), caption=caption, use_container_width=True)


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
    st.caption("ATA 26 · Engine & baggage fire · POH §6-06")

    folder = "assets/fire_protection"

    with st.expander("**1. Big picture**", expanded=True):
        st.markdown(
            """
| Layer | Function |
|-------|----------|
| **Detection** | Sensors + logic → CAS WARNING/CAUTION |
| **Isolation** | Fire handles / shutoff buttons → fuel, hydraulics, bleed |
| **Extinguishing** | Fire bottles → agent to engine nacelle or baggage zone |

**Pilot goal:** detect early, isolate the affected zone, discharge if required — follow **QRH** and **Memory Items** for engine fire.
"""
        )

    with st.expander("**2. Engine fire — crew interface**", expanded=False):
        st.markdown(
            """
### Typical sequence (concept — use QRH for exact steps):


1. **THRUST lever** — IDLE (affected engine)
2. **START/STOP** — STOP
3. **FIRE SHUTOFF** — PUSH IN (isolates fuel/hyd/bleed paths per design)
4. If fire persists (~30 s): **BOTTLE** — DISCH

**Memory Items:** *E1(2) FIRE*, *ENGINE FIRE SEVERE DAMAGE OR SEPARATION* — see **Memory Items**.

**Hydraulics link:** FIRE SHUTOFF also closes **FSOVs** (see **Hydraulics**).
"""
        )

    with st.expander("**3. Baggage compartment smoke**", expanded=False):
        st.markdown(
            """
**BAG SMK** WARNING — smoke detected in baggage compartment.

- Confirm indication; consider diversion and landing.
- Follow QRH for smoke/fire/fumes if smoke enters cabin (**Memory Items**).

Detection faults: **BAG SMK FAIL** (two detectors failed) or **BAG SMK FAULT** (one detector).
"""
        )

    cas_quick_reference(
        [
            ("Baggage", "WARNING", "BAG SMK", "Smoke in baggage compartment — immediate action."),
            ("Engine", "CAUTION", "E1 (2) FIRE DET FAIL", "Engine fire detection inoperative for that engine."),
            ("Engine", "CAUTION", "E1 (2) FIREX FAIL", "Engine fire extinguisher system failed."),
            ("Baggage", "CAUTION", "BAG SMK FAIL", "Both baggage smoke detectors failed."),
            ("Engine", "CAUTION", "ENG FIREX DISCH", "Bottle already discharged — no second shot on same bottle."),
            ("Baggage", "ADVISORY", "BAG SMK FAULT", "One baggage smoke detector failed."),
        ],
        title="4. CAS quick reference",
    )

    with st.expander("**5. What shutoff isolates (study model)**", expanded=False):
        st.markdown(
            """
When you push **FIRE SHUTOFF** or use the fire handle, think in terms of:

- **Fuel** — stop feeding the fire
- **Hydraulics** — FSOV closes (that engine's pump circuit)
- **Bleed / pneumatics** — isolate engine bleed

Cross-check indications and synoptic after each action.
"""
        )

    with st.expander("**6. POH extracts**", expanded=False):
        _show_poh_images(folder, "poh_6-06_synoptic_", "POH synoptic pages (Fire Protection)")

    back_to_top()
    source_footer("poh", "§6-06 Fire Protection · QRH engine fire memory items")
