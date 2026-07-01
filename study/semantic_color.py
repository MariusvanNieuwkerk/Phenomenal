"""Semantic color markup for Memory Items and SOP callouts."""

import html
import re

# Critical QRH actions — dark red
_MI_CRITICAL = re.compile(
    r"\b("
    r"PUSH\s+IN|STOP|DISCH|DON|EMERGENCY|100%|OPEN|PRESS|PERFORM|ACCOMPLISH|NOTIFY|"
    r"HOLD\s+DOWN(?:\s+FOR\s+\d+\s+SEC)?|FIXED|SHUTOFF|OFF\s+VENT|CREW\s+ONLY"
    r")\b",
    re.IGNORECASE,
)

_SOP_RULES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"UNSTABLE,\s*GO-AROUND", re.IGNORECASE), "briefly-sop-danger"),
    (re.compile(r"\bGO-AROUND\b", re.IGNORECASE), "briefly-sop-danger"),
    (re.compile(r"\bUNSTABLE\b", re.IGNORECASE), "briefly-sop-danger"),
    (re.compile(r"\bGREEN\b"), "briefly-sop-mode-green"),
    (re.compile(r"\bWHITE\b"), "briefly-sop-mode-white"),
    (re.compile(r"\bPINK\b"), "briefly-sop-mode-pink"),
    (re.compile(r"\bBLUE\b"), "briefly-sop-mode-blue"),
    (re.compile(r"\bCONTINUE\b"), "briefly-sop-mode-ok"),
    (re.compile(r"\bSTABLE\b"), "briefly-sop-mode-ok"),
]


def _span(cls: str, text: str) -> str:
    return f'<span class="{cls}">{html.escape(text)}</span>'


def _colorize_mi_action(action: str) -> str:
    if not action or "<span" in action:
        return action

    def repl(m: re.Match[str]) -> str:
        return _span("briefly-mi-critical", m.group(0))

    colored = _MI_CRITICAL.sub(repl, html.escape(action))
    if colored == html.escape(action):
        return _span("briefly-mi-action", action)
    return colored


def colorize_memory_md(text: str) -> str:
    """Color memory-item tables (Action column) and caution lines."""
    lines: list[str] = []
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("|") and not re.match(r"\|\s*[-:]+", stripped):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if len(cells) == 2 and cells[0].lower() != "item":
                cells[1] = _colorize_mi_action(cells[1])
                line = "| " + " | ".join(cells) + " |"
        elif stripped.startswith("*") and stripped.endswith("*") and stripped.count("*") == 2:
            line = f'<p class="briefly-mi-caution">{html.escape(stripped[1:-1])}</p>'
        elif stripped.startswith("**") and stripped.endswith("**") and stripped.count("**") == 2:
            inner = stripped[2:-2]
            line = f"<p><strong>{html.escape(inner)}</strong></p>"
        lines.append(line)
    return "\n".join(lines)


def colorize_sop_md(text: str) -> str:
    """Highlight FD modes, go-around, and continue/stable in SOP markdown."""
    if not text:
        return text

    bold_parts: list[str] = []

    def stash_bold(m: re.Match[str]) -> str:
        bold_parts.append(m.group(1))
        return f"@@BOLD{len(bold_parts) - 1}@@"

    text = re.sub(r"\*\*(.+?)\*\*", stash_bold, text, flags=re.DOTALL)

    chunks = re.split(r"(<[^>]+>)", text)
    out: list[str] = []
    for chunk in chunks:
        if chunk.startswith("<"):
            out.append(chunk)
        elif chunk:
            out.append(_colorize_sop_plain(chunk))

    text = "".join(out)

    for i, inner in enumerate(bold_parts):
        text = text.replace(f"@@BOLD{i}@@", f"<strong>{_colorize_sop_plain(inner)}</strong>")

    return text


def _colorize_sop_plain(text: str) -> str:
    if not text:
        return text

    matches: list[tuple[int, int, str, str]] = []
    for pattern, cls in _SOP_RULES:
        for m in pattern.finditer(text):
            overlaps = any(not (m.end() <= s or m.start() >= e) for s, e, _, _ in matches)
            if not overlaps:
                matches.append((m.start(), m.end(), m.group(0), cls))

    if not matches:
        return text

    matches.sort(key=lambda x: x[0])
    out: list[str] = []
    pos = 0
    for start, end, word, cls in matches:
        out.append(html.escape(text[pos:start]))
        out.append(_span(cls, word))
        pos = end
    out.append(html.escape(text[pos:]))
    return "".join(out)


def mi_md(text: str):
    """Render memory-item markdown with semantic colors."""
    import streamlit as st

    st.markdown(colorize_memory_md(text), unsafe_allow_html=True)


def sop_md_colored(text: str):
    """Render SOP markdown with semantic colors."""
    import streamlit as st

    st.markdown(colorize_sop_md(text), unsafe_allow_html=True)
