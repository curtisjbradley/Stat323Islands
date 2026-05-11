"""
Data loader for the Islands API.

Parses island and village data from the site's island.js file at import time.
House scraping is deferred to the first call to Village.get_houses() so that
startup is fast and a single bad village doesn't crash the whole import.
"""
import regex as re
import ast
from typing import List
from .islands_objects import Island, Village
from .village_scraper import scrape_village
from .session_manager import make_request


# ---------------------------------------------------------------------------
# Parse islands and villages from island.js
# ---------------------------------------------------------------------------

_island_js = make_request('js/island.js?v=3.1')

_island_list_match = re.compile(r"var islands = \[[\w\d\s.':{,}]*\];").search(_island_js)
if _island_list_match is None:
    raise Exception('Could not parse islands from js')

_islands: List[Island] = [
    Island(i['name'], i['island'], i['x'], i['y'])
    for i in [ast.literal_eval(p) for p in re.compile(r'\{[\w\d\s.\':,]*\}').findall(_island_list_match.group())]
]
_islands_idx: dict[int, Island] = {island.id: island for island in _islands}

_town_list_match = re.compile(r"var towns = \[[\s\{\w' :,\}-]*\];").search(_island_js)
if _town_list_match is None:
    raise Exception('Could not parse towns from js')

_villages: List[Village] = [
    Village(town['name'], _islands_idx[town['island']], town['x'], town['y'])
    for town in [ast.literal_eval(p) for p in re.compile(r'\{[\w\d\s.\':,-]*\}').findall(_town_list_match.group())]
]

# Register each village with its island (no house scraping yet)
for _village in _villages:
    _village.get_island()._villages.append(_village)


# ---------------------------------------------------------------------------
# Patch Village.get_houses() to scrape lazily
# ---------------------------------------------------------------------------

def _lazy_get_houses(self):
    """Scrape and cache houses on first access."""
    if not self._houses:
        self._houses = scrape_village(self)
    return self._houses

Village.get_houses = _lazy_get_houses


# ---------------------------------------------------------------------------
# Public accessors
# ---------------------------------------------------------------------------

def get_islands() -> List[Island]:
    """Return the list of all islands."""
    return _islands


def get_villages() -> List[Village]:
    """Return the flat list of all villages across all islands."""
    return _villages


__all__ = ['get_islands', 'get_villages']
