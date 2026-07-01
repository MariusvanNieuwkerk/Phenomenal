import os

# Keep Streamlit's runtime files inside the project folder (Cursor sandbox
# cannot write to `~/.streamlit`).
_app_dir = os.path.dirname(os.path.abspath(__file__))
os.environ.setdefault("STREAMLIT_HOME", os.path.join(_app_dir, ".streamlit_local"))

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from PIL import Image

from systems.air_management import render_air_management
from systems.airplane_general import render_airplane_general
from systems.automatic_flight import render_automatic_flight
from systems.cabin_ife import render_cabin_ife
from systems.electrics import render_electrics
from systems.fire_protection import render_fire_protection
from systems.flight_controls import render_flight_controls
from systems.fuel import render_fuel
from systems.hydraulics import render_hydraulics
from systems.ice_protection import render_ice_protection
from systems.landing_gear import render_landing_gear
from systems.oxygen import render_oxygen
from systems.powerplant import render_powerplant
from systems.rnav_approaches import render_rnav_approaches
from systems.warning_system import render_warning_system
from study.semantic_color import mi_md
from study.sop import render_sop
from study.special_airports import render_special_airports
from ui.shell import render_app_shell
from ui.theme import inject_scroll_to_top_chevron, inject_theme_css, inject_memory_page_css, inject_systems_page_css, render_page_header
from content.render_helpers import render_search_focus_banner, render_system_memory_items, source_footer, systems_page_top
from data.memory_items import MEMORY_CONTENT, MEMORY_TITLES, SYSTEM_MEMORY

def _page_icon() -> str:
    # Streamlit 1.18+ serves /app/static/* when enableStaticServing=true — use as favicon URL.
    if os.path.isfile(os.path.join(_app_dir, "static", "briefly-icon-32.png")):
        return "/app/static/briefly-icon-32.png"
    return "✈️"


def _inject_app_icons():
    """One-shot PWA head tags. No MutationObserver — that caused a browser hang."""
    components.html(
        """
<script>
(function () {
  if (window.__brieflyIconsApplied) return;
  window.__brieflyIconsApplied = true;
  document.querySelectorAll('link[rel*="icon"]').forEach(function (el) { el.remove(); });
  var link = document.createElement('link');
  link.rel = 'icon';
  link.type = 'image/png';
  link.href = '/app/static/briefly-icon-32.png';
  document.head.appendChild(link);
  if (!document.querySelector('link[rel="apple-touch-icon"]')) {
    var apple = document.createElement('link');
    apple.rel = 'apple-touch-icon';
    apple.sizes = '180x180';
    apple.href = '/app/static/briefly-icon-180.png';
    document.head.appendChild(apple);
  }
  if (!document.querySelector('link[rel="manifest"]')) {
    var manifest = document.createElement('link');
    manifest.rel = 'manifest';
    manifest.href = '/app/static/manifest.json';
    document.head.appendChild(manifest);
  }
})();
</script>
        """,
        height=0,
    )


st.set_page_config(
    page_title="Briefly",
    page_icon=_page_icon(),
    layout="wide",
)

_inject_app_icons()

DOCS_DIR = os.path.join(_app_dir, "documents", "operations_manuals")
OPERATIONS_MANUALS = [
    ("OM-A - Operations Manual Part A.pdf", "Operations Manual Part A — general company operations."),
    ("OM-B - Operations Manual Part B - EMB-505.pdf", "Operations Manual Part B — EMB-505 aircraft-specific procedures."),
    ("OM-C - Operations Manual Part C.pdf", "Operations Manual Part C — route and aerodrome reference."),
    ("Handbook Phenom 300.pdf", "Phenom 300 fleet handbook — full reference (detail lives in Briefly per topic)."),
]

def _inject_ui_css():
    inject_theme_css()


_inject_ui_css()

if 'section' not in st.session_state:
    st.session_state.section = 'limitations'
if 'system' not in st.session_state:
    st.session_state.system = None

