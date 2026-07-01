import os

import pandas as pd
import streamlit as st
from PIL import Image

from content.render_helpers import back_to_top, cas_quick_reference, source_footer


def render_hydraulics():
    st.markdown("## Hydraulic System")
    st.caption("ATA 29 | Source: Phenom 300 POH")

    folder = "assets/hydraulics"

    with st.expander("**0. How it works**", expanded=True):
        st.markdown(
            """
**One hydraulic system** powers gear, brakes, spoilers, and flight-control actuators.

| Source | Role |
|--------|------|
| **EDP ×2** | Normal pressure from each engine |
| **Accumulator** | Backup / emergency pressure |
| **FSOV ×2** | Fire shutoff isolates each engine pump circuit |

**3000 psi** red fluid — **FIRE SHUTOFF** closes FSOVs (see **Fire Protection**).

In practice, the main things to understand are: what still works with **one engine**, **one pump**, or an **FSOV** closed.
"""
        )

    with st.expander("**1. System Description**", expanded=False):
        st.markdown("""
### What makes up the system:

- Two **Engine Driven Pumps (EDP)** - one on each engine
- One **reservoir** with built-in manifold
- One **accumulator** for backup pressure
- Two **Fire Shutoff Valves (FSOV)** - one per engine
- One **nitrogen charging valve**
- One **pressure gauge**
- Two **temperature switches**

### Fluid specs:

- Type: MIL-PRF-87257 (synthetic hydrocarbon)
- Color: **Red** - and highly flammable!
- System pressure: **3000 psi**

### What does hydraulics power?

- Landing gear (extend/retract)
- Main wheel brakes
- Emergency/Parking brakes
- Spoilers (all functions)
- Stick pusher
- Rudder spring actuator

### Where to see hydraulic info:

- System status → **MFD synoptic page**
- Warnings/messages → **Both PFDs**
""")
    
    with st.expander("**2. Reservoir & Manifold**", expanded=False):
        st.markdown("""
### How the reservoir works:

- A **spring-rolling diaphragm** keeps the fluid pressurized
- There's a sight glass on the side so you can **visually check fluid level**

### Fluid flow path:

1. Fluid leaves the reservoir → goes to the pump
2. Pump pressurizes it → sends it to the manifold
3. Manifold filters the fluid → routes it to aircraft systems
4. Returning fluid gets **filtered again** before going back to reservoir

### Sensors built into the manifold:

- **2 temperature switches** - monitor fluid temp
- **2 pressure switches** - control automatic pump operation
- **1 pressure transducer** - provides continuous pressure reading to cockpit
""")
    
    with st.expander("**3. Engine Driven Pump (EDP)**", expanded=False):
        st.markdown("""
### The basics:

- Each engine has one pump attached to its **accessory gearbox**
- This is your **only** source of hydraulic power - there are no electric backup pumps
- Simple rule: **Engine running = pump running**

### How it works:

1. Engine spins the pump via a coupling shaft
2. Pump draws low-pressure fluid from the reservoir
3. Pump outputs **variable flow** at **3000 psi**

### Case drain line:

- The pump's internal parts need lubrication
- This lubricating fluid drains back to the reservoir through a dedicated line
- It passes through the **return filter** before reaching the reservoir
""")
    
    with st.expander("**4. Fire Shutoff Valve (FSOV)**", expanded=False):
        st.markdown("""
### What it is:

- Two valves total - one for each engine's hydraulic pump
- Powered by the **Emergency Bus** *(remember this!)*
- Position switches tell you if valve is fully **OPEN** or fully **CLOSED**

### Automatic protection:

- Valves **close automatically** if hydraulic fluid gets too hot (HYD HI TEMP)
- System won't let you reopen them manually while overtemp exists

### How to close them manually:

- **Option 1:** Engine fire extinguisher shutoff buttons (1 or 2)
- **Option 2:** HYD PUMP SOV switches on hydraulic panel

### When would you close them?

- Engine fire
- HYD HI TEMP message
- Hydraulic leak (follow QRH)
""")
    
    with st.expander("**5. Accumulator**", expanded=False):
        st.markdown("""
### What it does:

- Stores extra hydraulic pressure for high-demand situations
- Capacity: **25 cubic inches**

### When it helps:

- Braking + ground spoilers at the same time (landing roll)
- Any moment when demand exceeds what the pumps can supply

### How it's built:

- Cylinder with a sliding piston inside
- One side: hydraulic fluid | Other side: compressed gas (nitrogen)
- Piston keeps them separated and at **equal pressure**

### Emergency backup:

- If both pumps fail, the accumulator holds enough pressure for **6 full brake applications**
""")
    
    with st.expander("**6. Priority Valve**", expanded=False):
        st.markdown("""
**Purpose:** Protects the most critical systems when hydraulic demand is high.

### Priority systems (always get fluid first):

- Spoilers
- Stick pusher
- Rudder spring actuator
- Brakes

### What happens when demand is high:

- The valve **restricts flow to the landing gear**
- Gear still works - it just uses **accumulator pressure** instead
- Gear may cycle slower, but flight controls and brakes stay fully powered

### Example scenario:

- Engines at idle = low pump output
- You're moving gear AND using spoilers
- Priority valve says: "Spoilers and brakes first, gear can wait"
- **Bottom line:** You never lose control authority or braking
""")
    
    with st.expander("**7. Controls & Indications**", expanded=False):
        st.markdown("""
### Where to find hydraulic info:

- **MFD Synoptic Page** - shows system diagram plus emergency/parking brake accumulator pressure

### HYD PUMP SOV 1 & 2 Switches:


| Position | What it does |
|----------|--------------|
| **OPEN** | Opens the Fire Shutoff Valve (normal position) |
| **CLOSED** | Closes the FSOV - stops hydraulic fluid flow to that pump |

### When should you close the SOV?

- Engine fire
- HYD HI TEMP message
- Hydraulic leak (follow QRH procedure)
""")
        panel_path = os.path.join(folder, "hyd_panel.png")
        if os.path.exists(panel_path):
            st.image(Image.open(panel_path), caption="HYD PUMP SOV Switches", use_container_width=True)
    
    with st.expander("**8. Pressure Indication**", expanded=False):
        st.markdown("""
### Reading the digital pressure display:


| Color | What it means |
|-------|---------------|
| **GREEN digits** | All good - pressure is above 1800 psi |
| **YELLOW digits** | Caution - pressure is 1800 psi or below |
| **GRAY** | Just the "PSI" label |
| **YELLOW DASHED** | Data is invalid or out of range |

---

### Reading the pressure gauge (arc with pointer):


The pointer shows the same value as the digital readout.

| Part | Normal (>1800 psi) | Low (≤1800 psi) |
|------|-------------------|-----------------|
| **Scale arc** | WHITE | YELLOW |
| **Pointer** | GREEN | YELLOW |

If the value is invalid, the pointer disappears from the display.
""")
    
    cas_quick_reference(
        [
            ("Temperature", "CAUTION", "HYD HI TEMP", "Fluid overheating — FSOVs close automatically."),
            ("Pressure", "CAUTION", "HYD LO PRES", "System pressure below normal — check for leaks."),
            ("Fire shutoff", "CAUTION", "HYD SOV 1 (2) FAIL", "FSOV won't close when commanded — valve malfunction."),
            ("System", "ADVISORY", "HYD SYS FAULT", "Reduced hydraulic power — system degraded."),
        ],
        title="9. CAS quick reference",
    )

    cas_path = os.path.join(folder, "hyd_cas.png")
    if os.path.exists(cas_path):
        st.image(Image.open(cas_path), caption="POH CAS reference (Hydraulics)", use_container_width=True)

    with st.expander("**10. System Schematic**", expanded=False):
        schematic_path = os.path.join(folder, "hyd_schematic.png")
        if os.path.exists(schematic_path):
            st.image(Image.open(schematic_path), caption="Hydraulic System Schematic", use_container_width=True)

    with st.expander("**11. Synoptic pages (POH)**", expanded=False):
        poh_paths = []
        if os.path.isdir(folder):
            for name in os.listdir(folder):
                if name.startswith("poh_6-10_synoptic_") and name.lower().endswith(".png"):
                    poh_paths.append(os.path.join(folder, name))
        poh_paths.sort()
        if not poh_paths:
            st.info("No POH synoptic pages found for hydraulics yet.")
        else:
            cols = st.columns(2, gap="medium")
            for i, p in enumerate(poh_paths):
                with cols[i % 2]:
                    st.image(Image.open(p), caption=os.path.basename(p), use_container_width=True)

    back_to_top()
    source_footer("poh", "§6-10 Hydraulics")
