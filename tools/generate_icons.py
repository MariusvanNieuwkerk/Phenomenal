"""Generate favicon and PWA icons from static/briefly-icon-512.png (or a source PNG)."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

APP_DIR = Path(__file__).resolve().parents[1]
STATIC = APP_DIR / "static"
DEFAULT_SOURCE = STATIC / "briefly-icon-512.png"


def generate(source: Path = DEFAULT_SOURCE) -> None:
    img = Image.open(source).convert("RGBA")
    w, h = img.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    img = img.crop((left, top, left + side, top + side))

    img.save(STATIC / "briefly-icon-512.png", optimize=True)
    for name, size in {
        "briefly-icon-192.png": 192,
        "briefly-icon-180.png": 180,
        "briefly-icon-32.png": 32,
        "briefly-icon-16.png": 16,
    }.items():
        img.resize((size, size), Image.Resampling.LANCZOS).save(STATIC / name, optimize=True)

    img.resize((32, 32), Image.Resampling.LANCZOS).save(STATIC / "briefly-icon.png", optimize=True)
    img.save(STATIC / "favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])


if __name__ == "__main__":
    import sys

    src = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SOURCE
    generate(src)
    print("Icons written to", STATIC)
