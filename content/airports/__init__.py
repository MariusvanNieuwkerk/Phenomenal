"""Category C airport package — crew's most-used aerodromes."""

from content.airports.catalog import BRIEFING_STRUCTURE, CATEGORY_C_AIRPORTS
from content.airports.edfe import DETAIL as EDFE
from content.airports.eglc import DETAIL as EGLC
from content.airports.leso import DETAIL as LESO
from content.airports.lflb import DETAIL as LFLB
from content.airports.lftz import DETAIL as LFTZ
from content.airports.lipb import DETAIL as LIPB
from content.airports.lira import DETAIL as LIRA
from content.airports.lowi import DETAIL as LOWI
from content.airports.lsgs import DETAIL as LSGS
from content.airports.lsza import DETAIL as LSZA
from content.airports.lszs import DETAIL as LSZS

AIRPORT_DETAILS = {
    "EGLC": EGLC,
    "EDFE": EDFE,
    "LOWI": LOWI,
    "LSGS": LSGS,
    "LSZA": LSZA,
    "LSZS": LSZS,
    "LFLB": LFLB,
    "LFTZ": LFTZ,
    "LIPB": LIPB,
    "LIRA": LIRA,
    "LESO": LESO,
}

__all__ = ["BRIEFING_STRUCTURE", "CATEGORY_C_AIRPORTS", "AIRPORT_DETAILS"]
