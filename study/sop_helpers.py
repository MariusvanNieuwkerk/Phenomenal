"""Shared render helpers for SOP markdown tables and blocks."""

import streamlit as st


def sop_md(text: str):
    st.markdown(text)


def sop_crew_table(rows: list[tuple[str, str, str]], intro: str = ""):
    """Render Situation | PF | PM table."""
    if intro:
        sop_md(intro)
    lines = [
        "| Situation | PF | PM |",
        "|-----------|----|----|",
    ]
    for situation, pf, pm in rows:
        lines.append(f"| {situation} | {pf} | {pm} |")
    sop_md("\n".join(lines))


def sop_event_table(rows: list[tuple[str, str]], intro: str = ""):
    """Render Event | Callout / action table."""
    if intro:
        sop_md(intro)
    lines = [
        "| Event | Callout / action |",
        "|-------|------------------|",
    ]
    for event, action in rows:
        lines.append(f"| {event} | {action} |")
    sop_md("\n".join(lines))


def sop_checklist(title: str, items: list[str], trigger: str = ""):
    sop_md(f"**{title}**")
    if trigger:
        sop_md(f"*Trigger:* {trigger}")
    for item in items:
        sop_md(f"- {item}")


def sop_flow(title: str, trigger: str, pf: list[str] | None = None, pm: list[str] | None = None):
    sop_md(f"**{title}**")
    sop_md(f"*Trigger:* {trigger}")
    if pf:
        sop_md("**PF / LHS**")
        for line in pf:
            sop_md(f"- {line}")
    if pm:
        sop_md("**PM / RHS**")
        for line in pm:
            sop_md(f"- {line}")
