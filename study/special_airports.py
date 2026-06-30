import streamlit as st

from content.airports import AIRPORT_DETAILS, BRIEFING_STRUCTURE, CATEGORY_C_AIRPORTS
from content.render_helpers import render_search_focus_banner, source_banner, source_footer
from ui.theme import render_page_header, render_section_label


def _render_airport_detail(icao: str):
    airport = next(a for a in CATEGORY_C_AIRPORTS if a["icao"] == icao)
    detail = AIRPORT_DETAILS.get(icao, {})

    render_page_header(f"{icao} — {airport['name']}", detail.get("headline", "Category C aerodrome briefing"))
    source_banner("om_c", detail.get("pdf_section", f"Chapter 14 · {icao}"))

    if st.button("← Luchthavenlijst", use_container_width=True, type="secondary", key=f"airport_back_{icao}"):
        st.session_state.airport_selected = None
        st.rerun()

    tags = ", ".join(airport.get("tags", []))
    if tags:
        st.caption(tags)

    if detail.get("qualification"):
        with st.container(border=True):
            render_section_label("Qualification")
            for item in detail["qualification"]:
                st.markdown(f"- {item}")

    if detail.get("limitations"):
        with st.container(border=True):
            render_section_label("Limitations")
            for item in detail["limitations"]:
                st.markdown(f"- {item}")

    if detail.get("crew_assignment"):
        with st.container(border=True):
            render_section_label("Crew assignment")
            for item in detail["crew_assignment"]:
                st.markdown(f"- {item}")

    if detail.get("overview"):
        with st.container(border=True):
            render_section_label("Overview")
            st.markdown(detail["overview"])

    for key, label in [
        ("weather", "Weather / limitations"),
        ("departure", "Departure"),
        ("arrival", "Arrival"),
        ("ground", "Ground"),
    ]:
        value = detail.get(key)
        if not value:
            continue
        with st.container(border=True):
            render_section_label(label)
            if isinstance(value, list):
                for item in value:
                    st.markdown(f"- {item}")
            else:
                st.markdown(value)

    if not detail:
        st.info(
            f"Full briefing for **{icao}** is in OM-C Chapter 14. "
            "Open **Documents → OM-C** for the complete aerodrome briefing."
        )

    source_footer("om_c", detail.get("pdf_section", f"Chapter 14 · {icao}"))


def render_special_airports():
    if "airport_selected" not in st.session_state:
        st.session_state.airport_selected = None

    render_search_focus_banner()

    if st.session_state.airport_selected:
        _render_airport_detail(st.session_state.airport_selected)
        return

    source_banner("om_c", "Chapter 14 — Airport Briefings")

    with st.expander("**Briefing structure (OM-C standard)**", expanded=False):
        for i, item in enumerate(BRIEFING_STRUCTURE, 1):
            st.markdown(f"{i}. {item}")
        source_footer("om_c", "14.2 Aerodrome Briefing Standard Structure")

    query = st.text_input("Search airports", placeholder="e.g. EGLC, Innsbruck, steep, alpine…", key="airport_search")
    q = query.lower().strip()

    matches = []
    for airport in CATEGORY_C_AIRPORTS:
        haystack = " ".join([airport["icao"], airport["name"], *airport.get("tags", [])]).lower()
        if not q or q in haystack:
            matches.append(airport)

    render_section_label(f"Category C ({len(matches)} airports)")
    col1, col2 = st.columns(2, gap="medium")
    for i, airport in enumerate(matches):
        with [col1, col2][i % 2]:
            label = f"{airport['icao']} — {airport['name']}"
            if st.button(label, use_container_width=True, type="primary", key=f"airport_{airport['icao']}"):
                st.session_state.airport_selected = airport["icao"]
                st.rerun()

    if not matches:
        st.warning("No airports match your search.")

    st.divider()
    st.caption("Airports without expanded summaries still have full briefings in OM-C Part C (Documents).")
