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


def render_fuel():
    st.markdown("## Fuel System")
    st.caption("ATA 28 | Source: Phenom 300 POH (Section 6-09, Rev 12)")

    folder = "assets/fuel"

    with st.expander("**0. Big picture**", expanded=True):
        st.markdown(
            """
Two **integral wing tanks** (left and right) store fuel and feed **two independent engine lines**.

| Element | Role |
|---------|------|
| **Collector tank** | Keeps the pickup submerged for a steady feed |
| **Ejector (jet) pump** | Primary feed — no moving parts, driven by engine motive flow |
| **Electric boost pump** | Start, crossfeed, and backup when primary pressure is low |
| **EFCU** | Commands boost pumps in **AUTO**; processes quantity and alerts |

**Where you see it:** fuel synoptic and fuel data on the **MFD**; messages on **both PFDs**.

**Study focus:** normal feed vs when the electric pump runs; **XFEED LO1/LO2**; difference between **quantity**, **pressure**, and **feed fault** messages.

Numeric limits → **Limitations → Fuel**.
"""
        )

    with st.expander("**1. How fuel reaches the engine**", expanded=False):
        st.markdown(
            """
### Normal flight

Each engine is fed from **its own wing tank**. Fuel flows from the main tank into a **collector tank**, then to the engine through an **ejector pump** — a venturi driven by high-pressure fuel from the engine fuel system. No electric motor in normal cruise.

A **scavenge jet pump** keeps the collector tank filled during manoeuvres.

### When the electric boost pump runs

The **EFCU** turns the boost pump on when it is needed:

- **Engine start**
- **Crossfeed (XFEED)**
- **Primary feed pressure is low** — you may see **FUEL 1(2) FEED FAULT** as the system reacts

With the pump selector in **AUTO** (normal), you do not command this manually.

### Pump electrical sources (asymmetric by design)

- **Pump 1 (left)** — **Emergency Bus**
- **Pump 2 (right)** — **DC BUS 2**

### Independence

Left and right feed systems are **separate**. Closing one engine **fuel shutoff** (fire handle) does not starve the other engine.

**Engine-side fuel** (FMU, nozzles) → **Powerplant → Engine fuel system**.
"""
        )
        _img(f"{folder}/fuel_tanks_location.png", "Fuel tanks — main, surge, and collector (POH 6-09-10)")

    with st.expander("**2. Fuel panel controls**", expanded=False):
        st.markdown(
            """
### Fuel pump selector (one per side)


| Position | What it does |
|----------|--------------|
| **AUTO** | EFCU runs the boost pump when required — normal |
| **ON** | Boost pump runs continuously |
| **OFF** | Boost pump disabled |

### Crossfeed (XFEED)


| Position | What it does |
|----------|--------------|
| **LO1** | Opens crossfeed and runs **Pump 2** — both engines fed from the **right** tank |
| **OFF** | Crossfeed closed — each engine from its own tank |
| **LO2** | Opens crossfeed and runs **Pump 1** — both engines fed from the **left** tank |

**Do not use crossfeed during takeoff and landing.**

When XFEED is open, the **feeding** tank should decrease faster than the other. **FUEL EQUAL** (advisory) means lateral difference is small with XFEED open.
"""
        )
        _img(f"{folder}/fuel_control_panel.png", "Fuel control panel (POH 6-09-05)")

    with st.expander("**3. Indications & synoptic**", expanded=False):
        st.markdown(
            """
### Quantity

- **Capacitive** probes in each tank — no pilot calibration.
- Each tank has its own **EFCU** channel. If one tank quantity fails, **total** quantity is also removed.

### Fuel temperature

- Measured in the **right collector tank**.
- Display range: **> -37°C (-34°F)** and **< 80°C (176°F)**.

### MFD fuel synoptic

- Total remaining / total used
- Left and right tank quantities
- Electric pump status (ON / OFF / FAILED)
- Crossfeed valve (OPEN / CLOSED)

### Alerts you should distinguish


| Message type | What it reflects |
|--------------|------------------|
| **LO LEVEL** | Quantity — about **140 kg (310 lb)** left in that tank |
| **LO PRES** | **Pressure** to the engine while it is running — not the same as low quantity |
| **FEED FAULT** | Primary (ejector) feed pressure low — EFCU typically commands the boost pump |
| **IMBALANCE** | Lateral difference ≥ **100 kg (220 lb)**; clears at ≤ **40 kg (88 lb)** |
"""
        )
        _img(f"{folder}/fuel_synoptic_mfd.png", "Fuel synoptic (MFD)")

    with st.expander("**4. Fuel shutoff & fire protection**", expanded=False):
        st.markdown(
            """
Each wing feed line has a **fuel shutoff valve** — **normally open**.

Only the fire-panel **FIRE SHUTOFF** pushbutton closes it. That stops fuel to the affected engine and is part of fire isolation (see **Fire Protection**).

**FUEL 1(2) SOV FAIL** means the commanded and actual shutoff valve position do not agree.
"""
        )

    with st.expander("**5. Fleet note — spurious fuel CAS at power-up (FOL 001/14)**", expanded=False):
        st.markdown(
            """
**FUEL PUMP FAIL** or other fuel CAS right after loading the nav database into the **lower** MFD SD card slot.

Load the navigation database **only** in the **top** MFD slot (spare card). See **RNAV / RNP Approaches → Database updates**.
"""
        )

    cas_quick_reference(
        [
            ("Quantity", "CAUTION", "FUEL 1 (2) LO LEVEL", "Low-level sensors: 140 kg (310 lb) remains in that tank."),
            ("Pressure", "CAUTION", "FUEL 1 (2) LO PRES", "Low pressure to associated engine while engine is running."),
            ("Shutoff", "CAUTION", "FUEL 1 (2) SOV FAIL", "Mismatch between commanded and actual shutoff valve status."),
            ("Balance", "ADVISORY", "FUEL IMBALANCE", "Imbalance ≥ 100 kg (220 lb); clears when reduced to 40 kg (88 lb)."),
            ("Crossfeed", "CAUTION", "FUEL XFEED FAIL", "Mismatch between commanded and actual crossfeed valve status."),
            ("Pumps", "CAUTION", "FUEL PUMP 1 (2) FAIL", "Mismatch between commanded/actual pump status or pump failure."),
            ("Feed", "CAUTION", "FUEL 1 (2) FEED FAULT", "Primary feed low pressure → DC pump activates."),
            ("Servicing", "ADVISORY", "DOOR REFUEL OPEN", "Refuel panel door open; must be closed before takeoff."),
            ("Crossfeed", "ADVISORY", "FUEL EQUAL", "With XFEED open: lateral fuel difference < 20 kg (44 lb)."),
        ],
        title="6. CAS quick reference",
    )

    back_to_top()
    source_footer("poh", "§6-09 Fuel")
