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


def render_air_management():
    st.markdown("## Air Management System (Bleed, ECS, Pressurization)")
    st.caption("ATA 21 | Source: Phenom 300 POH (Section 6-02, Rev 6)")

    folder = "assets/air_management"
    press_folder = "assets/pressurization"

    with st.expander("**0. Big picture**", expanded=True):
        st.markdown(
            """
The Air Management System delivers **conditioned bleed air** for the cabin and **pressurization**, and supplies **bleed** for **wing/stab anti-ice**.

| Question | Answer |
|----------|--------|
| **Air in** | Engine bleed → **ECS** conditions it → cabin |
| **Air out** | **Outflow valve (OFV)** controls how much air leaves the cabin |
| **Bleed control** | **PRSOV** per engine regulates and can shut off bleed |
| **Cross-side bleed** | **XBV** can interconnect left and right bleed circuits |

**Where you see it:** air synoptic and **cabin pressure** on the **MFD**; bleed/press CAS on **PFDs**; **pressurization & pneumatic panel**.

**Study focus:** bleed in vs OFV out; what fails together when **bleed** is lost; **AUTO vs MAN** pressurization; **LFE** on descent.

Numeric limits → **Limitations → Air Management (Pressurization)**.
"""
        )

    with st.expander("**1. Bleed & pneumatic system**", expanded=False):
        st.markdown(
            """
### What bleed air feeds

- **ECS** — cabin temperature, flow, and pressurization supply
- **Wing & horizontal stabilizer anti-ice** — thermal anti-ice (see **Ice Protection**)

### Key valves


| Valve | Role |
|-------|------|
| **PRSOV** (per engine) | Regulates bleed pressure; firewall shutoff capability |
| **XBV** | Crossbleed between left and right circuits when required |

### When several “air” functions fail together

If **pressurization**, **cab temperature**, and **anti-ice** all degrade at once, suspect **bleed supply** upstream — not the outflow valve alone.

**BLEED 1(2) FAIL / LEAK / OVERPRES** and **DUCT 1(2) OVERTEMP** point to the pneumatic side.
"""
        )
        _img(f"{press_folder}/pneumatic_system_schematic.png", "Bleed / pneumatic schematic (POH 6-02-10)")

    with st.expander("**2. ECS & cabin conditioning**", expanded=False):
        st.markdown(
            """
The **Environmental Control System** takes bleed air and delivers:

- Correct **temperature** (temperature control system)
- Correct **flow and distribution** to the cabin zones

If cabin temperature responds slowly, check panel settings first — then confirm there is no broader **bleed limitation** on the synoptic.
"""
        )

    with st.expander("**3. Pressurization — how it works**", expanded=False):
        st.markdown(
            """
Pressurization is **air in vs air out**.

### Air in

Engine **bleed air**, conditioned by the ECS, flows into the pressurized cabin.

### Air out

The **Outflow Valve (OFV)** controls cabin exhaust. The **Cabin Pressure Control System (CPCS)** positions the OFV automatically in **AUTO**.

- **Close OFV** → less air escapes → cabin pressure **increases** (cabin altitude **decreases**)
- **Open OFV** → more air escapes → cabin pressure **decreases** (cabin altitude **increases**)

### Mechanical backup

**Negative Relief Valve (NRV)** and **Positive Relief Valve (PRV)** provide structural relief if control limits are exceeded.

### Landing field elevation (LFE)

In **AUTO**, the CPCS needs a destination pressure reference — normally from the **FMS**, or entered manually on the **MFD**. Wrong **LFE** on descent can produce an uncomfortable or incorrect cabin schedule near landing.

### By flight phase


| Phase | Goal |
|-------|------|
| Ground | Cabin near ambient; avoid unintended differential pressure |
| Climb | Schedule cabin altitude and rate within comfort and structural limits |
| Cruise | Stable cabin altitude; protect delta-P |
| Descent / landing | Schedule cabin down toward **LFE** so doors open normally on the ground |
"""
        )
        _img(f"{press_folder}/cpcs_schematic.png", "CPCS schematic (POH 6-02-20)")

    with st.expander("**4. Pressurization controls**", expanded=False):
        st.markdown(
            """
### AUTO (normal)

CPCS controls the OFV through ground, takeoff, climb, cruise, descent, and taxi. Requires valid **LFE**.

### MAN (abnormal)

- **MODE** switch → **MAN**
- **CABIN ALT UP / DN** commands OFV open/close
- Manual channel includes **altitude limiting** — structure is still protected

### DUMP

Rapid depressurization — ground or per QRH.

**Memory Items:** *CAB ALTITUDE HI*, *EMERGENCY DESCENT* — see **Memory Items** (not duplicated here).

**CAB ALTITUDE HI** triggers at **10,000 ft** cabin altitude.
"""
        )
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            _img(f"{press_folder}/pressurization_pneumatic_panel.png", "Pressurization & pneumatic panel")
        with c2:
            _img(f"{press_folder}/pressure_indication_mfd.png", "Cabin pressure indication (MFD)")

    with st.expander("**5. When something fails — what it usually means**", expanded=False):
        st.markdown(
            """
| Cue | System meaning |
|-----|----------------|
| **CAB ALTITUDE HI** | Cabin altitude climbing — often insufficient **bleed in** or OFV too open |
| **PRESN AUTO FAIL** | Automatic pressurization unavailable — **MAN** may be required |
| **CAB DELTA-P FAIL** | Differential pressure out of limits — structural protection active |
| **BLEED / DUCT messages** | Upstream bleed problem — often affects ECS, pressurization, and anti-ice together |

Use the **MFD synoptic** to see whether the problem is **supply** (bleed) or **exhaust** (OFV/CPCS).
"""
        )

    cas_quick_reference(
        [
            ("Pressurization", "WARNING", "CAB ALTITUDE HI", "Cabin altitude ≥ 10,000 ft — memory item."),
            ("Pressurization", "CAUTION", "PRESN AUTO FAIL", "Automatic pressurization lost — consider MAN."),
            ("Pressurization", "CAUTION", "CAB DELTA-P FAIL", "Delta-P out of limits — structural protection."),
            ("Bleed", "CAUTION", "BLEED 1 (2) FAIL", "Bleed unavailable on that engine."),
            ("Bleed", "CAUTION", "BLEED 1 (2) LEAK", "Leak in bleed line."),
            ("Bleed", "CAUTION", "BLEED 1 (2) OVERPRES", "Bleed manifold overpressure."),
            ("Bleed", "CAUTION", "DUCT 1 (2) OVERTEMP", "Bleed duct overheat."),
            ("Bleed", "CAUTION", "XBLEED FAIL", "Crossbleed valve not responding."),
            ("Avionics bay", "ADVISORY", "EBAY OVHT", "Avionics bay temp > 70°C."),
        ],
        title="6. CAS quick reference",
    )

    back_to_top()
    source_footer("poh", "§6-02 Air Management · Memory Items (CAB ALTITUDE HI)")
