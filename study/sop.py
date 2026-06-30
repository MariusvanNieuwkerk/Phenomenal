import streamlit as st

from content.render_helpers import source_banner
from study.sop_approaches import render_approaches, render_go_arounds
from study.sop_flows import (
    render_arrival_descent,
    render_general,
    render_landing_shutdown,
    render_predeparture,
    render_preflight,
    render_start_taxi_lineup,
    render_takeoff_climb_cruise,
)
from study.sop_styles import inject_sop_styles, render_sop_legend
from ui.theme import render_section_label


def render_sop():
    inject_sop_styles()
    source_banner("om_b", "Chapter 2 — Normal Procedures (preflight → landing)")
    render_sop_legend()

    render_general()
    render_preflight()
    render_predeparture()
    render_start_taxi_lineup()
    render_takeoff_climb_cruise()
    render_arrival_descent()
    render_approaches()
    render_go_arounds()
    render_landing_shutdown()

    render_section_label("Quick links")
    st.markdown("""
- **Flight Profiles** — profile diagrams (takeoff, approaches, RTO, EFATO, OEI)
- **Planning** — minima, alternates, go/no-go weather
- **Cold Weather** — de-icing, HOT, contaminated surfaces
- **Special Airports** — Cat C briefings (OM-C)
- **Memory** — emergency memory items (QRH)
- **Documents** — full OM-B PDF
""")
