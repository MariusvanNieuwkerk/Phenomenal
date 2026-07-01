"""Automatic Flight (AFCS) — Phenom 300 pilot guide (ATA 22)."""

import pandas as pd
import streamlit as st

from content.render_helpers import back_to_top, cas_quick_reference, source_footer


def _table(rows: list[tuple], columns: list[str]):
    st.dataframe(pd.DataFrame(rows, columns=columns), hide_index=True, use_container_width=True)


def render_automatic_flight():
    st.markdown("## Automatic Flight (AFCS)")
    st.caption("ATA 22 · Autopilot · Flight Director · Yaw damper · POH §6-03 · OM-B automation")

    with st.expander("**1. What the AFCS does**", expanded=True):
        st.markdown(
            """
The **Automatic Flight Control System** has three pilot-facing functions:

| Function | Button / cue | What it does |
|----------|--------------|--------------|
| **Flight Director (FD)** | Mode selections on AFCP | **Commands on the PFD** — you hand-fly the cues |
| **Autopilot (AP)** | AP switch | **Flies the aircraft** via servos on aileron, elevator, rudder |
| **Yaw damper (YD)** | YD switch (often with AP) | Damps **Dutch roll** — coordinates yaw |

**Servos** — electromechanical actuators on primary flight controls. AP commands go through them; you can override with force or **CWS**.

**FMA (Flight Mode Annunciator)** — always know **lateral** and **vertical** active modes (e.g. HDG + ALT, FMS + GP).

→ Exact callouts: **SOP → General → Automation**.
"""
        )

    with st.expander("**2. FD vs AP — when to use which**", expanded=False):
        st.markdown(
            """
### Flight Director only (AP OFF)

- PF hand-flies the **command bars**.
- PM selects modes and calls **'[MODE] GREEN'** after PF selects.
- Used below AP engage height, manoeuvring, or when AP not desired.

### Autopilot ON

- Servos fly to FD commands.
- PF monitors; PM verifies modes and manages nav/altitude changes.
- **CWS** — press and hold on the yoke to hand-fly **without** disconnecting AP; FD resynchronises to attitude when released.

### Quick disconnect (red button)

- Disconnects **AP and YD** immediately.
- After release: AP and YD stay **off** until re-selected (trim and pusher logic separate).

**Pilot tip:** AP reduces workload; it does **not** reduce responsibility. Unstable approach → **go-around** regardless of AP status.
"""
        )

    with st.expander("**3. Engagement & use heights**", expanded=False):
        st.markdown("Limits from OM-B / AFM (also in **Quick Lookup → Autoflight / YD**).")
        _table(
            [
                ("Min AP **engage** (both engines)", "600 ft AAL"),
                ("Min AP **engage** (OEI)", "1,000 ft AAL"),
                ("Min AP **use** — disconnect before landing (both engines)", "195 ft AGL"),
                ("Min AP **use** — disconnect before landing (OEI)", "220 ft AGL"),
                ("OM-B note", "Consider AP at 1,000 ft AAL on missed approach (YD OFF)"),
            ],
            ["Limit", "Value"],
        )
        st.markdown(
            """
**SOP landing** — PF disconnects **AP/YD ≥195 ft AGL** (220 OEI); PM verifies **AP/YD off** and **YD OFF** before touchdown.

**Takeoff** — AP typically after 1,000 ft; PM may select **YD ON** or AP on PF command. Avoid **MAX** thrust detent on roll (TO RSV / ECS risks).
"""
        )

    with st.expander("**4. Yaw damper & ventral rudder**", expanded=False):
        st.markdown(
            """
**Yaw damper (primary)** — damps Dutch roll via the **rudder** (AFCS servo). Engaged with YD switch; status on PFD (**YD GREEN** in SOP).

**Ventral rudder (backup SAS)** — small surface on the ventral fin, **not** connected to your pedals:
- **On ground / below ~60 KIAS** — centered
- **YD OFF, airborne** — active yaw damping (lets you dispatch if YD inop — **VRS**)
- **YD ON** — ventral rudder **trails** (streamlined)

**Why it matters on the 300** — swept wing → Dutch roll tendency; YD is more critical than on Phenom 100.

**Icing limitation** — with **YD OFF** in icing: **max 180 KIAS** (ventral rudder alone may not meet damping criteria in icing above that speed).
"""
        )
        _table(
            [
                ("YD ON", "Normal — ventral rudder streamlined, rudder YD active"),
                ("YD OFF, airborne", "Ventral rudder provides backup damping"),
                ("YD OFF + icing", "Max **180 KIAS**"),
                ("Abnormal YD disconnect", "YD flashes **reverse video** on PFD"),
            ],
            ["State", "What to know"],
        )

    with st.expander("**5. Common modes (mental model)**", expanded=False):
        st.markdown(
            """
**Lateral** — HDG · NAV/FMS · LOC · VOR · APPR (FMS approach) · TO/GA roll

**Vertical** — ALT · VS · FLC · FMS/VNAV · GP (glidepath) · TO/GA pitch

**Colour cues on PFD (SOP)** — **GREEN** = active captured mode · **WHITE** = armed · **PINK** = FMS lateral

**Approaches** — APPR mode for GPS approaches; see **Systems → RNAV / RNP Approaches** for LPV/LNAV logic.

**Steep approach** — special mode for steep glideslope airports (e.g. EGLC). Failure → **STEEP FAIL** CAS.
"""
        )

    with st.expander("**6. Steep approach mode**", expanded=False):
        st.markdown(
            """
Some airports require **steeper than normal** glideslope (e.g. London City 5.5°).

### Concept

- AFCS provides **steep approach** guidance when selected and available.
- Uses different gain/limits than normal ILS/APV.

| CAS | Meaning |
|-----|---------|
| **STEEP FAIL** | Steep approach mode unavailable — cannot use steep procedure as briefed; alternate minima/airport. |

Check **OM-C airport briefing** and **OM-B steep approach** supplement before operating to steep-approach aerodromes.
"""
        )

    with st.expander("**7. Mistrim, disconnects & go-around**", expanded=False):
        st.markdown(
            """
**Mistrim** — AP was trimming but something disagrees:

| CAS | Axis | Typical meaning |
|-----|------|-----------------|
| **AP PITCH MISTRIM** | Pitch | AP pitch trim command vs surface — verify trim, consider disconnect |
| **AP ROLL MISTRIM** | Roll | Roll servo / trim disagreement — hand-fly, QRH |

**AP FAIL** — autopilot has failed or disconnected abnormally. **Fly the aircraft** — FD may still guide if available.

### Go-around

- **TO/GA** mode (when armed/selected) — pitch and roll guidance for missed approach.
- Disconnect AP/FD as per QRH if behaviour is wrong.

**After any abnormal disconnect** — announce, fly path, complete QRH, then re-engage only when stable and above min heights.
"""
        )

    cas_quick_reference(
        [
            ("Autopilot", "CAUTION", "AP FAIL", "AP failed/disconnected — hand-fly or re-engage per QRH."),
            ("Autopilot", "CAUTION", "AP PITCH MISTRIM", "Pitch trim disagreement with AP — verify, disconnect if needed."),
            ("Autopilot", "CAUTION", "AP ROLL MISTRIM", "Roll mistrim — disconnect AP, check controls."),
            ("Steep approach", "CAUTION", "STEEP FAIL", "Steep approach not available."),
            ("SWPS", "—", "PUSHER / SWPS", "See Flight Controls — SWPS section."),
        ],
        title="8. CAS quick reference",
    )

    with st.expander("**9. Study checklist**", expanded=False):
        st.markdown(
            """
Before your session, you should be able to explain **without notes**:

1. Difference between **FD**, **AP**, and **YD**.
2. **Min engage** vs **min use** heights (600/1000 ft vs 195/220 ft).
3. What the **ventral rudder** does when YD is ON vs OFF.
4. What happens when you press **CWS** vs **quick disconnect**.
5. What **AP PITCH MISTRIM** and **AP ROLL MISTRIM** imply.
6. **STEEP FAIL** operational consequence.
7. Where **SWPS / pusher** fits (Flight Controls — not AFCS, but same training day).

### In Briefly

- **SOP → Approaches** — mode callouts on final
- **SOP → General → Automation** — AP/FD tables
- **Flight Profiles** — profile diagrams
- **Memory Items** — inadvertent pusher
- **Documents** — QRH for each failure
"""
        )

    back_to_top()
    source_footer("om_b", "§2.1 Automation · §2.12 Approach automation · POH §6-03 AFCS")
