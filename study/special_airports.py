import streamlit as st

from content.airports import AIRPORT_DETAILS, CATEGORY_C_AIRPORTS
from content.render_helpers import render_search_focus_banner
from study.airport_briefing_render import render_pilot_briefing


def _render_airport_detail(icao: str):
    airport = next(a for a in CATEGORY_C_AIRPORTS if a["icao"] == icao)
    detail = AIRPORT_DETAILS.get(icao, {})

    if st.button("← Special Airports", use_container_width=False, type="secondary", key=f"airport_back_{icao}"):
        st.session_state.airport_selected = None
        st.rerun()

    render_pilot_briefing(
        icao=icao,
        name=airport["name"],
        detail=detail,
        pdf_section=detail.get("pdf_section", f"Chapter 14 · {icao}"),
    )


def render_special_airports():
    if "airport_selected" not in st.session_state:
        st.session_state.airport_selected = None

    render_search_focus_banner()

    if st.session_state.airport_selected:
        _render_airport_detail(st.session_state.airport_selected)
        return

    col1, col2 = st.columns(2, gap="medium")
    for i, airport in enumerate(CATEGORY_C_AIRPORTS):
        with [col1, col2][i % 2]:
            if st.button(
                f"{airport['name']} · {airport['icao']}",
                use_container_width=True,
                type="primary",
                key=f"airport_{airport['icao']}",
            ):
                st.session_state.airport_selected = airport["icao"]
                st.rerun()
