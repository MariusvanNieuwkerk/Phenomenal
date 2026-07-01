"""Pilot guide — RNAV, RNP, and FMS approaches (understanding-first)."""

import streamlit as st

from content.render_helpers import back_to_top, source_footer
from study.semantic_color import colorize_sop_md
from ui.tokens import COLORS, FONT_FAMILY


def _css():
    return f"""
<style>
.briefly-rnav-wrap {{ font-family: {FONT_FAMILY}; color: {COLORS["ink"]}; }}
.briefly-rnav-hero {{
  background: linear-gradient(135deg, {COLORS["accent"]} 0%, {COLORS["accent_dark"]} 100%);
  border-radius: 16px; padding: 1.1rem 1.25rem; color: #fff; margin-bottom: 1rem;
}}
.briefly-rnav-hero h3 {{ margin: 0; font-size: 1.35rem; font-weight: 800; }}
.briefly-rnav-hero p {{ margin: 0.4rem 0 0; font-size: 0.92rem; opacity: 0.92; line-height: 1.5; }}
.briefly-rnav-card {{
  background: {COLORS["surface"]}; border: 1.5px solid {COLORS["border"]};
  border-radius: 14px; padding: 0.95rem 1.1rem; margin-bottom: 0.85rem;
}}
.briefly-rnav-card h4 {{
  margin: 0 0 0.55rem; font-size: 0.78rem; font-weight: 800;
  letter-spacing: 0.08em; text-transform: uppercase; color: {COLORS["accent_dark"]};
}}
.briefly-rnav-card p, .briefly-rnav-card li {{
  font-size: 0.94rem; line-height: 1.58; color: {COLORS["ink_soft"]};
}}
.briefly-rnav-card ul {{ margin: 0.35rem 0 0; padding-left: 1.15rem; }}
.briefly-rnav-card li {{ margin-bottom: 0.4rem; }}
.briefly-rnav-axis {{
  display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.55rem;
  margin: 0.5rem 0 0.25rem;
}}
.briefly-rnav-axis div {{
  background: rgba(255,255,255,0.55); border: 1px solid {COLORS["border"]};
  border-radius: 10px; padding: 0.65rem 0.8rem; font-size: 0.88rem; line-height: 1.45;
}}
.briefly-rnav-axis strong {{ color: {COLORS["ink"]}; display: block; margin-bottom: 0.2rem; }}
</style>
"""


def _md(text: str):
    st.markdown(colorize_sop_md(text), unsafe_allow_html=True)


def _card(title: str, body: str):
    st.markdown(
        f'<div class="briefly-rnav-wrap"><div class="briefly-rnav-card">'
        f"<h4>{title}</h4>{body}</div></div>",
        unsafe_allow_html=True,
    )