def navigate(section, system=None, airport=None, focus=None):
    st.session_state.section = section
    if system is not None:
        st.session_state.system = system
    elif section != "systems":
        st.session_state.system = None
    if airport is not None:
        st.session_state.airport_selected = airport
    else:
        st.session_state.airport_selected = None
    if focus is not None:
        st.session_state.search_focus = focus


def render_documents():
    for filename, description in OPERATIONS_MANUALS:
        path = os.path.join(DOCS_DIR, filename)
        with st.container(border=True):
            st.markdown(f"**{filename}**")
            st.caption(description)
            if os.path.isfile(path):
                size_mb = os.path.getsize(path) / (1024 * 1024)
                st.caption(f"Available locally ({size_mb:.1f} MB)")
                with open(path, "rb") as doc_file:
                    st.download_button(
                        "Download PDF",
                        data=doc_file,
                        file_name=filename,
                        mime="application/pdf",
                        key=f"dl_{filename}",
                        use_container_width=True,
                    )
            else:
                st.warning("File not found in the project folder.")


def render_systems():
    render_search_focus_banner()
    systems_list = [
        "Airplane General",
        "Air Management",
        "Automatic Flight",
        "Cabin & IFE",
        "RNAV / RNP Approaches",
        "Electrics",
        "Powerplant",
        "Fire Protection",
        "Flight Controls",
        "Fuel",
        "Hydraulics",
        "Ice Protection",
        "Landing Gear & Brakes",
        "Oxygen",
        "Warning System",
    ]

    st.markdown("#### Aircraft systems")
    systems_page_top()

    col1, col2 = st.columns(2, gap="large")
    for i, sys in enumerate(systems_list):
        col = [col1, col2][i % 2]
        with col:
            if st.button(sys, use_container_width=True, key=f"sys_{sys}", type="primary" if st.session_state.system != sys else "secondary"):
                st.session_state.system = sys
                st.rerun()
    
    st.markdown("---")

    system = st.session_state.system
    if system:
        inject_systems_page_css(SYSTEM_MEMORY.get(system, []))
        render_system_memory_items(system)

    if system == "Airplane General":
        render_airplane_general()
    elif st.session_state.system == "Air Management":
        render_air_management()
    elif st.session_state.system == "Automatic Flight":
        render_automatic_flight()
    elif st.session_state.system == "Cabin & IFE":
        render_cabin_ife()
    elif st.session_state.system == "RNAV / RNP Approaches":
        render_rnav_approaches()
    elif st.session_state.system == "Electrics":
        render_electrics()
    elif st.session_state.system == "Powerplant":
        render_powerplant()
    elif st.session_state.system == "Fire Protection":
        render_fire_protection()
    elif st.session_state.system == "Flight Controls":
        render_flight_controls()
    elif st.session_state.system == "Landing Gear & Brakes":
        render_landing_gear()
    elif st.session_state.system == "Fuel":
        render_fuel()
    elif st.session_state.system == "Hydraulics":
        render_hydraulics()
    elif st.session_state.system == "Ice Protection":
        render_ice_protection()
    elif st.session_state.system == "Oxygen":
        render_oxygen()
    elif st.session_state.system == "Warning System":
        render_warning_system()
    else:
        st.info("Klik hierboven op een systeem om de uitleg te zien.")

def render_limitations():
    render_search_focus_banner()
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
    render_search_focus_banner()
    inject_memory_page_css()
    for title in MEMORY_TITLES:
        with st.expander(f"**{title}**", expanded=False):
            mi_md(MEMORY_CONTENT[title])

