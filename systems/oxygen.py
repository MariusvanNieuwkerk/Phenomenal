"""Oxygen — crew and passenger supplemental O₂ (ATA 35)."""

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
        return
    st.markdown(f"**{title}**")
    cols = st.columns(2, gap="medium")
    for i, p in enumerate(paths):
        with cols[i % 2]:
            _img(p, os.path.basename(p))

def render_oxygen():
    st.markdown("## Oxygen")
    st.caption("ATA 35 · Crew & passenger O₂ · POH §6-13")

    folder = "assets/oxygen"

    with st.expander("**1. How it works**", expanded=True):
        st.markdown(
            """
Oxygen is supplemental — for smoke, fire, fumes, depressurization, and hypoxia. **Flight crew** use quick-don masks stowed at each seat; **passengers** get drop-down masks deployed automatically when cabin altitude climbs too high. Cylinder pressure shows on the MFD oxygen synoptic.

| User | Supply | When it matters |
|------|--------|-----------------|
| **Flight crew** | Quick-don masks in stowage | Smoke/fire/fumes, depressurization, hypoxia |
| **Passengers** | Drop-down masks (cabin system) | Cabin altitude high / depressurization |
"""
        )

    with st.expander("**2. Controls & indications**", expanded=False):
        st.markdown(
            """
### Crew interface

- **OXYGEN control panel** — supply control, crew mask selectors
- **Mask stowage boxes** — EMERGENCY vs NORMAL dilution (smoke: EMERGENCY + dilution CLOSED)
- **MFD synoptic** — cylinder pressure / system status

### Passenger system

- **SUPPLY CONTROL** — typically **PAX AUTO** for normal ops
- Automatic deployment when cabin altitude exceeds threshold (logic per POH)
"""
        )
        _show_poh_images(folder, "poh_6-13_synoptic_", "POH synoptic pages (Oxygen)")

    with st.expander("**3. Crew masks — operational**", expanded=False):
        st.markdown(
            """
### Smoke / fumes / fire

- **DON**, selector **EMERGENCY**, **dilution CLOSED**, smoke goggles as required
- Establish communication (mic on mask or interphone per POH)

### Depressurization

- **DON**, **100%** oxygen
- Descend to 10,000 ft or MEA — **CAB ALTITUDE HI** / **EMERGENCY DESCENT** memory items

**Fit and flow** — mask seal, positive pressure, verify flow indicator.
"""
        )

    with st.expander("**4. Passenger oxygen**", expanded=False):
        st.markdown(
            """
**Deployment** — masks drop when cabin altitude logic commands (or manual per QRH).

### PAX briefing essentials

- Pull mask firmly to start flow
- Fit over nose and mouth
- Normal breathing — bag may not fully inflate
- Secure own mask before helping others

**PAX OXY NO PRES** — masks may not have deployed when required; crew action per QRH.
"""
        )

    cas_quick_reference(
        [
            ("Crew O₂", "CAUTION", "OXY LO PRES", "Cylinder low, sensor fault, or supply handle pulled — check before dispatch."),
            ("Passenger O₂", "CAUTION", "PAX OXY NO PRES", "Passenger masks not deployed in depressurization condition."),
            ("Controls", "ADVISORY", "OXY SW NOT AUTO", "SUPPLY CONTROL not in PAX AUTO."),
        ],
        title="5. CAS quick reference",
    )

    back_to_top()
    source_footer("poh", "§6-13 Oxygen · Memory Items (masks)")