def render_rnav_approaches():
    st.markdown(_css(), unsafe_allow_html=True)

    st.markdown(
        f"""
<div class="briefly-rnav-wrap">
  <div class="briefly-rnav-hero">
    <h3>RNAV / RNP &amp; FMS Approaches</h3>
    <p>Pilot guide — understand what the chart says, what the Garmin does, and what OM-B expects.
    For exact callouts and profiles, use <strong>SOP → Approaches</strong> and <strong>Flight Profiles</strong>.</p>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

    tab_model, tab_terms, tab_types, tab_garmin, tab_downgrade, tab_map, tab_db, tab_fleet = st.tabs(
        ["Mental model", "Terms", "Approach types", "Garmin G3000", "Downgrades", "Chart → cockpit", "Database updates", "Fleet setup"]
    )

    with tab_model:
        _card(
            "The confusion in one sentence",
            "<p>Pilots mix up <strong>three different things</strong>: what the "
            "<em>chart/regulation</em> calls the procedure, what <em>type of approach</em> "
            "you are flying (APV vs NPA), and what the <em>Garmin annunciates</em> on the HSI.</p>",
        )
        st.markdown(
            f"""
<div class="briefly-rnav-wrap">
  <div class="briefly-rnav-card">
    <h4>Three axes — keep them separate</h4>
    <div class="briefly-rnav-axis">
      <div><strong>1 · Chart / regulation</strong>RNAV1, RNP APCH, RNP AR, “RNAV GNSS RWY 18” — names and nav specs on the plate.</div>
      <div><strong>2 · Approach class (OM-B)</strong>Precision (ILS) · <strong>APV</strong> (LPV, LNAV/VNAV) · <strong>NPA</strong> (LNAV, overlays, CDFA).</div>
      <div><strong>3 · Garmin mode (HSI)</strong>FMS LPV · FMS L/VNAV · FMS LNAV · FMS LNAV+V · FMS PINK (overlay).</div>
    </div>
  </div>
</div>
""",
            unsafe_allow_html=True,
        )
        _card(
            "Practical rule",
            "<ul>"
            "<li>Pick your <strong>minima line</strong> on the Jeppesen chart first (LPV, LNAV/VNAV, LNAV…).</li>"
            "<li>That choice drives <strong>which OM-B section</strong> applies (2.14 APV vs 2.15 NPA).</li>"
            "<li>Before the FAF, confirm the <strong>HSI annunciation</strong> matches what you briefed.</li>"
            "</ul>",
        )
        _card(
            "CDFA — why NetJets cares",
            "<p>All non-precision approaches at NTA are flown as <strong>Continuous Descent Final Approach (CDFA)</strong> "
            "— a steady descent to minima, not dive-and-drive. OM-B §2.16 states non-CDFA is "
            "<strong>not applicable</strong>. That is why LNAV and overlay approaches use "
            "VS / profile gates and PM calls like <strong>ON PROFILE</strong>.</p>",
        )

    with tab_terms:
        _card(
            "RNAV (Area Navigation)",
            "<p>Ability to fly a desired path using GPS/FMS waypoints, not only raw navaid radials. "
            "On charts you see <em>RNAV transitions</em>, <em>RNAV SIDs</em>, or specs like <strong>RNAV1</strong> "
            "(lateral accuracy requirement for a segment).</p>"
            "<p><strong>Think:</strong> RNAV describes <em>navigation capability</em>, not one approach type.</p>",
        )
        _card(
            "RNP (Required Navigation Performance)",
            "<p>RNAV <strong>plus</strong> stricter performance and monitoring. "
            "Chart title <strong>“RNP Z RWY 18”</strong> is the <em>procedure name</em> — you still choose "
            "which <strong>minima row</strong> to fly (LPV, LNAV/VNAV, LNAV).</p>"
            "<p><strong>RNP AR</strong> = Authorization Required (tighter paths). NetJets may prohibit specific "
            "AR procedures — check OM-C airport briefing.</p>",
        )
        _card(
            "APV — Approach with Vertical Guidance",
            "<p>Not as precise as ILS, but you get a <strong>glidepath-like</strong> vertical path to a "
            "<strong>DA</strong> (Decision Altitude). Phenom OM-B: <strong>LPV</strong> and <strong>LNAV/VNAV</strong>.</p>",
        )
        _card(
            "NPA — Non-Precision Approach",
            "<p>No continuous vertical guidance from an ILS beam — includes <strong>LNAV</strong> (GPS lateral only) "
            "and <strong>overlays</strong> (FMS path over VOR/NDB/LOC). Flown as <strong>CDFA</strong> with "
            "MDA/DA per chart. Vertical: VS or LNAV+V assistance.</p>",
        )
        _card(
            "LPV vs LNAV/VNAV vs LNAV",
            "<ul>"
            "<li><strong>LPV</strong> — SBAS (WAAS/EGNOS) gives localiser-performance lateral + vertical; DA minima; HSI: <strong>FMS LPV</strong>.</li>"
            "<li><strong>LNAV/VNAV</strong> — Vertical from SBAS or <strong>Baro VNAV</strong> (baro-corrected); DA minima; HSI: <strong>FMS L/VNAV</strong>.</li>"
            "<li><strong>LNAV</strong> — Lateral GPS only; CDFA with VS (or LNAV+V aid); LNAV minima; HSI: <strong>FMS LNAV</strong> or <strong>LNAV+V</strong>.</li>"
            "</ul>",
        )

    with tab_types:
        with st.expander("**LPV (OM-B 2.14.1) — highest GNSS approach**", expanded=True):
            _md(
                """
**What it is:** GPS + SBAS gives ILS-like lateral and vertical guidance to a **DA**.

**When you use it:** Chart has an **LPV** minima line and aircraft/airport support it.

**Setup (concept):** Load approach from FMS → **APPR** → expect **FMS PINK, GP WHITE** then **GP PINK** at intercept.

**PM check before FAF:** HSI shows **FMS LPV** · no **SUSP** · MAA set.

**Key idea:** You are flying **APV** — treat it like a precision approach mentally, but brief SBAS loss.
"""
            )
        with st.expander("**LNAV / VNAV (OM-B 2.14.2) — APV without LPV**", expanded=False):
            _md(
                """
**What it is:** Still **APV** with a **DA**, but vertical path may come from **SBAS** or **Baro VNAV** (pressure altitude).

**When you use it:** Chart minima row says **LNAV/VNAV** (often when LPV not published or not desired).

**PM check before FAF:** HSI **FMS L/VNAV** · compare FMS vertical profile to plate · **do not edit** approach waypoints in the FMS database.

**VDI shape tells you the source:**
- **Magenta diamond** → SBAS glidepath
- **Magenta pentagon** → Baro VNAV

**Baro VNAV limits:** Altimeter difference ≤ **100 ft** between pilots; respect chart **minimum temperature**.
"""
            )
        with st.expander("**LNAV — NPA with CDFA (OM-B 2.15.1)**", expanded=False):
            _md(
                """
**What it is:** GPS lateral path only; you fly a **steady descent** (CDFA) to minima.

**LNAV+V:** Garmin can show **LNAV+V** — internal vertical *advisory* to help stay on profile. If **LNAV+V** is annunciated before FAF, you may couple vertical guidance. If only **LNAV**, use **VS** for the profile.

**If vertical error on LNAV+V:** OM-B — switch to **VS**, correct, stay in VS for remainder.

**PM role:** Distance vs altitude gates — **ON PROFILE** / **HIGH** / **LOW** / **NEXT x NM, xxxx FEET**.
"""
            )
        with st.expander("**FMS Overlay — VOR/NDB (OM-B 2.15.2)**", expanded=False):
            _md(
                """
**What it is:** FMS flies the lateral path; **primary aid (VOR/NDB) must remain in view** on PM PFD or RMI.

**Modes:** **FMS PINK** + **VS GREEN** for CDFA — same vertical callouts as LNAV.

**When:** Approach not in FMS list, or OM-B note requires green needles / overlay technique.
"""
            )
        with st.expander("**Non-FMS Overlay — LOC / VOR / NDB (OM-B 2.15.3)**", expanded=False):
            _md(
                """
**What it is:** Lateral guidance from the **navaid**, not FMS track — LOC approaches are **always** non-FMS overlay.

**Modes:** **LOC WHITE/GREEN** or **VAPP WHITE/GREEN** · vertical still CDFA with VS.

**Same CDFA profile** as FMS overlay — only the **lateral mode callouts** change.
"""
            )

    with tab_garmin:
        _card(
            "G3000 in one picture",
            "<p>The <strong>Prodigy Touch / G3000</strong> loads procedures from the nav database. "
            "You select <strong>APPR</strong> for GPS approaches; the HSI shows what the box is doing.</p>",
        )
        _md(
            """
| What you see | Meaning |
|--------------|---------|
| **FMS PINK** | Lateral guidance from FMS (approach or overlay) |
| **GP WHITE** → **GP PINK** | Glidepath armed → captured |
| **FMS LPV** | Flying LPV service level (SBAS APV) |
| **FMS L/VNAV** | Flying LNAV/VNAV (SBAS or Baro VNAV) |
| **FMS LNAV** | Lateral GPS only — NPA |
| **FMS LNAV+V** | LNAV with advisory vertical (+V) |
| **SUSP** | Sequencing suspended — fix before FAF |
| VDI **diamond** | SBAS vertical |
| VDI **pentagon** | Baro VNAV vertical |
"""
        )
        _card(
            "APPR button — what it really does",
            "<ul>"
            "<li>Arms the FMS approach you loaded from the procedure list.</li>"
            "<li>Couples FD laterally (and vertically when GP is valid).</li>"
            "<li>Does <strong>not</strong> replace briefing the correct <strong>minima line</strong> on the chart.</li>"
            "</ul>",
        )
        _card(
            "OM-B automation notes (2.12.11)",
            "<ul>"
            "<li>Approach <strong>not</strong> in FMS list → PF nav source <strong>green needles</strong>.</li>"
            "<li>Approach <strong>in</strong> FMS list → may fly overlay; PF source <strong>FMS</strong>; show primary aid on bearing pointer if required.</li>"
            "<li>RNAV approaches: display must show position vs lateral and vertical path.</li>"
            "<li>Circling after ILS → set up as <strong>LOC</strong>; AAD to circling altitude.</li>"
            "</ul>",
        )
        _card(
            "Hard rules from OM-B",
            "<p>It is <strong>prohibited</strong> to insert or change lateral or vertical elements of "
            "database approach waypoints. If the FMS profile does not match the plate — stop and resolve "
            "before continuing.</p>",
        )
        _card(
            "GPS total failure (Handbook Ch 5.2)",
            "<p><strong>GPS is the only FMS position input.</strong> VOR/DME cannot feed the FMS — use "
            "<strong>green needles</strong> for conventional nav.</p>"
            "<ul>"
            "<li>Cues: <strong>GPS LOI</strong>, <strong>GPS NAV LOST</strong>, <strong>NO FMS POSITION</strong>, DR/LOI on map.</li>"
            "<li>Jamming/external loss: FMS magenta may stay in DR (ENR/OCN only); otherwise <strong>HDG</strong> + raw data.</li>"
            "<li><strong>CDI softkey</strong> → tune VOR/DME; select conventional approach (ILS/VOR).</li>"
            "<li><strong>AHRS FAULT</strong> (not FAIL) from GPS loss — reduce speed per QRH (<strong>MAX 240 KIAS / 0.63 M</strong>) to avoid miscompare.</li>"
            "<li>When GPS returns: CDI to magenta GPS; HDG may help re-engagement.</li>"
            "<li><strong>AHRS FAIL / AP FAIL / YD FAIL</strong> — QRH; ventral rudder available Load 1X+.</li>"
            "</ul>",
        )
        _card(
            "Synthetic Vision (Handbook Ch 5.6)",
            "<p><strong>SVS</strong> — PFD softkeys → PFD Settings → Attitude Overlays → Synthetic Terrain. "
            "Enhances SA; does not replace attitude/flight instruments. "
            "<strong>At least one pilot with SVS on in mountainous terrain.</strong></p>",
        )

    with tab_downgrade:
        _card(
            "Why downgrades matter",
            "<p>SBAS (EGNOS/WAAS) can become unavailable. The Garmin <strong>steps down</strong> the approach "
            "service level. You must know what was briefed and whether lower minima still work.</p>",
        )
        with st.expander("**LPV — APR DWNGRADE (OM-B 2.14.1)**", expanded=True):
            _md(
                """
**Before 1 min to FAF:** LPV may show **amber**; VDI still visible. At 1 min to FAF system downgrades to:
- **LNAV/VNAV** (Baro VNAV) — L/VNAV magenta/amber, **APR DWNGRADE** message, VDI **NO GP** until acknowledged on **GTC**
- or **LNAV** — LNAV magenta/amber, **APR DWNGRADE**, **NO GP**

**After 1 min to FAF:** downgrade to **LNAV** when past FAF — may be **no message**.

**Pilot actions:**
- **Acknowledge** GTC message to allow automatic downgrade
- **Before FAF:** missed approach, or continue to **LNAV/VNAV** or **LNAV** minima if briefed and available
- **After FAF:** missed approach unless visual references, or above 1000 ft continue to **LNAV** minima if briefed
- **GPS integrity lost** before visuals → discontinue
"""
            )
        with st.expander("**LNAV/VNAV — APR ADVISORY (Phenom 300, OM-B 2.14.2)**", expanded=False):
            _md(
                """
**Before 1 min to FAF:** L/VNAV amber → switches to **Baro VNAV** (L/VNAV magenta), **APR ADVISORY**, **NO GP** until acknowledged.

**After 1 min to FAF:** may downgrade to **LNAV** silently. If no LNAV minima → approach aborts past FAF.

**Before FAF:** may continue on **Baro VNAV** (same minima) or revert to **LNAV** NPA.

**After FAF:** missed approach unless visuals, or above 1000 ft continue to **LNAV** if briefed.
"""
            )
        _card(
            "Common mistakes",
            "<ul>"
            "<li>Briefing **LPV** but not briefing the **LNAV** backup if SBAS fails.</li>"
            "<li>Ignoring **SUSP** on the HSI.</li>"
            "<li>Editing FMS waypoints to ‘fix’ the path.</li>"
            "<li>Confusing chart title <strong>RNP Z</strong> with actually flying **LPV** minima.</li>"
            "<li>Not comparing **FMS vertical profile** to the plate on LNAV/VNAV.</li>"
            "</ul>",
        )

    with tab_map:
        _md(
            """
| Jeppesen minima row | OM-B section | Approach class | HSI (typical) | Vertical guidance |
|---------------------|--------------|----------------|---------------|-------------------|
| **LPV** | 2.14.1 | APV | FMS LPV | SBAS GP (diamond) |
| **LNAV/VNAV** | 2.14.2 | APV | FMS L/VNAV | SBAS or Baro VNAV (diamond/pentagon) |
| **LNAV** (+V) | 2.15.1 | NPA CDFA | FMS LNAV or LNAV+V | VS or +V advisory |
| **VOR/NDB + FMS** | 2.15.2 | NPA CDFA overlay | FMS PINK | VS |
| **LOC / VOR** | 2.15.3 | NPA non-FMS overlay | LOC/VAPP GREEN | VS |
| **ILS** | 2.13.x | Precision | LOC/GS GREEN | ILS beam |
"""
        )
        st.markdown(
            """
**Where to go next in Briefly**
- **SOP → Approaches** — exact PF/PM callouts per type
- **Flight Profiles** — stabilised point, config gates, profile diagrams
- **Special Airports** — airport-specific RNP/RNAV restrictions (e.g. RNP AR prohibited)
"""
        )

    with tab_db:
        _card(
            "Aircraft laptop",
            "<p>On-board laptop for <strong>Garmin database updates</strong>, CMC download, and Go-Go troubleshooting. "
            "Bag contains USB–SD adapter and spare SD cards. Account details on <strong>A4 sheet in laptop bag</strong> "
            "(Handbook Ch 8.1). Treat laptop carefully — no remote IT support off-base.</p>",
        )
        _card(
            "Golden rules — SD cards",
            "<ul>"
            "<li><strong>Navigation database</strong> — load via <strong>TOP MFD SD slot only</strong> (never lower slot — risk spurious fuel CAS, FOL 01/14).</li>"
            "<li><strong>Lower MFD slot</strong> — Garmin SD with all other databases; stays in aircraft except during update.</li>"
            "<li><strong>Standby Nav folder</strong> — next nav DB can be pre-loaded up to 7 days before expiry; activates on expiry at power-up.</li>"
            "<li><strong>Terrain + Jepp eCharts</strong> — must update <strong>all 3 lower cards</strong> (MFD + both PFDs) — no auto-sync.</li>"
            "</ul>",
        )
        _card(
            "Jeppesen Distribution Manager (JDM)",
            "<p>All G3000 databases via <strong>JDM</strong> on the aircraft laptop (not FlyGarmin). "
            "Download to laptop hard drive 3–7 days before expiry, then write SD cards on the jet without internet. "
            "Use <strong>PowerUser</strong> account when Windows prompts for JDM updates. "
            "Update the laptop when you can — helps the next crew.</p>",
        )
        _md(
            """
| Database | Validity | Lead time | SD card |
|----------|----------|-----------|---------|
| **Navigation** | 28 days | 7 days early load OK | **Top MFD only** |
| Obstacle / Safe Taxi / Airport dir / Base map | 56 days | 7 days | Lower MFD → auto-sync |
| Terrain / eCharts | as required | 7 days | **All 3 lower slots** |

**After lower MFD update** — one power-up usually syncs to PFDs and GTCs (except terrain/charts).

**Too early activation** — Handbook Ch 8.4: troubleshooting if nav DB activated before old expires.

_Full screenshots and step-by-step: **Documents → Handbook Phenom 300**, Chapter 8._
"""
        )
        _card(
            "Fleet Operational Letters (FOLs) — Handbook Ch 7.4",
            "<ul>"
            "<li><strong>FOL 001/14, 012/14</strong> — fuel pump fail CAS at power-up if nav DB loaded in <strong>lower</strong> MFD slot.</li>"
            "<li><strong>FOL 001/13, 013/11</strong> — battery best practices / GPU ops → see <strong>Electrics</strong>.</li>"
            "<li><strong>FOL 015/11</strong> — FCE CAS at power-up (flap, spoiler, pitch trim) → <strong>Flight Controls</strong>.</li>"
            "<li><strong>FOL 006/13</strong> — engine no start / starter-generator.</li>"
            "<li><strong>FOL 011/13</strong> — ECS cold weather AUX HEAT → <strong>Cold Weather</strong>.</li>"
            "<li><strong>FOL 002/14</strong> — dual BLEED FAIL below 13,000 ft with anti-ice.</li>"
            "<li><strong>FOL 010/13, 005/16</strong> — BRK FAIL reset → <strong>Landing Gear</strong>.</li>"
            "</ul>"
            "<p>FOLs are manufacturer advice — not a substitute for OM/QRH. Fault clearance per approved manuals.</p>",
        )

    with tab_fleet:
        _card(
            "NETJETS DEFAULT profile (Handbook Ch 7.1)",
            "<p>Fleet <strong>LOAD 1X</strong> profile saved as <strong>NETJETS DEFAULT</strong> in "
            "<strong>Utilities → Crew Profile</strong>. Standardises map/avionics at power-up — "
            "<strong>do not alter or delete</strong> it. Split PFD screens on power-up = profile active.</p>"
            "<ul>"
            "<li><strong>PFD</strong> — Split (chart + PFD); Bearing 1/2 OFF until set; Wind option 3; HPA alt.</li>"
            "<li><strong>MFD map</strong> — Track up; detail Most; traffic ON; terrain absolute; WX source Connext.</li>"
            "<li><strong>Avionics</strong> — UTC; dual-cue FD; GPS CDI AUTO; 8.33 kHz; nearest rwy hard ≥3000 ft.</li>"
            "<li><strong>Trip stats</strong> — flight time &amp; departure time <em>In-Air</em>; resets manual.</li>"
            "</ul>"
            "<p>Full map ranges and alert settings → <strong>Documents → Handbook</strong> Ch 7.1.</p>",
        )
        with st.expander("**Restore default profile after maintenance (Ch 7.1.1)**", expanded=False):
            _md(
                """
1. Insert **nav SD card** in **top MFD** slot; power on.
2. **Utilities → Crew Profile** → **EXPORT** (button active with SD in top slot).
3. **Aircraft Systems → Maintenance** → code **EMBRG3K** → **Set Default Profile** → **NETJETS DEFAULT** → OK caution.
4. **END Maintenance** — split screens should return on next power-up.

If profile missing after maintenance, re-enter settings per handbook then export + set default.
"""
            )
        _card(
            "CMC download (Handbook Ch 7.2)",
            "<ol>"
            "<li>Blank/spare SD in <strong>top MFD</strong> slot.</li>"
            "<li><strong>Aircraft Systems → Maintenance</strong> → <strong>EMBRG3K</strong>.</li>"
            "<li><strong>CMC Logs → CAS CMC</strong> (or Engine folder for engine faults).</li>"
            "<li>Select flight → <strong>Save CMC Log File to Card</strong> (not ‘Save All’).</li>"
            "<li>Power down before removing SD; email files to <strong>lis-mxembraer@netjets.com</strong>.</li>"
            "</ol>"
            "<p>Early crew download can save hours AOG — Embraer analyses before parts order.</p>",
        )
        _card(
            "Connext Weather (Handbook Ch 7.3)",
            "<ul>"
            "<li><strong>Auto Request OFF</strong> — otherwise fleet polls every 15 min (cost/data).</li>"
            "<li><strong>CONNEXT</strong> page → define coverage (e.g. flight plan ±100 nm) → <strong>Send Immediate Request</strong>.</li>"
            "<li>Smaller coverage = faster download. METAR/TAF on airport flags and waypoint pages.</li>"
            "<li>Codes can drop after maintenance — handbook Ch 7.3 has tail-specific access codes; test sat phone if still down.</li>"
            "</ul>",
        )
        _card(
            "Comply365 memos (Handbook Ch 7.5)",
            "<p>Key fleet comms (full list on Comply365): GPS loss (2016-07-04), BRK FAIL alert, Wi-Fi rollout, "
            "oxygen mask change PHI+, GURU performance guide, Guru pilots guide.</p>",
        )

    back_to_top()
    source_footer("om_b", "§2.12–2.15 Approaches · Handbook Ch 7–8 (G3000 fleet setup & databases)")
