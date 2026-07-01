"""Single-page app shell — header, search, nav, and inline content."""

import streamlit as st

from search.bar import render_home_search
from ui.theme import render_header, render_nav_button_row

NAV_ITEMS = [
    ("Limitations", "limitations"),
    ("Memory Items", "memory"),
    ("Systems", "systems"),
    ("Planning", "planning"),
    ("SOP", "sop"),
    ("Profiles", "profiles"),
    ("Cold Weather", "cold_weather"),
    ("Special Airports", "airports"),
    ("Documents", "documents"),
]


def render_main_nav(active: str, navigate_fn):
    row1 = NAV_ITEMS[:5]
    row2 = NAV_ITEMS[5:]
    render_nav_button_row(row1, active, navigate_fn, row_key="nav_r1")
    render_nav_button_row(row2, active, navigate_fn, row_key="nav_r2")


def render_app_shell(navigate_fn, render_content_fn):
    render_header()
    render_home_search(navigate_fn)
    render_main_nav(st.session_state.section, navigate_fn)
    st.markdown("---")
    render_content_fn(st.session_state.section)
