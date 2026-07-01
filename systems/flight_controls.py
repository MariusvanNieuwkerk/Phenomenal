"""Flight Controls — Phenom 300 pilot guide (ATA 27)."""

import pandas as pd
import streamlit as st

from content.render_helpers import back_to_top, cas_quick_reference, source_footer


def _table(rows: list[tuple], columns: list[str]):
    st.dataframe(pd.DataFrame(rows, columns=columns), hide_index=True, use_container_width=True)


def render_flight_controls():
    st.markdown("## Flight Controls")
    st.caption("ATA 27 · Primary & secondary surfaces · Flaps · Trim · Spoilers · SWPS · POH §6-07")

    with st.expander("**1. Big picture — how it all fits together**", expanded=True):
        st.markdown(
            """
### Two layers to remember


| Layer | What it is | How you move it |
|-------|------------|-----------------|
| **Primary** | Ailerons, elevators, rudder | Control wheels + rudder pedals → **control cables** |
| **Secondary** | Flaps, spoilers, stabilizer trim, trim tabs | Switches/levers → **electric + hydraulic** actuators |

**Flight Control Electronics (FCE)** — two units that command secondary surfaces:
- **FCE 1** — flaps + **pitch trim backup**
- **FCE 2** — **normal pitch trim** + spoilers

**AFCS (autopilot)** adds **electromechanical servos** on the primary controls — it does not replace your cables, it *overlays* commands on aileron, elevator, and rudder.

**Hydraulics priority** — when demand is high, a **priority valve** protects spoilers, **stick pusher**, rudder spring actuator, and brakes over landing gear extension.
"""
        )

    with st.expander("**2. Primary flight controls**", expanded=False):
        st.markdown(
            """
**Ailerons** — roll. Control wheels, duplicated and interconnected between pilots.

**Elevators** — pitch. Control column/wheel aft-forward.

**Rudder** — yaw. Rudder pedals. Includes **rudder boost** (spring actuator) to help pedal force at low speed / OEI.

**Auto-tabs** — small tabs on the elevator trailing edge that deflect automatically with elevator movement — improves pitch authority and feel.

**Pilot tip:** Primary controls are **mechanical**. If hydraulics or electrics misbehave, you can still fly the basics — but secondary systems (flaps, spoilers, trim) may be degraded.
"""
        )

    with st.expander("**3. Flaps**", expanded=False):
        st.markdown(
            """
**What they are** — four-position Fowler flaps (0 · 1 · 2 · 3/FULL), four panels per side.

**How they move** — DC electric motor → jackscrews → flap actuators (via flexible shafts). **FCE 1** commands the single Power Drive Unit (PDU).

### Speed limits (VFE)


| Position | Max speed |
|----------|-----------|
| Flap 1 | **180 KIAS** |
| Flap 2 & 3 | **170 KIAS** |
| Flap FULL | **160 KIAS** |

**Max altitude with flaps extended:** 18,000 ft.

**Indications** — flap lever position + flap indication on display; PM confirms after PF callout (**SOP: 'FLAP [X]' → 'FLAP [X]'**).

**Gear warning interaction** — aural warning logic is tied to flap position and WOW (e.g. flaps not 0 with gear up).
"""
        )
        _table(
            [
                ("CAUTION", "FLAP FAIL", "Flap system failed or jammed — flaps will not move. Use QRH. Brief landing without flaps or alternate."),
                ("ADVISORY", "FLAPS NOT AVAIL", "Flaps unavailable — do not plan normal flap extension. Check QRH / performance."),
            ],
            ["Level", "CAS", "What it means for you"],
        )

    with st.expander("**4. Trim — pitch, roll, rudder**", expanded=False):
        st.markdown(
            """
**Pitch trim (main)** — **movable horizontal stabilizer** (not just a tab). This is your primary pitch trim.

| Channel | Controlled by | CAS examples |
|---------|---------------|--------------|
| **Normal pitch trim** | FCE 2 | PTRIM NML FAIL, PTRIM LO RATE, PTRIM SW 1/2 FAIL |
| **Backup pitch trim** | FCE 1 | PTRIM BKP FAIL |

**Roll trim** — aileron trim tab via Trim Actuation System (TAS) from trim panel.

**Rudder / yaw trim** — rudder trim tab (also TAS).

**3-second rule (roll & rudder trim)** — hold trim switch > **3 seconds** and movement **stops** (runaway protection). Release, then trim again in steps.

**No CAS for roll/rudder trim failure** — you discover it because the tab **does not move** when you command trim.

**AP mistrim** — if autopilot was trimming pitch, see **Automatic Flight** (AP PITCH MISTRIM) — different from PTRIM failures.
"""
        )
        _table(
            [
                ("CAUTION", "PTRIM NML FAIL", "Normal pitch trim channel lost — backup may still work."),
                ("CAUTION", "PTRIM BKP FAIL", "Backup pitch trim lost — if normal also failed, pitch trim severely degraded."),
                ("ADVISORY", "PTRIM LO RATE", "Trim moving slowly — monitor; may not reach desired setting quickly."),
                ("ADVISORY", "PTRIM SW 1 FAIL", "Trim switch channel 1 failed."),
                ("ADVISORY", "PTRIM SW 2 FAIL", "Trim switch channel 2 failed."),
            ],
            ["Level", "CAS", "Pilot action (concept)"],
        )

    with st.expander("**5. Spoilers & speedbrake**", expanded=False):
        st.markdown(
            """
### One spoiler system — three jobs


| Function | When | Purpose |
|----------|------|---------|
| **Roll spoiler** | Flaps ≠ 0 and control wheel **> ~30°** | Extra roll authority |
| **Ground spoiler** | Armed + on ground + thrust idle (RTO/landing) | Dump lift, increase braking |
| **Speedbrake** | In flight, **flaps 0 only** | Drag / descent |

**Ground spoiler deploy** — typically requires: **armed**, **on ground (WOW)**, **thrust levers idle**. Deploy ~35° in ~1.2 s.

**Flaps vs speedbrake** — speedbrake **will not extend** if flaps beyond 0; if already open, spoilers **retract** when flaps extend.

**Hydraulic protection** — internal stops limit spoiler travel if hydraulic pressure is lost (prevents uncontrolled full deployment).

**Control** — speedbrake lever; verify on **MFD** synoptic (**SOP: 'SPEEDBRAKE OPEN/CLOSED'**).

**Handbook note (Ch 5.5)** — **SPOILER FAULT** after deploying speedbrake in flight is often **water ingress** in LVDT sensors after heavy rain (false asymmetric detection). Usually clears after **power cycle** when dry. Avoid selecting speedbrake in flight if heading to a performance-limited runway as precaution — **ground spoilers still deploy on WOW** (different logic).
"""
        )
        _table(
            [
                ("CAUTION", "GND SPLR FAIL", "Ground spoiler function lost — longer stopping distance on RTO/landing. Brief performance."),
                ("ADVISORY", "SPDBRK SW DISAG", "Speedbrake lever position disagrees with actual spoiler position — verify visually/synoptic."),
                ("ADVISORY", "SPOILER FAULT", "Spoiler system fault — roll assist / speedbrake / ground spoilers may be affected."),
            ],
            ["Level", "CAS", "What it means"],
        )

    with st.expander("**6. Rudder — gust lock, boost, ventral rudder**", expanded=False):
        st.markdown(
            """
**Gust lock** — protects rudder on the ground in strong winds. Must be **unlocked before flight**.

| CAS | Meaning |
|-----|---------|
| **RUD GUST LOCKED** | Gust lock not retracted — do not take off until resolved (QRH). |

**Rudder boost** — hydraulic assist on the rudder pedals (spring actuator). Helps during takeoff, crosswind, OEI.

| CAS | Meaning |
|-----|---------|
| **RUD OVERBOOST** | Uncommanded rudder boost / spring actuator activity — fly the aircraft, QRH. |
| **RUD BOOST FAIL** (advisory) | Boost unavailable — heavier rudder forces, especially low speed. |

**Ventral rudder** — separate small surface on the ventral fin; **not** on your pedals. Used for **yaw damping** when primary **yaw damper is OFF** (above ~60 KIAS). When **YD is ON**, ventral rudder **trails** (streamlined).

→ Details: **Systems → Automatic Flight → Yaw damper & ventral rudder**.
"""
        )

    with st.expander("**7. SWPS — stall warning & stick pusher**", expanded=False):
        st.markdown(
            """
**SWPS** = Stall Warning and Protection System.

**Stall warning** — aural + stick shaker before the stall. Activation angles/speeds come from angle-of-attack logic.

**Stick pusher** — if you do not recover, the pusher drives the column **forward** to reduce AoA (hydraulic priority protected).

| Item | Location / action |
|------|-------------------|
| **PUSHER CUTOUT** | Push in to inhibit pusher (e.g. inadvertent activation — **Memory Items**) |
| **STALL WARN CUTOUT** | Inhibits shaker (limited use per QRH — e.g. some maintenance/test) |

**Icing interaction** — with **WINGSTAB** anti-ice ON, stall speeds increase → **SWPS ICE SPEED** / **ICE SPEED** CAS. Reset **ICE SPEED** only above 1,500 ft AAL when sure ice is gone.

**Takeoff configuration check** — part of the warning system; verifies flaps/trim/speedbrake etc. before takeoff (see **Warning System**).
"""
        )
        _table(
            [
                ("CAUTION", "PUSHER FAIL", "Pusher may not activate — treat stall margins conservatively."),
                ("CAUTION", "PUSHER OFF", "Pusher inhibited (cutout or fault) — know why before continuing."),
                ("CAUTION", "SWPS FAIL", "Stall warning/protection degraded — QRH."),
                ("CAUTION", "SWPS FAULT", "SWPS fault — verify status before takeoff or continuing."),
                ("CAUTION", "SWPS UNTESTED", "Power-up test not completed — do not dispatch until resolved."),
            ],
            ["Level", "CAS", "What it means"],
        )
        st.markdown(
            "**Memory item:** *Inadvertent pusher actuation* → **PUSHER CUTOUT — PUSH IN** (see **Memory Items**)."
        )

    cas_quick_reference(
        [
            ("Flaps", "CAUTION", "FLAP FAIL", "No flap movement — QRH, performance, alternate."),
            ("Flaps", "ADVISORY", "FLAPS NOT AVAIL", "Plan approach without flaps."),
            ("Spoilers", "CAUTION", "GND SPLR FAIL", "No ground spoilers — stopping distance."),
            ("Spoilers", "ADVISORY", "SPDBRK SW DISAG", "Lever vs actual — verify synoptic."),
            ("Spoilers", "ADVISORY", "SPOILER FAULT", "Spoiler functions degraded."),
            ("Pitch trim", "CAUTION", "PTRIM NML FAIL", "Normal trim lost — try backup."),
            ("Pitch trim", "CAUTION", "PTRIM BKP FAIL", "Backup trim lost."),
            ("Pitch trim", "ADVISORY", "PTRIM LO RATE", "Slow trim rate."),
            ("Pitch trim", "ADVISORY", "PTRIM SW 1/2 FAIL", "Trim switch channel failed."),
            ("Rudder", "CAUTION", "RUD GUST LOCKED", "Do not depart — unlock gust lock."),
            ("Rudder", "CAUTION", "RUD OVERBOOST", "Uncommanded boost — QRH."),
            ("Rudder", "ADVISORY", "RUD BOOST FAIL", "Heavier rudder forces."),
            ("SWPS", "CAUTION", "PUSHER FAIL / OFF", "Pusher unavailable or inhibited."),
            ("SWPS", "CAUTION", "SWPS FAIL / FAULT / UNTESTED", "Stall protection degraded."),
        ],
        title="8. CAS quick reference",
    )

    with st.expander("**9. Power-up FCE messages (handbook note)**", expanded=False):
        st.markdown(
            """
NetJets Handbook references **FOL 015/11** for **FCE-related CAS at power-up** (flap fail, spoiler fault, pitch trim faults).

### Practical approach:

1. Note exact CAS level and text.
2. Check MFD **flight controls synoptic**.
3. Do not rush past **Before Takeoff** — config check may catch related issues.
4. Use **QRH** + maintenance if message persists.
"""
        )

    back_to_top()
    source_footer("poh", "§6-07 Flight Controls · Handbook FOL 015/11 (FCE CAS)")
