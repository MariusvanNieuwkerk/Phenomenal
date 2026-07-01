"""Pilot-first aerodrome briefing — curated overview + OM-C reference."""

import html
import os

import streamlit as st

from content.airports.briefing_loader import load_parsed_briefing, static_exists, static_path
from content.render_helpers import source_footer
from ui.tokens import COLORS, FONT_FAMILY, FONT_URL


def _inject_briefing_css():
    css = f"""
@import url('{FONT_URL}');
.briefly-briefing-wrap {{ font-family: {FONT_FAMILY}; color: {COLORS['ink']}; }}
.briefly-hero {{
  background: linear-gradient(135deg, {COLORS['accent']} 0%, {COLORS['accent_dark']} 100%);
  border-radius: 18px; padding: 1.25rem 1.4rem; color: #fff; margin-bottom: 1rem;
  box-shadow: 0 8px 24px rgba(61, 95, 138, 0.22);
}}
.briefly-hero-title {{
  font-size: 1.65rem; font-weight: 800; letter-spacing: -0.02em; margin: 0; line-height: 1.2;
}}
.briefly-hero-meta {{
  font-size: 0.88rem; opacity: 0.88; margin: 0.35rem 0 0; font-weight: 600; letter-spacing: 0.04em;
}}
.briefly-glance {{
  display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.55rem;
  margin: 0 0 0.25rem;
}}
.briefly-glance-item {{
  background: {COLORS['surface']}; border: 1.5px solid {COLORS['border']}; border-radius: 12px;
  padding: 0.65rem 0.85rem; font-size: 0.9rem; font-weight: 600; color: {COLORS['ink_soft']}; line-height: 1.4;
}}
.briefly-block {{
  background: {COLORS['surface']}; border: 1.5px solid {COLORS['border']}; border-radius: 14px;
  padding: 1rem 1.15rem; margin-bottom: 0.85rem;
}}
.briefly-block-title {{
  font-size: 0.72rem; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase;
  color: {COLORS['accent_dark']}; margin: 0 0 0.65rem;
}}
.briefly-block ul {{ margin: 0; padding-left: 1.1rem; }}
.briefly-block li {{ margin-bottom: 0.45rem; font-size: 0.94rem; line-height: 1.55; color: {COLORS['ink_soft']}; }}
.briefly-block p {{ margin: 0; font-size: 0.94rem; line-height: 1.6; color: {COLORS['ink_soft']}; }}
.briefly-limit li {{ color: #7F1D1D; }}
.briefly-approach {{
  border-left: 3px solid {COLORS['accent']}; padding-left: 0.85rem; margin-bottom: 1rem;
}}
.briefly-approach-name {{ font-weight: 800; font-size: 0.95rem; color: {COLORS['ink']}; margin: 0 0 0.4rem; }}
"""
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def _ul(items: list[str], *, limit_style: bool = False) -> str:
    if not items:
        return ""
    cls = "briefly-limit" if limit_style else ""
    lis = "".join(f"<li>{html.escape(i)}</li>" for i in items)
    return f'<ul class="{cls}">{lis}</ul>'


def _block(title: str, content: str) -> str:
    if not content:
        return ""
    return f'<div class="briefly-block"><div class="briefly-block-title">{html.escape(title)}</div>{content}</div>'


def _render_block(title: str, items: list[str] | str | None, *, limit_style: bool = False):
    if not items:
        return
    if isinstance(items, str):
        body = f"<p>{html.escape(items)}</p>"
    else:
        body = _ul(items, limit_style=limit_style)
    st.markdown(f'<div class="briefly-briefing-wrap">{_block(title, body)}</div>', unsafe_allow_html=True)


def _glance_items(headline: str) -> list[str]:
    return [p.strip() for p in headline.split("·") if p.strip()]


def _render_glance(items: list[str]):
    if not items:
        return
    cells = "".join(f'<div class="briefly-glance-item">{html.escape(i)}</div>' for i in items)
    st.markdown(f'<div class="briefly-briefing-wrap"><div class="briefly-glance">{cells}</div></div>', unsafe_allow_html=True)


