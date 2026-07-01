"""Search index — maps terms to app destinations."""

from content.airports import CATEGORY_C_AIRPORTS
from data.quick_lookup import LOOKUP_CATEGORIES

from data.memory_items import MEMORY_TITLES

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
    "flight controls": ("Flight Controls", ["flap", "aileron", "rudder", "spoiler", "pusher", "swps", "trim", "ptrim", "gust lock"]),
    "fire protection": ("Fire Protection", ["fire", "extinguisher"]),
    "warning system": ("Warning System", ["cas", "warning", "caution", "advisory", "egpws", "taws", "tcas", "transponder"]),
    "automatic flight": ("Automatic Flight", ["autopilot", "ap", "fms", "yd", "yaw damper", "mistrim", "steep fail", "flight director"]),
    "rnav / rnp approaches": (
        "RNAV / RNP Approaches",
        ["rnav", "rnp", "lnav", "vnav", "lpv", "apv", "cdfa", "garmin", "g3000", "sbas", "overlay", "fms pink", "jdm", "database", "nav database", "sd card", "connext", "cmc", "default profile", "netjets default", "crew profile"],
    ),
    "airplane general": (
        "Airplane General",
        ["dimensions", "door", "walkaround", "walkround", "exterior", "nose gear", "brake wear", "static discharger", "hydraulic reservoir", "emergency lights", "pitot", "radome"],
    ),
    "cabin & ife": (
        "Cabin & IFE",
        ["wifi", "wi-fi", "go-go", "gogo", "ife", "lavatory", "toilet", "nespresso", "coffee", "ped", "galley", "ucs"],
    ),
}

MEMORY_ITEMS = MEMORY_TITLES

STUDY_MODULES = [
    ("Systems", "systems", "POH aircraft systems"),
    ("Flight Planning", "planning", "OM-A minima and alternates"),
    ("SOP", "sop", "OM-B standard operating procedures"),
    ("Flight Profiles", "profiles", "Normal and abnormal profiles · OEI gradient · min fuel · cruise Mach"),
    ("Cold Weather Ops", "cold_weather", "OM-B cold weather · severe icing · temp comp"),
    ("Special Airports", "airports", "OM-C Category C aerodromes"),
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
    entries.append(_entry("Handbook PDF", "documents", "Phenom 300 Handbook (full fleet manual)", keywords="handbook training wifi toilet nespresso fms database"))

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
