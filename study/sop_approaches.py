import streamlit as st

from content.render_helpers import source_footer
from study.sop_styles import sop_note
from ui.theme import render_section_label


def render_approaches():
    render_section_label("6 · Approaches — exact callouts")
    with st.expander("**General — all approaches (2.12.2)**", expanded=False):
        st.markdown("""
**Descent & config (every approach)**
| Situation | PF | PM |
|-----------|----|----|
| Passing FL100 / 10,000 ft | **'FL100'** or **'10,000 FEET'** | **'XXX'** (current speed; reduce if >250 KIAS) |
| QNH / QFE set | **'SET QNH / QFE'** | **'QNH / QFE XXXX SET AND BLUE'** |
| Flap change | **'FLAP [X]'** | **'XXX'** → move lever → **'FLAP [X]'** |
| Gear down | **'GEAR DOWN'** | **'XXX'** → lever DN → **'GEAR DOWN'** |

**At DA / MDA (2.12.2.2)**
- Baro MINIMUMS set → auto **'MINIMUMS, MINIMUMS'** at selected altitude.
- If no auto call: PM **'DECIDE'**.
- PF: **'CONTINUE'** or **'GO-AROUND, FLAP 1 or 2'**.

**Not stable at gate**
- PM: **'UNSTABLE, GO-AROUND'**
- PF: **'GO-AROUND, FLAP 1 (or 2)'**
""")
        sop_note("warn", "Unstable → PM: <strong>'UNSTABLE, GO-AROUND'</strong> · PF: <strong>'GO-AROUND, FLAP 1 (or 2)'</strong>")
        source_footer("om_b", "2.12.2 Approach Callouts")

    with st.expander("**CAT I — ILS (2.13.1 + profile)**", expanded=False):
        st.markdown("""
**Procedure callouts (verbatim)**
| Situation | PF | PM |
|-----------|----|----|
| Cleared approach | **'LOC WHITE, GS WHITE'** | Verifies modes |
| LOC capture | **'LOC GREEN'** | Verifies |
| GS capture | **'GS GREEN'** | **'[XXXX] FT SET'** (MAA) |
| | **'CHECKED'** | Verifies MAA |
| GS check (until OM or 4 NM) | **'[XXXX] FT'** | **'GLIDESLOPE CHECK'** |
| Not stable at gate | — | **'UNSTABLE, GO-AROUND'** → **'GO-AROUND, FLAP 1 (or 2)'** |
| 100 ft above DA | **'ONE HUNDRED ABOVE'** | Scan outside |
| DA | — | **'MINIMUMS, MINIMUMS'** |
| Decision | **'CONTINUE'** or **'GO-AROUND FLAP 1 (or 2)'** | — |

**Profile stabilised point:** **Stabilised or Go Around** · Final: **V_REF** at runway

**Configuration — LATEST gates**
| DME | Configuration | Speed |
|-----|---------------|-------|
| 6 DME | Flap 1 | 160 KIAS |
| 5 DME | Gear Down, Flap 2 | 160 KIAS |
| 4 DME | Flap 3 (or FULL), V_AP | V_AP |

**Flow:** DOWNWIND 170 KIAS → APR: HDG + AP YD + VS → LOC + AP YD + ALT + GS → GS capture + AAD → **BEFORE LANDING CHECKLIST**
""")
        source_footer("om_b", "2.13.1 ILS · Flight Profile CAT I")

    with st.expander("**PAR approach (2.13.2)**", expanded=False):
        st.markdown("""
Same profile as **NPA CDFA**, but **HDG** instead of FMS.

| Situation | PF | PM |
|-----------|----|----|
| Radar vectors | **'HDG GREEN'** | Verifies |
| ATC: *Approaching descent point* | Set AAD 300 ft above current (or MAA if higher); **'VS GREEN'** | Verifies VS |
| ATC: *Begin descent now* | Select ROD | **'[XXXX] FT SET'** (MAA when below MAA) |
| | **'CHECKED'** | — |
| Not stable | — | **'UNSTABLE, GO-AROUND'** |
| Go-around | **'GO-AROUND, FLAP 1 (or 2)'** | — |
| 100 ft above DA | **'ONE HUNDRED ABOVE'** | — |
| DA | — | **'MINIMUMS, MINIMUMS'** |
| Decision | **'CONTINUE'** or **'GO-AROUND FLAP 1 (or 2)'** | — |

**Note:** Set MAA only when MAA is **above** current altitude.
""")
        source_footer("om_b", "2.13.2 PAR Approach")

    with st.expander("**LPV — APV (2.14.1)**", expanded=False):
        st.markdown("""
| Situation | PF | PM |
|-----------|----|----|
| Cleared approach | **'FMS PINK, GP WHITE'** | Verify; confirm **FMS LPV** on HSI before FAP |
| GP intercept | **'GP PINK'** | **'[XXXX] FT SET'** |
| | **'CHECKED'** | — |
| Not stable at gate | — | **'UNSTABLE, GO-AROUND'** → **'GO-AROUND, FLAP 1 (or 2)'** |
| 100 ft above DA | **'ONE HUNDRED ABOVE'** | — |
| DA | — | **'MINIMUMS, MINIMUMS'** |
| Decision | **'CONTINUE'** or **'GO-AROUND FLAP 1 (or 2)'** | — |

**Profile:** Same config gates as CAT I (see CAT I expander).
""")
        source_footer("om_b", "2.14.1 LPV · Flight Profile APV")

    with st.expander("**LNAV / VNAV — APV (2.14.2)**", expanded=False):
        st.markdown("""
| Situation | PF | PM |
|-----------|----|----|
| Cleared approach | **'FMS PINK, GP WHITE'** | Verify; confirm **FMS L/VNAV** on HSI before FAP |
| GP intercept | **'GP PINK'** | **'[XXXX] FT SET'** |
| | **'CHECKED'** | — |
| Not stable at gate | — | **'UNSTABLE, GO-AROUND'** → **'GO-AROUND, FLAP 1 (or 2)'** |
| 100 ft above DA | **'ONE HUNDRED ABOVE'** | — |
| DA | — | **'MINIMUMS, MINIMUMS'** |
| Decision | **'CONTINUE'** or **'GO-AROUND FLAP 1 (or 2)'** | — |

**Profile:** Same config gates as CAT I / APV diagram.
""")
        source_footer("om_b", "2.14.2 LNAV/VNAV · Flight Profile APV")

    with st.expander("**LNAV — NPA CDFA (2.15.1)**", expanded=False):
        st.markdown("""
| Situation | PF | PM |
|-----------|----|----|
| Cleared (LNAV+V) | **'FMS PINK, GP WHITE'** | Verify **FMS LNAV+V** or **LNAV** before FAP |
| Cleared (LNAV only) | **'FMS PINK'** | Verify **LNAV**; use VS for profile |
| On vertical path | **'CORRECTING'** (if high/low) | **'[X] DME at [XXXX] FEET'** |
| Within 50 ft | — | **'ON PROFILE'** or **'[XXX] FEET HIGH or LOW'** |
| | — | **'NEXT [X] NM, [XXXX] FEET'** |
| Not stable | — | **'UNSTABLE, GO-AROUND'** → **'GO-AROUND, FLAP 1 (or 2)'** |
| 100 ft above DA | **'ONE HUNDRED ABOVE'** | — |
| DA | — | **'MINIMUMS, MINIMUMS'** |
| Decision | **'CONTINUE'** or **'GO-AROUND FLAP 1 (or 2)'** | — |

**Profile:** NPA CDFA diagram — same LATEST config gates as CAT I.
""")
        source_footer("om_b", "2.15.1 LNAV · Flight Profile NPA CDFA")

    with st.expander("**FMS Overlay — VOR/NDB CDFA (2.15.2)**", expanded=False):
        st.markdown("""
| Situation | PF | PM |
|-----------|----|----|
| Cleared approach | **'FMS PINK'** | Verify FMS mode |
| Approaching FAF | **'VS GREEN'** (0.3 NM before FAF) | **'[XXXX] FT SET'** (MAA) |
| | **'CHECKED'** | — |
| On vertical path | **'CORRECTING'** | **'[X] DME at [XXXX] FEET'** / **'ON PROFILE'** / **HIGH or LOW** |
| | — | **'NEXT [X] NM, [XXXX] FEET'** |
| Not stable | — | **'UNSTABLE, GO-AROUND'** → **'GO-AROUND, FLAP 1 (or 2)'** |
| 100 ft above DA | **'ONE HUNDRED ABOVE'** | — |
| DA | — | **'MINIMUMS, MINIMUMS'** |
| Decision | **'CONTINUE'** or **'GO-AROUND FLAP 1 (or 2)'** | — |

**Note:** Primary aid (VOR/NDB) displayed at all times on PM PFD or RMI.
""")
        source_footer("om_b", "2.15.2 FMS Overlay · Flight Profile NPA CDFA")

    with st.expander("**Non-FMS Overlay — LOC / VOR / NDB / SRA (2.15.3)**", expanded=False):
        st.markdown("""
Same CDFA profile and vertical callouts as **FMS Overlay**, but lateral modes differ:

| Situation | PF | PM |
|-----------|----|----|
| Cleared approach | **'LOC WHITE'** or **'VAPP WHITE'** | Verify mode |
| Intercepting final | **'LOC GREEN'** or **'VAPP GREEN'** | Verify active mode |

**Technique**
- **LOC** NPA: always Non-FMS overlay, FD coupled to LOC.
- **VOR:** APR (VAPP) mode.
- **NDB:** HDG mode.
- **SRA:** HDG + VS CDFA; add **50 ft** to minima; same vertical callouts as CDFA table above.

**Vertical / DA callouts:** same as FMS Overlay (ON PROFILE, MINIMUMS MINIMUMS, etc.).
""")
        source_footer("om_b", "2.15.3 Non-FMS Overlay · 2.15.3.1 SRA")

    with st.expander("**IGS approach (2.15.4)**", expanded=False):
        st.markdown("""
Flown **as ILS** (use **CAT I / ILS callouts**), but published altitudes at each DME/LOC step must be **strictly observed**.

Refer to OM-A for IGS-specific rules.
""")
        source_footer("om_b", "2.15.4 IGS")

    with st.expander("**Visual approach (2.17 + profile)**", expanded=False):
        st.markdown("""
**Procedure callouts**
| Situation | PF | PM |
|-----------|----|----|
| Not stable at gate | **'GO-AROUND, FLAP 1 (or 2)'** | **'UNSTABLE, GO-AROUND'** |

**Profile callouts**
| Point | Verbatim callout |
|-------|------------------|
| Stabilised approach point | **Stabilised or Go Around** (Wings level by 300') |
| Final approach | **V_REF** |

**Pattern phases**
| Phase | Action |
|-------|--------|
| 1500 ft downwind | 150 kts, N1 ±50%, HDG + AP YD + ALT |
| Abeam threshold | Start timing, Gear Down, Flap 2 |
| Base turn | Max bank 30°, start descent, HDG + AP YD + VS |
| Finals turn | Complete ~600 ft, V_AP, N1 ±48% (min 125 kts) |
| Before landing | Flap 3 (OR FULL), Before Ldg Checklist, 140 kts |
| Final | 150 kts on final |

**Timing:** 3 secs per 100 ft AAL ± wind (1500 ft AAL nil wind = 45 secs)
""")
        source_footer("om_b", "2.17 Visual · Flight Profile")

    with st.expander("**Circling approach (2.18 + profile)**", expanded=False):
        st.markdown("""
**Instrument segment callouts (2.18)**
| Situation | PF | PM |
|-----------|----|----|
| Cleared | **'LOC/VAPP WHITE'** | — |
| Intercept | **'LOC/VAPP GREEN'** | **'[XXX] FT SET'** (AAD circling alt) |
| Approaching FAF | **'VS GREEN'** (0.3 NM before) | Verify VS |
| | **'CHECKED'** | — |
| NPA on path | **'CORRECTING'** | **'[X] DME at [XXXX] FEET'** / **ON PROFILE** / **HIGH or LOW** |
| Precision GS check | **'[XXXX] FT'** | **'GLIDESLOPE CHECK'** |
| 100 ft above circling alt | **'ONE HUNDRED ABOVE'** | Scan outside |
| Level at circling alt | **'ALT GREEN'** | **'[XXXX] FEET SET'** (MAA) |
| Circling minima / break-off | — | **'MINIMUMS, MINIMUMS'** |
| Decision | **'CONTINUE'** or **'GO-AROUND FLAP 1 (or 2)'** | — |
| If CONTINUE | **'HDG GREEN'** | Start clock |
| Not stable (visual) | — | **'UNSTABLE, GO-AROUND'** |

**Profile stabilised point:** **V_REF** (Min wings level by 300'), **Stabilised or Go Around**

**Missed approach from circling:** MAP of the **active instrument approach**.
""")
        source_footer("om_b", "2.18 Circling · Flight Profile")

    with st.expander("**Steep approach (2.25.7 + profile)**", expanded=False):
        st.markdown("""
**Profile callouts**
| Point | Verbatim callout |
|-------|------------------|
| At DA | **"MINIMUMS"** |
| Stabilised approach point | **Stabilised or Go Around** |
| Final approach speed | **V_REF STEEP** |

**Configuration:** 2 NM to G/S — Gear Down, Flap 2 · 1 NM — Flap FULL, AAD MAA · GS capture — PM Speedbrake OPEN

**Go-around from steep:** Flap 2, min **V_AC** — PM verify speedbrake **CLOSED**
""")
        source_footer("om_b", "2.25.7 Steep · Flight Profile")

    with st.expander("**OEI approach & landing — abnormal**", expanded=False):
        st.markdown("""
**Profile callouts (verbatim)**
| Point | Verbatim callout |
|-------|------------------|
| Stabilised approach point | **'Stable'** or **'Go Around Flap 1'** |
| At DA | **"MINIMUMS"** |
| Final approach speed | **Corrected V_REF** |

**Configuration triggers**
| Trigger | Action |
|---------|--------|
| G/S Alive | Flap 1 |
| One dot above | Gear Down, Flap 2 |
| G/S Intercept | Flap 3, AAD set to **MAA** |
| G/S Capture | LOC + AP + GS, V_AP, Flap 3 & Gear, N1 ±63% |

**Pattern:** DOWNWIND 170 KIAS, N1 ±65% · YD optional but **OFF for landing**

Also valid for **OEI CDFA** and **OEI visual straight-in**.
""")
        source_footer("om_b", "Flight Profiles · OEI Approach")

    with st.expander("**NPA Non-CDFA (2.16)**", expanded=False):
        sop_note("info", "<strong>Not applicable</strong> — all NPA flown as CDFA per OM-B / OM-A.")
        source_footer("om_b", "2.16 NPA Non-CDFA")

    with st.expander("**Stabilised approach criteria (2.12.9)**", expanded=False):
        st.markdown("""
| Approach type | Height (ft AAL) | Stable criteria |
|---------------|-----------------|-----------------|
| IFR straight-in | 1000 | Stable except speed |
| IFR straight-in | 500 | Fully stable |
| VFR / visual | 500 | Fully stable |
| Circle to land | 1000 | Circling configuration |
| Circle to land | 500 | Fully stable (wings level by 300 ft if manoeuvring below 500) |

**Not stable at gate:** PM **'UNSTABLE, GO-AROUND'** → PF **'GO-AROUND, FLAP 1 (or 2)'**

**Go-around if** criteria not met, cannot safely achieve them, or destabilised after the gate.
""")
        source_footer("om_b", "2.12.9 Stabilised Approach")


