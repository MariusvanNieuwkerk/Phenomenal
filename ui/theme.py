import base64
import os

import streamlit as st
import streamlit.components.v1 as components

from ui.tokens import COLORS, FONT_FAMILY

APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(APP_DIR, "static")


def _svg_data_uri(filename: str) -> str:
    path = os.path.join(STATIC_DIR, filename)
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded}"


def _theme_css() -> str:
    return f"""
html, body, [class*="css"] {{
  font-family: {FONT_FAMILY} !important;
}}

.stApp {{
  background: linear-gradient(165deg, {COLORS["bg_top"]} 0%, {COLORS["bg_bottom"]} 100%);
}}

[data-testid="stAppViewContainer"] > .main {{
  background: transparent;
}}

.block-container {{
  max-width: 1400px;
  padding-top: 0.75rem;
  padding-bottom: 2rem;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}}

footer {{
  visibility: hidden;
}}

div.stButton > button {{
  width: 100%;
  min-height: 68px;
  padding: 0.95rem 1rem;
  border-radius: 14px;
  font-size: 1.05rem;
  font-weight: 650;
  font-family: {FONT_FAMILY} !important;
  border: 1.5px solid {COLORS["border"]};
  background: {COLORS["surface"]};
  color: {COLORS["ink"]};
  box-shadow: 0 2px 8px rgba(26, 77, 122, 0.06);
}}

div.stButton > button[kind="primary"],
div.stButton > button[data-testid="baseButton-primary"] {{
  background: {COLORS["accent"]} !important;
  color: #FFFFFF !important;
  border: 1.5px solid {COLORS["accent_dark"]} !important;
}}

div.stButton > button[kind="secondary"],
div.stButton > button[data-testid="baseButton-secondary"] {{
  background: rgba(255, 255, 255, 0.92) !important;
  color: {COLORS["ink"]} !important;
  border: 1.5px solid {COLORS["border"]} !important;
}}

.briefly-search-label,
[data-testid="stMarkdownContainer"] p.briefly-search-label {{
  margin: 0 0 0.45rem !important;
  padding: 0 !important;
  text-align: center;
  font-family: {FONT_FAMILY} !important;
  font-size: 0.78rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.14em !important;
  color: {COLORS["muted"]} !important;
}}

[data-testid="stTextInput"] > div,
[data-testid="stTextInput"] [data-baseweb="input"],
[data-testid="stTextInput"] [data-baseweb="base-input"] {{
  border: none !important;
  box-shadow: none !important;
  background: transparent !important;
}}

[data-testid="stTextInput"] input {{
  min-height: 48px;
  font-size: 1rem !important;
  font-family: {FONT_FAMILY} !important;
  border-radius: 14px !important;
  padding: 0.75rem 1rem !important;
  border: 1.5px solid {COLORS["border"]} !important;
  background: {COLORS["surface"]} !important;
  color: {COLORS["ink"]} !important;
  box-shadow: none !important;
}}

[data-testid="stTextInput"] input::placeholder {{
  color: {COLORS["muted"]} !important;
  opacity: 1;
}}

[data-testid="stTextInput"] input:focus {{
  border-color: {COLORS["accent"]} !important;
  box-shadow: none !important;
  outline: none !important;
}}

[data-testid="stExpander"] details {{
  border: 1.5px solid {COLORS["border"]};
  border-radius: 14px;
  background: {COLORS["surface"]};
}}

hr {{
  border: none !important;
  height: 1px !important;
  background: linear-gradient(90deg, transparent, {COLORS["border"]}, transparent) !important;
  margin: 1.25rem 0 !important;
}}
"""


def inject_theme_css():
    css = _theme_css().replace("\\", "\\\\").replace("`", "\\`")
    components.html(
        f"""
        <script>
        (function() {{
          const doc = window.parent.document;
          doc.body.classList.remove("briefly-sop-page");
          let style = doc.getElementById("briefly-theme");
          if (!style) {{
            style = doc.createElement("style");
            style.id = "briefly-theme";
            doc.head.appendChild(style);
          }}
          style.textContent = `{css}`;
        }})();
        </script>
        """,
        height=0,
    )


def render_header():
    logo_uri = _svg_data_uri("briefly-logo.svg")
    components.html(
        f"""
        <div style="padding:0.5rem 0 0.85rem;overflow:visible;">
          <img src="{logo_uri}" alt="Briefly" style="height:44px;width:auto;display:block;" />
        </div>
        """,
        height=76,
    )


def render_nav_button_row(items, active_section: str, navigate_fn, row_key: str):
    cols = st.columns(len(items), gap="small")
    for col, (label, section) in zip(cols, items):
        with col:
            is_active = active_section == section
            if st.button(
                label,
                use_container_width=True,
                type="primary" if is_active else "secondary",
                key=f"{row_key}_{section}",
            ):
                navigate_fn(section)
                st.rerun()


def render_hero(subtitle: str | None = None):
    render_header()


def inject_memory_page_css():
    css = (
        '[data-testid="stExpander"] details summary p {'
        f'color: {COLORS["memory"]} !important; font-weight: 700 !important; }}'
    ).replace("\\", "\\\\").replace("`", "\\`")
    components.html(
        f"""
        <script>
        (function() {{
          const doc = window.parent.document;
          let style = doc.getElementById("briefly-memory-theme");
          if (!style) {{
            style = doc.createElement("style");
            style.id = "briefly-memory-theme";
            doc.head.appendChild(style);
          }}
          style.textContent = `{css}`;
        }})();
        </script>
        """,
        height=0,
    )


def render_page_header(title: str, subtitle: str | None = None):
    st.markdown(
        f'<div style="margin:0 0 1rem; font-family:{FONT_FAMILY};">'
        f'<h2 style="margin:0; font-size:2rem; font-weight:800; letter-spacing:-0.04em; '
        f'color:{COLORS["ink"]};">{title}</h2>'
        + (
            f'<p style="margin:0.4rem 0 0; color:{COLORS["muted"]}; font-size:1.05rem;">{subtitle}</p>'
            if subtitle
            else ""
        )
        + "</div>",
        unsafe_allow_html=True,
    )


def render_section_label(label: str):
    st.markdown(
        f'<p style="margin:1.25rem 0 0.65rem; font-size:0.78rem; font-weight:700; '
        f'letter-spacing:0.1em; text-transform:uppercase; color:{COLORS["accent_dark"]};">{label}</p>',
        unsafe_allow_html=True,
    )
