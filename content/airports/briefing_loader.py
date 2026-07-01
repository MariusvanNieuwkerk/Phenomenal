"""Load parsed OM-C aerodrome briefings (text blocks + image paths)."""

import json
import os
from functools import lru_cache

APP_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PARSED_DIR = os.path.join(APP_DIR, "content", "airports", "parsed")


def static_path(relative: str) -> str:
    return os.path.join(APP_DIR, relative.replace("/", os.sep))


def static_exists(relative: str) -> bool:
    return os.path.isfile(static_path(relative))


@lru_cache(maxsize=16)
def load_parsed_briefing(icao: str) -> dict | None:
    path = os.path.join(PARSED_DIR, f"{icao.lower()}.json")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)
