import os

# Keep Streamlit's runtime files inside the project folder (Cursor sandbox
# cannot write to `~/.streamlit`).
_app_dir = os.path.dirname(os.path.abspath(__file__))
os.environ.setdefault("STREAMLIT_HOME", os.path.join(_app_dir, ".streamlit_local"))
os.environ["STREAMLIT_SERVER_WEB_INDEX_TEMPLATE"] = ".streamlit/index.html"

import streamlit as st
import pandas as pd
from PIL import Image

from systems.electrics import render_electrics
from systems.fuel import render_fuel
from systems.ice_protection import render_ice_protection
from systems.powerplant import render_powerplant
from systems.pressurization import render_pressurization

icon_url = "https://phenomenal--mariusvannieuwk.replit.app/app/static/apple-touch-icon.png"
st.set_page_config(page_title="Phenom 300 Training", page_icon=icon_url, layout="wide")

st.markdown("""
<style>
    .stApp {
        max-width: 1024px;
        margin: 0 auto;
    }
    .main-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 700;
        color: #1a365d;
        margin-bottom: 0.3rem;
        margin-top: 0;
        padding-top: 0;
    }
    .subtitle {
        text-align: center;
        font-size: 1rem;
        color: #4a5568;
        margin-bottom: 1rem;
    }
    .stButton > button {
        min-height: 55px;
        font-size: 1rem !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        margin-bottom: 0.4rem;
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%) !important;
        border: none !important;
    }
    .block-container {
        padding: 0.5rem 1.5rem !important;
        padding-top: 1rem !important;
    }
    h2, h3 {
        color: #1a365d;
        margin-top: 0.5rem;
    }
    .stMarkdown {
        font-size: 1rem;
        line-height: 1.5;
    }
    .stTable {
        font-size: 0.9rem;
    }
    div[data-testid="stExpander"] {
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin-bottom: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

if 'section' not in st.session_state:
    st.session_state.section = 'home'
if 'system' not in st.session_state:
    st.session_state.system = None

def navigate(section, system=None):
    st.session_state.section = section
    st.session_state.system = system

def render_home():
    st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>Phenom 300</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Netjets Edition</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Systems", use_container_width=True, type="primary"):
            navigate('systems')
            st.rerun()
    
    with col2:
        if st.button("Limitations", use_container_width=True, type="primary"):
            navigate('limitations')
            st.rerun()
    
    col3, col4 = st.columns(2)
    
    with col3:
        if st.button("Memory Items", use_container_width=True, type="primary"):
            navigate('memory')
            st.rerun()
    
    with col4:
        if st.button("Planning", use_container_width=True, type="primary"):
            navigate('planning')
            st.rerun()
    
    col5, col6 = st.columns(2)
    
    with col5:
        if st.button("SOP", use_container_width=True, type="primary"):
            navigate('sop')
            st.rerun()
    
    with col6:
        if st.button("Flight Profiles", use_container_width=True, type="primary"):
            navigate('profiles')
            st.rerun()
    
    col7, col8 = st.columns(2)
    
    with col7:
        if st.button("Special Airports", use_container_width=True, type="primary"):
            navigate('airports')
            st.rerun()
    
    with col8:
        if st.button("Cold Weather Ops", use_container_width=True, type="primary"):
            navigate('cold_weather')
            st.rerun()
    
    st.markdown("---")
    st.info("Select a module above to begin studying.")

def render_systems():
    st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>Phenom 300</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Netjets Edition</p>", unsafe_allow_html=True)
    if st.button("Home", use_container_width=False, type="primary", key="home_btn"):
        navigate('home')
        st.rerun()
    
    st.markdown("### Aircraft Systems")
    
    systems_list = ["Hydraulics", "Electrics", "Powerplant", "Landing Gear & Brakes", "Fuel", "Pressurization", "Ice Protection"]
    
    col1, col2 = st.columns(2)
    for i, sys in enumerate(systems_list):
        with col1 if i % 2 == 0 else col2:
            if st.button(sys, use_container_width=True, key=f"sys_{sys}", type="primary" if st.session_state.system != sys else "secondary"):
                st.session_state.system = sys
                st.rerun()
    
    st.markdown("---")
    
    if st.session_state.system == "Hydraulics":
        render_hydraulics()
    elif st.session_state.system == "Electrics":
        render_electrics()
    elif st.session_state.system == "Powerplant":
        render_powerplant()
    elif st.session_state.system == "Landing Gear & Brakes":
        render_landing_gear()
    elif st.session_state.system == "Fuel":
        render_fuel()
    elif st.session_state.system == "Pressurization":
        render_pressurization()
    elif st.session_state.system == "Ice Protection":
        render_ice_protection()
    else:
        st.info("Select a system above to view details.")

def render_hydraulics():
    st.markdown("## Hydraulic System")
    st.caption("ATA 29 | Source: Phenom 300 POH")
    
    folder = "assets/hydraulics"
    
    with st.expander("**1. System Description**", expanded=True):
        st.markdown("""
**What makes up the system:**
- Two **Engine Driven Pumps (EDP)** - one on each engine
- One **reservoir** with built-in manifold
- One **accumulator** for backup pressure
- Two **Fire Shutoff Valves (FSOV)** - one per engine
- One **nitrogen charging valve**
- One **pressure gauge**
- Two **temperature switches**

**Fluid specs:**
- Type: MIL-PRF-87257 (synthetic hydrocarbon)
- Color: **Red** - and highly flammable!
- System pressure: **3000 psi**

**What does hydraulics power?**
- Landing gear (extend/retract)
- Main wheel brakes
- Emergency/Parking brakes
- Spoilers (all functions)
- Stick pusher
- Rudder spring actuator

**Where to see hydraulic info:**
- System status → **MFD synoptic page**
- Warnings/messages → **Both PFDs**
""")
    
    with st.expander("**2. Reservoir & Manifold**", expanded=False):
        st.markdown("""
**How the reservoir works:**
- A **spring-rolling diaphragm** keeps the fluid pressurized
- There's a sight glass on the side so you can **visually check fluid level**

**Fluid flow path:**
1. Fluid leaves the reservoir → goes to the pump
2. Pump pressurizes it → sends it to the manifold
3. Manifold filters the fluid → routes it to aircraft systems
4. Returning fluid gets **filtered again** before going back to reservoir

**Sensors built into the manifold:**
- **2 temperature switches** - monitor fluid temp
- **2 pressure switches** - control automatic pump operation
- **1 pressure transducer** - provides continuous pressure reading to cockpit
""")
    
    with st.expander("**3. Engine Driven Pump (EDP)**", expanded=False):
        st.markdown("""
**The basics:**
- Each engine has one pump attached to its **accessory gearbox**
- This is your **only** source of hydraulic power - there are no electric backup pumps
- Simple rule: **Engine running = pump running**

**How it works:**
1. Engine spins the pump via a coupling shaft
2. Pump draws low-pressure fluid from the reservoir
3. Pump outputs **variable flow** at **3000 psi**

**Case drain line:**
- The pump's internal parts need lubrication
- This lubricating fluid drains back to the reservoir through a dedicated line
- It passes through the **return filter** before reaching the reservoir
""")
    
    with st.expander("**4. Fire Shutoff Valve (FSOV)**", expanded=False):
        st.markdown("""
**What it is:**
- Two valves total - one for each engine's hydraulic pump
- Powered by the **Emergency Bus** *(remember this!)*
- Position switches tell you if valve is fully **OPEN** or fully **CLOSED**

**Automatic protection:**
- Valves **close automatically** if hydraulic fluid gets too hot (HYD HI TEMP)
- System won't let you reopen them manually while overtemp exists

**How to close them manually:**
- **Option 1:** Engine fire extinguisher shutoff buttons (1 or 2)
- **Option 2:** HYD PUMP SOV switches on hydraulic panel

**When would you close them?**
- Engine fire
- HYD HI TEMP message
- Hydraulic leak (follow QRH)
""")
    
    with st.expander("**5. Accumulator**", expanded=False):
        st.markdown("""
**What it does:**
- Stores extra hydraulic pressure for high-demand situations
- Capacity: **25 cubic inches**

**When it helps:**
- Braking + ground spoilers at the same time (landing roll)
- Any moment when demand exceeds what the pumps can supply

**How it's built:**
- Cylinder with a sliding piston inside
- One side: hydraulic fluid | Other side: compressed gas (nitrogen)
- Piston keeps them separated and at **equal pressure**

**Emergency backup:**
- If both pumps fail, the accumulator holds enough pressure for **6 full brake applications**
""")
    
    with st.expander("**6. Priority Valve**", expanded=False):
        st.markdown("""
**Purpose:** Protects the most critical systems when hydraulic demand is high.

**Priority systems (always get fluid first):**
- Spoilers
- Stick pusher
- Rudder spring actuator
- Brakes

**What happens when demand is high:**
- The valve **restricts flow to the landing gear**
- Gear still works - it just uses **accumulator pressure** instead
- Gear may cycle slower, but flight controls and brakes stay fully powered

**Example scenario:**
- Engines at idle = low pump output
- You're moving gear AND using spoilers
- Priority valve says: "Spoilers and brakes first, gear can wait"
- **Bottom line:** You never lose control authority or braking
""")
    
    with st.expander("**7. Controls & Indications**", expanded=False):
        st.markdown("""
**Where to find hydraulic info:**
- **MFD Synoptic Page** - shows system diagram plus emergency/parking brake accumulator pressure

**HYD PUMP SOV 1 & 2 Switches:**

| Position | What it does |
|----------|--------------|
| **OPEN** | Opens the Fire Shutoff Valve (normal position) |
| **CLOSED** | Closes the FSOV - stops hydraulic fluid flow to that pump |

**When should you close the SOV?**
- Engine fire
- HYD HI TEMP message
- Hydraulic leak (follow QRH procedure)
""")
        panel_path = os.path.join(folder, "hyd_panel.png")
        if os.path.exists(panel_path):
            st.image(Image.open(panel_path), caption="HYD PUMP SOV Switches", use_container_width=True)
    
    with st.expander("**8. Pressure Indication**", expanded=False):
        st.markdown("""
**Reading the digital pressure display:**

| Color | What it means |
|-------|---------------|
| **GREEN digits** | All good - pressure is above 1800 psi |
| **YELLOW digits** | Caution - pressure is 1800 psi or below |
| **GRAY** | Just the "PSI" label |
| **YELLOW DASHED** | Data is invalid or out of range |

---

**Reading the pressure gauge (arc with pointer):**

The pointer shows the same value as the digital readout.

| Part | Normal (>1800 psi) | Low (≤1800 psi) |
|------|-------------------|-----------------|
| **Scale arc** | WHITE | YELLOW |
| **Pointer** | GREEN | YELLOW |

If the value is invalid, the pointer disappears from the display.
""")
    
    with st.expander("**9. CAS Messages**", expanded=False):
        st.markdown("**What the warning messages mean:**")
        
        cas_data = [
            ["CAUTION", "HYD HI TEMP", "Fluid is overheating - FSOVs will close automatically"],
            ["CAUTION", "HYD LO PRES", "System pressure dropped below normal - check for leaks"],
            ["CAUTION", "HYD SOV 1 (2) FAIL", "FSOV won't close when commanded - valve malfunction"],
            ["ADVISORY", "HYD SYS FAULT", "Reduced hydraulic power available - system degraded"]
        ]
        df_cas = pd.DataFrame(cas_data, columns=["Level", "Message", "What it means"])
        st.dataframe(df_cas, hide_index=True, use_container_width=True)
        
        cas_path = os.path.join(folder, "hyd_cas.png")
        if os.path.exists(cas_path):
            st.image(Image.open(cas_path), caption="CAS Messages Reference", use_container_width=True)
    
    with st.expander("**10. System Schematic**", expanded=False):
        schematic_path = os.path.join(folder, "hyd_schematic.png")
        if os.path.exists(schematic_path):
            st.image(Image.open(schematic_path), caption="Hydraulic System Schematic", use_container_width=True)

def render_landing_gear():
    st.markdown("## Landing Gear & Brakes")
    st.caption("ATA 32 | Source: Phenom 300 POH")
    
    folder = "assets/landing_gear"
    
    with st.expander("**1. System Description**", expanded=True):
        st.markdown("""
**Configuration:** Tricycle retractable gear, hydraulically powered

**The three gear legs:**
- **Nose gear (NLG):** Retracts **forward** into the fuselage
- **Main gear (MLG):** Retracts **inward** into the wing-fuselage fairing

**How the gear works:**
- Controlled by the **LDG GEAR lever** on the main instrument panel
- Two positions: **UP** (retract) and **DN** (extend)
- Command is **electrical**, actuation is **hydraulic**

**Built-in safety (ground lock):**
- An interlock **prevents** moving the lever to UP while on the ground
- In an emergency, you can override this with the **DN LCK REL** button on the LDG GEAR panel
""")
        lg_overview_path = os.path.join(folder, "lg_overview.png")
        if os.path.exists(lg_overview_path):
            st.image(Image.open(lg_overview_path), caption="Landing Gear Overview", use_container_width=True)
        
        lg_control_path = os.path.join(folder, "lg_control_panel.png")
        if os.path.exists(lg_control_path):
            st.image(Image.open(lg_control_path), caption="LDG GEAR Control Panel", use_container_width=True)
    
    with st.expander("**2. Landing Gear Operation**", expanded=False):
        st.markdown("""
**RETRACTION (Lever UP)**

When you move the lever to UP:
1. Electrical command activates the hydraulic retraction actuators
2. **Wheels are automatically braked** to stop spinning
3. Gear retracts and locks into the **uplock box**
4. All gear doors close

---

**NORMAL EXTENSION (Lever DN)**

When you move the lever to DN:
1. Uplock box releases each gear leg
2. Gear extends under hydraulic power
3. **Down lock mechanism** holds gear in extended position
4. Green lights illuminate when locked down

**What's normal:**
- The nose gear often takes **longer** to show a green light than the mains
- All three legs don't necessarily lock at the exact same time
- A short delay in position indications is **normal** - don't panic
""")
    
    with st.expander("**3. Emergency Extension (Free-Fall)**", expanded=False):
        st.markdown("""
**What it's for:** Extends the gear when normal hydraulic extension fails

**Emergency handle location:** On the cockpit **floor**

**How it works:**
1. Pull the free-fall handle
2. This activates the **free-fall selector valve**
3. Valve dumps all hydraulic pressure from the gear lines
4. Up locks are **mechanically released**

**What happens next:**
- **Gravity and airflow** push the gear down (no hydraulics needed)
- **Down lock mechanism** locks the gear in place
- Green DN lights appear only **after** you move the LDG GEAR lever to DN

**Important details:**
- Maximum pull force needed: **25 kg (55 lb)**
- If a main gear won't lock, you may need to **slip the airplane** to use airflow to push that leg into the lock
""")
        freefall_path = os.path.join(folder, "freefall_handle.png")
        if os.path.exists(freefall_path):
            st.image(Image.open(freefall_path), caption="Free-Fall Handle Location", use_container_width=True)
    
    with st.expander("**4. Uplock Box**", expanded=False):
        st.markdown("""
**What it does:** Holds each gear leg **up and locked** when retracted

**Two ways to unlock it:**
1. **Normal:** Hydraulic actuator releases the lock when you select gear DN
2. **Emergency:** Mechanical release via the free-fall handle (no hydraulics needed)

**How the system knows the gear is up:**
- Each uplock box has a **proximity sensor**
- When the gear locks in, the sensor signals "up and locked" to the cockpit
""")
    
    with st.expander("**5. Position & Warning Subsystem**", expanded=False):
        st.markdown("""
**Sensors that tell the system where the gear is:**
- **Down and locked** proximity switches (one per leg)
- **Up and locked** proximity switches (one per leg)
- **Weight On Wheels (WOW)** switches - two per main gear
- **Lever position** micro switches

**What happens with this data:**
- The system combines all these signals to show you gear position
- Also generates CAS messages when something is wrong

**Weight On Wheels (WOW) - important for many systems:**
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

**With flaps at 0, 1, or 2:**

The horn sounds when **ALL** of these are true:
- Below **700 ft AGL** (radio alt) or within **700 ft** of field elevation
- Airspeed below **160 KIAS**
- Power is reduced (thrust levers below **26°/40°** depending on engine status)

---

**With flaps at 3 or FULL:**

- Warning sounds **regardless** of speed, altitude, or power setting
- **Cannot be silenced** with the WRN INHIB button

---

**If flaps have failed:**

- Warning sounds if descending through **700 ft** above field elevation

**Note:** Pre-Mod SB 505-27-0011 aircraft: FULL flap position is blocked by a mechanical stop.
""")
    
    with st.expander("**7. Brakes System Overview**", expanded=False):
        st.markdown("""
**Two separate brake systems:**
1. **Main brakes** - your normal braking system
2. **Emergency/Parking brakes** - backup and parking

Both use hydraulic pressure from the main hydraulic system.

---

**Main Brake System - what it does:**
- Applies brake pressure based on how hard you push the pedals
- Provides **antiskid protection** to prevent skidding
- Minimizes stopping distance

**Emergency/Parking Brake - what it does:**
- Stops the airplane if main brakes fail
- Holds the airplane parked (works even with hydraulics off)

---

**How the main brakes work (brake-by-wire):**
1. You push the rudder pedals (top portion)
2. **Pedal transducers** sense how much pressure you're applying
3. Signal goes to the **Brake Control Unit (BCU)**
4. BCU commands the **brake control valves (BCVs)** - one per wheel
5. BCVs apply the right amount of hydraulic pressure to the brakes

**Key component - the BCU:**
- Controls left and right brakes **independently**
- Connected to the **Emergency Bus** (important for emergencies!)
- Monitors: wheel speed, pedal position, and brake pressure
""")
    
    with st.expander("**8. Brake System Functions**", expanded=False):
        st.markdown("""
The brake system has **four automatic protection functions:**

---

**A. LOCKED WHEEL PROTECTION**

**Purpose:** Prevents a tire from blowing out if one wheel locks up

**How it works:**
- BCU compares left and right wheel speeds
- If one wheel drops to **≤30%** of the other's speed, it's "locked"
- System **releases pressure** on that wheel so it can spin back up
- Normal braking resumes when the slow wheel reaches **70%** of the other wheel's speed

**Below 30 kt:** Protection turns off so you can use differential braking for steering

---

**B. ANTISKID PROTECTION**

**Purpose:** Maximizes braking without skidding

**How it works:**
- If a wheel starts to skid, the system **reduces brake pressure** automatically
- This lets the tire regain grip, then reapplies pressure
- Active when both wheels are above **30 kt**

**Below 10 kt:** Antiskid turns off - you can lock a wheel for pivoting

**Important:** Antiskid is **NOT available** on the emergency/parking brake!

---

**C. TOUCHDOWN PROTECTION**

**Purpose:** Prevents braking before the wheels spin up at landing

**How it works:**
- Even if you're pressing the pedals in the flare, **no brake pressure is applied**
- Wheels are allowed to spin up freely at touchdown
- Prevents tire blowout from sudden braking on a stationary wheel

**When it cancels:**
- Both wheels exceed **60 kt** (even before WOW says "on ground")
- **3 seconds** after WOW indicates "on ground" (regardless of speed)
- After touchdown, the spin-up threshold drops from **60 → 30 kt** over 3 seconds

**Note:** Below **10 kt** with WOW showing airborne, normal braking is disabled

---

**D. GEAR RETRACT BRAKING**

**Purpose:** Stops the wheels from spinning before they enter the wheel well

**How it works:**
1. When WOW = airborne AND you select gear UP
2. BCU waits **3 seconds** (for hydraulic demand to settle)
3. Then applies ramped brake pressure to stop the wheels
4. If wheels aren't stopped in **10 seconds**, system resets and tries again
5. When wheel speed = zero, brake pressure is released
""")
    
    with st.expander("**9. Initiated Built-In Test (IBIT)**", expanded=False):
        st.markdown("""
**What it is:** An automatic self-test the brake system runs in flight

**When it runs (all conditions must be true):**
- Gear lever moves from UP to DN
- At least one gear shows down and locked
- WOW indicates airborne
- Both wheels are stationary
- 10-second delay (lets hydraulic pressure stabilize)

**What it tests:**
- Runs the brake pressure loop through its full range
- Checks the SOV, brake control valves, and pressure transducers

**Duration:** About **5 seconds**
""")
    
    with st.expander("**10. Emergency/Parking Brake**", expanded=False):
        st.markdown("""
**Two uses for this system:**
1. **Parking brake** - hold the airplane while parked
2. **Emergency brake** - stop the airplane if main brakes fail

---

**The T-Handle:**
- Located on the **center pedestal**
- Connected to the brake valve by a steel cable
- Pull up = brakes ON | Push down = brakes OFF
- You can **modulate** pressure by how much you pull

---

**The Accumulator (stores pressure for emergencies):**
- Isolated from the main hydraulic system by a check valve and shutoff valve
- Shutoff valve opens during engine start (on ground, both thrust levers at idle for **>50 seconds**)
- Holds enough pressure for **6 full brake applications**

---

**How you know it's working:**
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
**FUSIBLE PLUGS**

**What they are:** Safety plugs in the main wheels with a metal core that melts when hot

**Why they exist:**
- After a high-energy event (like an RTO), brakes get extremely hot
- Heat transfers to the tires, which could explode in the wheel well
- The fusible plug melts and **releases tire pressure safely** before that can happen

**Location:** Main wheel assemblies only

---

**BRAKE WEAR PINS**

**What they are:** Visual indicators showing how much brake pad is left

**How to check:**
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
    
    with st.expander("**13. CAS Messages**", expanded=False):
        st.markdown("**What these warning messages mean:**")
        
        cas_data = [
            ["WARNING", "LG LEVER DISAG", "Gear position doesn't match lever position - something's wrong"],
            ["WARNING", "ANTI-SKID FAIL", "Antiskid protection is not working - expect longer stopping distances"],
            ["WARNING", "BRK FAIL", "Lost braking on one main wheel - use emergency brakes if needed"],
            ["CAUTION", "EMER BRK LO PRES", "Emergency/parking brake accumulator is running low on pressure"],
            ["CAUTION", "LG WOW SYS FAIL", "Weight on wheels sensors are disagreeing - affects many systems"],
            ["CAUTION", "PARK BRK NOT REL", "Parking brake is still set - release before takeoff!"]
        ]
        df_cas = pd.DataFrame(cas_data, columns=["Level", "Message", "What it means"])
        st.dataframe(df_cas, hide_index=True, use_container_width=True)
    
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

def render_limitations():
    st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>Phenom 300</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Netjets Edition</p>", unsafe_allow_html=True)
    if st.button("Home", use_container_width=False, type="primary", key="home_btn"):
        navigate('home')
        st.rerun()
    
    st.markdown("## Limitations & Performance")
    st.caption("Source: Netjets EASA / FlightSafety Training Guide")
    
    with st.expander("**1. Structural & Weight Limits**", expanded=True):
        st.markdown("""
**Weight Limits (Lbs)**

| Limit | Value |
|-------|-------|
| **MRW** (Max Ramp Weight) | 18,497 lb |
| **MTOW** (Max Takeoff Weight) | 18,387 lb |
| **MLW** (Max Landing Weight) | 17,042 lb |
| **MZFW** (Max Zero Fuel Weight) | 14,220 lb |

**Study Tip:** Check fuel burn! You cannot land with full tanks if departing at MTOW.

---

**Baggage Loading**
- Max Fwd Baggage (Nose): **110 lb**
- Max Aft Baggage (Tail): **463 lb**

---

**Runway & Environment**
- Max Airport Elevation: **8,300 ft**
- Runway Slope: **-2% to +2%**
- Max Operating Altitude: **45,000 ft**
- Max Altitude (Flaps Extended): **18,000 ft**
""")
    
    with st.expander("**2. Speed Limitations (V-Speeds)**", expanded=False):
        st.markdown("""
**Operational Speeds (KIAS)**

| Speed | Value |
|-------|-------|
| **VMO / MMO** | 320 KIAS / 0.78 M |
| **VA / VO** (Maneuvering Speed) | 205 KIAS |
| **Turbulence Penetration** | 232 KIAS / 0.65 M |
| **Max Tire Ground Speed** | 182 kt |

---

**Gear Speeds**
- **VLO** (Operating/Extension): **250 KIAS**
- **VLE** (Extended): **250 KIAS**

---

**Flap Speeds (VFE)**

| Flaps | Max Speed |
|-------|-----------|
| Flaps 1 | 180 KIAS |
| Flaps 2 & 3 | 170 KIAS |
| Flaps 4 (Full) | 160 KIAS |

---

**Minimum Manoeuvring Speeds**

| Gear/Flap Setting | Airspeed |
|-------------------|----------|
| UP / ZERO | 150 KIAS |
| UP / 1 | 140 KIAS |
| * UP / 2 | VREF + 10 KIAS |
| * DN / 3 | VREF + 10 KIAS |
| * DN / FULL | VREF + 10 KIAS |

\\* Max 30° AOB

---

**Load Factor Limit**
- Flaps 0: **3 G**
- Flaps Down: **2 G**

---

**Take-Off Pitch Trim Settings**

| %MAC | FLAP 1 | FLAP 2 |
|------|--------|--------|
| 19 | 7.7 | 6.8 |
| 24 | 8.9 | 8.2 |
| 27 | 9.6 | 9.0 |
| 30 | 10.3 | 9.9 |
| 33 | 11.0 | 10.7 |
| 36 | 11.7 | 11.5 |
| 39 | 12.4 | 12.4 |
| 42 | 12.4 | 12.4 |
""")
    
    with st.expander("**3. Wind Limitations**", expanded=False):
        st.markdown("""
**Takeoff & Landing**

| Condition | Limit |
|-----------|-------|
| Max Tailwind | 10 kt |
| Max Crosswind (Takeoff - Demonstrated) | 25 kt |
| Max Crosswind (Takeoff - Static) | 18 kt |
| Max Crosswind (Landing - Demonstrated) | 28 kt |
""")
    
    with st.expander("**4. Engine Limits (PW535E)**", expanded=False):
        st.caption("Source: Phenom 300 AFM Rev.19 (March 20, 2020)")
        
        data = [
            ["Maximum", "10 min", "725", "101", "100", "45 - 160", "10 - 132.2"],
            ["Takeoff", "5 min", "700", "101", "100", "45 - 160", "10 - 132.2"],
            ["MCT / CLB", "-", "680", "-", "-", "45 - 160", "10 - 132.2"],
            ["Ground Idle", "-", "-", "Min (OEI) 55.1 / (AEO) 51.2", "-", "25 - 160", "-40 - 132.2"],
            ["Flight Idle", "-", "-", "55.1", "-", "-", "-"],
            ["Starting", "5 sec", "765", "103", "102", "-", "-40 min"],
            ["Transient", "20 sec", "765", "103", "102", "0 - 20", "-"],
            ["Transient", "200 sec", "-", "-", "-", "-", "140.5"],
            ["Transient", "400 sec", "-", "-", "-", "20 - 270", "-"]
        ]
        
        df_engine = pd.DataFrame(data, columns=[
            "Thrust Setting", "Time Limit", "Max ITT (°C)", "N2 (%)", "N1 (%)", "Oil Pressure (psid)*", "Oil Temp (°C)**"
        ])
        
        st.dataframe(df_engine, hide_index=True, use_container_width=True)
        
        st.markdown("**Notes**")
        st.info("""
\\* For N2 speeds above 60% the oil pressure below 45 psid is undesirable and should be tolerated only for the completion of the flight, preferably, at reduced power setting.

\\*\\* For operation in severe cold environments, following engine start, it is permissible to operate the engine up to 70% N2, in order to warm the oil to the minimum temperature for normal operation (above 10°C).
""")
        
        st.markdown("---")
        st.markdown("**Starter Limits**")
        
        starter_data = [
            ["Motoring Number 1", "60 sec"],
            ["Motoring Number 2", "60 sec"],
            ["Motoring Number 3", "15 min"],
            ["Motoring Number 4", "30 min"]
        ]
        df_starter = pd.DataFrame(starter_data, columns=["Motoring", "Duration"])
        st.dataframe(df_starter, hide_index=True, use_container_width=True)
    
    with st.expander("**5. Fuel**", expanded=False):
        st.markdown("""
- Max Fuel Capacity: **5,401 lb**
- Max Useable Fuel: **5,352 lb**
- Max Fuel Imbalance: **220 lb**
- Min Fuel Tank Temp: **-37°C**
- Max Fuel Tank Temp (ground): **52°C**
- Max Fuel Tank Temp (flight): **80°C**
- **XFEED:** Use is restricted for Takeoff and Landing
""")
    
    with st.expander("**6. Electrical**", expanded=False):
        st.markdown("""
- Min Batt Voltage for Engine Start: **24 V**
- Min GPU Voltage to Charge Batt: **27 V**
- Max Generator Load on Ground: **330 A**
- Max Generator Load in Flight: **390 A**
""")
    
    with st.expander("**7. Air Management System (Pressurization)**", expanded=False):
        st.markdown("""
- Max Diff Press: **9.4 psi**
- Max Diff OverPress: **9.6 psi**
- Max Diff Negative Press: **-0.3 psi**
- Max Diff Press for T/O & Landing: **0.2 psi**
""")
    
    with st.expander("**8. Ice & Rain Protection**", expanded=False):
        st.markdown("""
- Max Airspeed in Icing w/ YD Off: **180 KIAS**
- Min Airspeed in Icing WingStab A/I Inhibited or Armed: **165 KIAS**
- Min Airspeed in Icing WingStab A/I Uninhibited: **150 KIAS**
- Max Altitude for Operation AEO: **45,000 ft**
- Max Altitude for Operation OEI: **15,000 ft**
- Min Temp for Landing in Icing: **-38°C**
""")
    
    with st.expander("**9. Autoflight / YD**", expanded=False):
        st.markdown("""
- Min Engagement Height (AEO): **600 ft**
- Min Engagement Height (OEI): **1,000 ft**
- Min Use Height (AEO): **195 ft**
- Min Use Height (OEI): **220 ft**
""")
    
    with st.expander("**10. Wake Turbulence (RECAT-EU)**", expanded=False):
        st.markdown("**RECAT-EU Wake Turbulence Groups**")
        
        recat_data = [
            ["Super Heavy (A)", ">100T", ">72 m", "Super (J) A380"],
            ["Upper Heavy (B)", ">100T", "60 - 72 m", "Heavy (H) ≥136000lbs"],
            ["Lower Heavy (C)", ">100T", ">52 m", "Heavy (H) ≥136000lbs"],
            ["Upper Medium (D)", "15 - 100T", ">32 m", "Medium (M) >7000lbs - <136000"],
            ["Lower Medium (E)", "15 - 100T", "Up to 32 m", "Medium (M) >7000lbs - <136000"],
            ["Light (F)", "Up to 15T", "-", "Light (L) ≤7000lbs"]
        ]
        df_recat = pd.DataFrame(recat_data, columns=["Category", "Max Take off Mass", "Wing Span", "Current ICAO Categories"])
        st.dataframe(df_recat, hide_index=True, use_container_width=True)
        
        st.markdown("---")
        st.markdown("**Departure Separation Time (Secs) - Following Aircraft: Light**")
        
        dep_data = [
            ["Super Heavy", "180"],
            ["Upper Heavy", "140"],
            ["Lower Heavy", "120"],
            ["Upper Medium", "100"],
            ["Lower Medium", "80"]
        ]
        df_dep = pd.DataFrame(dep_data, columns=["Leading Aircraft", "Time (sec)"])
        st.dataframe(df_dep, hide_index=True, use_container_width=True)
        
        st.markdown("---")
        st.markdown("**Approach Separation Distance (NMs) - Following Aircraft: Light**")
        
        app_data = [
            ["Super Heavy", "8"],
            ["Upper Heavy", "7"],
            ["Lower Heavy", "6"],
            ["Upper Medium", "5"],
            ["Lower Medium", "4"],
            ["Light", "3"]
        ]
        df_app = pd.DataFrame(app_data, columns=["Leading Aircraft", "Distance (NM)"])
        st.dataframe(df_app, hide_index=True, use_container_width=True)

def render_memory():
    st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>Phenom 300</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Netjets Edition</p>", unsafe_allow_html=True)
    if st.button("Home", use_container_width=False, type="primary", key="home_btn"):
        navigate('home')
        st.rerun()
    
    st.markdown("## Memory Items")
    st.caption("Source: Phenom 300 QRH Rev.19 (March 20, 2020)")
    
    st.markdown("""
    <style>
    [data-testid="stExpander"] details summary p {
        color: #CC0000 !important;
        font-weight: bold !important;
    }
    [data-testid="stExpander"] table {
        width: 100% !important;
    }
    [data-testid="stExpander"] table th:first-child,
    [data-testid="stExpander"] table td:first-child {
        width: 50% !important;
    }
    [data-testid="stExpander"] table th:last-child,
    [data-testid="stExpander"] table td:last-child {
        width: 50% !important;
        text-align: left !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    with st.expander("**SMOKE EVACUATION**", expanded=False):
        st.markdown("""
| Item | Action |
|------|--------|
| Oxygen Masks | DON, EMERGENCY |
| Dilution Valve | CLOSED |
| Smoke Goggles | DON |
| Communication | ESTABLISH |
| Oxygen Knob | CREW ONLY |
| DUMP Button | PUSH IN |
| ECS Knob | OFF VENT |
""")
    
    with st.expander("**SMOKE / FIRE / FUME**", expanded=False):
        st.markdown("""
| Item | Action |
|------|--------|
| Oxygen Masks | DON, EMERGENCY |
| Dilution Valve | CLOSED |
| Smoke Goggles | DON |
| Communication | ESTABLISH |
| DUMP Button | PUSH IN |
""")
    
    with st.expander("**E1(2) FIRE**", expanded=False):
        st.markdown("""
**Affected Engine:**

| Item | Action |
|------|--------|
| Thrust Lever | IDLE |
| START/STOP Knob | STOP |
| SHUTOFF Button | PUSH IN |

*On ground or if fire persists after 30 seconds in flight:*

| Item | Action |
|------|--------|
| BOTTLE Switch | DISCH |
""")
    
    with st.expander("**ENGINE FIRE, SEVERE DAMAGE or SEPARATION**", expanded=False):
        st.markdown("""
**Affected Engine:**

| Item | Action |
|------|--------|
| Thrust Lever | IDLE |
| START/STOP Knob | STOP |
| SHUTOFF Button | PUSH IN |

*Wait 30 seconds and if fire persists:*

| Item | Action |
|------|--------|
| BOTTLE Switch | DISCH |
""")
    
    with st.expander("**DUAL ENGINE FAILURE**", expanded=False):
        st.markdown("""
| Item | Action |
|------|--------|
| Thrust Lever | IDLE |
| Crew Oxygen Masks | DON, 100% |
| Communication | ESTABLISH |
""")
    
    with st.expander("**ENGINE ABNORMAL START**", expanded=False):
        st.markdown("""
**Affected Engine:**

| Item | Action |
|------|--------|
| START/STOP Knob | STOP |
""")
    
    with st.expander("**ELEC EMERGENCY**", expanded=False):
        st.markdown("""
| Item | Action |
|------|--------|
| PRESN MODE Switch | MAN |
| CABIN ALT Switch | HOLD DOWN FOR 10 SEC |

*If at or above 25,000 ft:*

| Item | Action |
|------|--------|
| Rudder Pedals | FIXED |

*If above 10,000 ft:*

| Item | Action |
|------|--------|
| CAB ALTITUDE HI Procedure | ACCOMPLISH |
""")
    
    with st.expander("**ELEC XFR FAIL**", expanded=False):
        st.markdown("""
| Item | Action |
|------|--------|
| ELEC EMER Button | PUSH IN |
""")
    
    with st.expander("**EMERGENCY EVACUATION**", expanded=False):
        st.markdown("""
| Item | Action |
|------|--------|
| Thrust Levers | IDLE |
| Emergency/Parking Brake | ON |
| START/STOP Knobs | STOP |
| FIRE SHUTOFF Buttons | PUSH IN |
| PRESN MODE Switch | MAN |
| DUMP Button | PUSH IN |
| ATC | NOTIFY |
| Emergency Evacuation | PERFORM |
| BATT 1 & 2 Switches | OFF |
""")
    
    with st.expander("**CAB ALTITUDE HI**", expanded=False):
        st.markdown("""
| Item | Action |
|------|--------|
| Oxygen Masks | DON, 100% |
| Communication | ESTABLISH |
| SIGNS/OUTLET Switch | PED BELTS / OFF |
| Altitude | Max 10,000ft or MEA (whichever is higher) |
| Thrust Levers | IDLE |
| SPEED BRAKE Switch | OPEN |
| Airspeed | 250 KIAS / MMO Max |
| LDG GEAR Lever | DN |
| Transponder | 7700 |
| ATC | NOTIFY |
""")
    
    with st.expander("**EMERGENCY DESCENT**", expanded=False):
        st.markdown("""
| Item | Action |
|------|--------|
| SIGNS/OUTLET Switch | PED BELTS / OFF |
| Altitude | Max 10,000ft or MEA (whichever is higher) |
| Thrust Levers | IDLE |
| SPEED BRAKE Switch | OPEN |
| Airspeed | 250 KIAS / MMO Max |
| LDG GEAR Lever | DN |
| Transponder | 7700 |
| ATC | NOTIFY |
""")
    
    with st.expander("**LG WOW SYS FAIL**", expanded=False):
        st.markdown("""
*If associated with engine failure and obstacle clearance, simultaneously proceed:*

| Item | Action |
|------|--------|
| DN LCK REL Button | PRESS |
| LDG GEAR Lever | UP |
""")
    
    with st.expander("**GEAR LEVER CANNOT BE MOVED UP**", expanded=False):
        st.markdown("""
*If associated with engine failure and obstacle clearance, simultaneously proceed:*

| Item | Action |
|------|--------|
| DN LCK REL Button | PRESS |
| LDG GEAR Lever | UP |
""")
    
    with st.expander("**INADVERTANT PUSHER ACTUATION**", expanded=False):
        st.markdown("""
| Item | Action |
|------|--------|
| PUSHER CUTOUT Button | PUSH IN |
""")

def render_flight_profiles():
    st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>Phenom 300</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Netjets Edition</p>", unsafe_allow_html=True)
    if st.button("Home", use_container_width=False, type="primary", key="home_btn"):
        navigate('home')
        st.rerun()
    
    st.markdown("## Flight Profiles")
    st.caption("Netjets Operations Manual | EMB-505")
    
    folder = "assets/flight_profiles"
    
    st.markdown("### Normal Procedures")
    
    with st.expander("**1. Normal Take-off and Noise Abatement**", expanded=False):
        st.markdown("""
**Takeoff Sequence:**
- **Brakes Released** - "Thrust Set"
- **"60"** - Speed check callout
- **"V1"** - Takeoff decision speed
- **"ROTATE"** - Rotate initially to 15° pitch

**After Liftoff:**
- **POSITIVE RATE** - "GEAR UP"
- PM: Select FLC, Set 150 KIAS

**Climb Phase:**
- **1000 FT AAL** - Set thrust at or below CLB, "FLAP 0"
- **3000 FT AAL** - 225 KIAS or max SID speed
- PM: Select YD ON or engage AP on PF command, LDG/TAXI light TAXI

**At Transition Altitude or Cleared to Flight Level:**
- Set STD, AFTER T/O CHECKLIST

**FL 100 and Above:**
- CLIMB CHECKLIST

**Notes:**
- FMS can be used for any PRNAV/RNAV SID, or a conventional SID from the database backed up with NAV aids
- Minimum AP engage height: 600' AAL

**Autopilot Modes:**
- Takeoff: FMS + TO/ALTS or HDG + TO/ALTS
- After PM Select FLC: FMS + FLC/ALTS or HDG + FLC/ALTS
- After 1000 FT: HDG or FMS + FLC or VS
""")
        img_path = os.path.join(folder, "normal_takeoff_cat1.jpg")
        if os.path.exists(img_path):
            st.image(Image.open(img_path), caption="Normal Take-off Profile", use_container_width=True)
    
    with st.expander("**2. CAT I Approach**", expanded=False):
        st.markdown("""
**Pattern Entry:**
- **DOWNWIND** - 170 KIAS, N1 +/- 55%
- APR SELECTED: HDG + AP YD + VS (or LOC + GS when available)

**Configuration Points (LATEST points):**
| DME | Configuration | Speed |
|-----|--------------|-------|
| 6 DME | Flap 1 | 160 KIAS |
| 5 DME | Gear Down, Flap 2 | 160 KIAS |
| 4 DME | Flap 3 (or FULL), V_AP | V_AP |

**LOC INTERCEPT:**
- LOC + AP YD + ALT + GS

**GS CAPTURE:**
- LOC + AP YD + GS
- Set AAD to Missed App Alt

**BEFORE LANDING CHECKLIST**

**Stabilised Approach Point:**
- Stabilised or Go Around

**Final Approach:**
- V_REF at runway

**At DA:**
- "MINIMUMS" - Continue or Go Around

**Notes:**
- To ensure a stabilised approach, 6, 5, and 4 DME are the LATEST points at which configuration changes shall be made
- If an earlier configuration is planned, it should be briefed in advance
- When flap configuring involves bypassing a position, flap lever should be paused at the intermediate position before selecting desired setting
""")
    
    with st.expander("**3. Visual Approach**", expanded=False):
        st.markdown("""
**Pattern Entry:**
- **1500ft Downwind** - 150kts, N1 +/- 50%
- HDG + AP YD + ALT

**Abeam Threshold:**
- Start Timing, Gear Down, Flap 2

**Base Turn:**
- Max bank 30°, Start descent
- HDG + AP YD + VS

**Finals Turn:**
- Aim to complete at approx 600'
- V_AP, N1 +/- 48%

**Min 125kts** during turn

**Before Landing:**
- Flap 3 (OR FULL), Before Ldg Checklist
- 140kts

**Final Approach:**
- 150kts on final

**Stabilised Approach Point:**
- Stabilised or Go Around (Wings level by 300')
- V_REF

**Recommended Timings:**
- 3 secs per 100' AAL +/- wind correction
- (1500ft AAL nil wind = 45 secs)

**Note:** When flap configuring involves bypassing a position, flap lever should be paused at the intermediate position before selecting desired setting

**Deviations:** Acceptable provided they are briefed beforehand and stable criteria are satisfied
""")
        img_path = os.path.join(folder, "visual_circling.jpg")
        if os.path.exists(img_path):
            st.image(Image.open(img_path), caption="Visual & Circling Approach Profiles", use_container_width=True)
    
    with st.expander("**4. Circling Approach**", expanded=False):
        st.markdown("""
**Pattern Setup:**
- Follow published procedure for Precision or Non-precision Approach
- SET AAD to CIRCLING ALTITUDE

**1000FT AAL:**
- Aircraft in Circling Approach Configuration
- Consider pre-setting the HDG bug to the required circling hdg

**Before FAF:**
- Gear Down, Flap A/R

**Final Approach (Instrument):**
- LOC + AP YD + VS
- **Caution:** Do not select APR if there is vertical guidance on the approach or the AAD altitude will not be captured. VS should be used to maintain desired vertical profile

**170kts** during circling

**Downwind Turn:**
- 45°/45 secs, HDG + AP YD + ALT
- Correct for wind, Remain within circling radius

**Recommended Timings:** 3 secs per 100' AAL +/- wind correction

**Base Turn:**
- Flap 3 (or FULL), BEFORE LANDING CHECKLIST

**Stabilised Approach Point:**
- V_REF (Min wings level by 300'), Stabilised or Go Around

**Circling Minima:**
| CAT | MAX SPEED | RADIUS | MAX Vref | Min Vis |
|-----|-----------|--------|----------|---------|
| B | 135kts | 2.66nm | 120kts | 2800m |
| C | 180kts | 4.2nm | 140kts | 3700m |

**Caution:** Should a missed approach be required any time after commencing circling it will need to comply with the Missed Approach Procedure for the active instrument approach
""")
    
    with st.expander("**5. Steep Approach**", expanded=False):
        st.markdown("""
**Pattern Entry:**
- **FINAL VECTOR** - Flap 1
- HDG + AP YD + VS (or LOC + ALTS GS)

**BASE LEG:**
- 170 KIAS, Flap 1

**Configuration:**
- **2NM to G/S** - Gear Down, Flap 2
- **1NM to G/S** - Flap FULL, AAD set to Missed App Alt

**LOC INTERCEPT:**
- LOC + AP YD + ALT + GS

**GS CAPTURE:**
- LOC + AP YD + GS
- PM Speedbrake OPEN
- Speed V_REF STEEP

**BEFORE LANDING CHECKLIST**

**At DA:**
- "MINIMUMS"

**Stabilised Approach Point:**
- Stabilised or Go Around
- V_REF STEEP

**GO AROUND (from Steep):**
- Flap 2, Min Speed V_AC
- PM Verify Speed Brake CLOSED
- Speed Brake switch to CLOSE as after take-off flow item

**Important Notes:**
- Flap must be in the FLAP FULL position before setting SPEED BRAKE OPEN
- When flap configuring involves bypassing a position, flap lever should be paused at the intermediate position before selecting desired setting
- Deviations from this profile are permitted provided they are briefed in advance and all Operational Limitations are observed
- AFM Procedures and Limitations for Steep Approach Landing should be reviewed prior to carrying out a Steep Approach
""")
        img_path = os.path.join(folder, "steep_goaround.jpg")
        if os.path.exists(img_path):
            st.image(Image.open(img_path), caption="Steep Approach & All Engines Go-Around Profiles", use_container_width=True)
    
    with st.expander("**6. All Engines Go-Around**", expanded=False):
        st.markdown("""
**Initiation (from Stabilised Final Approach Flap 3/Full):**

**"GO AROUND, FLAP 1 (or 2)":**
- Simultaneously: Push TO/GA button, Set Thrust A/R, Pitch to the FD
- PM: Set Flap 1 (or 2)
- ROL + GA

**"POSITIVE RATE" - "Gear Up":**
- PM: Select Gear Up
- FMS + FLC

**PM Actions:**
- Select FLC, Set 150 KIAS
- Select NAV or HDG

**PF:**
- Manages thrust to control ROC

**1000'AAL:**
- Flap 0, Consider A/P ON

**After Actions:**
- PM Select YD ON or engage AP on PF command
- LDG/TAXI light TAXI
- If after Steep Approach: SPDBRK Switch to closed

**AFTER T/O CHECKLIST**

**Notes:**
- Minimum AP engage height: 600' AAL
- FMS mode should only be engaged if Missed Approach Procedure is correctly programmed into the FMS
- When flap configuring involves bypassing a position, flap lever should be paused at the intermediate position before selecting desired setting
""")
    
    st.markdown("---")
    st.markdown('<h3 style="color: #CC0000;">Emergency Procedures</h3>', unsafe_allow_html=True)
    
    with st.expander("**1. Rejected Take-off (RTO)**", expanded=False):
        st.markdown("""
<div style="background-color: #fff3cd; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
<strong>A REJECTED TAKE OFF CAN BE CALLED BY EITHER PILOT</strong>
</div>

**Abort Criteria:**

**BELOW 60 KTS - Abort for:**
- ANY System Failure or Fault Annunciation

**BETWEEN 60 KTS AND V1 - Abort for:**
- Any sign of FIRE
- Loss of Thrust or Engine Failure
- Loss of Directional Control
- Any RED CAS MESSAGE

---

**RTO Procedure:**

**"STOP STOP"** - Called by initiating pilot

**PF Actions:**
| Item | Action |
|------|--------|
| THRUST LEVERS | IDLE |
| BRAKES | APPLY MAXIMUM |
| DIRECTIONAL CONTROL | MAINTAIN |

**PM Actions:**
- CONFIRM SPOILERS DEPLOYED
- INFORM ATC "Fraction 123 Stopping"

---

**ACTIONS AFTER STOPPING:**
- Parking Brake ON
- Remain on Runway until diagnosis is complete
- Consider if Emergency Services are required
- Consider if an Emergency Evacuation is required
- Consider taxiing clear of the runway if able
- Ensure ATC and PAX aware of intentions
- Consider brake cooling time if another take off is to be attempted

**Note:** As aircraft slows, consider turning into wind, especially if stopping because of FIRE
""", unsafe_allow_html=True)
        img_path = os.path.join(folder, "rto_efato.jpg")
        if os.path.exists(img_path):
            st.image(Image.open(img_path), caption="RTO & Engine Failure After V1 Profiles", use_container_width=True)
    
    with st.expander("**2. Engine Failure After V1 (EFATO)**", expanded=False):
        st.markdown("""
<div style="background-color: #ffcccb; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
<strong>ENGINE FAILURE</strong> - Continue takeoff, maintain directional control
</div>

**At V1 - ENGINE FAILURE:**
- Continue takeoff

**"ROTATE":**
- Rotate to initial pitch attitude
- Flap 1: 10.5°
- Flap 2: 8°

**"POSITIVE RATE" - "GEAR UP":**
- PM Select FLC, Set V2
- Low Bank A/R: HDG + FLC/ALTS or FMS + FLC/ALTS

**Climb at V2** (Max Speed V2 + 10)

**1000FT AAL:**
- Consider AP (YD OFF)

**MEMORY ITEMS WHEN SAFE TO CARRY OUT**

**MAA from Flygprestanda, 1500' AAL MIN:**

**FLYGPRESTANDA:**
- Flap retraction point should be clearly briefed if an Emergency Turn Procedure is called for

**Acceleration:**
- Set speed V_FS

**CON Thrust, Disengage Low Bank** (see note)
- Speed V2 + 10, Flap 0

**EMER/NORMAL/ABNORMAL CHECKLISTS**

**ATC Communication:**
- A MAYDAY call should be made when safe to do so, ideally before reaching 1000' in order for ATC to coordinate other traffic, especially if Flygprestanda dictates an Emergency Turn Procedure

**Notes:**
- V_FS provides max angle of climb and should be used if obstacle clearance remains a factor. If terrain clearance is assured speed may be increased to 150 kts
- Low Bank should only be disengaged when IAS above V_FS
""", unsafe_allow_html=True)
    
    with st.expander("**3. Engine Failure During the Cruise**", expanded=False):
        st.markdown("""
<div style="background-color: #ffcccb; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
<strong>E1(2) FAIL</strong>
</div>

**PF Actions:**
- Apply CON Thrust, maintain Altitude
- Allow speed to reduce towards Driftdown Speed (initially 165/140KIAS, Ice Protection ON/OFF)

**PM Actions:**
- Check Driftdown Speed and Altitude in QRH
- Advise ATC (MAYDAY/PAN PAN)

**PM:** Action E1(2) FAIL Checklist when called for by PF

**Approaching Driftdown Speed:**
- HDG + AP YD + FLC/ALTS

**Descent to MSA:**

**Note:** Typical Driftdown Altitude at mid-range weights will be between FL240 and FL290. If Icing conditions are encountered or expected, Max Driftdown Altitude will be FL 150 - due allowance should be made when planning descent

---

**CONSIDERATIONS:**
- Terrain (MSA)
- Icing
- Suitable Alternates
- Fuel Crossfeed
- Restart?
- DORDAR

**Caution:** Max Altitude on Single Bleed Source is 36000' - descent below this altitude should be achieved before employing driftdown procedures
""", unsafe_allow_html=True)
        img_path = os.path.join(folder, "cruise_oei_apch.jpg")
        if os.path.exists(img_path):
            st.image(Image.open(img_path), caption="Engine Failure During Cruise & OEI Approach Profiles", use_container_width=True)
    
    with st.expander("**4. One Engine Inoperative Approach and Landing**", expanded=False):
        st.markdown("""
<div style="background-color: #e7f3ff; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
<strong>ONE ENGINE INOPERATIVE APPROACH AND LANDING CHECKLIST</strong>
</div>

**Pattern Entry:**
- **DOWNWIND** - 170 KIAS, N1 +/- 65%

**USE OF YAW DAMPER:**
- YD use is optional, but must be off for landing
- **Note:** Max spd without YD in icing conditions: 180KIAS

**Cleared for Approach:**
- HDG + AP + VS (or LOC + ALTS GS)

**BASE LEG:**
- 170 KIAS

**LOC INTERCEPT:**
- LOC + AP + ALT + GS

**Configuration:**
- **G/S Alive** - Flap 1
- **One dot above** - Gear Down, Flap 2
- **G/S Intercept** - Flap 3, AAD set to MAA

**GS CAPTURE:**
- LOC + AP + GS
- V_AP, FLAP 3 & GEAR = N1 +/- 63%

**BEFORE LANDING CHECKLIST**

**Stabilised Approach Point:**
- 'Stable' or 'Go Around Flap 1'

**At DA:**
- "MINIMUMS"
- Corrected V_REF

**Notes:**
- The aim is to commence the final approach in an already stabilised configuration. Configuration may be achieved earlier if necessary
- The speed schedule and configuration changes displayed in this profile are also valid for OEI CDFA or OEI Visual Straight-in Approaches
- When flap configuring involves bypassing a position, flap lever should be paused at the intermediate position before selecting desired setting
""", unsafe_allow_html=True)
    
    with st.expander("**5. One Engine Inoperative Go-Around**", expanded=False):
        st.markdown("""
<div style="background-color: #ffcccb; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
<strong>OEI GO-AROUND</strong> - From Stabilised Final Approach Flap 3
</div>

**"GO AROUND, FLAP 1":**
- Simultaneously: Push TO/GA button, Set GA Thrust, Pitch to FD initially
- PM: Set Flap 1
- ROL + GA/ALTS

**"POSITIVE RATE" - "Gear Up":**
- PM: Select FLC, Set V_AC
- Engage HDG or NAV, LOW BANK A/R
- HDG + FLC/ALTS or FMS + FLC/ALTS

**Climb at V_AC** (Max Speed V_AC + 10)

**1000FT AAL:**
- Consider AP (YD OFF)

**1500'AAL or briefed Min:**
- Accel Alt if higher

**Acceleration:**
- Set speed V_FS

**CON Thrust, Disengage Low Bank** (see note)
- Speed V_AC + 10, Flap 0

**AFTER T/O CHECKLIST**

**Notes:**
- V_FS provides max angle of climb and should be used if obstacle clearance remains a factor. If terrain clearance is assured speed may be increased to 150 kts
- Low Bank should only be disengaged when IAS above V_FS
- NAV mode should only be engaged if Missed Approach Procedure has sequenced correctly
- When flap configuring involves bypassing a position, flap lever should be paused at the intermediate position before selecting desired setting
""", unsafe_allow_html=True)
        img_path = os.path.join(folder, "oei_ga_emer_desc.jpg")
        if os.path.exists(img_path):
            st.image(Image.open(img_path), caption="OEI Go-Around & Emergency Descent Profiles", use_container_width=True)
    
    with st.expander("**6. Emergency Descent**", expanded=False):
        st.markdown("""
<div style="background-color: #ffcccb; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
<strong>CAB ALTITUDE HI - Memory Items</strong>
</div>

**MEMORY ITEMS:**
| Item | Action |
|------|--------|
| OXYGEN MASKS | DON, 100% |
| COMMUNICATION | ESTABLISH |
| SIGNS/OUTLET | PED-BELTS/OFF |
| ALTITUDE | 10000FT OR MEA |
| THRUST LEVERS | IDLE |
| SPEED BRAKE | OPEN |
| AIRSPEED | MAX 250/Mmo |
| LDG GEAR | DN |
| TRANSPONDER | 7700 |
| ATC | NOTIFY |

---

**"EMERGENCY DESCENT":**

**PF Actions:**
- Engage HDG and FLC
- Max 250 KIAS
- AAD set to 10000' or MEA if higher
- HDG + AP YD + FLC/ALTS

**Note:** If an Emergency Descent is about to be carried out, Consider setting 7700 before starting the descent if appropriate

---

**ESTABLISHED IN DESCENT:**

**PM Actions:**
- MAYDAY call
- Check MEA/QNH/AAD
- Transponder 7700
- QRH Checklist

---

**1000' ABOVE LEVEL OFF:**

**PF Actions:**
- SPEED BRAKE - CLOSED

---

**AT LEVEL (MEA):**
- LDG GEAR UP
- Assess options
- Check Pax
- HDG + AP YD + ALT

---

**CONSIDER:**
- DIVERSION OR CONTINUE TO DESTINATION (FUEL BURN)?
- CALL COMPANY?
""", unsafe_allow_html=True)

def render_planning():
    st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>Phenom 300</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Netjets Edition</p>", unsafe_allow_html=True)
    if st.button("Home", use_container_width=False, type="primary", key="home_btn"):
        navigate('home')
        st.rerun()
    
    st.markdown("## Flight Planning")
    st.caption("Netjets Operations Manual Part A")
    
    with st.expander("**1. Operating Minima - Key Rules**", expanded=True):
        st.markdown("""
**Golden Rule:** Always use the **highest** published minima (Jeppesen, AIP, RTOW/M, AOM, RM).

**CDFA Required** for all non-precision approaches.
- Non-CDFA penalty: +200m RVR (CAT A/B) or +400m (CAT C/D)
""")
    
    with st.expander("**2. Aeroplane Categories**", expanded=False):
        st.markdown("**VAT (VREF):** VSO × 1.3 or VS1G × 1.23 at max landing mass. Use higher value.")
        
        cat_data = [
            ["A", "<91", "90-150", "70-100", "100"],
            ["B", "91-120", "120-180", "85-130", "135"],
            ["C", "121-140", "160-240", "115-160", "180"],
            ["D", "141-165", "185-250", "130-185", "205"],
            ["E", "166-210", "185-250", "155-230", "204"]
        ]
        df_cat = pd.DataFrame(cat_data, columns=["CAT", "VAT (KIAS)", "Initial", "Final", "Circling"])
        st.dataframe(df_cat, hide_index=True, use_container_width=True)
        
        st.markdown("**Note:** Cannot use lower category minima unless AIP explicitly permits.")
    
    with st.expander("**3. Alternate Requirements**", expanded=False):
        st.markdown("""
**TAKE-OFF ALTERNATE** (if departure unusable):
- Within **1 hour OEI cruise** (or ETOPS time, max 2 hrs)

---

**DESTINATION ALTERNATE - How Many?**

| Alternates | When Required |
|:-----------|:--------------|
| **0** | Flight ≤6 hrs + 2 separate runways + ceiling ≥2000ft + vis ≥5km |
| **1** | Standard IFR flight |
| **2** | Weather below planning minima OR no met info |

*With 2 alternates: fuel for most distant*

---

**ALTERNATE SELECTION:**
- Within **50 nm** of destination (preferred)
- Departure may be used as destination alternate
- Must meet weather requirements
""")
    
    with st.expander("**4. Planning Minima Tables**", expanded=False):
        st.markdown("""
**Type A** = DH/MDH ≥ 250 ft | **Type B** = DH < 250 ft

Weather at ETA ±1 hour must meet these minima:
""")
        
        st.markdown("**Flights > 6 hours:**")
        plan_a_data = [
            ["Type B (DH < 250ft)", "+200 ft", "+800 m"],
            ["Type A (DH ≥ 250ft)", "+400 ft", "+1500 m"],
            ["Circling", "+400 ft", "+1500 m"]
        ]
        df_plan_a = pd.DataFrame(plan_a_data, columns=["Approach", "Add to Ceiling", "Add to RVR/VIS"])
        st.dataframe(df_plan_a, hide_index=True, use_container_width=True)
        
        st.markdown("**Flights ≤ 6 hours:**")
        plan_b_data = [
            ["Type B", "+200 ft", "+550 m"],
            ["3D Type A (sys min ≤200ft)", "+200 ft", "+800 m"],
            ["2+ Type A (sep nav aids)", "+200 ft", "+1000 m"],
            ["Other Type A", "+400 ft", "+1500 m"],
            ["Circling", "+400 ft", "+1500 m"]
        ]
        df_plan_b = pd.DataFrame(plan_b_data, columns=["Approach", "Add to Ceiling", "Add to RVR/VIS"])
        st.dataframe(df_plan_b, hide_index=True, use_container_width=True)
        
        st.markdown("*Use lowest applicable minima when multiple rows apply.*")
    
    with st.expander("**5. Go/No-Go Weather Rules**", expanded=False):
        st.markdown("""
**TAKE-OFF:** Destination + alternates must be at/above **planning minima**

**CONTINUE TO DESTINATION:** Weather at destination OR one alternate at/above **operating minima**

**BEYOND DECISION POINT:** Conditions must meet planning minima at PNR
""")
    
    with st.expander("**6. Take-off Minima**", expanded=False):
        st.markdown("""
**Requirements:**
- Departure weather ≥ landing minima (or T/O alternate available)
- If reported vis < required: pilot assessment OK
- Night ops: runway + obstacle lighting required

**Before Take-off, verify:**
- Ground equipment operative
- Aircraft systems operative
- Performance adequate
- Crew qualified
""")
    
    with st.expander("**7. Approach Minima - DH/MDH**", expanded=False):
        st.markdown("""
**Use the HIGHEST of:**
- OCH for aircraft category
- Published DH/MDH
- System minimum (see table)
- AFM minimum
- NPA with CDFA: add +50 ft to published MDA

---

**Temperature Correction:** Apply when significantly below ISA

**EVS:** May reduce RVR by up to 1/3 (CAT I, APV, NPA+CDFA)
- Below 100 ft AGL: visual ref required **without EVS**
- **No EVS for circling**
""")
    
    with st.expander("**8. System Minima by Facility**", expanded=False):
        facility_data = [
            ["ILS / MLS / GLS / LPV*", "200"],
            ["LP / LNAV / LNAV-VNAV / LOC", "250"],
            ["VOR/DME / SRA (½ NM)", "250"],
            ["VOR / SRA (1 NM) / NDB/DME", "300"],
            ["NDB / VDF / SRA (2+ NM)", "350"]
        ]
        df_facility = pd.DataFrame(facility_data, columns=["Facility", "Min DH/MDH (ft)"])
        st.dataframe(df_facility, hide_index=True, use_container_width=True)
        st.caption("*LPV: 200ft only if VAL ≤ 35m, otherwise 250ft")
        
        st.markdown("---")
        
        rwy_data = [
            ["PA CAT I runway", "200"],
            ["NPA runway", "250"],
            ["Non-instrument", "Circling"]
        ]
        df_rwy = pd.DataFrame(rwy_data, columns=["Runway Type", "Min DH/MDH (ft)"])
        st.dataframe(df_rwy, hide_index=True, use_container_width=True)
    
    with st.expander("**9. Minimum RVR/VIS**", expanded=False):
        rvr_data = [
            ["PA CAT I runway", "550m"],
            ["NPA runway", "750m"],
            ["Non-instrument", "Circling minima"]
        ]
        df_rvr = pd.DataFrame(rvr_data, columns=["Runway Type", "Min RVR"])
        st.dataframe(df_rvr, hide_index=True, use_container_width=True)
        
        st.markdown("""
**CAT A/B:** Max RVR capped at **1500m**

**Level segment above MDA:** Add +200m (A/B) or +400m (C/D)

**Night ops:** All required lighting must be serviceable
""")
    
    with st.expander("**10. LVTO Quick Reference**", expanded=False):
        st.markdown("""
- Initial RVR may use **pilot assessment**
- RVR required for entire **ASD** distance
- Night: Edge + end lights OR centreline lights
- LVTO training required (**125m** approved)
""")

def render_cold_weather():
    st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>Phenom 300</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Netjets Edition</p>", unsafe_allow_html=True)
    if st.button("Home", use_container_width=False, type="primary", key="home_btn"):
        navigate('home')
        st.rerun()
    
    st.markdown("## Cold Weather Operations")
    st.caption("Source: Netjets Operations Manual Part B (Section 2.24)")
    
    folder = "assets/cold_weather_ops"
    
    with st.expander("**1. When Do Icing Conditions Exist?**", expanded=True):
        st.markdown("""
**In flight:**
- SAT or TAT is **10°C or below** AND visible moisture is present

**On the ground:**
- SAT is **10°C or below** for takeoff, AND
- Surface snow, ice, standing water, or slush on ramps/taxiways/runways
- Risk of ingestion by engines or freezing on engine/sensor probes

**Key temperatures to remember:**
- **-40°C** = Minimum oil temperature for engine start
- **-37°C** = Minimum fuel temperature for engine start
- **-10°C** = Batteries become sluggish - request GPU early
""")
    
    with st.expander("**2. Pre-Flight Preparation**", expanded=False):
        st.markdown("""
**Before arriving at the aircraft:**
- Know the airport's de-icing procedures and location
- Find out if de-icing is done pre-start or with engines running
- Plan for delays - especially at busy airports
- Confirm fluid stocks are available (check the night before)

**If aircraft was left in cold conditions:**
- Replace batteries as soon as possible
- Request a GPU early (even above -10°C, batteries can be sluggish)
- If lavatory was drained overnight, refill before departure

**Contamination check (PIC responsibility):**
- Visually inspect wings, control surfaces, engines, and fuselage
- When possible, do a hands-on check (but don't touch with bare hands - skin can stick!)
- Aircraft must be **clear of ice, frost, and snow** before takeoff

**Pre-flight walk-around - check these are clear:**
- Pitot tubes and static ports
- Pressurization inlets, outlets, and vents
- Landing gear doors
""")
    
    with st.expander("**3. Cold-Soaked Aircraft**", expanded=False):
        st.markdown("""
**What is "cold soaking"?**
- After flying at high altitude, the fuel and structure are very cold
- Even if OAT is above freezing, ice can form on the aircraft

**When it happens:**
- High humidity, fog, drizzle, or rain
- Cold fuel causes moisture to freeze on wing surfaces

**What to do:**
- If ice, snow, or frost is found during walk-around, de-icing is required
- Use heated water or Type I, II, III, or IV de-icing fluids
""")
    
    with st.expander("**4. Approved De-Icing Fluids**", expanded=False):
        st.markdown("""
**Type I fluids:**
- Must meet SAE AMS 1424 specifications
- Heated fluid - removes contamination
- Short holdover time

**Type II, III, and IV fluids:**
- Must meet SAE AMS 1428 specifications
- Provide anti-icing protection (longer holdover)
- Thicker fluids that stay on the surface

**Reference documents:**
- OM-A: De-Icing and Anti-Icing on the Ground
- POH Section II: Cold Weather Operation
- AFM Section III: Operation in Icing Conditions
""")
    
    with st.expander("**5. De-Icing Before Engine Start**", expanded=False):
        st.markdown("""
**Before fluid application:**
1. Complete normal pre-flight exterior inspection
2. Ensure all covers are removed
3. Close all doors and panels

**After de-icing (before start):**
- Thorough surface check by crew required
- Verify aircraft is free of snow/ice and protected by fluid
- Be aware: opening doors may cause fluid to drip down
- Surface around aircraft will be **extremely slippery**
""")
    
    with st.expander("**6. Engine Starting in Cold Weather**", expanded=False):
        st.markdown("""
**Before starting:**
- Remove ALL ice deposits from engine intakes
- If in doubt, verify blades are free to turn and engine is not seized
- Use safe ground equipment - don't climb on icy wings!

**CAUTION:** If no GPU available, do not let battery voltage drop below **24V**

**Before starting in ground icing conditions:**
- Select **ADS PROBES ON**
- Start engines and complete After Start Flows
""")
    
    with st.expander("**7. De-Icing After Engine Start**", expanded=False):
        st.markdown("""
**Reposition aircraft if required**

**De-Icing Configuration:**

| Item | Setting |
|------|---------|
| Parking Brake | ON |
| Thrust Levers | IDLE |
| Bleed 1 & 2 | OFF (close PRSOV - keeps fumes out) |
| Air Conditioning Mode | OFF (turn off VCS) |
| ECS | OFF VENT (opens RAV for emergency ventilation) |
| Pitch Trim | FULL NOSE UP |
| Flaps | 0 |
| Yoke | FULL AFT AND HOLD |
| Rudder and Ailerons | NEUTRAL |
| De/Anti-Icing | ACCOMPLISH |

**Note:** In cold conditions (8°C and below), ECS uses high flow mode = increased cabin noise. May switch to ECS 2 to reduce noise, then reset to BOTH before takeoff.
""")
    
    with st.expander("**8. Post De-Icing Checklist**", expanded=False):
        st.markdown("""
**Immediately after de-icing:**
- Note de-icing details in AFL (type, time, holdover)
- ADS Probes → **AUTO**
- Pitch Trim → **SET**

**Wait at least 1 minute after fluid application OR after second engine start:**
- Bleed 1 & 2 → **AUTO**

**Wait at least 3 minutes after fluid application OR after second engine start:**
- ECS → **BOTH**
- Air Conditioning Mode → **AUTO**
""")
    
    with st.expander("**9. Ice Protection Check (Engines Running)**", expanded=False):
        st.markdown("""
**Windshield heat check:**
1. WSHLD 1 & 2 Switches → **ON**
2. Verify NO "WSHLD 1 (2) HTR FAIL" CAS message
3. WSHLD 1 & 2 Switches → **OFF**

**Engine anti-ice check:**
1. ENG 1 & 2 Switches → **ON**
2. After 10 seconds, verify "A-I E1 (2) ON" CAS appears
3. ENG 1 & 2 Switches → **OFF**
4. Verify CAS messages disappear

**Wing anti-ice check:**
1. Bleed 1 & 2 Switches → **AUTO**
2. WINGSTAB Switch → **ON**
3. Verify "A-I WINGSTB ARM" or "A-I WINGSTB INHB" may appear
4. WINGSTAB Switch → **OFF**
5. Verify CAS messages disappear

**If ice detector is available:**
1. Test Panel Knob → **ICE PROT**
2. Start Test Button → **PRESS**
3. Verify "ICE CONDITION" CAS appears
""")
    
    with st.expander("**10. After Ice Protection Check**", expanded=False):
        st.markdown("""
**If SAT is between 5°C and 10°C:**

| Item | Setting |
|------|---------|
| ENG 1 & 2 Switches | ON |
| WINGSTAB Switch | OFF |
| WSHLD 1 & 2 Switches | OFF |

**If SAT is below 5°C:**

| Item | Setting |
|------|---------|
| WSHLD 1 & 2 Switches | ON |
| ENG 1 & 2 Switches | ON |
| WINGSTAB Switch | ON |
""")
    
    with st.expander("**11. De-Icing Fluid Application Guidelines**", expanded=False):
        st.markdown("""
**If the de-icing crew is unfamiliar with the Phenom 300, brief them:**

1. **Do NOT spray directly into:**
   - Ram air inlets
   - Engine inlets or exhausts
   - Engine pylons
   - ADS probes

2. **Do NOT spray directly onto windows/windshields**
   - Spray above and let fluid flow down, OR
   - Use a windshield-approved cloth to wipe

3. **Do NOT spray onto wheel and brake assemblies**

4. **Follow the spray pattern** (see diagram below)
""")
        spray_path = os.path.join(folder, "deicing_spray_pattern.png")
        if os.path.exists(spray_path):
            st.image(Image.open(spray_path), caption="De-Icing Spray Pattern", use_container_width=True)
    
    with st.expander("**12. Taxi on Contaminated Surfaces**", expanded=False):
        st.markdown("""
**Before taxi:**
- Complete Normal Checklist in Icing Conditions
- Test anti-ice systems per checklist
- WINGSTAB INHB CAS may appear depending on SAT

**Taxi considerations:**
- Set flaps to **0** if taxiways are contaminated (prevents slush spray onto flaps)
- Use **minimum thrust** to avoid blowing snow/slush on people or other aircraft
- Keep ground speed **below 10 kts** on snow/ice (antiskid not available below 10 kts)
- Use **firm braking** to warm up brakes and dry moisture from brake stack
- Maintain larger gap behind other aircraft to avoid jet blast snow/slush

**Flap setting:**
- Leave flaps at 0 until line-up if taxiways are contaminated
- Don't forget to set them before takeoff! (Config test button will catch this)

**Important warnings:**
- Taxiways may not be cleared to runway standard - some may be closed
- Taxiway markings may be obscured
- Braking action may be worse than reported runway condition
- **NEVER operate on runways with braking action reported as POOR**
""")
    
    with st.expander("**13. Pre-Takeoff Contamination Check**", expanded=False):
        st.markdown("""
**Holdover Time (HOT):**
- For Type I fluid, use **Composite Table** (OM-A, Table 1-c) - more conservative due to composite tail
- Check OM-A for crosswind limits with reduced braking action

**Pre-takeoff contamination check:**
- Perform **prior to takeoff** and **within holdover time**
- Surfaces must be free of frost, ice, snow, and slush
- If holdover time is about to expire, this check is **critical**
- If any contamination found, **return for re-treatment**

**How to check:**
- Visually inspect wing surfaces and leading edges
- Look through an appropriate window at wing/engine areas
""")
    
    with st.expander("**14. Line-Up Checks**", expanded=False):
        st.markdown("""
**Flight controls:**
- Check for **full and free movement**
- If flaps were at 0 for taxi, set them for takeoff now
- Final surface check - no snow accumulation from taxi

**Ice Protection Systems:**
- Set as required per AFM icing conditions procedures
- Complete Ice Protection Check
""")
    
    with st.expander("**15. Takeoff on Contaminated Runway**", expanded=False):
        st.markdown("""
**Commander responsibilities:**
- Assess whether holdover time is still valid
- If HOT expired OR any doubt about ice-free condition → **return for de-icing**

**Technique:**
- Do NOT use static takeoff technique on slippery runways (aircraft may slide)
- Apply **light forward pressure** on control column to improve nosewheel steering

**After takeoff:**
- In severe icing, ice may build on fan or spinner blades → possible fan vibration
- Do NOT reset Ice Speed until certain all ice has been removed
""")
    
    with st.expander("**16. Climb & Cruise**", expanded=False):
        st.markdown("""
**Climb:**
- Severe icing may cause ice buildup on fan/spinner blades
- This may result in fan vibration
- Do NOT reset Ice Speed until you're certain all ice is gone

**Cruise:**
- Reserved (no specific cold weather notes)
""")
    
    with st.expander("**17. Descent**", expanded=False):
        st.markdown("""
**Cold-soaked aircraft descending into clouds:**
- Anticipate cloud entry during descent
- Aircraft will ice up **faster than normal** when cold-soaked
- Be prepared to activate ice protection systems early
""")
    
    with st.expander("**18. Approach**", expanded=False):
        st.markdown("""
**With anti-ice systems ON:**
- Minimum power setting increases automatically
- Aircraft may be **reluctant to slow down** for glideslope intercept and final

**Ice speeds:**
- If WingStab expected to be ON below 1500 ft, use **higher Ice Speeds** for approach
- Only reset SWPS Ice Speed if above 1500 AAL AND certain aircraft is clear of ice

**Speed management:**
- Use caution selecting flaps close to limiting speeds
- Consider selecting gear first to help slow down
""")
    
    with st.expander("**19. Landing on Contaminated Runway**", expanded=False):
        st.markdown("""
**Touchdown technique:**
- Make a **positive landing** - ensure wheel spin-up
- Initiate **firm ground contact**

**Factors that increase aquaplaning risk:**
- High speed
- Standing water
- Poor runway surface

**Braking:**
- Apply moderate to firm braking pressure
- Let antiskid do its job
- Slow down before exiting runway - taxiway may be slippery

**Flaps:**
- On contaminated runway, **leave flaps at landing setting** until at the gate
- Perform visual inspection before raising flaps
""")
    
    with st.expander("**20. Taxi In**", expanded=False):
        st.markdown("""
**Take it slow:**
- Taxiways may not be as well cleared as the runway
- Snow banks near taxiway edges make surface more slippery
- Exercise caution
""")
    
    with st.expander("**21. Parking & Post-Flight**", expanded=False):
        st.markdown("""
**Parking:**
- Get chocks in position ASAP so you can release parking brake

**Post-flight inspection:**
- Check carefully for flap or gear damage from slush and ice

**If aircraft will stay outside overnight:**
- Consider applying **anti-icing fluid** after landing (clean surfaces)
- This prevents frozen contamination from adhering overnight
- Makes next morning's de-icing faster and easier

**If temperature forecast is -10°C or below:**
- Remove all items that may freeze:
  - Water bottles
  - Soda cans
  - Coffee and water containers
  - Wine and champagne bottles

**Lavatory:**
- Empty fluid and don't refill until prior to next departure
""")

def render_placeholder(title):
    st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>Phenom 300</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Netjets Edition</p>", unsafe_allow_html=True)
    if st.button("Home", use_container_width=False, type="primary", key="home_btn"):
        navigate('home')
        st.rerun()
    
    st.markdown(f"### {title}")
    st.info("This module is under development.")

if st.session_state.section == 'home':
    render_home()
elif st.session_state.section == 'systems':
    render_systems()
elif st.session_state.section == 'limitations':
    render_limitations()
elif st.session_state.section == 'memory':
    render_memory()
elif st.session_state.section == 'planning':
    render_planning()
elif st.session_state.section == 'sop':
    render_placeholder("SOP")
elif st.session_state.section == 'profiles':
    render_flight_profiles()
elif st.session_state.section == 'airports':
    render_placeholder("Special Airports")
elif st.session_state.section == 'cold_weather':
    render_cold_weather()
