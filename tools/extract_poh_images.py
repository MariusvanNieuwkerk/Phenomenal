import os
import re
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Section:
    code: str
    title: str
    start_page: int  # 0-based PDF page index (inclusive)
    end_page: int  # 0-based PDF page index (exclusive)
    assets_dir: str


def _slug(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_") or "page"


def _ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def _iter_pages(doc, start: int, end: int) -> Iterable[tuple[int, str]]:
    for i in range(start, end):
        yield i, doc.load_page(i).get_text("text")


def _render_page_png(doc, page_idx: int, out_path: str, zoom: float = 2.0) -> None:
    page = doc.load_page(page_idx)
    pix = page.get_pixmap(matrix=(zoom, zoom), alpha=False)
    pix.save(out_path)


def _match_any(text: str, patterns: list[re.Pattern]) -> bool:
    return any(p.search(text) for p in patterns)


def main() -> None:
    # NOTE: This script is for local extraction only. It does not run in-app.
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pdf_path = os.environ.get(
        "POH_PDF",
        "/Users/mariusvannieuwkerk/Desktop/Apps/Phenom 300/818878637-POH-2908-04-REV14-FULL.pdf",
    )

    # Section start pages were found by searching for the first occurrence of each "6-xx-00" block.
    # They are 0-based PDF page indices.
    sections: list[Section] = [
        Section("6-01", "Airplane General", 252, 344, os.path.join(project_root, "assets", "airplane_general")),
        Section("6-02", "Air Management System", 344, 380, os.path.join(project_root, "assets", "air_management")),
        Section("6-03", "Automatic Flight", 380, 424, os.path.join(project_root, "assets", "automatic_flight")),
        Section("6-04", "Electrical", 424, 464, os.path.join(project_root, "assets", "electrics")),
        Section("6-05", "Engine", 464, 504, os.path.join(project_root, "assets", "powerplant")),
        Section("6-06", "Fire Protection", 504, 518, os.path.join(project_root, "assets", "fire_protection")),
        Section("6-07", "Flight Controls", 518, 564, os.path.join(project_root, "assets", "flight_controls")),
        # 6-08 Flight Instruments/Comm/Nav intentionally excluded
        Section("6-09", "Fuel", 688, 708, os.path.join(project_root, "assets", "fuel")),
        Section("6-10", "Hydraulic", 708, 720, os.path.join(project_root, "assets", "hydraulics")),
        Section("6-11", "Ice and Rain Protection", 720, 746, os.path.join(project_root, "assets", "ice_protection")),
        Section("6-12", "Landing Gear and Brakes", 746, 786, os.path.join(project_root, "assets", "landing_gear")),
        Section("6-13", "Oxygen", 786, 834, os.path.join(project_root, "assets", "oxygen")),
        Section("6-14", "Warning System", 834, 9999, os.path.join(project_root, "assets", "warning_system")),
    ]

    import fitz  # PyMuPDF (installed locally via .python_packages)

    doc = fitz.open(pdf_path)
    print(f"Opened PDF: {pdf_path} ({doc.page_count} pages)")

    # Patterns for synoptic pages.
    synoptic_pats = [
        re.compile(r"\bSYNOPTIC\b", re.I),
        re.compile(r"\bSYNOPTICS\b", re.I),
        re.compile(r"\bMFD\b.*\bSYNOPTIC\b", re.I),
    ]

    # Patterns for electrical system configuration pages.
    elec_cfg_pats = [
        re.compile(r"\bBUS\b.*\bCONFIG", re.I),
        re.compile(r"\bCONFIGURATION\b", re.I),
        re.compile(r"\bS/?GEN\b", re.I),
    ]

    for sec in sections:
        end = min(sec.end_page, doc.page_count)
        if sec.start_page >= end:
            continue

        _ensure_dir(sec.assets_dir)

        extracted = 0
        extracted_cfg = 0

        for page_idx, text in _iter_pages(doc, sec.start_page, end):
            # Normalize whitespace for more stable matching.
            norm = re.sub(r"\s+", " ", text)

            is_synoptic = _match_any(norm, synoptic_pats)
            is_elec_cfg = sec.code == "6-04" and _match_any(norm, elec_cfg_pats)

            if not is_synoptic and not is_elec_cfg:
                continue

            tag = []
            if is_synoptic:
                extracted += 1
                tag.append("synoptic")
            if is_elec_cfg:
                extracted_cfg += 1
                tag.append("config")

            out_name = f"poh_{sec.code}_{'_'.join(tag)}_p{page_idx+1}.png"
            out_path = os.path.join(sec.assets_dir, out_name)

            if os.path.exists(out_path):
                continue

            _render_page_png(doc, page_idx, out_path, zoom=2.0)

        print(
            f"{sec.code} {sec.title}: extracted synoptic={extracted}, electrical_config={extracted_cfg} -> {os.path.relpath(sec.assets_dir, project_root)}"
        )

    print("Done.")


if __name__ == "__main__":
    main()

