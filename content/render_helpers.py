import pandas as pd
import streamlit as st

from content.sources import SOURCES
from data.memory_items import MEMORY_CONTENT, SYSTEM_MEMORY
from study.semantic_color import mi_md

CAS_COLUMNS = ["Topic", "Level", "CAS", "Pilot focus"]

_CAS_INTRO = (
    "Grouped by topic. **Always complete the QRH** when a message requires action."
)


def systems_page_top():
    st.markdown('<div id="briefly-systems-top"></div>', unsafe_allow_html=True)


def back_to_top():
    st.markdown(
        '<div style="text-align:center;margin:1.25rem 0 0.5rem;">'
        '<a href="#briefly-systems-top" style="text-decoration:none;font-weight:600;">'
        "↑ Terug naar boven</a></div>",
        unsafe_allow_html=True,
    )


def cas_quick_reference(
    rows: list[tuple[str, str, str, str]],
    *,
    title: str = "CAS quick reference",
    expanded: bool = False,
    intro: str | None = None,
):
    with st.expander(f"**{title}**", expanded=expanded):
        st.markdown(intro or _CAS_INTRO)
        st.dataframe(
            pd.DataFrame(rows, columns=CAS_COLUMNS),
            hide_index=True,
            use_container_width=True,
        )


def source_footer(key: str, section: str | None = None):
    label = SOURCES.get(key, key)
    ref = f"{label}" + (f" · {section}" if section else "")
    st.caption(f"Source: {ref}")


def source_banner(key: str, section: str | None = None):
    label = SOURCES.get(key, key)
    ref = f"{label}" + (f" · {section}" if section else "")
    st.info(f"Reference material from **{ref}**. For full detail, use **Documents** to open the PDF.")


def render_search_focus_banner():
    focus = st.session_state.get("search_focus")
    if not focus:
        return
    c1, c2 = st.columns([5, 1])
    with c1:
        st.success(f"Zoekresultaat — kijk bij: **{focus}**")
    with c2:
        if st.button("✕", key="clear_search_focus", help="Sluiten"):
            st.session_state.search_focus = None
            st.rerun()


def render_system_memory_items(system: str):
    """QRH memory items for this system — red expanders above study content."""
    titles = SYSTEM_MEMORY.get(system, [])
    if not titles:
        return
    st.markdown(
        f'<p class="briefly-system-memory-label">QRH memory items</p>',
        unsafe_allow_html=True,
    )
    for title in titles:
        with st.expander(f"**{title}**", expanded=False):
            mi_md(MEMORY_CONTENT[title])
    st.markdown(
        f'<p class="briefly-system-study-label">System study</p>',
        unsafe_allow_html=True,
    )