def render_flight_profiles():
    source_footer("om_b", "Chapter 2 Normal Procedures · Flight profile diagrams")
    
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

    st.markdown("### Performance (Handbook Ch 9)")
    with st.expander("**7. Min fuel altitude — short sectors (Ch 9.1)**", expanded=False):
        st.markdown(
            "Suggested **max FL** for least fuel on hops **< 200 nm** "
            "(climb 225/M0.60, ≥5 min cruise, descent M0.75/250 @ 3000 fpm). "
            "Values = **flight level**."
        )
        df_min = pd.DataFrame(
            [
                ["17,600", ">MLW", ">MLW", "240", "390"],
                ["17,200", "170", "220", "320", "400"],
                ["16,800", "170", "220", "320", "400"],
                ["16,400", "170", "230", "330", "410"],
                ["16,000", "180", "230", "330", "420"],
                ["15,600", "180", "230", "340", "420"],
                ["15,200", "180", "240", "340", "420"],
                ["14,800", "190", "240", "350", "430"],
                ["14,400", "190", "240", "360", "440"],
                ["14,000", "200", "240", "360", "440"],
            ],
            columns=["TOW (lb)", "50 nm", "100 nm", "150 nm", "200 nm"],
        )
        st.dataframe(df_min, hide_index=True, use_container_width=True)
        st.caption("Tankering vs cost — handbook table; use OFP + dispatch guidance for tanker decisions.")

    with st.expander("**8. Max speed cruise — Mach & range (Ch 9.2)**", expanded=False):
        st.markdown(
            "**ISA, ice protection OFF** — Mach and **nm per 100 lb** at max-speed cruise. "
            "Coloured areas in handbook = reduced **g-stall margin**; heavy + ISA+ → FL390 may beat FL410+."
        )
        df_cruise = pd.DataFrame(
            [
                ["18,387", "FL370", "0.75", "35.8", "FL390", "0.74", "38.6", "FL410", "0.71", "40.9", "FL430", "0.69", "43.1"],
                ["17,200", "FL370", "0.76", "36.1", "FL390", "0.75", "39.1", "FL410", "0.73", "41.8", "FL430", "0.71", "44.1"],
                ["16,000", "FL370", "0.76", "36.4", "FL390", "0.75", "39.5", "FL410", "0.75", "42.6", "FL430", "0.73", "45.0"],
                ["15,200", "FL370", "0.77", "36.5", "FL390", "0.76", "39.7", "FL410", "0.75", "42.9", "FL430", "0.75", "45.8"],
            ],
            columns=[
                "TOW", "FL1", "M1", "R1", "FL2", "M2", "R2", "FL3", "M3", "R3", "FL4", "M4", "R4",
            ],
        )
        st.dataframe(df_cruise, hide_index=True, use_container_width=True)
        st.caption("R = range (nm) per 100 lb fuel. ISA+10 table in Handbook PDF.")

    with st.expander("**9. OEI climb gradient & climb technique (Ch 9.3–9.4)**", expanded=False):
        st.markdown("""
**PAN OPS / SID context**
- SID designed for **2.5%** gross gradient → **3.3% net** minimum for obstacle guarantee (0.8% engine margin).
- Plate gradients may be **ATM only** — you can fly the SID OEI if obstacle-safe; **tell ATC**.
- Tables: **Flap 1**, **V2–V2+10**, ice protection OFF. Below **3.3%** highlighted in handbook.

**Sample OEI gradient % (ISA, selected AMSL ft)**
""")
        df_oei = pd.DataFrame(
            [
                ["1,000", "12.4", "11.2", "10.0", "8.9", "8.1", "7.3"],
                ["3,000", "11.9", "10.6", "9.5", "8.5", "7.6", "6.8"],
                ["5,000", "10.9", "9.6", "8.6", "7.7", "6.9", "6.1"],
                ["7,000", "9.4", "8.3", "7.5", "6.7", "6.0", "5.4"],
            ],
            columns=["AMSL", "14,400", "15,200", "16,000", "16,800", "17,600", "18,386"],
        )
        st.dataframe(df_oei, hide_index=True, use_container_width=True)
        st.markdown("""
**Climb technique (9.4)**
- POH schedule: **225 KIAS** to **M0.60** @ 29,600 ft — workable but **M0.60 above FL300** is behind the drag curve (ISA+5, heavy, FL400+).
- Preferred: **225 KIAS** (or **250 KIAS** above FL200) to **FL300**, then **VS** — **1500 fpm** typical, **500 fpm** above **FL400**.
- Short max-CLB thrust (up to ~5 min) before cruise power if needed.

_Full OEI tables (all ISA deviations) → **Documents → Handbook** Ch 9.3._
""")

