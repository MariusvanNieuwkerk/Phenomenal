import os

import streamlit as st
from PIL import Image

from content.render_helpers import back_to_top, cas_quick_reference, source_footer


def _img(path: str, caption: str):
    if os.path.exists(path):
        st.image(Image.open(path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Missing image: `{path}`")


def render_ice_protection():
    st.markdown("## Ice and Rain Protection")
    st.caption("ATA 30 | Source: Phenom 300 POH (Section 6-11, Rev 12/6)")

    folder = "assets/ice_protection"

    with st.expander("**0. How it works**", expanded=True):
        st.markdown(
            """
Ice and rain protection keeps **performance**, **handling**, and **visibility** acceptable in icing and precipitation.

| Area | Method | Energy source |
|------|--------|---------------|
| **Wing & stab leading edges** | Hot **bleed air** | Engine bleed — reduces available thrust |
| **Engine inlet lips** | Hot **bleed air** | Engine bleed — independent per side |
| **Windshields** | **Electrical** heating | Electrical — lower engine impact |
| **ADS / stall probes** | **Electrical** heating | AUTO or ON |
| **Rain** | Hydrophobic **coating** on windshields | No power — limited service life |
"""
        )
        _img(f"{folder}/ice_rain_protection_system_overview.png", "Ice and rain protection overview (POH 6-11-00)")

    with st.expander("**1. Wing & stabilizer anti-ice (WINGSTAB)**", expanded=False):
        st.markdown(
            """
### How it works

Hot **bleed air** is regulated to the wing and horizontal stabilizer leading edges. The system balances temperature and flow to heat the surfaces without overheating.

### Ground inhibition

**WINGSTAB** is inhibited on the ground when **wheel speed < 40 kt** — overheat protection.

### Operational effect (important)

With **WINGSTAB ON**, stall warning logic changes — activation speeds **increase**. You will see **SWPS ICE SPEED** or **ICE SPEED** related cues.

Use **ICE SPEED RESET** only when you are sure **no ice remains** on the aircraft.

### Messages


| Cue | Meaning |
|-----|---------|
| **A-I WINGSTB ON / ARM** | System active or armed for takeoff |
| **A-I LO CAPACITY** | Not enough thermal energy for wing/stab anti-ice |
| **A-I WINGSTB INHB** | Commanded ON outside operational envelope |
| **A-I WINGSTB LEAK / FAIL** | Duct leak or system fault |

→ **Flight Controls → SWPS** for stick shaker / pusher interaction.
"""
        )
        _img(
            f"{folder}/wingstab_antiice_airflow_control.png",
            "Wing/stab anti-ice airflow control (POH 6-11-10)",
        )

    with st.expander("**2. Engine anti-ice (nacelle lip)**", expanded=False):
        st.markdown(
            """
### Purpose

Prevents ice on the **engine inlet cowl** and heats the **starter/generator air inlet** region.

### Behaviour

- Each side is **independent** — bleed cannot be shared between engines.
- When **ENG 1(2) anti-ice** is ON, the **TT0 probe heater** on that side is also ON (see **Powerplant → TT0**).
- The **EAI shutoff valve** is designed to **fail-safe open** without electrical signal.

**A-I E1(2) ON** — normal operation. **FAIL / FAULT** — valve or duct problem.
"""
        )
        _img(f"{folder}/engine_antiice_system.png", "Engine anti-ice schematic (POH 6-11-10)")

    with st.expander("**3. Windshield heat & rain**", expanded=False):
        st.markdown(
            """
### Windshield heating

Embedded mats heat each windshield to prevent **external ice** and **internal fog**.

- Normal control band: **35–43°C**
- Overheat trip: **60°C** → **WSHLD 1(2) HTR FAIL**; reset by cycling **both** WSHLD switches

### Rain protection

**Rain Repellent Coating (RRC)** makes water bead; slipstream clears the view. Coating wears with time and cleaning — not unlimited.

Use **WSHLD heat** when visibility drops in rain or icing.
"""
        )
        _img(
            f"{folder}/windshield_heating_system_schematic.png",
            "Windshield heating schematic (POH 6-11-10)",
        )

    with st.expander("**4. ADS probe heating**", expanded=False):
        st.markdown(
            """
Heated probes: **integrated air data & stall probes (IASP/MFP)** and **standby pitot-static probe**.

### AUTO (normal)

Heaters energize when at least one engine is running **or** the aircraft is **airborne** (not on wheels).

### ON

- On the ground before start — remove ice from probes
- In flight if automatic control fails

**ADS 1(2) HTR FAIL** or **STBY HTR FAIL** — associated heater off or failed.
"""
        )

    with st.expander("**5. Ice protection panel & synoptic**", expanded=False):
        st.markdown(
            """
### Switches

- **WINGSTAB** anti-ice
- **ENG 1 / ENG 2** anti-ice
- **WSHLD 1 / WSHLD 2** heat
- **ADS PROBES** — OFF / AUTO / ON
- **ICE SPEED RESET**

### When to use what (concept)


| Situation | Action |
|-----------|--------|
| Visible moisture + cold | **ENG anti-ice** early |
| Icing on wings or in icing conditions | **WINGSTAB** per procedures |
| Probes iced before start | **ADS PROBES ON** on ground |
| Reduced visibility in rain/ice | **WSHLD** heat |

**MFD synoptic** shows valve/flow status and legend symbology.
"""
        )
        _img(f"{folder}/ice_protection_synoptic_mfd.png", "Ice & rain synoptic (MFD)")

    cas_quick_reference(
        [
            ("ADS probes", "CAUTION", "ADS 1 (2) HTR FAIL", "Associated heater is off or failed."),
            ("ADS probes", "CAUTION", "STBY HTR FAIL", "Standby ADS heater is off or failed."),
            ("Engine A-I", "CAUTION", "A-I E1 (2) FAIL", "Nacelle anti-ice valve closed when commanded open, or duct failure."),
            ("Engine A-I", "CAUTION", "A-I E1 (2) FAULT", "Engine anti-ice valve failed when commanded to close."),
            ("Engine A-I", "ADVISORY", "A-I E1 (2) ON", "Engine anti-ice is ON and operating normally."),
            ("Wing/stab A-I", "CAUTION", "A-I LO CAPACITY", "Not enough thermal energy for wing/stab anti-ice."),
            ("Wing/stab A-I", "ADVISORY", "A-I WINGSTB INHB", "WINGSTAB commanded ON outside operational envelope."),
            ("Wing/stab A-I", "CAUTION", "A-I WINGSTB LEAK", "Hot bleed air leak in wing/stab anti-ice ducting."),
            ("Wing/stab A-I", "CAUTION", "A-I WINGSTB FAIL", "Wing/stab anti-ice failure or thrust lever asymmetry."),
            ("Wing/stab A-I", "ADVISORY", "A-I WINGSTB ARM", "WINGSTAB commanded ON prior to takeoff / certain conditions."),
            ("Wing/stab A-I", "ADVISORY", "A-I WINGSTB ON", "Wing/stab anti-ice is ON and operating normally."),
            ("Detection", "ADVISORY", "ICE CONDITION", "Ice detector indicates icing conditions (optional)."),
            ("Detection", "CAUTION", "ICE DET FAIL", "Ice detector failed (optional)."),
            ("Windshield", "CAUTION", "WSHLD 1 (2) HTR FAIL", "Windshield overheated or heating system failed."),
            ("ADS probes", "ADVISORY", "ADS HTR SW ON", "ADS probes knob is ON."),
        ],
        title="6. CAS quick reference",
    )

    back_to_top()
    source_footer("poh", "§6-11 Ice Protection · Flight Controls (SWPS ICE SPEED)")
