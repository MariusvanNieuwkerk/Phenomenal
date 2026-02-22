import os

import pandas as pd
import streamlit as st
from PIL import Image


def _img(path: str, caption: str):
    if os.path.exists(path):
        st.image(Image.open(path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Missing image: `{path}`")


def render_ice_protection():
    st.markdown("## Ice and Rain Protection")
    st.caption("ATA 30 | Source: Phenom 300 POH (Section 6-11, Rev 12/6)")

    folder = "assets/ice_protection"

    with st.expander("**1. System overview (what’s protected)**", expanded=True):
        st.markdown(
            """
The ice and rain protection system is designed to prevent performance/handling degradation from ice and maintain visibility.

**Protected areas**
- **Wing & horizontal stabilizer leading edges** (thermal anti-ice using bleed air)
- **Engine inlets (lip)** (thermal anti-ice using engine bleed)
- **Windshields** (electrical heating + rain repellent coating)
- **Air data / stall probes** (electrical heating)
- **Wing inspection light** (left side) for night ice checks

_Source: POH 6-11-00 (Rev 6)._"""
        )
        _img(f"{folder}/ice_rain_protection_system_overview.png", "Ice and rain protection system (overview)")

    with st.expander("**2. Controls & indications (quick orientation)**", expanded=False):
        st.markdown(
            """
**Controls**
- Ice/rain protection control panel includes switches for:
  - **WINGSTAB** anti-ice
  - **ENG 1 / ENG 2** anti-ice
  - **WSHLD 1 / WSHLD 2** heating
  - **ADS PROBES** heating (OFF / AUTO / ON)
  - **ICE SPEED RESET** (after confirming no ice remains)

**Indications**
- Synoptic page on the **MFD** provides valve/flow status and legend symbology.

_Source: POH 6-11-05 (Rev 6)._"""
        )
        _img(f"{folder}/ice_protection_synoptic_mfd.png", "Ice & rain protection synoptic (MFD)")

    with st.expander("**3. Wing & stabilizer anti-ice (WHSAIS)**", expanded=False):
        st.markdown(
            """
**How it works**
- Uses bleed air and regulation logic to provide adequate thermal energy to the leading edges.
- System balances bleed temperature vs flow to keep leading edges effective without overheating.

**Ground inhibition**
- WHSAIS is inhibited on the ground when **wheel speed is below 40 kt** (overheat protection).

**Operational effect (important)**
- When **WINGSTAB** is ON, stall warning activation angles are adjusted and **stall warning speeds increase**.
- The CAS message **SWPS ICE SPEED** is displayed when WINGSTAB is ON.
- Use **ICE SPEED RESET** only when you’re sure there is **no more ice** on the airplane.

_Source: POH 6-11-10 (Rev 12)._"""
        )
        _img(
            f"{folder}/wingstab_antiice_airflow_control.png",
            "Wing & stabilizer anti-ice airflow/pressure/temperature control (schematic)",
        )

    with st.expander("**4. Engine anti-ice (nacelle lip + S/G inlet)**", expanded=False):
        st.markdown(
            """
**Purpose**
- Prevent/remove ice around the engine inlet cowls (lip).
- Also routes heat to the **starter/generator air inlet** region to prevent ice accumulation.

**Key components**
- Supply duct
- **EAI shutoff valve** (pressure-regulating shutoff valve)
- **Flow limiter (venturi)**
- Pressure transducer
- Piccolo tube (distributes hot air inside the inlet lip)
- Exhaust vent

**Behavior you should know**
- Each side is **independent**; bleed cannot be shared between engines.
- When ENG 1(2) anti-ice is ON, the **TT0 probe heater** is also turned ON.
- The valve is designed to **fail-safe open** in the absence of an electrical signal.

_Source: POH 6-11-10 (Rev 12) + 6-05-30._"""
        )
        _img(f"{folder}/engine_antiice_system.png", "Engine anti-ice system (schematic)")

    with st.expander("**5. Windshield heating (anti-ice / anti-fog)**", expanded=False):
        st.markdown(
            """
**What it does**
- Regulates temperature of heating mats embedded in each windshield to prevent:
  - **Ice on the outside**, and
  - **Fog on the inside**

**Normal control range**
- Controlled between **35°C and 43°C** (95–110°F).
- Overheat set point: **60°C** (140°F).

**Overheat / failure**
- Overheat removes power and triggers **WSHLD 1(2) HTR FAIL**.
- Reset requires cycling **both WSHLD switches** (system architecture dependency).

_Source: POH 6-11-10 (Rev 12) + 6-11-20._"""
        )
        _img(
            f"{folder}/windshield_heating_system_schematic.png",
            "Windshield heating system (schematic)",
        )

    with st.expander("**6. Windshield rain protection (wiperless)**", expanded=False):
        st.markdown(
            """
**Concept**
- A hydrophobic **Rain Repellent Coating (RRC)** on each windshield panel causes water to bead.
- Slipstream removes beads, leaving enough clear area for forward visibility.

**Practical note**
- The coating does not remain effective indefinitely; service life depends on environment and cleaning practices.
- Re-application kits are used when required.

_Source: POH 6-11-10 (Rev 12)._"""
        )

    with st.expander("**7. ADS probe heating (AUTO / ON logic)**", expanded=False):
        st.markdown(
            """
**What’s heated**
- Integrated Air Data & Stall Protection Probes (IASP / MFP)
- Standby pitot-static probe

**Normal position: AUTO**
- Heaters energize automatically when:
  - At least one engine is running, **or**
  - Airplane weight is **not on wheels**.

**ON (ground use)**
- Can be used on the ground to remove ice from probes before engine start.
- Can be used in flight if automatic control fails.

_Source: POH 6-11-10 (Rev 12)._"""
        )

    with st.expander("**8. CAS messages (quick meanings)**", expanded=False):
        rows = [
            ("ADS 1 (2) HTR FAIL", "Associated heater is off or failed."),
            ("STBY HTR FAIL", "Standby ADS heater is off or failed."),
            ("A-I E1 (2) FAIL", "Nacelle anti-ice valve closed when commanded open, or duct failure detected."),
            ("A-I E1 (2) FAULT", "Engine anti-ice valve failed when commanded to close."),
            ("A-I E1 (2) ON", "Engine anti-ice is ON and operating normally."),
            ("A-I LO CAPACITY", "Not enough thermal energy available for wing/stab anti-ice operation."),
            ("A-I WINGSTB INHB", "WINGSTAB commanded ON outside operational envelope."),
            ("A-I WINGSTB LEAK", "Hot bleed air leak in wing/stab anti-ice ducting."),
            ("A-I WINGSTB FAIL", "Wing/stab anti-ice failure (or significant thrust lever asymmetry)."),
            ("A-I WINGSTB ARM", "WINGSTAB commanded ON prior to takeoff / certain conditions."),
            ("A-I WINGSTB ON", "Wing/stab anti-ice is ON and operating normally."),
            ("ICE CONDITION", "Ice detector indicates icing conditions (optional equipment)."),
            ("ICE DET FAIL", "Ice detector failed (optional equipment)."),
            ("WSHLD 1 (2) HTR FAIL", "Windshield overheated or heating system failed."),
            ("ADS HTR SW ON", "ADS probes knob is ON."),
        ]
        st.table(pd.DataFrame(rows, columns=["CAS message", "Meaning (summary)"]))
        st.markdown("_Source: POH 6-11-20 (Rev 6)._")

