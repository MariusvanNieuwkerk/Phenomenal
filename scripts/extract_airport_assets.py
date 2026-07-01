#!/usr/bin/env python3
"""Extract OM-C aerodrome briefing pages, diagrams, and parsed text for Briefly.

Run after updating OM-C Part C:
    .venv/bin/python scripts/extract_airport_assets.py
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

import fitz

ROOT = pathlib.Path(__file__).resolve().parents[1]
PDF = ROOT / "documents/operations_manuals/OM-C - Operations Manual Part C.pdf"
STATIC = ROOT / "static/airports"
PARSED = ROOT / "content/airports/parsed"

STARTS = {
    "EDFE": (446, 8),
    "EGLC": (455, 8),
    "LESO": (502, 10),
    "LFLB": (526, 23),
    "LFTZ": (557, 12),
    "LIPB": (607, 29),
    "LOWI": (637, 19),
    "LSGS": (665, 17),
    "LSZA": (683, 21),
    "LSZS": (705, 27),
}

SECTION_TITLES = {
    "1": "Qualification requirements",
    "2": "Initial qualification requirements",
    "3": "Revalidation requirements",
    "4": "In-flight familiarisation syllabus",
    "5": "Limitations / Miscellaneous",
    "6": "Weather / Airport limitations",
    "7": "Overview",
    "8": "Operational procedures — General",
    "9": "Arrival procedures",
    "10": "Departure procedures",
    "11": "Ground procedures",
    "12": "Miscellaneous",
    "13": "Charts / Pictures / Other",
    "14": "Changes since the last revision",
}


def clean_page_text(t: str) -> str:
    lines: list[str] = []
    for line in t.splitlines():
        line = line.strip()
        if not line:
            lines.append("")
            continue
        if "Uncontrolled Copy" in line:
            continue
        if re.match(r"OM-C\s+14-CAT-C-", line):
            continue
        if line in {"AERODROME BRIEFING", "MOUNTAIN AIRPORT", "OM-C"}:
            continue
        if re.match(r"14-CAT-C-[A-Z0-9]+-\d+/\d+", line):
            continue
        if re.match(r"^\d{2} [A-Z]{3} \d{4}$", line):
            continue
        if re.match(r"^[A-Z]{4}/[A-Z]{3}$", line):
            continue
        if re.match(r"^(CAT C|~CAT C)", line):
            continue
        lines.append(line)
    out: list[str] = []
    blank = 0
    for ln in lines:
        if not ln:
            blank += 1
            if blank <= 1:
                out.append("")
        else:
            blank = 0
            out.append(ln)
    return "\n".join(out).strip()


def body_to_blocks(body: str) -> list[dict]:
    blocks: list[dict] = []
    current: dict = {"type": "text", "lines": []}
    for line in body.split("\n"):
        u = line.upper().strip()
        if u.startswith("WARNING"):
            if current["lines"]:
                blocks.append(current)
            current = {"type": "warning", "lines": [line]}
            continue
        if u.startswith("CAUTION"):
            if current["lines"]:
                blocks.append(current)
            current = {"type": "caution", "lines": [line]}
            continue
        if u.startswith("NOTE:") or u.startswith("NOTE "):
            if current["lines"]:
                blocks.append(current)
            current = {"type": "note", "lines": [line]}
            continue
        if line.strip().startswith("•") or line.strip().startswith("- "):
            if current["type"] != "list":
                if current["lines"]:
                    blocks.append(current)
                current = {"type": "list", "lines": []}
            current["lines"].append(line.strip().lstrip("•- ").strip())
            continue
        if current["type"] in ("warning", "caution", "note") and line.strip():
            current["lines"].append(line)
            continue
        if current["type"] == "list" and line.strip():
            if current["lines"]:
                blocks.append(current)
            current = {"type": "text", "lines": [line]}
            continue
        if current["type"] != "text":
            if current["lines"]:
                blocks.append(current)
            current = {"type": "text", "lines": []}
        if line.strip():
            current["lines"].append(line)
        elif current["lines"]:
            blocks.append(current)
            current = {"type": "text", "lines": []}
    if current["lines"]:
        blocks.append(current)
    return blocks


def parse_sections(full_text: str) -> list[dict]:
    pattern = r"\n(\d{1,2})\.\s+([A-Z][^\n]+?)\s*\n"
    parts = list(re.finditer(pattern, "\n" + full_text))
    sections: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for i, m in enumerate(parts):
        num = m.group(1)
        title = m.group(2).strip()
        start = m.end()
        end = parts[i + 1].start() if i + 1 < len(parts) else len(full_text)
        body = full_text[start:end].strip()
        if len(body) < 10:
            continue
        key = (num, title[:30])
        if key in seen:
            continue
        seen.add(key)
        sections.append(
            {
                "num": int(num) if num.isdigit() else num,
                "title": SECTION_TITLES.get(num, title.title()),
                "body": body,
                "blocks": body_to_blocks(body),
            }
        )
    return sections


def main() -> int:
    if not PDF.is_file():
        print(f"Missing OM-C PDF: {PDF}", file=sys.stderr)
        return 1

    doc = fitz.open(PDF)
    STATIC.mkdir(parents=True, exist_ok=True)
    PARSED.mkdir(parents=True, exist_ok=True)

    for icao, (start, n) in STARTS.items():
        dest = STATIC / icao.lower()
        dest.mkdir(parents=True, exist_ok=True)
        pages_meta: list[dict] = []
        full_parts: list[str] = []
        sec_pages: dict[str, list[int]] = {}

        for i, pno in enumerate(range(start - 1, start - 1 + n)):
            page = doc[pno]
            raw = page.get_text()
            text = clean_page_text(raw)
            full_parts.append(text)

            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
            page_path = dest / f"page-{i + 1:02d}.png"
            pix.save(str(page_path))

            embeds: list[str] = []
            for j, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                try:
                    base = doc.extract_image(xref)
                    if base["ext"] in ("jpeg", "png", "jpg") and len(base["image"]) > 5000:
                        ep = dest / f"embed-p{i + 1:02d}-{j + 1:02d}.{base['ext']}"
                        ep.write_bytes(base["image"])
                        embeds.append(f"static/airports/{icao.lower()}/{ep.name}")
                except Exception:
                    pass

            pages_meta.append(
                {
                    "page": i + 1,
                    "image": f"static/airports/{icao.lower()}/page-{i + 1:02d}.png",
                    "embeds": embeds,
                }
            )
            for m in re.finditer(r"(?:^|\n)(\d{1,2})\.\s+[A-Z]", "\n" + raw):
                sec_pages.setdefault(m.group(1), []).append(i + 1)

        full_text = "\n\n".join(full_parts)
        sections = parse_sections(full_text)
        for s in sections:
            num = str(s["num"])
            pnums = sec_pages.get(num, [])
            s["pages"] = pnums
            s["page_images"] = [f"static/airports/{icao.lower()}/page-{p:02d}.png" for p in pnums]
            embeds: list[str] = []
            for p in pnums:
                embeds.extend(
                    sorted(
                        f"static/airports/{icao.lower()}/{x.name}"
                        for x in dest.glob(f"embed-p{p:02d}-*")
                    )
                )
            s["embeds"] = embeds

        data = {"icao": icao, "page_count": n, "pages": pages_meta, "sections": sections}
        (PARSED / f"{icao.lower()}.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
        print(f"{icao}: {n} pages, {len(sections)} sections")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