def _render_approaches(approaches: list[dict]):
    if not approaches:
        return
    for ap in approaches:
        parts = []
        for label, key in [
            ("Minima", "minima"),
            ("Performance", "performance"),
            ("Warning", "warning"),
            ("Caution", "caution"),
        ]:
            val = ap.get(key)
            if val:
                parts.append(f"<p><strong>{label}:</strong> {html.escape(val)}</p>")
        proc = ap.get("procedure")
        if proc:
            if isinstance(proc, list):
                parts.append(_ul(proc))
            else:
                parts.append(f"<p>{html.escape(proc)}</p>")
        missed = ap.get("missed")
        if missed:
            if isinstance(missed, list):
                parts.append(f"<p><strong>Missed / balked:</strong></p>{_ul(missed)}")
            else:
                parts.append(f"<p><strong>Missed / balked:</strong> {html.escape(missed)}</p>")
        name = ap.get("name", "Approach")
        st.markdown(
            f'<div class="briefly-briefing-wrap"><div class="briefly-approach">'
            f'<p class="briefly-approach-name">{html.escape(name)}</p>{"".join(parts)}</div></div>',
            unsafe_allow_html=True,
        )


def _collect_diagrams(icao: str) -> list[str]:
    parsed = load_parsed_briefing(icao)
    if not parsed:
        return []
    seen: set[str] = set()
    paths: list[str] = []
    for page in parsed.get("pages", []):
        for rel in page.get("embeds", []):
            if rel not in seen and static_exists(rel):
                seen.add(rel)
                paths.append(rel)
    return paths


def _render_diagrams(paths: list[str]):
    if not paths:
        st.caption("No procedure diagrams extracted for this airport.")
        return
    cols = st.columns(2 if len(paths) > 1 else 1)
    for i, rel in enumerate(paths):
        with cols[i % len(cols)]:
            st.image(static_path(rel), use_container_width=True)


def _render_omc_reference(icao: str):
    parsed = load_parsed_briefing(icao)
    if not parsed:
        st.caption("OM-C page images not available.")
        return
    cols = st.columns(2)
    for i, page in enumerate(parsed.get("pages", [])):
        rel = page.get("image")
        if rel and static_exists(rel):
            with cols[i % 2]:
                st.image(static_path(rel), use_container_width=True)
                st.caption(f"OM-C p.{page.get('page', i + 1)}")


def render_pilot_briefing(icao: str, name: str, detail: dict, pdf_section: str):
    _inject_briefing_css()

    category = detail.get("category", "Cat C")
    headline = detail.get("headline", "")

    st.markdown(
        f"""
        <div class="briefly-briefing-wrap">
          <div class="briefly-hero">
            <p class="briefly-hero-title">{html.escape(name)} · {html.escape(icao)}</p>
            <p class="briefly-hero-meta">{html.escape(category)} · OM-C</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    tab_overview, tab_arrival, tab_departure, tab_limits, tab_charts = st.tabs(
        ["Overview", "Arrival", "Departure", "Limits", "Charts"]
    )

    with tab_overview:
        _render_glance(_glance_items(headline))
        _render_block("Overview", detail.get("overview"))
        _render_block("Threats", detail.get("threats"))
        qual = (detail.get("qualification") or []) + (detail.get("revalidation") or [])
        _render_block("Qualification & recency", qual or None)
        _render_block("Operational notes", detail.get("operational_general"))

    with tab_arrival:
        _render_block("Arrival procedures", detail.get("arrival"))
        _render_approaches(detail.get("approaches", []))

    with tab_departure:
        _render_block("Departure", detail.get("departure"))
        _render_block("Ground", detail.get("ground"))
        _render_block("Miscellaneous", detail.get("miscellaneous"))

    with tab_limits:
        _render_block("Hard limits", detail.get("limitations"), limit_style=True)
        _render_block("Crew assignment", detail.get("crew_assignment"))
        weather = detail.get("weather")
        if weather:
            _render_block("Weather minima", weather if isinstance(weather, list) else [weather])

    with tab_charts:
        _render_block("Chart references", detail.get("charts"))
        diagrams = _collect_diagrams(icao)
        if diagrams:
            st.markdown(
                f'<p style="font-size:0.72rem;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;'
                f'color:{COLORS["accent_dark"]};margin:0.5rem 0 0.65rem;">Procedure diagrams</p>',
                unsafe_allow_html=True,
            )
            _render_diagrams(diagrams)

    with st.expander("Full OM-C reference pages", expanded=False):
        _render_omc_reference(icao)

    source_footer("om_c", pdf_section)
