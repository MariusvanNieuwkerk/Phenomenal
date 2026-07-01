import os

import pandas as pd
import streamlit as st
from PIL import Image

from content.render_helpers import back_to_top, cas_quick_reference, source_footer


def render_landing_gear():
    st.markdown("## Landing Gear & Brakes")
    st.caption("ATA 32 | Source: Phenom 300 POH")

    folder = "assets/landing_gear"

    with st.expander("**0. How it works**", expanded=True):
        st.markdown(
            """
**Tricycle retractable gear** — electrical command, **hydraulic** actuation.

| Leg | Retraction |
|-----|------------|
| **NLG** | Forward into fuselage |
| **MLG** | Inward into wing fairing |

**LDG GEAR lever** UP/DN — ground lock prevents UP on ground (override: **DN LCK REL**).

**Brakes:** normal + emergency/parking (accumulator). **Anti-skid** for rejected landing / wet runway.

Related: **Hydraulics**, **Warning System**, **Flight Controls**.
"""
        )

    with st.expander("**1. System Description**", expanded=False):
        st.markdown("""
**Configuration:** Tricycle retractable gear, hydraulically powered

### The three gear legs:

- **Nose gear (NLG):** Retracts **forward** into the fuselage
- **Main gear (MLG):** Retracts **inward** into the wing-fuselage fairing

### How the gear works:

- Controlled by the **LDG GEAR lever** on the main instrument panel
- Two positions: **UP** (retract) and **DN** (extend)
- Command is **electrical**, actuation is **hydraulic**

### Built-in safety (ground lock):

- An interlock **prevents** moving the lever to UP while on the ground
- In an emergency, you can override this with the **DN LCK REL** button on the LDG GEAR panel
""")
        lg_overview_path = os.path.join(folder, "lg_overview.png")
        if os.path.exists(lg_overview_path):
            st.image(Image.open(lg_overview_path), caption="Landing Gear Overview", use_container_width=True)
        
        lg_control_path = os.path.join(folder, "lg_control_panel.png")
        if os.path.exists(lg_control_path):
            st.image(Image.open(lg_control_path), caption="LDG GEAR Control Panel", use_container_width=True)

    with st.expander("**1b. Synoptic pages (POH)**", expanded=False):
        poh_paths = []
        if os.path.isdir(folder):
            for name in os.listdir(folder):
                if name.startswith("poh_6-12_synoptic_") and name.lower().endswith(".png"):
                    poh_paths.append(os.path.join(folder, name))
        poh_paths.sort()
        if not poh_paths:
            st.info("No POH synoptic pages found for landing gear yet.")
        else:
            cols = st.columns(2, gap="medium")
            for i, p in enumerate(poh_paths):
                with cols[i % 2]:
                    st.image(Image.open(p), caption=os.path.basename(p), use_container_width=True)
    
    with st.expander("**2. Landing Gear Operation**", expanded=False):
        st.markdown("""
### RETRACTION (Lever UP)


When you move the lever to UP:
1. Electrical command activates the hydraulic retraction actuators
2. **Wheels are automatically braked** to stop spinning
3. Gear retracts and locks into the **uplock box**
4. All gear doors close

---

### NORMAL EXTENSION (Lever DN)


When you move the lever to DN:
1. Uplock box releases each gear leg
2. Gear extends under hydraulic power
3. **Down lock mechanism** holds gear in extended position
4. Green lights illuminate when locked down

### What's normal:

- The nose gear often takes **longer** to show a green light than the mains
- All three legs don't necessarily lock at the exact same time
- A short delay in position indications is **normal** - don't panic
""")
    
    with st.expander("**3. Emergency Extension (Free-Fall)**", expanded=False):
        st.markdown("""
**What it's for:** Extends the gear when normal hydraulic extension fails

### Emergency handle location:** On the cockpit **floor


### How it works:

1. Pull the free-fall handle
2. This activates the **free-fall selector valve**
3. Valve dumps all hydraulic pressure from the gear lines
4. Up locks are **mechanically released**

### What happens next:

- **Gravity and airflow** push the gear down (no hydraulics needed)
- **Down lock mechanism** locks the gear in place
- Green DN lights appear only **after** you move the LDG GEAR lever to DN

### Important details:

- Maximum pull force needed: **25 kg (55 lb)**
- If a main gear won't lock, you may need to **slip the airplane** to use airflow to push that leg into the lock
""")
        freefall_path = os.path.join(folder, "freefall_handle.png")
        if os.path.exists(freefall_path):
            st.image(Image.open(freefall_path), caption="Free-Fall Handle Location", use_container_width=True)
    
    with st.expander("**4. Uplock Box**", expanded=False):
        st.markdown("""
**What it does:** Holds each gear leg **up and locked** when retracted

### Two ways to unlock it:

1. **Normal:** Hydraulic actuator releases the lock when you select gear DN
2. **Emergency:** Mechanical release via the free-fall handle (no hydraulics needed)

### How the system knows the gear is up:

- Each uplock box has a **proximity sensor**
- When the gear locks in, the sensor signals "up and locked" to the cockpit
""")
    
    with st.expander("**5. Position & Warning Subsystem**", expanded=False):
        st.markdown("""
### Sensors that tell the system where the gear is:

- **Down and locked** proximity switches (one per leg)
- **Up and locked** proximity switches (one per leg)
- **Weight On Wheels (WOW)** switches - two per main gear
- **Lever position** micro switches

### What happens with this data:

- The system combines all these signals to show you gear position
- Also generates CAS messages when something is wrong

### Weight On Wheels (WOW) - important for many systems:

- These switches detect whether the airplane is **on the ground** or **airborne**
- Compressed = on ground | Extended = airborne
- If WOW sensors disagree for more than **30 seconds**, you get: **"LG WOW SYS FAIL"**
""")
        lg_ind_path = os.path.join(folder, "lg_indications.png")
        if os.path.exists(lg_ind_path):
            st.image(Image.open(lg_ind_path), caption="Landing Gear Position Indications (Normal vs Abnormal)", use_container_width=True)
    
    with st.expander("**6. Landing Gear Aural Warning**", expanded=False):
        st.markdown("""
**Purpose:** Warns you if the gear isn't down and locked when it should be

---

### With flaps at 0, 1, or 2:


The horn sounds when **ALL** of these are true:
- Below **700 ft AGL** (radio alt) or within **700 ft** of field elevation
- Airspeed below **160 KIAS**
- Power is reduced (thrust levers below **26°/40°** depending on engine status)

---

### With flaps at 3 or FULL:


- Warning sounds **regardless** of speed, altitude, or power setting
- **Cannot be silenced** with the WRN INHIB button

---

### If flaps have failed:


- Warning sounds if descending through **700 ft** above field elevation

**Note:** Pre-Mod SB 505-27-0011 aircraft: FULL flap position is blocked by a mechanical stop.
""")
    
    with st.expander("**7. Brakes System Overview**", expanded=False):
        st.markdown("""
### Two separate brake systems:

1. **Main brakes** - your normal braking system
2. **Emergency/Parking brakes** - backup and parking

Both use hydraulic pressure from the main hydraulic system.

---

### Main Brake System - what it does:

- Applies brake pressure based on how hard you push the pedals
- Provides **antiskid protection** to prevent skidding
- Minimizes stopping distance

### Emergency/Parking Brake - what it does:

- Stops the airplane if main brakes fail
- Holds the airplane parked (works even with hydraulics off)

---

### How the main brakes work (brake-by-wire):

1. You push the rudder pedals (top portion)
2. **Pedal transducers** sense how much pressure you're applying
3. Signal goes to the **Brake Control Unit (BCU)**
4. BCU commands the **brake control valves (BCVs)** - one per wheel
5. BCVs apply the right amount of hydraulic pressure to the brakes

### Key component - the BCU:

- Controls left and right brakes **independently**
- Connected to the **Emergency Bus** (important for emergencies!)
- Monitors: wheel speed, pedal position, and brake pressure
""")
    
    with st.expander("**8. Brake System Functions**", expanded=False):
        st.markdown("""
The brake system has **four automatic protection functions:**

---

### A. LOCKED WHEEL PROTECTION


**Purpose:** Prevents a tire from blowing out if one wheel locks up

### How it works:

- BCU compares left and right wheel speeds
- If one wheel drops to **≤30%** of the other's speed, it's "locked"
- System **releases pressure** on that wheel so it can spin back up
- Normal braking resumes when the slow wheel reaches **70%** of the other wheel's speed

**Below 30 kt:** Protection turns off so you can use differential braking for steering

---

### B. ANTISKID PROTECTION


**Purpose:** Maximizes braking without skidding

### How it works:

- If a wheel starts to skid, the system **reduces brake pressure** automatically
- This lets the tire regain grip, then reapplies pressure
- Active when both wheels are above **30 kt**

**Below 10 kt:** Antiskid turns off - you can lock a wheel for pivoting

**Important:** Antiskid is **NOT available** on the emergency/parking brake!

---

### C. TOUCHDOWN PROTECTION


**Purpose:** Prevents braking before the wheels spin up at landing

### How it works:

- Even if you're pressing the pedals in the flare, **no brake pressure is applied**
- Wheels are allowed to spin up freely at touchdown
- Prevents tire blowout from sudden braking on a stationary wheel

### When it cancels:

- Both wheels exceed **60 kt** (even before WOW says "on ground")
- **3 seconds** after WOW indicates "on ground" (regardless of speed)
- After touchdown, the spin-up threshold drops from **60 → 30 kt** over 3 seconds

**Note:** Below **10 kt** with WOW showing airborne, normal braking is disabled

---

### D. GEAR RETRACT BRAKING


**Purpose:** Stops the wheels from spinning before they enter the wheel well

### How it works:

1. When WOW = airborne AND you select gear UP
2. BCU waits **3 seconds** (for hydraulic demand to settle)
3. Then applies ramped brake pressure to stop the wheels
4. If wheels aren't stopped in **10 seconds**, system resets and tries again
5. When wheel speed = zero, brake pressure is released
""")
    
    with st.expander("**9. Initiated Built-In Test (IBIT)**", expanded=False):
        st.markdown("""
**What it is:** An automatic self-test the brake system runs in flight

### When it runs (all conditions must be true):

- Gear lever moves from UP to DN
- At least one gear shows down and locked
- WOW indicates airborne
- Both wheels are stationary
- 10-second delay (lets hydraulic pressure stabilize)

### What it tests:

- Runs the brake pressure loop through its full range
- Checks the SOV, brake control valves, and pressure transducers

### Duration:** About **5 seconds

""")
    
    with st.expander("**10. Emergency/Parking Brake**", expanded=False):
        st.markdown("""
### Two uses for this system:

1. **Parking brake** - hold the airplane while parked
2. **Emergency brake** - stop the airplane if main brakes fail

---

### The T-Handle:

- Located on the **center pedestal**
- Connected to the brake valve by a steel cable
- Pull up = brakes ON | Push down = brakes OFF
- You can **modulate** pressure by how much you pull

---

### The Accumulator (stores pressure for emergencies):

- Isolated from the main hydraulic system by a check valve and shutoff valve
- Shutoff valve opens during engine start (on ground, both thrust levers at idle for **>50 seconds**)
- Holds enough pressure for **6 full brake applications**

---

### How you know it's working:

- When you pull the handle, hydraulic pressure goes to the brakes
- A **white PARK BRK light** illuminates on the front panel

---

**⚠️ CAUTION:** No antiskid protection with emergency/parking brake!
""")
        col1, col2 = st.columns(2)
        with col1:
            park_handle_path = os.path.join(folder, "parking_brake_handle.png")
            if os.path.exists(park_handle_path):
                st.image(Image.open(park_handle_path), caption="Parking Brake T-Handle Location", use_container_width=True)
        with col2:
            park_light_path = os.path.join(folder, "parking_brake_light.png")
            if os.path.exists(park_light_path):
                st.image(Image.open(park_light_path), caption="Parking Brake Light Indicator", use_container_width=True)
        
        emer_brk_path = os.path.join(folder, "emer_brk_accu.png")
        if os.path.exists(emer_brk_path):
            st.image(Image.open(emer_brk_path), caption="Emergency Brake Accumulator Pressure Display (MFD)", use_container_width=True)
    
    with st.expander("**11. Fusible Plugs & Brake Wear Pins**", expanded=False):
        st.markdown("""
### FUSIBLE PLUGS


**What they are:** Safety plugs in the main wheels with a metal core that melts when hot

### Why they exist:

- After a high-energy event (like an RTO), brakes get extremely hot
- Heat transfers to the tires, which could explode in the wheel well
- The fusible plug melts and **releases tire pressure safely** before that can happen

**Location:** Main wheel assemblies only

---

### BRAKE WEAR PINS


**What they are:** Visual indicators showing how much brake pad is left

### How to check:

1. Set the **parking brake** (required for accurate reading!)
2. Look at the wear pins on each main wheel
3. If pins are **flush with Face A**, brakes need replacement

**Simple rule:** Pins sticking out = good | Pins flush = time to replace
""")
        
        img_path = os.path.join(folder, "brake_wear_pins_new.png")
        if os.path.exists(img_path):
            st.image(Image.open(img_path), caption="Brake Wear Pins Location", use_container_width=True)
    
    with st.expander("**12. Turning Radius Data**", expanded=False):
        st.markdown("**TURNING RADIUS (STEERING 20°)**")
        
        turn_20_data = [
            ["Nose R1", "19.68 m", "64 ft 6.8 in"],
            ["Nose Gear R2", "19.18 m", "52 ft 11 in"],
            ["Inboard Gear R3", "16.5 m", "54 ft 1.6 in"],
            ["Outboard Gear R4", "19.54 m", "64 ft 1.3 in"],
            ["Right Wing Tip R5", "26.1 m", "85 ft 7.5 in"],
            ["Right Tail Tip R6", "22.25 m", "73 ft"]
        ]
        df_turn20 = pd.DataFrame(turn_20_data, columns=["Position", "Metric", "Imperial"])
        st.dataframe(df_turn20, hide_index=True, use_container_width=True)
        
        st.markdown("**Wingspan clearance (Steering 20°):** 52.20 m (171 ft 3 in)")
        st.markdown("**Wing-to-wing clearance:** 39.10 m (128 ft 3.4 in)")
        
        st.markdown("---")
        st.markdown("**TURNING ASSISTED BY BRAKES RADIUS (STEERING 20° + 23°)**")
        
        turn_43_data = [
            ["Nose R1", "10.78 m", "35 ft 4.4 in"],
            ["Nose Gear R2", "9.64 m", "31 ft 7.5 in"],
            ["Inboard Gear R3", "5.51 m", "18 ft 0.9 in"],
            ["Outboard Gear R4", "8.56 m", "28 ft 1.0 in"],
            ["Right Wing Tip R5", "15.2 m", "49 ft 10.4 in"],
            ["Right Tail Tip R6", "12.5 m", "41 ft"]
        ]
        df_turn43 = pd.DataFrame(turn_43_data, columns=["Position", "Metric", "Imperial"])
        st.dataframe(df_turn43, hide_index=True, use_container_width=True)
        
        st.markdown("**Wingspan clearance (43°):** 30.40 m (99 ft 8.8 in)")
        st.markdown("**Wing-to-wing clearance:** 18.18 m (59 ft 7.7 in)")
        
        st.markdown("---")
        st.markdown("**TURNING RADIUS (BRAKED)**")
        
        braked_data = [
            ["R1", "2.84 m", "9 ft 3.8 in"],
            ["R2", "6.71 m", "22 ft"],
            ["R3", "9.71 m", "31 ft 10.3 in"]
        ]
        df_braked = pd.DataFrame(braked_data, columns=["Position", "Metric", "Imperial"])
        st.dataframe(df_braked, hide_index=True, use_container_width=True)
        
        st.markdown("**Wall-to-Wall:** 19.41 m (63 ft 8.2 in)")
        st.markdown("**Curb-to-Curb:** 9.55 m (31 ft 4 in)")
        
        st.markdown("---")
        st.markdown("**TURNING RADIUS (TOWBAR)**")
        
        towbar_data = [
            ["R1", "1.42 m", "4 ft 8 in"],
            ["R2", "6.56 m", "21 ft 6.3 in"],
            ["R3", "8.34 m", "27 ft 4.3 in"]
        ]
        df_towbar = pd.DataFrame(towbar_data, columns=["Position", "Metric", "Imperial"])
        st.dataframe(df_towbar, hide_index=True, use_container_width=True)
        
        st.markdown("**Wall-to-Wall:** 16.68 m (54 ft 8.7 in)")
        st.markdown("**Curb-to-Curb:** 7.98 m (26 ft 2.2 in)")
    
    with st.expander("**12. Handbook — brakes & BRK FAIL (Ch 5.1)**", expanded=False):
        st.markdown(
            """
**Emergency / parking brake** — T-handle on pedestal; accumulator isolated from main hydraulics.

**Brake-by-wire** — BCU modulates pressure by runway condition (less decel on contaminated runway for same pedal input).

### BRK FAIL causes (fleet experience)

- Residual brake pressure at touchdown after rudder brake during approach.
- Bounce: wheels stop (anti-skid) → pedals after spin-up before WOW → BCU manual mode → **BRK FAIL**.
- **FOL 010/13**, **FOL 005/16** — system reset may help if no real fault; QRH landing factor if CAS persists.

**Emergency braking** — use parking brake T-handle per QRH if main brakes lost.

_See **Flight Controls** for ground spoiler interaction with stopping distance._
"""
        )

    cas_quick_reference(
        [
            ("Gear", "WARNING", "LG LEVER DISAG", "Gear position doesn't match lever — verify synoptic."),
            ("Brakes", "WARNING", "ANTI-SKID FAIL", "Antiskid not working — longer stopping distances."),
            ("Brakes", "WARNING", "BRK FAIL", "Lost braking on one main wheel — emergency brakes if needed."),
            ("Brakes", "CAUTION", "EMER BRK LO PRES", "Emergency/parking brake accumulator pressure low."),
            ("WOW", "CAUTION", "LG WOW SYS FAIL", "Weight-on-wheels sensors disagree — affects many systems."),
            ("Brakes", "CAUTION", "PARK BRK NOT REL", "Parking brake still set — release before takeoff."),
        ],
        title="13. CAS quick reference",
    )

    with st.expander("**14. System Diagrams**", expanded=False):
        st.markdown("**Landing Gear Components**")
        col1, col2 = st.columns(2)
        with col1:
            mlg_path = os.path.join(folder, "mlg_components.png")
            if os.path.exists(mlg_path):
                st.image(Image.open(mlg_path), caption="Main Landing Gear Components", use_container_width=True)
        with col2:
            nlg_path = os.path.join(folder, "nlg_components.png")
            if os.path.exists(nlg_path):
                st.image(Image.open(nlg_path), caption="Nose Landing Gear Components", use_container_width=True)
        
        st.markdown("---")
        st.markdown("**Landing Gear Hydraulic Schematic**")
        schematic_path = os.path.join(folder, "lg_schematic_new.png")
        if os.path.exists(schematic_path):
            st.image(Image.open(schematic_path), caption="Landing Gear Hydraulic System", use_container_width=True)
        
        st.markdown("---")
        st.markdown("**Brake System Schematic**")
        brake_path = os.path.join(folder, "brake_schematic_new.png")
        if os.path.exists(brake_path):
            st.image(Image.open(brake_path), caption="Brake System Schematic", use_container_width=True)
        
        st.markdown("---")
        st.markdown("**Turning Radius (Towbar)**")
        towbar_path = os.path.join(folder, "turn_towbar_new.png")
        if os.path.exists(towbar_path):
            st.image(Image.open(towbar_path), caption="Turning Radius with Towbar", use_container_width=True)

    back_to_top()
    source_footer("poh", "§6-12 Landing Gear & Brakes")