def render_go_arounds():
    render_section_label("7 · Go-around — exact callouts")
    with st.expander("**Missed approach — all engines (2.19.1 + profile)**", expanded=False):
        st.markdown("""
**OM-B procedure callouts (verbatim)**
| Situation | PF | PM |
|-----------|----|----|
| Go-around | Push TOGA, thrust, pitch to FD | **'GO-AROUND, FLAP 1 (or 2)'** — move flap |
| Positive rate | Verify rate & IAS | **'POSITIVE RATE'** |
| Gear up | **'GEAR UP'** | Move gear up; FLC, **'FLC GREEN, SPEED 150'** |
| | Verify FLC | **'GEAR UP, FLAP 1 (or 2)'** |
| FMS missed app | Verify FMS pink | **'FMS PINK'** (if MAP in FMS) |
| HDG/VOR missed app | Verify mode green | **'HDG / VOR GREEN'** |
| 1000 ft AAL | Manage thrust | **'1000 FEET'** → **'FLAP 0'** |
| Flap 0 closed loop | Verify flaps | **'XXX'** → **'FLAP 0'** |
| Complete | — | **'YD GREEN'** (YD ON, LDG/TAXI TAXI) |

**Profile shorthand:** **"GO AROUND, FLAP 1 (or 2)"** → **"POSITIVE RATE"** — **"Gear Up"** → Flap 0 at 1000 ft → **AFTER T/O CHECKLIST**

**After steep:** SPDBRK switch closed · Min AP engage **600 ft AAL**
""")
        source_footer("om_b", "2.19.1 Missed Approach · Flight Profile GA")

    with st.expander("**Balked landing (2.19.2)**", expanded=False):
        sop_note(
            "warn",
            "Low-energy go-around — TOGA, hold attitude, accelerate to <strong>V_REF</strong>, "
            "then <strong>V_AC</strong> before GA flap. Continue missed approach callouts.",
        )
        source_footer("om_b", "2.19.2 Balked Landing")

    with st.expander("**OEI go-around (abnormal profile)**", expanded=False):
        st.markdown("""
**Exact callouts (OM-B profile — from Flap 3)**
| Event | Verbatim callout / action |
|-------|---------------------------|
| Initiation | **"GO AROUND, FLAP 1"** |
| PF | Push TO/GA, Set GA Thrust, Pitch to FD — ROL + GA/ALTS |
| PM | Set Flap 1 |
| Positive rate | **"POSITIVE RATE"** — **"Gear Up"** |
| PM | Select FLC, Set **V_AC**, HDG or NAV, LOW BANK A/R |
| Climb | **V_AC** (max V_AC + 10) |
| 1000 ft AAL | Consider AP (YD OFF) |
| 1500 ft AAL or briefed min | Accel alt if higher |
| Acceleration | V_FS → CON thrust, disengage low bank, V_AC + 10, Flap 0 |
| | **AFTER T/O CHECKLIST** |
""")
        source_footer("om_b", "Flight Profiles · OEI Go-Around")
