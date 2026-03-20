import os

import pandas as pd
import streamlit as st
from PIL import Image


def _img(path: str, caption: str):
    if os.path.exists(path):
        st.image(Image.open(path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Missing image: `{path}`")


def _show_folder_images(folder: str, prefix: str, title: str, columns: int = 2):
    paths = []
    if os.path.isdir(folder):
        for name in os.listdir(folder):
            if name.lower().endswith(".png") and name.startswith(prefix):
                paths.append(os.path.join(folder, name))
    paths.sort()

    if not paths:
        st.info("No POH images found for this section yet.")
        return

    st.markdown(f"**{title}**")
    cols = st.columns(columns, gap="medium")
    for i, p in enumerate(paths):
        with cols[i % columns]:
            _img(p, os.path.basename(p))


def render_electrics():
    st.markdown("## Electrical System")
    st.caption("ATA 24 | Source: Phenom 300 POH (Section 6-04, Rev 14)")

    folder = "assets/electrics"

    with st.expander("**1. System overview**", expanded=True):
        st.markdown(
            """
**What this system does**
- Provides **28 VDC** electrical power to aircraft systems.
- Designed for **automatic** operation with low pilot workload.
- Built around **two independent DC channels** for fault isolation; **bus ties** can automatically connect networks if needed.

**Primary power sources**
- **Starter Generators 1/2 (SG1/SG2)**: normal primary sources.
- **Batteries 1/2**: backup sources (and support starts).
- **DC GPU**: ground power to energize the airplane on the ramp.

_Source: POH 6-04-00, 6-04-15 (Rev 14)._"""
        )

    with st.expander("**2. Conceptual model (how to think about it)**", expanded=False):
        st.markdown(
            """
Core concept: **two independent DC channels with automatic bus-tie logic**.

**Two DC channels (left/right)**
- In normal flight, each starter generator powers **its own network**.
- This keeps faults isolated (a problem on one side is less likely to take the other side down).

**BUS TIE (AUTO)**
- In AUTO, the airplane can **connect the networks** to keep essential buses powered when a source is lost.
- You’ll see this on the electrical synoptic as a change in which source feeds which bus.

**Emergency philosophy**
- If you lose the normal sources, the system goes into a **simplified emergency configuration**: fewer loads, longer endurance.
"""
        )

    with st.expander("**3. Controls (Electrical panel)**", expanded=False):
        st.markdown(
            """
**Left lateral console – Electrical panel**
- **GEN 1 / GEN 2 (AUTO / OFF)**: connects or isolates each starter generator from its DC bus.
- **GPU button (push in/out)**: connects GPU to the **Central Bus** when power quality is acceptable.
  - **GPU AVAIL** indicates the GPU is properly connected and within limits.
  - **IN USE** indicates GPU is actually powering the airplane.
- **BATT 1 / BATT 2 (ON / OFF)**:
  - BATT 1 ON connects Hot Batt Bus 1 to the **Emergency Bus**.
  - BATT 2 ON connects Hot Batt Bus 2 to the **Central Bus**.
- **ELEC EMER button**: forces electrical emergency configuration (batteries directly to Emergency Bus).
- **BUS TIE knob (1 OPEN / AUTO / 2 OPEN)**: isolates either side or allows automatic bus tie logic.

_Source: POH 6-04-05 (Rev 10/14)._"""
        )
        _img(f"{folder}/electrical_panel.png", "Electrical panel (controls & indications)")

    with st.expander("**4. Normal operation (what you should expect)**", expanded=False):
        st.markdown(
            """
**In flight (typical)**
- Each starter generator powers its **own DC bus** (split configuration).
- **SG2 also supplies the Central Bus** under normal conditions.
- Batteries are generally **charging** when generators/GPU are available.

**On the ramp**
- A **DC GPU** can power the **Central Bus** for preflight/servicing and can assist starting.
- After engine start, the associated **starter generator comes online automatically** (if GEN switch is in AUTO).

_Source: POH 6-04-15 (Rev 14)._"""
        )

    with st.expander("**5. Key numbers (quick lookup)**", expanded=False):
        st.markdown(
            """
**Starter generators**
- Continuous current capability: **330 A (ground)** / **390 A (flight)** each, at **28 VDC**.

**Batteries**
- Two lead-acid **24 VDC** batteries.
- Backup endurance for emergency loads: **up to 45 minutes** (dual generator failure).

**GPU (external power) – minimum specs**
- DC rectifier: **28.5 VDC**, nominal **600 A** (input 200–480 VAC, 25 kVA).
- Overload capability: **2000 A up to 2 seconds**.
- GPU AVAIL (power quality): **25–29 V**.

_Source: POH 6-04-15 (Rev 14)._"""
        )
        _img(f"{folder}/electrical_power_sources_overview.png", "Electrical power sources (SGs, batteries, GPU)")

    with st.expander("**6. Distribution concept (PDUs & buses)**", expanded=False):
        st.markdown(
            """
**Power Distribution Units (PDUs)**
- **LPDU / RPDU**: main distribution units (rear electronic bay).
- **EPDU**: emergency distribution (nose electronic bay).

**Buses you’ll see referenced**
- **DC BUS 1 / DC BUS 2**
- **Central Bus**
- **Emergency Bus**
- **Hot Batt Bus 1 / Hot Batt Bus 2**
- **Shed Bus 1 / Shed Bus 2**

**Shed buses (load shedding)**
- Shed buses are **non-essential loads** that can be removed automatically to protect essential buses and prevent overload.
- When electrical power is limited, it is normal to see **SHED BUS** indications change as loads are shed/restored.

_Source: POH 6-04-20 (Original/Rev 14)._"""
        )
        _img(
            f"{folder}/bus_configuration_sgen1_failed_inflight.png",
            "Example bus configuration (S/GEN 1 failed, inflight)",
        )

    with st.expander("**7. Typical reconfiguration scenarios (what to expect)**", expanded=False):
        st.markdown(
            """
The system is designed to **re-route power automatically**. Typical crew focus is:
- confirm **which source is feeding which bus** on the synoptic, and
- monitor for **overload / load shedding**.
"""
        )
        scenarios = [
            ("One generator lost", "Remaining generator + bus ties try to keep buses powered; watch for overload / shed buses."),
            ("Both generators lost", "Batteries become the main source; loads are reduced to stretch endurance (electrical emergency)."),
            ("GPU connected (ramp)", "GPU normally powers the Central Bus; batteries may charge; confirm GPU AVAIL / IN USE."),
            ("BUS TIE forced OPEN", "You are intentionally isolating sides; expect some buses/loads to go dark depending on sources."),
        ]
        st.table(pd.DataFrame(scenarios, columns=["Scenario", "What you should expect (concept)"]))
        st.markdown("_Use the electrical synoptic to verify the actual configuration._")

    with st.expander("**8. Common CAS messages (what they mean)**", expanded=False):
        rows = [
            ("ELEC EMERGENCY", "DC main buses de-energized; batteries discharging in electrical emergency."),
            ("ELEC XFR FAIL", "Automatic transfer to electrical emergency condition failed."),
            ("GEN 1 (2) OFF BUS", "Generator failure or GEN switch OFF; associated generator isolated."),
            ("GEN OVLD", "Remaining generator current above 330 A (ground) / 390 A (flight)."),
            ("BATT 1 (2) OFF BUS", "Associated battery isolated from electrical network."),
            ("BATT DISCHARGE", "At least one battery discharging during normal operation."),
            ("DC BUS 1 (2) OFF", "Associated DC bus is de-energized."),
            ("EMER BUS OFF", "Emergency Bus is de-energized."),
            ("GPU CONNECTED", "Ground power unit connected to the airplane."),
            ("SHED BUS OFF", "Shed bus is de-energized."),
        ]
        st.table(pd.DataFrame(rows, columns=["CAS message", "Meaning (summary)"]))
        st.markdown("_Source: POH 6-04-45 (Rev 10/14)._")

    with st.expander("**9. Where to look (fast)**", expanded=False):
        st.markdown(
            """
- **Electrical synoptic**: MFD (system overview, buses, voltages).
- **CAS messages**: both PFDs.
- **Switches**: Electrical panel (left lateral console).
"""
        )

    with st.expander("**10. Synoptic pages (POH)**", expanded=False):
        _show_folder_images(folder, "poh_6-04_synoptic_", "Electrical synoptic pages (MFD)")

    with st.expander("**11. System configurations (POH)**", expanded=False):
        st.markdown(
            """
This section includes the POH electrical system configuration pages that show how power is distributed with different source availability and failures.
"""
        )
        _show_folder_images(folder, "poh_6-04_config_", "Electrical system configurations", columns=2)

