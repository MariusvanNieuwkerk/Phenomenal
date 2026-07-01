"""Convert standalone **Subheading** lines to ### in systems study markdown blocks."""

from __future__ import annotations

import re
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1]
SYSTEMS_DIR = APP_DIR / "systems"

BLOCK_RE = re.compile(
    r"((?:st\.markdown|_md)\(\s*(?:f)?\"\"\"\n?)(.*?)(\"\"\"\s*(?:,\s*unsafe_allow_html=True)?\s*\))",
    re.DOTALL,
)


def is_subheading(line: str) -> bool:
    s = line.strip()
    if not s or s.startswith("### "):
        return False
    if s.startswith("_Source") or s.startswith("---"):
        return False
    if s == "Colour logic summary:":
        return True
    if re.match(r"^\*\*[^*]+\*\* — .+", s):
        return False
    if re.match(r"^\*\*[^*]+\*\* .+", s) and not re.fullmatch(
        r"\*\*(.+?)\*\*(\s+\([^)]+\))?", s
    ):
        return False
    return bool(re.fullmatch(r"\*\*(.+?)\*\*(\s+\([^)]+\))?", s))


def heading_text(line: str) -> str:
    if line.strip() == "Colour logic summary:":
        return "Colour logic summary"
    m = re.fullmatch(r"\*\*(.+?)\*\*(\s+\([^)]+\))?", line.strip())
    assert m
    return m.group(1) + (m.group(2) or "")


def convert_body(body: str) -> str:
    lines = body.split("\n")
    out: list[str] = []
    for line in lines:
        if is_subheading(line):
            if out and out[-1] != "":
                out.append("")
            out.append(f"### {heading_text(line)}")
            out.append("")
        else:
            out.append(line)
    return "\n".join(out)


def process_file(path: Path) -> bool:
    original = path.read_text()
    changed = False

    def repl(match: re.Match[str]) -> str:
        nonlocal changed
        prefix, body, suffix = match.group(1), match.group(2), match.group(3)
        new_body = convert_body(body)
        if new_body != body:
            changed = True
        return prefix + new_body + suffix

    updated = BLOCK_RE.sub(repl, original)
    if changed:
        path.write_text(updated)
    return changed


def main() -> None:
    updated = []
    for path in sorted(SYSTEMS_DIR.glob("*.py")):
        if path.name == "__init__.py":
            continue
        if process_file(path):
            updated.append(path.name)
    if updated:
        print("Updated:", ", ".join(updated))
    else:
        print("No changes needed.")


if __name__ == "__main__":
    main()
