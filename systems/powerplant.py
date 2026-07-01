import os

import streamlit as st
from PIL import Image

from content.render_helpers import back_to_top, cas_quick_reference, source_footer


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
        return
    st.markdown(f"**{title}**")
    cols = st.columns(columns, gap="medium")
    for i, p in enumerate(paths):
        with cols[i % columns]:
            _img(p, os.path.basename(p))


def render_powerplant():
    st.markdown("## Powerplant (PW535E engines)")
    st.caption("ATA 71 | Source: Phenom 300 POH (Section 6-05)")

    folder = "assets/powerplant"

    # ------------------------------------------------------------------ 0
    with st.expander("**0. Big picture**", expanded=True):
        st.markdown(
            """
The Phenom 300 is powered by **two Pratt & Whitney PW535E turbofan engines** mounted on the
rear fuselage. Each engine produces thrust by accelerating a large volume of air: most air bypasses
the core (the **fan**); a smaller portion passes through the **core** where it is compressed, burned,
and expanded through the turbines.

### How you control thrust

You set **thrust lever** position. A computer called the **FADEC** (Full Authority Digital Engine Control)
meters fuel, controls start and shutdown, and keeps the engine within speed and temperature limits.
In normal flight you select a rating; the FADEC delivers the matching fan speed (**N1**).

### Three numbers to know on the MFD

| Parameter | What it is |
|-----------|------------|
| **N1** | Fan speed (%) — main indicator of thrust |
| **N2** | Core speed (%) — important during start |
| **ITT** | Inter-turbine temperature — main thermal indicator |

### What each engine also provides

Each engine drives an **accessory gearbox** that turns the starter/generator, hydraulic pump, and
bleed air for pressurisation and anti-ice. Those outputs are described under **Electrics**,
**Hydraulics**, and **Air Management**.

### Where you see engine data

Engine parameters on the **MFD engine page**. Alerts on the **PFDs**.
Numeric limits are listed under **Limitations → Engine Limits (PW535E)**.
"""
        )

    # ------------------------------------------------------------------ 1
    with st.expander("**1. Engine layout & components**", expanded=False):
        st.markdown(
            """
### Engine type

Two-spool turbofan with a full-length annular bypass duct integrated with the nacelle.

### Two independent shafts

- **LP (inner) shaft** — fan, booster, and dual-stage LP turbine
- **HP (outer) shaft** — HP compressor (dual axial + one centrifugal stage) and single-stage HP turbine

### Air path

Inlet air → fan (LP compressor) → HP compressor → **combustor** (11 fuel nozzles, annular reverse-flow)
→ HP turbine → LP turbine → mixed with bypass air → exhaust.

### Accessory gearbox (AGB)

All engine-driven accessories mount on the AGB, driven from the HP shaft via a tower shaft and bevel gear.
Typical accessories on the Phenom installation:

| Item | Role |
|------|------|
| **Starter/generator** | Start the engine; generate electrical power when running |
| **Hydraulic pump** | Pressurises the hydraulic system |
| **Oil pressure pump** | Part of the lubrication system (see §7) |
| **PMA** | Permanent magnet alternator inside the FMU — primary FADEC power when engine is running |

### Other major engine-mounted items

- **FMU** — fuel metering and shutoff (see §6)
- **FOHE** — fuel/oil heat exchanger (shared by fuel and oil systems)
- **Fuel filter** and **oil filter**
- **Bleed Off Valve (BOV)** — FADEC-controlled valve that modulates engine bleed air extraction
- **TT0 sensor** — total temperature probe in the inlet duct (FADEC ambient input; heated in icing)
- **Ignition exciters** and **igniters**
- **EDCU** — Engine Data Collection Unit (engine condition monitoring and maintenance reporting)
- **Oil tank, sightglass, chip detector** — lubrication system (see §7)

_Source: POH 6-05-00 (Rev 12)._"""
        )
        c1, c2 = st.columns(2)
        with c1:
            _img(f"{folder}/poh_6-05_engine_external_p468.png", "PW535E — external components (POH 6-05-00)")
        with c2:
            _img(f"{folder}/poh_6-05_engine_airflow_p469.png", "PW535E — airflow path (POH 6-05-00)")

    # ------------------------------------------------------------------ 2
    with st.expander("**2. FADEC & engine control**", expanded=False):
        st.markdown(
            """
### What the FADEC does

The FADEC is a dual-channel computer that:
- Modulates **fuel flow** through a torque motor in the FMU
- Modulates **bleed extraction** through a torque motor in the **BOV**
- Controls **ignition**, **start protection**, and **thrust ratings**
- Trims **N1** and **ITT** so both engines match thrust at the same lever position
- Reports engine data via the **EDCU**

### Dual-channel architecture

- Two identical isolated channels: one **in control**, one **standby**
- Automatic switchover on internal fault
- Channel in control alternates between engines on start (when both channels are healthy)

### Electrical power

- **28 VDC airframe power** required to energise FADEC and start the engine
- When running, FADEC uses whichever provides more power: **PMA** or **28 VDC airframe**
- Both FADEC **channel A** units connect to the **Emergency Bus** for starting during electrical emergencies

### Thrust lever input

Thrust lever angle (TLA) is sent to both FADEC channels. The FADEC calculates an **N1 target** for the
selected rating, corrected for OAT, pressure altitude, and bleed/anti-ice configuration.

**Thrust rating modes** (selected by thrust lever detent; FADEC schedules rated N1):

| Mode | Description | Time limit |
|------|-------------|------------|
| **TO** | Takeoff | 5 min |
| **TO RSV** | Takeoff reserve (ATR active) | 10 min |
| **GA** | Go-around | 5 min |
| **GA RSV** | Go-around reserve (ATR / OEI) | 10 min |
| **CON** | Max continuous | None |
| **CLB** | Max climb | None |
| **CRZ** | Max cruise | None |
| **IDLE** | Ground or flight idle (several sub-modes — FADEC selects automatically) |

**Idle sub-modes** (automatic FADEC selection based on aircraft inputs):
Remote start ground idle · ground idle AEO · ground idle OEI · flight idle (anti-ice ON/OFF) ·
landing idle (anti-ice ON, AEO or OEI/single-bleed).

### Anti-ice effect on thrust

With engine/wing anti-ice ON, maximum available thrust is reduced (bleed extraction). The MFD may
show a **minimum N1 bug** when wing/stab anti-ice is ON and gear is extended, or with single engine/bleed.

_Source: POH 6-05-30 (Rev 12)._"""
        )

    # ------------------------------------------------------------------ 3
    with st.expander("**3. Cockpit controls**", expanded=False):
        st.markdown(
            """
### Thrust levers (one per engine)


| Detent | Rating commanded |
|--------|------------------|
| **MAX** | Maximum thrust (may command TO RSV when ATR is armed — see §8) |
| **TO/GA** | Takeoff or go-around |
| **CON / CLB** | Max continuous / max climb |
| **MAX CRZ** | Max cruise |
| **IDLE** | Ground or flight idle |

Intermediate positions between detents are valid. The **TO/GA button** on the thrust quadrant
commands go-around thrust — see **Automatic Flight** for AFCS interaction.

### ENG START/STOP knob (one per engine)


| Position | Function |
|----------|----------|
| **RUN** | Normal operating position |
| **START** | Momentary — initiates start sequence (thrust lever at IDLE) |
| **STOP** | Commands FADEC shutdown (thrust lever must reach IDLE within **5 s** or command is ignored) |

If shutdown fails, recycle the knob (RUN then STOP again) with thrust lever at IDLE within 5 s.

### ENG IGNITION switch (one per engine)


| Position | Function |
|----------|----------|
| **AUTO** | FADEC controls igniters as required |
| **ON** | Both igniters energised continuously while engine runs |
| **OFF** | Igniters disabled — dry motoring only |

### Fire panel — FIRE SHUTOFF pushbutton

Closes the airframe fuel shutoff valve in the wing feed line to that engine. Also isolates hydraulics
and bleed paths associated with fire protection — see **Fire Protection**.

_Source: POH 6-05-05 (Rev 12)._"""
        )
        _img(f"{folder}/poh_6-05_engine_control_panel_p473.png", "Engine control panel (POH 6-05-05)")

    # ------------------------------------------------------------------ 4
    with st.expander("**4. MFD engine indications**", expanded=False):
        st.markdown(
            """
The **MFD engine page** shows both engines side by side. Key indication groups:

### Thrust mode & ATR

- **Thrust rating label** (cyan): CRZ, CLB, CON, TO, or GA — current FADEC rating mode
- **RSV suffix** on the label when reserve thrust is active (ATR triggered)
- **ATR indication**: GREEN = armed · WHITE = enabled · blank = not selected

### N1

- **Digital readout** and **dial pointer** — fan speed (%)
- **N1 target bug** (cyan T on dial) — maximum N1 for current rating mode
- **N1 rating commanded** — N1 the FADEC is commanding for current TLA
- **N1 red line** on dial — N1 limit; digits turn red if exceeded
- **FAIL** (yellow box on dial) — uncommanded flameout
- **OFF** (cyan on dial) — engine shut down in flight by crew action

### ITT

- Digital readout and dial pointer
- **Yellow line** — cautionary limit (ground start reference)
- **Red line** — maximum operating ITT
- **FIRE** (red on dial) — fire detection input

**N2** — core speed (%); green normal, red if limit exceeded

**Ignition channel** — cyan label: A, B, AB, or OFF (which igniter channel is active)

**Oil pressure / oil temperature** — green normal, yellow caution, red limit

**Fuel flow** — kg/h or lb/h; green when valid

**Minimum N1 anti-icing bug** — yellow; minimum N1 for full anti-ice capability

### Colour logic summary


| Indication | Green | Yellow | Red |
|------------|-------|--------|-----|
| N1 / N2 | Normal | — | Limit exceeded |
| ITT | Normal | Ground start reference exceeded | Limit exceeded |
| Oil pres / temp | Normal | Caution band | Limit exceeded |

_Source: POH 6-05-05 (Rev 12)._"""
        )
        _img(f"{folder}/poh_6-05_mfd_engine_indications_p474.png", "MFD engine page — overview (POH 6-05-05 p4)")
        _show_folder_images(folder, "poh_6-05_mfd_indications_", "MFD engine page — indication details (POH 6-05-05 p5–8)")

    # ------------------------------------------------------------------ 5
    with st.expander("**5. Starting, ignition & shutdown**", expanded=False):
        st.markdown(
            """
### Starting system

The **starter/generator** on the AGB spins the engine. FADEC controls fuel, BOV position, ignition,
and ground-start protection.

### Starting modes


| Mode | START/STOP | Ignition | Condition |
|------|------------|----------|-----------|
| **Normal start** | START → RUN | AUTO or ON | Standard ground or air start |
| **Wet motoring** | START | AUTO/ON + ignition CBs open | Fuel/ignition limited — **15 s** max after fuel on |
| **Dry motoring** | START | OFF | No fuel/ignition — **30 s** max |
| **Off** | STOP | any | No start |

### Normal start sequence

1. Starter accelerates core → **N2** rises
2. FADEC schedules fuel and ignition → **ITT** rises
3. Engine reaches idle → starter disengages; generator can come online

**FADEC ground-start protection** (automatic — fuel and ignition cut off):

| Condition | Detection |
|-----------|-----------|
| No light-off | ITT not rising significantly within **10 s** after fuel on |
| Hot start | ITT exceeds steady-state limit by half the transient margin |
| Hung start | Idle not reached within **60 s** after fuel commanded |
| High ITT | ITT reaches **720°C** on the ground |

Ground-start protection is **inhibited in flight** — FADEC does not auto-abort an air start.

**Manual abort** — START/STOP knob to STOP at any time.

### Ignition system

- Two exciters and two igniters per engine; dual-channel FADEC control
- Ground start above 0°C TT0: **one** igniter; below 0°C or in-flight start: **both** igniters
- Channel A exciters on **Emergency Bus** — battery-powered ignition possible after dual shutdown
- FADEC channel B exciter power: DC BUS 1 (left) / DC BUS 2 (right); FADEC can transfer to Emergency Bus

### Auto-relight

On flameout (knob not on STOP), FADEC energises both igniters and schedules relight fuel until
**N2 < 40%** or knob moved to STOP.

### Shutdown

- Normal: thrust lever IDLE → START/STOP knob STOP
- FADEC alternates internal shutdown paths to detect dormant valve failures
- Emergency fuel shutoff: **FIRE SHUTOFF** pushbutton (Fire Protection system)
- After shutdown the fan may **windmill** — normal, not harmful

**Starter/generator motoring limits** (AFM) — cumulative per start cycle:
60 s · 60 s · 15 min · 30 min (motoring events 1–4).

_Source: POH 6-05-20._"""
        )
        _img(f"{folder}/poh_6-05_ground_starting_p491.png", "Starting modes and ground start (POH 6-05-20)")

    # ------------------------------------------------------------------ 6
    with st.expander("**6. Engine fuel system**", expanded=False):
        st.markdown(
            """
The engine fuel system **pressurises, filters, heats, meters, and delivers** fuel to the combustor.

### Fuel flow path (summary)

Airframe wing feed → **centrifugal boost pump** → **FOHE** (heating) → **fuel filter** →
**FMU** (HP pump, PRV, proportional module) → **fuel flow meter (FFT)** → **flow divider** →

### primary & secondary manifolds** → **11 fuel nozzles


### FMU (Fuel Metering Unit) — central assembly


| Element | Role |
|---------|------|
| **Centrifugal boost pump** | Positive inlet pressure to the FMU across the flight envelope |
| **HP gear pump** | High-pressure supply to nozzles and motive flow |
| **PRV** | Maintains constant differential pressure across the metering valve |
| **Proportional module** | Meters burn flow proportional to valve position |
| **Flow divider & shutoff valve** | Splits primary/secondary flow; shuts off fuel for shutdown |
| **Wash screen** | Upstream filter protecting PRV and proportional module |
| **Motive flow takeoff** | High-pressure tap powering the wing-tank **ejector pump** (above idle) |
| **Ecology system** | Purges unburned fuel from the manifold after shutdown |
| **ESOV** | Emergency shutoff — mechanically tripped on LP turbine shaft failure |
| **PMA** | Dual-wound alternator — FADEC primary power when engine is running |

### Integrated fuel manifold & nozzles

- Flow divider sends fuel to **primary** and **secondary** manifolds
- Last-chance inlet screens at manifold inlets and each nozzle
- 11 nozzles arranged for start performance and even combustor temperature distribution

### FOHE

Heats fuel (anti-icing) and cools engine oil. Fuel filter housing includes impending-bypass
monitoring and a bypass valve for clogging or ice.

### Fuel flow meter (FFT)

Measures fuel flow to the cockpit. If FFT lines fail and the engine shuts down from starvation,
FADEC closes internal FMU valves upstream of the FFT to prevent excess fuel escape.

### Airframe fuel shutoff

The fire-panel **FIRE SHUTOFF** pushbutton closes the shutoff valve in the wing feed line
(see **Fuel** and **Fire Protection**).

_Source: POH 6-05-10 (Rev 6)._"""
        )
        _img(f"{folder}/engine_fuel_system_schematic.png", "Engine fuel system schematic (POH 6-05-10)")

    # ------------------------------------------------------------------ 7
    with st.expander("**7. Lubrication system**", expanded=False):
        st.markdown(
            """
Each engine has a **fully independent** oil system.

### Purpose

Lubricate and cool the main shaft bearings and the **accessory gearbox (AGB)**.

### Three sub-systems

1. **Pressure system** — delivers oil to bearings, gears, and splines
2. **Scavenge system** — returns oil to the tank
3. **Secondary air system** — pressurises the oil tank to prevent pump **cavitation**

### Pressure-side flow path

Oil tank → **chip detector/collector** (magnetic; mesh screen upstream of pump) →
**oil pressure pump** → **PAV/CSV** (pressure adjusting / cold-start valve) →
**oil filter** → **FOHE** → **MOP sensor** (main oil pressure) → **MOT sensor** (main oil temperature) →
calibrated nozzles → bearings & AGB → scavenge pumps → tank

### Oil pump (single housing, three elements)

- One **pressure** (supply) element — fed from oil tank
- Two **scavenge** elements — bearing #5 scavenge and AGB scavenge return oil to tank
- Pump runs whenever the core engine is turning

### Oil tank

- Integral with the intermediate engine case (no flexible liner)
- **Sightglass** on the ground for quantity check
- **Oil filler neck** on the engine exterior
- Tank pressurised by secondary air via a calibrated orifice to the AGB

### Oil filter

- Traps particles from circulating oil
- **Bypass valve** opens if filter becomes clogged — oil continues to flow unfiltered
- **Impending bypass switch** monitors differential pressure across the filter
  (inhibited when oil is cold and viscous to avoid false alerts)

### Chip detector

Magnetic sensor in the scavenge line — triggers **CHIP DETECTED** if metal particles are collected.

### Breather / air-oil separator

Vents the system and separates air from scavened oil before return to the tank.

### Cockpit indications

- **Oil pressure** and **oil temperature** on the MFD engine page
- Green = normal · Yellow = caution · Red = limit exceeded

Numeric limits → **Limitations → Engine Limits (PW535E)**.

_Source: POH 6-05-15 (Rev 6)._"""
        )
        _img(f"{folder}/poh_6-05_lubrication_schematic_p487.png", "Lubrication system schematic (POH 6-05-15)")

    # ------------------------------------------------------------------ 8
    with st.expander("**8. Takeoff dataset, ATR & engine protection**", expanded=False):
        st.markdown(
            """
### Takeoff dataset (MFD)

Before takeoff the crew enters **OAT** and **ATR ON/OFF** on the MFD:
SYSTEM → ENG SET → enter values → ACCEPT.

FADEC uses this data for takeoff thrust computation. If not entered → **ENG NO TO DATA** advisory.
If no ATR selection is made before takeoff, the system **defaults to ATR ON**.

### ATR (Automatic Thrust Reserve)

When armed, FADEC automatically commands **TO RSV** or **GA RSV** if:

| Trigger | Result |
|---------|--------|
| **N1 difference > 20%** between engines (engine failure) | Reserve thrust on remaining engine |
| **Loss of communication** between both engines | Reserve thrust |
| Both levers at **MAX** with ATR armed (both engines operating) | **TO RSV** |
| Go-around with ATR (always ON for GA) | **GA RSV** |

When ATR activates:
- Green **ATR** indication disappears; thrust mode shows **RSV** suffix
- FADEC may close the **ECS flow control valve** on that engine (no bleed to air conditioning)
- ECS OFF is also commanded if one bleed fails during T/O or GA with wing/stab anti-ice ON

### FADEC overspeed / overtemperature protection

FADEC reduces fuel automatically when limits are approached:

| Parameter | Fuel reduction begins |
|-----------|----------------------|
| **N1** | Above 100% |
| **N2** | Above 101% |
| **ITT (start)** | Above 700°C |
| **ITT (running)** | Above 765°C |
| **ITT (ground start abort)** | FADEC aborts start at 720°C |

An in-flight exceedance is logged as **ENG EXCEEDANCE**.

### TT0 probe & heating

- **TT0 sensor** — total temperature probe in the engine inlet; dual RTDs, one per FADEC channel
- **TT0 heater** prevents thrust loss from ice crystal accumulation on the probe
- Heater activates when TT0 < 10°C on ground (engine running), or TT0 < 15°C in flight,
  and when cockpit **ENG 1/2 anti-ice switches** are selected
- Ice crystal detection logic active above **4,000 ft**
- If ice does not clear within **2 minutes** after anti-ice ON → **TT0 PROBE ICE** advisory

Nacelle anti-ice and TT0 interaction → **Ice Protection**.

_Source: POH 6-05-30 (Rev 12) · 6-05-35._"""
        )
        c1, c2 = st.columns(2)
        with c1:
            _img(f"{folder}/takeoff_dataset_menu_mfd.png", "Takeoff dataset menu (MFD)")
        with c2:
            _img(f"{folder}/poh_6-05_atr_logic_p497.png", "ATR logic table (POH 6-05-30)")

    # ------------------------------------------------------------------ CAS
    cas_quick_reference(
        [
            ("Fire", "WARNING", "E1 (2) FIRE", "Engine fire detected."),
            ("Engine", "WARNING", "E1 (2) FAIL", "Engine shutdown occurred without crew command."),
            ("Oil", "CAUTION", "E1 (2) OIL LO PRES", "Engine oil pressure is low."),
            ("Control", "CAUTION", "E1 (2) CTRL FAULT", "Thrust modulation degraded or engine responds slowly."),
            ("Control", "CAUTION", "E1 (2) TLA FAIL", "Dual thrust lever angle sensor failure on that engine."),
            ("FADEC", "CAUTION", "E1 (2) FADEC FAULT", "Avionics not receiving data from one FADEC channel."),
            ("Engine", "CAUTION", "E1 (2) CHIP DETECTED", "Magnetic chip detector triggered in scavenge oil."),
            ("Filters", "ADVISORY", "E1 (2) FUEL IMP BYP", "Engine fuel filter impending bypass."),
            ("Filters", "ADVISORY", "E1 (2) OIL IMP BYP", "Engine oil filter impending bypass."),
            ("TT0 probe", "CAUTION", "E1 (2) TT0 HTR FAIL", "TT0 probe heater failed."),
            ("TT0 probe", "ADVISORY", "E1 (2) TT0 PROBE ICE", "TT0 heater off due to ice crystal formation on probe."),
            ("Performance", "ADVISORY", "ENG NO TO DATA", "Takeoff dataset (OAT / ATR) not entered successfully."),
            ("Performance", "ADVISORY", "ENG NO DISPATCH", "FADEC has detected a no-dispatch condition."),
            ("Limits", "CAUTION", "ENG EXCEEDANCE", "In-flight engine operating limit exceedance detected."),
        ],
        title="9. CAS quick reference",
        intro="Grouped by topic. Meanings from POH 6-05-35 — systems perspective only.",
    )

    back_to_top()
    source_footer("poh", "§6-05 Powerplant")
