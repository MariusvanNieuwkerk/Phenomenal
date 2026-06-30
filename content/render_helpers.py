import streamlit as st

from content.sources import SOURCES


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
