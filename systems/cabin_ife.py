"""Cabin & IFE — Wi-Fi, Go-Go, lavatory, Nespresso, PED (Handbook Ch 2.3, 3.1, 4.4)."""

import streamlit as st

from content.render_helpers import back_to_top, cas_quick_reference, source_footer


def render_cabin_ife():
    st.markdown("## Cabin & IFE")
    st.caption("Cabin systems · Wi-Fi / Go-Go · Lavatory · Galley · PED · Handbook Ch 2.3, 3.1, 4.4")

    with st.expander("**0. How it works**", expanded=True):
        st.markdown(
            """
Cabin & IFE covers everything behind the cockpit door: internet, entertainment, lavatory, galley, and passenger power. Internet comes via **SwiftBroadBand (SBB)** to a cabin router; entertainment streams from a roller-cabinet server. Most of it is crew-controlled through a few switches and follows Handbook/OM-A policy.

| System | What it does | Crew touchpoint |
|--------|--------------|-----------------|
| **SBB Wi-Fi** | Internet via Cobham Aviator 200 → UCS-5000 → cabin Wi-Fi | **IFE** switch |
| **Go-Go** | Streaming entertainment (roller cabinet) | iPad / NetJets IFE app |
| **Lavatory** | Vacuum toilet + external service panel | Pre-flight check + post-flight service |
| **Nespresso** | Galley coffee | Aircraft socket only; Volvic water |
| **PED / outlets** | Passenger AC outlets | **PED-BELTS** switch per OM-A |

**Authority:** Handbook + OM-A for PED policy.
"""
        )

    with st.expander("**1. Wi-Fi (SwiftBroadBand)**", expanded=False):
        st.markdown(
            """
**Architecture:** SBB (Cobham Aviator 200) → UCS-5000 multimedia server → router → **Your Aircraft's Wi-Fi** (no password).

**IFE switch** — ON/OFF for the system. **Recycle IFE first** if passengers cannot connect.

### Ground vs air

- On the ground, data often comes via **3G modem** (can feel faster than in flight).
- **Test/troubleshoot airborne** when possible — ground 3G can mask a broken SBB link.

**Crew devices (revenue flights)** — flight-safe mode; Wi-Fi **off** on personal devices. Use **GTC / Iridium** for office contact.

**Ferry flights** — light data only (e.g. WhatsApp).

**Passenger briefing** — briefing card on board; ~16 Mb/s max — mail/text OK, not heavy streaming (Go-Go box handles streaming separately).

**Hardware location** — equipment under roller cabinet; CBs on panel **behind left pilot seat** (crew normally only reset CBs, not open panels).

**Failures** — report to **nje-wireless@netjets.com**.
"""
        )

    with st.expander("**2. Go-Go / NetJets IFE — troubleshooting**", expanded=False):
        st.markdown(
            """
### 1. Wi-Fi error on NetJets Entertainment app

- Read message (ramp Wi-Fi vs aircraft).
- Connect to **Your Aircraft's Wi-Fi** or recycle **IFE** switch.
- Cabin power **≥ 10 minutes** after power-on before reconnecting.

### 2. DRM errors

- Power aircraft; wait 5–10 min for UCS boot.
- iPad: close all apps → Wi-Fi to aircraft → browser **splash.gogo.aero** → confirm load → close apps → open IFE app.
- If still failing: off-aircraft Wi-Fi + **nje-wireless@netjets.com** to unlock/reinstall app.

### 3. No media / blank storefront

- Often after content update with poor 3G.
- UCS internet: ground = 3G; in flight = SBB only (3G disabled).
- iPad: close apps → internet → retry app → hard reset if needed.

### 4. Grey screen (“grey screen of death”)

- Go-Go box corruption — usually needs **maintenance remote reboot**; aircraft may go to MX.

_Full maintenance memo: NTA 12/2017 Rev 1 (Handbook ref.)._
"""
        )

    with st.expander("**3. Nespresso coffee machine**", expanded=False):
        st.markdown(
            """
### Before use

- Instruction book next to machine.
- **Door fully open** — secondary power switch in door cuts power when closed.
- Use **Volvic** water (large bottles on board) — Evian causes limescale damage.
- **ONLY** plug into **aircraft socket** — never FBO/hotel (pop + burning smell).

### No power

- Check door open; try another aircraft socket with **iPhone charger** to test socket.
- CBs above baggage bay can trip — **maintenance** (crew cannot access).

**Quick flash then off** — internal tank empty; exercise valve at base of water container, reseat firmly.

### Cold weather

- If aircraft stays cold: run **EMPTY FLUID SYSTEM** (manual p.7) or remove machine to FBO.
- Frozen pipes have destroyed machines after multi-day cold soak.

**Descaling** — minimum yearly (often November reminder); kits in nose/stock. Descale early if flow weak.

**Ferry/hot spare** — clean and dry container before stowing.
"""
        )

    with st.expander("**4. Lavatory — pre-flight & operation**", expanded=False):
        st.markdown(
            """
### Pre-flight

- Check flush works (button not **red** = not ~90% full).
- If no flush and button not red → may need **~1 L more water** in bowl (handbook uses conservative **4 L** after service).

### Capacity

- Tank ~12 L; **red flush button** ~90% (~10 L). Overflow capability ~16 L — stay well below.

**Cold weather link** — if lavatory drained overnight, **refill before departure** (see **Cold Weather**).
"""
        )

    with st.expander("**5. Lavatory — servicing (post-flight)**", expanded=False):
        st.markdown(
            """
### Service panel (exterior)

1. Open inlet rinse + drain valve doors — no leak from internal door before connecting hoses.
2. **Do not open internal flapper** until waste hose connected.
3. Attach waste + rinse hoses per handbook diagram.
4. Pull **T handle** out, turn to lock, open RTS waste drain inside lavatory.
5. Drain until flow stops — **confirm tank actually emptied** before adding water.
6. Rinse ~3 min via inlet valve; close T handle; add **4 L water** for flush mechanism.
7. Remove hoses; secure **inner** door, then outer door.

**T handle** — do not over-rotate same direction (damage). Can loosen and fall behind hinge — check if missing.

**Inlet cap** — must lock (ball bearings). Loose cap → vibration/noise after takeoff, fluid syphoned down fuselage.

**After service** — tug test on rinse cap even if left in place.
"""
        )

    with st.expander("**6. Lavatory — troubleshooting**", expanded=False):
        st.markdown(
            """
| Issue | What to do |
|-------|------------|
| **Flood** | Servicing team may not have emptied tank before refill — monitor service; max **4 L** after empty |
| **Too much water** | Red button = stop using; service when possible |
| **Frozen / dirty outflow** | Leak or cannot empty — warm soak on ground; empty → rinse → empty → fill cycle |
| **Not enough water** | Add ~1 L if button not red; torch-check bowl |

**Overflow discipline** — numerous floods from overfill + incomplete emptying. **Watch the service.**
"""
        )

    with st.expander("**7. PED & power banks**", expanded=False):
        st.markdown(
            """
**Before engine start** — any PED is allowed.

**After engine start, and below 10,000 ft** (EMB-505, OM-A 8 Jun 2026):

- Devices that do not transmit: unrestricted
- Transmitting devices: **Wi-Fi and Bluetooth only**
- Large devices: stowed until taxi-in after landing
- Aircraft outlets: not during taxi, takeoff, below 10,000 ft, or the landing roll

**Above 10,000 ft** — Wi-Fi and Bluetooth are allowed. On an **LVO approach**, all PEDs off.

**Power banks**

- Carry-on only. **Two per person.** Never in checked baggage.
- Do not recharge a power bank on board.
- Charging a device from a power bank only if someone is watching, the pack is fully visible, and not during taxi, takeoff, below 10,000 ft, landing, or an emergency.
- Say this in the passenger brief before taxi.

**PED-BELTS** still follows the cabin briefing. Aircraft outlets at or below 10,000 ft: Embraer ETD asks for **aircraft mode** and **Wi-Fi only**.
"""
        )

    with st.expander("**8. Cabin checks (preflight PM)**", expanded=False):
        st.markdown(
            """
### Interior (Handbook 2.3.1 + SOP cabin prep)

- Emergency equipment, life jackets, FAK/AED, briefing cards
- Galley / **toilet** clean and stocked
- iPads charged; magazines / seat pockets
- **Wi-Fi / IFE** — IFE switch, briefing card available
- **Nespresso** — water (Volvic), machine secured for flight

See **SOP → Preflight** for crew flow.
"""
        )

    cas_quick_reference(
        [
            ("IFE", "—", "Wi-Fi / Go-Go dead", "Recycle IFE; 10 min boot; check CBs; nje-wireless@netjets.com"),
            ("Lavatory", "—", "Flush button RED", "~90% full — do not use; service required"),
            ("Lavatory", "—", "No flush (button OK)", "Low water — add ~1 L or service"),
            ("Lavatory", "—", "Vibration after TO", "Check external service caps locked"),
            ("Galley", "—", "Coffee no power", "Door open; test socket; maintenance if CB"),
            ("PED", "—", "Outlets / power banks", "No charging on taxi, takeoff, below 10,000 ft, or landing. Power banks: cabin only, max 2, do not recharge the pack."),
        ],
        title="9. Quick reference",
    )

    back_to_top()
    source_footer("om_a", "8.3.15.10 PED · 9.2 Power banks · Handbook Ch 2.3 / 4.4")
