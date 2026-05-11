"""
Village scraper for the Islands API.

Fetches and parses the house map for a given Village by requesting its
village.php page and extracting the embedded JavaScript data.
"""
import ast
from .session_manager import make_request
from .islands_objects import Village, House
from bs4 import BeautifulSoup
import regex as re
from typing import List

_RE_V_VALUE = re.compile(r"var v=([\d]*);")
_RE_MAP     = re.compile(r'var map=\[.*\];')


def scrape_village(town: Village) -> List[House]:
    """
    Scrape all houses in *town* from the site and return them as House objects.

    Raises an Exception if the village number or map data cannot be found in
    the page's JavaScript.
    """
    town_php = make_request(f'village.php?{town.get_name()}')
    # The village data lives in the first inline (attribute-less) script block
    village_script = list(
        filter(lambda tag: len(tag.attrs) == 0,
               BeautifulSoup(town_php, 'html.parser').findAll('script'))
    )[0].text

    v_match = _RE_V_VALUE.search(village_script)
    if v_match is None:
        raise Exception('Could not find village number when scraping village')
    v = int(v_match.group(1))

    map_match = _RE_MAP.search(village_script)
    if map_match is None:
        raise Exception('Could not find village map when scraping village')

    village_map = ast.literal_eval(map_match.group()[8:-1])
    return [House(h[0], h[1], h[2], h[3], town, v) for h in village_map]
