import os

import pandas as pd
import streamlit as st
from PIL import Image

from content.render_helpers import back_to_top, cas_quick_reference, source_footer


def _img(path: str, caption: str):
    if os.path.exists(path):
        st.image(Image.open(path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Missing image: `{path}`")


def render_electrics():
    st.markdown("## Electrical System")
    st.caption("ATA 24 | Source: Phenom 300 POH (Section 6-04, Rev 14)")

    folder = "assets/electrics"

    with st.expander("**0. Big picture**", expanded=True):
        st.markdown(
            """
**28 VDC** powers the aircraft through **two independent DC channels** (left and right). In normal flight each **starter generator** feeds its own network; **bus ties** can connect the sides automatically when a source is lost.

| Source | Role |
|--------|------|
| **SG1 / SG2** | Primary power when engines are running |
| **Battery 1 / 2** | Backup; support starts and emergency loads |
| **DC GPU** | Ground power on the ramp |

**Where you see it:** **electrical synoptic** on the MFD; CAS on **both PFDs**; switches on the **electrical panel** (left console).

**Study focus:** split vs tied configuration; what changes with **one generator lost**, **both lost**, or **GPU** connected.
"""
        )

    with st.expander("**1. How power is distributed**", expanded=False):
        st.markdown(
            """
### Two channels

Each side has a **starter generator**, **DC bus**, and **power distribution unit (PDU)**. Normal flight keeps faults **isolated** — a problem on one side is less likely to take down the other.

### Buses you will see on the synoptic

- **DC BUS 1 / DC BUS 2** — main left/right networks
- **Central Bus** — normally fed by SG2; GPU connects here on the ground
- **Emergency Bus** — essential loads; batteries can feed it directly
- **Hot Batt Bus 1 / 2** — always connected to the physical batteries
- **Shed Bus 1 / 2** — non-essential loads the system can drop under stress

### Bus tie (AUTO)

In **AUTO**, the airplane **connects the networks** when needed so remaining sources can feed essential buses. Watch the synoptic after a generator failure — the diagram shows **who feeds whom**.

### Load shedding

When power is limited, **shed buses** drop non-essential equipment automatically to protect essential buses and avoid overload. **SHED BUS OFF** is often normal in a degraded configuration.

### Battery endurance

With **both generators lost**, batteries supply emergency loads for **up to 45 minutes** (design). Generator continuous limits → **Limitations → Electrical**.
"""
        )
        _img(f"{folder}/electrical_power_sources_overview.png", "Power sources — SGs, batteries, GPU (POH 6-04-15)")

    with st.expander("**2. Electrical panel**", expanded=False):
        st.markdown(
            """
### GEN 1 / GEN 2 (AUTO / OFF)

Connects or isolates each starter generator from its DC bus. **AUTO** is normal — the generator comes online after engine start.

### GPU (push in / out)

Connects external **DC GPU** to the **Central Bus** when voltage and quality are acceptable.

- **GPU AVAIL** — GPU connected and within limits
- **IN USE** — GPU is powering the airplane

### BATT 1 / BATT 2 (ON / OFF)

- **BATT 1 ON** — Hot Batt Bus 1 to **Emergency Bus**
- **BATT 2 ON** — Hot Batt Bus 2 to **Central Bus**

### ELEC EMER (pushbutton)

Forces **electrical emergency** configuration — batteries directly to Emergency Bus, reduced load set.

### BUS TIE (1 OPEN / AUTO / 2 OPEN)

- **AUTO** — automatic tie logic (normal)
- **1 OPEN** or **2 OPEN** — intentionally isolate one side

Cold-weather battery care → **Cold Weather** preflight.
"""
        )
        _img(f"{folder}/electrical_panel.png", "Electrical panel (POH 6-04-05)")

    with st.expander("**3. Normal operation**", expanded=False):
        st.markdown(
            """
### In flight

- Each starter generator powers **its own DC bus** (split configuration).
- **SG2** also supplies the **Central Bus** under normal conditions.
- Batteries **charge** when generators or GPU are available.

### On the ground

- **DC GPU** can power the **Central Bus** for preflight and can assist engine start.
- After start, the associated generator comes online automatically with GEN in **AUTO**.

External lights check sequence → **Airplane General → External walkround**.
"""
        )

    with st.expander("**4. When a source fails — what to expect**", expanded=False):
        st.markdown(
            """
The system **re-routes power automatically**. Your job is to read the **synoptic** and watch for **overload** or **shed buses**.


| Situation | What the system tries to do |
|-----------|----------------------------|
| **One generator lost** | Remaining generator + bus ties keep buses powered; watch **GEN OVLD** |
| **Both generators lost** | Batteries become main source; **ELEC EMERGENCY** logic; loads shed to extend endurance |
| **GPU on ramp** | Central Bus from GPU; confirm **GPU AVAIL** / **IN USE** |
| **BUS TIE forced OPEN** | Sides isolated — some buses may de-energize depending on available sources |

**GEN 1(2) OFF BUS** — generator not on the bus (failure or GEN switch OFF).

**BATT DISCHARGE** during normal operation — a battery is discharging when it should be charging.

**DC BUS 1(2) OFF** or **EMER BUS OFF** — that bus has no power.
"""
        )
        _img(
            f"{folder}/bus_configuration_sgen1_failed_inflight.png",
            "Example: S/GEN 1 failed in flight (POH configuration page)",
        )

    with st.expander("**5. Where to look**", expanded=False):
        st.markdown(
            """
- **MFD electrical synoptic** — buses, tie status, voltages, generator load
- **PFDs** — CAS messages
- **Electrical panel** — GEN, GPU, BATT, BUS TIE, ELEC EMER

Full POH configuration diagrams → **Documents** (POH §6-04).
"""
        )

    cas_quick_reference(
        [
            ("Emergency", "WARNING", "ELEC EMERGENCY", "DC main buses de-energized; batteries discharging in electrical emergency."),
            ("Emergency", "CAUTION", "ELEC XFR FAIL", "Automatic transfer to electrical emergency condition failed."),
            ("Generators", "CAUTION", "GEN 1 (2) OFF BUS", "Generator failure or GEN switch OFF; associated generator isolated."),
            ("Generators", "CAUTION", "GEN OVLD", "Remaining generator current above 330 A (ground) / 390 A (flight)."),
            ("Batteries", "CAUTION", "BATT 1 (2) OFF BUS", "Associated battery isolated from electrical network."),
            ("Batteries", "CAUTION", "BATT DISCHARGE", "At least one battery discharging during normal operation."),
            ("Buses", "CAUTION", "DC BUS 1 (2) OFF", "Associated DC bus is de-energized."),
            ("Buses", "CAUTION", "EMER BUS OFF", "Emergency Bus is de-energized."),
            ("Ground power", "ADVISORY", "GPU CONNECTED", "Ground power unit connected to the airplane."),
            ("Buses", "ADVISORY", "SHED BUS OFF", "Shed bus is de-energized."),
        ],
        title="6. CAS quick reference",
    )

    back_to_top()
    source_footer("poh", "§6-04 Electrics")
