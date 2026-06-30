import streamlit as st

from content.render_helpers import source_banner, source_footer
from ui.theme import render_page_header, render_section_label


HANDBOOK_SECTIONS = [
    {
        "title": "Introduction",
        "source": "Chapter 1",
        "items": [
            ("General", "Handbook purpose: practical Phenom 300 operational guidance for NetJets crews."),
            ("Crew input", "Report discrepancies and improvement suggestions through company channels."),
            ("Best practice", "Use handbook together with OM-A/B/C and POH — not as a standalone authority."),
        ],
    },
    {
        "title": "Pre-flight — External",
        "source": "Chapter 2.1",
        "items": [
            ("External walkround", "Structured walkaround guide — use as systematic exterior inspection reference."),
            ("External lights", "Verify navigation, landing, taxi, and inspection lights per handbook sequence."),
            ("Emergency lighting", "Check emergency exit and escape path lighting operation."),
            ("Pre-check checks", "Detailed item-by-item exterior checks before flight."),
            ("Main door", "Door operation, seals, and safety considerations."),
        ],
    },
    {
        "title": "Pre-flight — Additional checks",
        "source": "Chapter 2.2",
        "items": [
            ("Generators", "Visual and operational checks before engine start."),
            ("Batteries", "Condition, connections, and voltage awareness."),
            ("Wheels and tyres", "Wear, pressure, and brake area inspection."),
            ("Brakes and surrounds", "Rivets, leaks, and surrounding structure."),
            ("Nose baggage bay", "Loading limits and door security."),
            ("Nose steering / tow", "Steering lock and tow arm condition."),
            ("Refuelling panel", "Panel security and contamination checks."),
        ],
    },
    {
        "title": "Pre-flight — Internal & ops",
        "source": "Chapter 2.3",
        "items": [
            ("Cabin checks", "Interior safety, equipment, and passenger area readiness."),
            ("Wi-Fi", "System status and passenger connectivity setup."),
            ("Nespresso machine", "Water supply, operation, and securing for flight."),
            ("Passenger baggage", "Loading, weight, and securing guidance."),
            ("Airport slots & A-CDM", "Slot compliance and collaborative decision-making awareness."),
        ],
    },
    {
        "title": "In-flight",
        "source": "Chapter 3",
        "items": [
            ("Sockets & PED-BELTS", "Passenger device and seat belt switch usage."),
            ("Over-weight landings", "When applicable, inspection and reporting requirements."),
            ("Windshear detection", "System behaviour and crew response cues."),
        ],
    },
    {
        "title": "Post-flight",
        "source": "Chapter 4",
        "items": [
            ("Passenger belongings", "Cabin sweep before securing aircraft."),
            ("External inspection", "Post-flight walkaround for damage or fluid leaks."),
            ("Engine oil", "Oil level checks and servicing awareness."),
            ("Toilet servicing", "Lavatory system handling on turnaround."),
        ],
    },
]


def render_handbook():
    source_banner("handbook")

    render_section_label("Chapters")
    for section in HANDBOOK_SECTIONS:
        with st.expander(f"**{section['title']}**", expanded=False):
            for name, desc in section["items"]:
                st.markdown(f"**{name}** — {desc}")
            source_footer("handbook", section["source"])

    st.divider()
    st.caption(
        "Detailed step-by-step content (photos, checklists, cabin equipment) is in the full Handbook PDF under **Documents**."
    )
