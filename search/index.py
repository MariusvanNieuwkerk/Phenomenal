"""Search index — maps terms to app destinations."""

from content.airports import CATEGORY_C_AIRPORTS
from data.quick_lookup import LOOKUP_CATEGORIES

LIMITATION_HINTS = {
    "speeds": "Speed Limitations (V-Speeds)",
    "weights": "Structural & Weight Limits",
    "fuel": "Fuel",
    "ice": "Ice & Rain Protection",
    "electrical": "Electrical",
    "pressurization": "Air Management System (Pressurization)",
    "engine": "Engine Limits (PW535E)",
    "wind": "Wind Limitations",
    "autoflight": "Autoflight / YD",
    "memory": "Memory Items",
}

SYSTEM_KEYWORDS = {
    "fuel": ("Fuel", ["fuel", "xfeed", "crossfeed", "tank", "pump"]),
    "electrics": ("Electrics", ["electrical", "generator", "battery", "gpu", "bus", "elec"]),
    "ice protection": ("Ice Protection", ["ice", "anti-ice", "de-ice", "wingstab", "icing"]),
    "powerplant": ("Powerplant", ["engine", "itt", "n1", "n2", "fadec", "oil"]),
    "hydraulics": ("Hydraulics", ["hydraulic", "3000 psi", "edp"]),
    "landing gear & brakes": ("Landing Gear & Brakes", ["gear", "brake", "landing gear", "wow"]),
    "air management": ("Air Management", ["pressurization", "press", "cabin altitude", "ecs"]),
    "oxygen": ("Oxygen", ["oxygen", "o2", "mask"]),
    "flight controls": ("Flight Controls", ["flap", "aileron", "rudder", "spoiler", "pusher"]),
    "fire protection": ("Fire Protection", ["fire", "extinguisher"]),
    "warning system": ("Warning System", ["cas", "warning", "caution", "advisory"]),
    "automatic flight": ("Automatic Flight", ["autopilot", "ap", "fms", "yd", "yaw damper"]),
    "airplane general": ("Airplane General", ["dimensions", "door", "walkaround"]),
}

MEMORY_ITEMS = [
    "SMOKE EVACUATION",
    "SMOKE / FIRE / FUME",
    "E1(2) FIRE",
    "ENGINE FIRE, SEVERE DAMAGE or SEPARATION",
    "DUAL ENGINE FAILURE",
    "ENGINE ABNORMAL START",
    "ELEC EMERGENCY",
    "ELEC XFR FAIL",
    "EMERGENCY EVACUATION",
    "CAB ALTITUDE HI",
    "EMERGENCY DESCENT",
    "LG WOW SYS FAIL",
    "GEAR LEVER CANNOT BE MOVED UP",
    "INADVERTANT PUSHER ACTUATION",
]

STUDY_MODULES = [
    ("Systems", "systems", "POH aircraft systems"),
    ("Flight Planning", "planning", "OM-A minima and alternates"),
    ("SOP", "sop", "OM-B standard operating procedures"),
    ("Flight Profiles", "profiles", "Normal and abnormal profiles"),
    ("Cold Weather Ops", "cold_weather", "OM-B cold weather procedures"),
    ("Special Airports", "airports", "OM-C Category C aerodromes"),
    ("Handbook", "handbook", "Phenom 300 training handbook"),
    ("Limitations", "limitations", "Weights, speeds, engine and system limits"),
    ("Memory Items", "memory", "QRH memory items"),
    ("Documents", "documents", "OM-A, OM-B, OM-C, Handbook PDFs"),
]


def _entry(title, section, subtitle="", keywords="", system=None, airport=None, focus=None):
    return {
        "title": title,
        "section": section,
        "subtitle": subtitle,
        "keywords": keywords.lower(),
        "system": system,
        "airport": airport,
        "focus": focus,
    }


def build_search_index():
    entries = []

    for title, section, subtitle in STUDY_MODULES:
        entries.append(_entry(title, section, subtitle, keywords=f"{title} {subtitle}"))

    for system, (label, kws) in SYSTEM_KEYWORDS.items():
        entries.append(
            _entry(label, "systems", "Aircraft system", keywords=" ".join(kws), system=label)
        )

    for title in MEMORY_ITEMS:
        entries.append(
            _entry(title, "memory", "QRH memory item", keywords=title.lower(), focus=title)
        )

    for cat in LOOKUP_CATEGORIES:
        hint = LIMITATION_HINTS.get(cat["id"], cat["label"])
        entries.append(
            _entry(
                cat["label"],
                "limitations",
                cat["description"],
                keywords=f"{cat['label']} {cat['description']}",
                focus=hint,
            )
        )
        for item in cat["items"]:
            entries.append(
                _entry(
                    item["term"],
                    "limitations",
                    item["value"][:80],
                    keywords=f"{item['term']} {item['value']} {cat['label']}",
                    focus=hint,
                )
            )

    for airport in CATEGORY_C_AIRPORTS:
        tags = " ".join(airport.get("tags", []))
        entries.append(
            _entry(
                f"{airport['icao']} — {airport['name']}",
                "airports",
                "Category C airport",
                keywords=f"{airport['icao']} {airport['name']} {tags}".lower(),
                airport=airport["icao"],
            )
        )

    entries.append(_entry("OM-A", "documents", "Operations Manual Part A", keywords="om-a om a manual"))
    entries.append(_entry("OM-B", "documents", "Operations Manual Part B EMB-505", keywords="om-b om b sop manual"))
    entries.append(_entry("OM-C", "documents", "Operations Manual Part C", keywords="om-c om c airport manual"))
    entries.append(_entry("Handbook", "documents", "Phenom 300 Handbook", keywords="handbook training"))

    return entries


SEARCH_INDEX = build_search_index()


def search(query: str, limit: int = 8):
    q = query.lower().strip()
    if not q:
        return []

    scored = []
    for entry in SEARCH_INDEX:
        haystack = f"{entry['title']} {entry['subtitle']} {entry['keywords']}".lower()
        if q not in haystack:
            continue
        score = 0
        if q in entry["title"].lower():
            score += 3
        if entry["title"].lower().startswith(q):
            score += 2
        if q in entry["keywords"]:
            score += 1
        scored.append((score, entry))

    scored.sort(key=lambda x: (-x[0], x[1]["title"]))
    return [e for _, e in scored[:limit]]