def render_planning():
    source_footer("om_a", "Operating minima, alternates, approach minima")
    
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

    with st.expander("**11. Over-weight landings (Handbook Ch 3.2)**", expanded=False):
        st.markdown("""
**MLW Phenom 300: 17,042 lbs** — **no buffer**. Any exceedance → **full overweight inspection** (costly; aircraft to maintenance).

**Practical rules (fleet handbook)**
- Keep a **couple of hundred pounds** margin — do not aim to land just under max.
- Accurate **ZFW and pax weight** in GTC; use OFP figures.
- Short flight + large taxi bias unused + ATC shortcut → recalculate landing weight.
- Past events were **< 100 lbs** over — still required inspection.
- Dispatch targets **≥ 700 lbs fuel buffer** on tankering — with accurate weights you should not be surprised by FDM.

_See also **Limitations** → Structural & Weight Limits._
""")


def render_cold_weather():
    source_footer("om_b", "2.24 Cold Weather Ops")
    
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
- If lavatory was drained overnight, refill before departure (**Cabin & IFE** → lavatory)

**Contamination check (PIC responsibility):**
- Visually inspect wings, control surfaces, engines, and fuselage
- When possible, do a hands-on check (but don't touch with bare hands - skin can stick!)
- Aircraft must be **clear of ice, frost, and snow** before takeoff

**ECS cold weather (FOL 011/13)** — below **8°C** OAT, ECS may use **AUX HEAT MODE** (high flow) to optimise cockpit temperature.

**Anti-ice below 13,000 ft (FOL 002/14)** — simultaneous **BLEED 1 FAIL + BLEED 2 FAIL** possible when anti-ice commanded — see **Air Management** CAS table.

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

    with st.expander("**22. Handbook — scheduling & pre-flight time (Ch 6.2.1)**", expanded=False):
        st.markdown("""
**+15 minutes show time** (OM-A 7.2.5.4) when icing expected and aircraft **not** hangared overnight.
- Especially in the dark, 15 min is often the **minimum** for thorough exterior check + de/anti-ice decision.
- Inform Scheduling and update duty day if you need extra time.

**Practical prep:** refill liquid stock, toilet service if drained overnight, GPU early if batteries were removed.
""")

    with st.expander("**23. Severe icing — exit procedures (Ch 6.7.4)**", expanded=False):
        st.markdown("""
**Visual cues** — request priority handling to exit icing if any:
- Extensive ice on areas that normally stay clean
- Ice **aft of protected surfaces** on the wing
- Unusual roll / trim / autopilot trim warnings in icing

**Actions**
- Do **not** use autopilot when cues exist — disengage and hold yoke firmly
- Avoid abrupt manoeuvres; reduce AOA if unusual roll
- Do **not** extend flaps in prolonged icing; if extended, do not retract until airframe clear
- Report conditions to ATC

**Engine anti-ice below -40°C** at altitude — risk of compressor stalls; use judgement.
""")

    with st.expander("**24. Altimeter temperature correction (Ch 6.9.2)**", expanded=False):
        st.markdown("""
**Phenom shortcut:** GTC **minimums** page → **TEMP COMP** → set aerodrome OAT → **COMP MIN** on PFD.

**When required (≤ -10°C OAT)**
- Add correction to **DA/MDA** and step fixes inside FAF
- All low-altitude procedure altitudes in **mountainous** areas (≥3000 ft AMSL)
- At **≤ -30°C**, add **1000 ft to MSA**

**Rule of thumb:** ~**4 ft per 1000 ft** height per °C below ISA (table in handbook). Cold → aircraft **lower** than altimeter indicates — **add** to minima.
""")

def _render_section(section: str):
    inject_scroll_to_top_chevron(enabled=(section == "systems"))
    if section == "documents":
        render_documents()
    elif section == "systems":
        render_systems()
    elif section == "limitations":
        render_limitations()
    elif section == "memory":
        render_memory()
    elif section == "planning":
        render_planning()
    elif section == "sop":
        render_sop()
    elif section == "profiles":
        render_flight_profiles()
    elif section == "airports":
        render_special_airports()
    elif section == "cold_weather":
        render_cold_weather()


render_app_shell(navigate, _render_section)
