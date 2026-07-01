"""Colored styling for the SOP study page — soft, muted palette."""

import streamlit as st
import streamlit.components.v1 as components

from ui.tokens import COLORS, FONT_FAMILY

# Muted tints aligned with Briefly slate-blue theme
SOP_COLORS = {
    "pf_bg": "#E8EEF5",
    "pf_ink": "#3D5F8A",
    "pm_bg": "#E7F0EF",
    "pm_ink": "#4A6561",
    "callout_bg": "rgba(212, 224, 234, 0.45)",
    "callout_ink": "#2D4560",
    "warn_bg": "#F6F0F0",
    "warn_ink": "#7A5555",
    "ok_bg": "#EFF3F0",
    "ok_ink": "#4F6356",
}


def _sop_css() -> str:
    c = SOP_COLORS
    return f"""
body.briefly-sop-page [data-testid="stMarkdownContainer"] table {{
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  margin: 0.65rem 0 1rem;
  font-size: 0.92rem;
  border: 1px solid rgba(155, 180, 201, 0.55);
  border-radius: 12px;
  overflow: hidden;
}}

body.briefly-sop-page [data-testid="stMarkdownContainer"] table thead th {{
  background: {COLORS["accent_soft"]};
  color: {COLORS["ink_soft"]};
  font-weight: 600;
  font-size: 0.76rem;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  padding: 0.5rem 0.75rem;
  border-bottom: 1px solid rgba(155, 180, 201, 0.4);
}}

body.briefly-sop-page [data-testid="stMarkdownContainer"] table thead th:nth-child(2) {{
  color: {c["pf_ink"]};
}}

body.briefly-sop-page [data-testid="stMarkdownContainer"] table thead th:nth-child(3) {{
  color: {c["pm_ink"]};
}}

body.briefly-sop-page [data-testid="stMarkdownContainer"] table td {{
  padding: 0.5rem 0.75rem;
  border-bottom: 1px solid rgba(155, 180, 201, 0.22);
  vertical-align: top;
  color: {COLORS["ink"]};
  background: transparent;
}}

body.briefly-sop-page [data-testid="stMarkdownContainer"] table tr:last-child td {{
  border-bottom: none;
}}

body.briefly-sop-page [data-testid="stMarkdownContainer"] table td:first-child {{
  font-weight: 550;
  color: {COLORS["ink_soft"]};
}}

body.briefly-sop-page [data-testid="stMarkdownContainer"] strong {{
  color: {c["callout_ink"]};
  background: {c["callout_bg"]};
  padding: 0.04em 0.28em;
  border-radius: 4px;
  font-weight: 600;
}}

body.briefly-sop-page [data-testid="stExpander"] details {{
  border-left: 2px solid rgba(74, 111, 165, 0.35);
}}

body.briefly-sop-page [data-testid="stExpander"] details[open] {{
  box-shadow: 0 2px 10px rgba(74, 111, 165, 0.06);
}}

.briefly-sop-legend {{
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin: 0.45rem 0 1rem;
  font-family: {FONT_FAMILY};
}}

.briefly-sop-pill {{
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.22rem 0.58rem;
  border-radius: 999px;
  font-size: 0.74rem;
  font-weight: 550;
  border: 1px solid rgba(155, 180, 201, 0.45);
}}

.briefly-sop-pill.pf {{ background: {c["pf_bg"]}; color: {c["pf_ink"]}; }}
.briefly-sop-pill.pm {{ background: {c["pm_bg"]}; color: {c["pm_ink"]}; }}
.briefly-sop-pill.callout {{ background: rgba(244, 247, 250, 0.95); color: {COLORS["ink_soft"]}; }}
.briefly-sop-pill.warn {{ background: {c["warn_bg"]}; color: {c["warn_ink"]}; }}
.briefly-sop-pill.ok {{ background: {c["ok_bg"]}; color: {c["ok_ink"]}; }}

.briefly-sop-note {{
  padding: 0.6rem 0.8rem;
  border-radius: 10px;
  margin: 0.45rem 0 0.75rem;
  font-size: 0.88rem;
  line-height: 1.45;
  font-family: {FONT_FAMILY};
}}

.briefly-sop-note.warn {{
  background: {c["warn_bg"]};
  border: 1px solid rgba(155, 180, 201, 0.35);
  color: {COLORS["ink_soft"]};
}}

.briefly-sop-note.info {{
  background: rgba(244, 247, 250, 0.9);
  border: 1px solid rgba(155, 180, 201, 0.4);
  color: {COLORS["ink_soft"]};
}}

.briefly-sop-note.ok {{
  background: {c["ok_bg"]};
  border: 1px solid rgba(155, 180, 201, 0.35);
  color: {COLORS["ink_soft"]};
}}

.briefly-sop-note strong {{
  color: {COLORS["ink"]};
  background: transparent;
  padding: 0;
  font-weight: 600;
}}

.briefly-sop-mode-green {{
  color: #15803D;
  font-weight: 800;
}}
.briefly-sop-mode-white {{
  color: #374151;
  font-weight: 800;
  background: #E5E7EB;
  padding: 0.04em 0.22em;
  border-radius: 4px;
}}
.briefly-sop-mode-pink {{
  color: #BE185D;
  font-weight: 800;
}}
.briefly-sop-mode-blue {{
  color: #1D4ED8;
  font-weight: 800;
}}
.briefly-sop-mode-ok {{
  color: #15803D;
  font-weight: 800;
}}
.briefly-sop-danger {{
  color: #B91C1C;
  font-weight: 800;
}}
"""


def inject_sop_styles():
    css = _sop_css().replace("\\", "\\\\").replace("`", "\\`")
    components.html(
        f"""
        <script>
        (function() {{
          const doc = window.parent.document;
          doc.body.classList.add("briefly-sop-page");
          doc.body.classList.remove("briefly-memory-page");
          let style = doc.getElementById("briefly-sop-styles");
          if (!style) {{
            style = doc.createElement("style");
            style.id = "briefly-sop-styles";
            doc.head.appendChild(style);
          }}
          style.textContent = `{css}`;
        }})();
        </script>
        """,
        height=0,
    )


def render_sop_legend():
    st.markdown(
        """
<div class="briefly-sop-legend">
  <span class="briefly-sop-pill pf">PF — Pilot Flying</span>
  <span class="briefly-sop-pill pm">PM — Pilot Monitoring</span>
  <span class="briefly-sop-pill callout">Spoken callout</span>
  <span class="briefly-sop-pill warn">Go-around / unstable</span>
  <span class="briefly-sop-pill ok">Continue / stable</span>
</div>
""",
        unsafe_allow_html=True,
    )


def sop_note(kind: str, text: str):
    from study.semantic_color import colorize_sop_md

    st.markdown(
        f'<div class="briefly-sop-note {kind}">{colorize_sop_md(text)}</div>',
        unsafe_allow_html=True,
    )
