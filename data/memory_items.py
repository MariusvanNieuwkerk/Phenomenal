"""QRH memory items — shared by Memory Items page and system modules."""

MEMORY_CONTENT: dict[str, str] = {
    "SMOKE EVACUATION": """
| Item | Action |
|------|--------|
| Oxygen Masks | DON, EMERGENCY |
| Dilution Valve | CLOSED |
| Smoke Goggles | DON |
| Communication | ESTABLISH |
| Oxygen Knob | CREW ONLY |
| DUMP Button | PUSH IN |
| ECS Knob | OFF VENT |
""",
    "SMOKE / FIRE / FUME": """
| Item | Action |
|------|--------|
| Oxygen Masks | DON, EMERGENCY |
| Dilution Valve | CLOSED |
| Smoke Goggles | DON |
| Communication | ESTABLISH |
| DUMP Button | PUSH IN |
""",
    "E1(2) FIRE": """
**Affected Engine:**

| Item | Action |
|------|--------|
| Thrust Lever | IDLE |
| START/STOP Knob | STOP |
| SHUTOFF Button | PUSH IN |

*On ground or if fire persists after 30 seconds in flight:*

| Item | Action |
|------|--------|
| BOTTLE Switch | DISCH |
""",
    "ENGINE FIRE, SEVERE DAMAGE or SEPARATION": """
**Affected Engine:**

| Item | Action |
|------|--------|
| Thrust Lever | IDLE |
| START/STOP Knob | STOP |
| SHUTOFF Button | PUSH IN |

*Wait 30 seconds and if fire persists:*

| Item | Action |
|------|--------|
| BOTTLE Switch | DISCH |
""",
    "DUAL ENGINE FAILURE": """
| Item | Action |
|------|--------|
| Thrust Levers | IDLE |
| Crew Oxygen Masks | DON, 100% |
| Communication | ESTABLISH |
""",
    "ENGINE ABNORMAL START": """
**Affected Engine:**

| Item | Action |
|------|--------|
| START/STOP Knob | STOP |
""",
    "ELEC EMERGENCY": """
| Item | Action |
|------|--------|
| PRESN MODE Switch | MAN |
| CABIN ALT Switch | HOLD DOWN FOR 10 SEC |

*If at or above 25,000 ft:*

| Item | Action |
|------|--------|
| Rudder Pedals | FIXED |

*If above 10,000 ft:*

| Item | Action |
|------|--------|
| CAB ALTITUDE HI Procedure | ACCOMPLISH |
""",
    "ELEC XFR FAIL": """
| Item | Action |
|------|--------|
| ELEC EMER Button | PUSH IN |
""",
    "EMERGENCY EVACUATION": """
| Item | Action |
|------|--------|
| Thrust Levers | IDLE |
| Emergency/Parking Brake | ON |
| START/STOP Knobs | STOP |
| FIRE SHUTOFF Buttons | PUSH IN |
| PRESN MODE Switch | MAN |
| DUMP Button | PUSH IN |
| ATC | NOTIFY |
| Emergency Evacuation | PERFORM |
| BATT 1 & 2 Switches | OFF |
""",
    "CAB ALTITUDE HI": """
| Item | Action |
|------|--------|
| Oxygen Masks | DON, 100% |
| Communication | ESTABLISH |
| SIGNS/OUTLET Switch | PED BELTS / OFF |
| Altitude | Max 10,000ft or MEA (whichever is higher) |
| Thrust Levers | IDLE |
| SPEED BRAKE Switch | OPEN |
| Airspeed | 250 KIAS / MMO Max |
| LDG GEAR Lever | DN |
| Transponder | 7700 |
| ATC | NOTIFY |
""",
    "EMERGENCY DESCENT": """
| Item | Action |
|------|--------|
| SIGNS/OUTLET Switch | PED BELTS / OFF |
| Altitude | Max 10,000ft or MEA (whichever is higher) |
| Thrust Levers | IDLE |
| SPEED BRAKE Switch | OPEN |
| Airspeed | 250 KIAS / MMO Max |
| LDG GEAR Lever | DN |
| Transponder | 7700 |
| ATC | NOTIFY |
""",
    "LG WOW SYS FAIL": """
*If associated with engine failure and obstacle clearance, simultaneously proceed:*

| Item | Action |
|------|--------|
| DN LCK REL Button | PRESS |
| LDG GEAR Lever | UP |
""",
    "GEAR LEVER CANNOT BE MOVED UP": """
*If associated with engine failure and obstacle clearance, simultaneously proceed:*

| Item | Action |
|------|--------|
| DN LCK REL Button | PRESS |
| LDG GEAR Lever | UP |
""",
    "INADVERTANT PUSHER ACTUATION": """
| Item | Action |
|------|--------|
| PUSHER CUTOUT Button | PUSH IN |
""",
}

MEMORY_TITLES: list[str] = list(MEMORY_CONTENT.keys())

SYSTEM_MEMORY: dict[str, list[str]] = {
    "Fire Protection": [
        "SMOKE EVACUATION",
        "SMOKE / FIRE / FUME",
        "E1(2) FIRE",
        "ENGINE FIRE, SEVERE DAMAGE or SEPARATION",
    ],
    "Powerplant": [
        "DUAL ENGINE FAILURE",
        "ENGINE ABNORMAL START",
        "E1(2) FIRE",
        "ENGINE FIRE, SEVERE DAMAGE or SEPARATION",
    ],
    "Electrics": ["ELEC EMERGENCY", "ELEC XFR FAIL"],
    "Air Management": ["CAB ALTITUDE HI", "EMERGENCY DESCENT"],
    "Oxygen": ["CAB ALTITUDE HI", "EMERGENCY DESCENT", "SMOKE EVACUATION"],
    "Landing Gear & Brakes": ["LG WOW SYS FAIL", "GEAR LEVER CANNOT BE MOVED UP"],
    "Flight Controls": ["INADVERTANT PUSHER ACTUATION"],
    "Warning System": ["CAB ALTITUDE HI", "EMERGENCY DESCENT"],
}
