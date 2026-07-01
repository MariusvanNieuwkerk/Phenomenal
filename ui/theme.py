import base64
import os

import streamlit as st
import streamlit.components.v1 as components

from ui.tokens import COLORS, FONT_FAMILY, LOGO_FONT_FAMILY, LOGO_FONT_URL

APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(APP_DIR, "static")


def _svg_data_uri(filename: str) -> str:
    path = os.path.join(STATIC_DIR, filename)
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded}"


def _theme_css() -> str:
    return f"""
@import url('{LOGO_FONT_URL}');

html, body, [class*="css"] {{
  font-family: {FONT_FAMILY} !important;
}}

.briefly-logo,
[data-testid="stMarkdownContainer"] p.briefly-logo {{
  margin: 1.65rem 0 0.85rem !important;
  padding: 0 !important;
  font-family: {LOGO_FONT_FAMILY} !important;
  font-weight: 600 !important;
  font-size: 2.85rem !important;
  letter-spacing: 0.03em !important;
  line-height: 1.05 !important;
  color: {COLORS["ink"]} !important;
}}

.stApp {{
  background: linear-gradient(165deg, {COLORS["bg_top"]} 0%, {COLORS["bg_bottom"]} 100%);
}}

[data-testid="stAppViewContainer"] > .main {{
  background: transparent;
}}

.block-container {{
  max-width: 1400px;
  padding-top: 1.75rem;
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


def inject_scroll_to_top_chevron(*, enabled: bool = True, anchor_id: str = "briefly-systems-top"):
    """Fixed side chevron — visible after scrolling down (Systems page)."""
    accent = COLORS["accent"]
    accent_dark = COLORS["accent_dark"]
    enabled_js = "true" if enabled else "false"
    components.html(
        f"""
        <script>
        (function() {{
          const doc = window.parent.document;
          const enabled = {enabled_js};
          const anchorId = "{anchor_id}";
          let btn = doc.getElementById("briefly-scroll-top");
          if (!enabled) {{
            if (btn) {{
              btn.style.opacity = "0";
              btn.style.pointerEvents = "none";
            }}
            return;
          }}
          if (!btn) {{
            btn = doc.createElement("button");
            btn.id = "briefly-scroll-top";
            btn.type = "button";
            btn.setAttribute("aria-label", "Terug naar boven");
            btn.innerHTML = `
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
                   xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <path d="M6 14l6-6 6 6" stroke="currentColor" stroke-width="2.5"
                      stroke-linecap="round" stroke-linejoin="round"/>
              </svg>`;
            btn.style.cssText = `
              position: fixed;
              right: max(0.75rem, env(safe-area-inset-right));
              top: 50%;
              z-index: 99999;
              width: 46px;
              height: 46px;
              margin-top: -23px;
              border-radius: 50%;
              border: 1.5px solid {accent_dark};
              background: {accent};
              color: #fff;
              display: flex;
              align-items: center;
              justify-content: center;
              cursor: pointer;
              box-shadow: 0 4px 16px rgba(26, 77, 122, 0.32);
              opacity: 0;
              pointer-events: none;
              transition: opacity 0.22s ease, transform 0.22s ease;
              transform: translateX(12px);
            `;
            doc.body.appendChild(btn);
            btn.addEventListener("click", () => {{
              const target = doc.getElementById(anchorId);
              const main = doc.querySelector("section.main");
              if (target) {{
                target.scrollIntoView({{ behavior: "smooth", block: "start" }});
              }} else if (main) {{
                main.scrollTo({{ top: 0, behavior: "smooth" }});
              }} else {{
                window.parent.scrollTo({{ top: 0, behavior: "smooth" }});
              }}
            }});
          }}
          function scrollY() {{
            const main = doc.querySelector("section.main");
            if (main && main.scrollHeight > main.clientHeight) return main.scrollTop;
            return doc.documentElement.scrollTop || doc.body.scrollTop || 0;
          }}
          function onScroll() {{
            const show = scrollY() > 200;
            btn.style.opacity = show ? "1" : "0";
            btn.style.pointerEvents = show ? "auto" : "none";
            btn.style.transform = show ? "translateX(0)" : "translateX(12px)";
          }}
          if (!window.__brieflyScrollTopInit) {{
            window.__brieflyScrollTopInit = true;
            const main = doc.querySelector("section.main");
            if (main) main.addEventListener("scroll", onScroll, {{ passive: true }});
            window.parent.addEventListener("scroll", onScroll, {{ passive: true }});
          }}
          onScroll();
        }})();
        </script>
        """,
        height=0,
    )


def inject_theme_css():
    css = _theme_css().replace("\\", "\\\\").replace("`", "\\`")
    components.html(
        f"""
        <script>
        (function() {{
          const doc = window.parent.document;
          doc.body.classList.remove("briefly-sop-page");
          doc.body.classList.remove("briefly-memory-page");
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
    st.markdown('<p class="briefly-logo">Briefly</p>', unsafe_allow_html=True)


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
    css = f"""
body.briefly-memory-page [data-testid="stExpander"] summary,
body.briefly-memory-page [data-testid="stExpander"] summary p,
body.briefly-memory-page [data-testid="stExpander"] summary strong,
body.briefly-memory-page [data-testid="stExpander"] summary span,
body.briefly-memory-page [data-testid="stExpander"] summary [data-testid="stMarkdownContainer"],
body.briefly-memory-page [data-testid="stExpander"] summary [data-testid="stMarkdownContainer"] p,
body.briefly-memory-page [data-testid="stExpander"] summary [data-testid="stMarkdownContainer"] strong {{
  color: {COLORS["memory"]} !important;
  font-weight: 700 !important;
}}
body.briefly-memory-page [data-testid="stMarkdownContainer"] table {{
  border-collapse: separate;
  border-spacing: 0;
  width: 100%;
  margin: 0.5rem 0 0.85rem;
  border: 1px solid rgba(155, 180, 201, 0.45);
  border-radius: 10px;
  overflow: hidden;
}}
body.briefly-memory-page [data-testid="stMarkdownContainer"] table thead th {{
  background: {COLORS["accent_soft"]};
  color: {COLORS["ink_soft"]};
  font-size: 0.76rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  padding: 0.45rem 0.7rem;
}}
body.briefly-memory-page [data-testid="stMarkdownContainer"] table td {{
  padding: 0.45rem 0.7rem;
  border-top: 1px solid rgba(155, 180, 201, 0.22);
  vertical-align: top;
  background: transparent;
}}
body.briefly-memory-page [data-testid="stMarkdownContainer"] table td:first-child {{
  color: {COLORS["ink_soft"]};
  font-weight: 600;
  width: 42%;
}}
.briefly-mi-critical {{
  color: #B91C1C;
  font-weight: 800;
}}
.briefly-mi-action {{
  color: #C2410C;
  font-weight: 700;
}}
.briefly-mi-caution {{
  color: #92400E;
  background: #FFFBEB;
  border-left: 3px solid #F59E0B;
  padding: 0.45rem 0.65rem;
  border-radius: 0 8px 8px 0;
  margin: 0.35rem 0 0.55rem;
  font-size: 0.9rem;
  font-style: italic;
}}
""".replace("\\", "\\\\").replace("`", "\\`")
    components.html(
        f"""
        <script>
        (function() {{
          const doc = window.parent.document;
          doc.body.classList.add("briefly-memory-page");
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
