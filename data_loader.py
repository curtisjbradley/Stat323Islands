import session_manager
import regex as re
import ast
from typing import List
from islands_objects import Island, Village
from village_scraper import scrape_village


island_js = session_manager.make_request('/js/island.js?v=3.1')
_island_list = re.compile('var islands = \\[[\\w\\d\\s.\':\\{,\\}]*\\];').search(island_js)

if _island_list is None:
    raise Exception('Cound not parse islands from js')

_island_list = _island_list.group()

_parsed_islands = re.compile('\\{[\\w\\d\\s.\':,]*\\}').findall(_island_list)

_islands = [ast.literal_eval(p) for p in _parsed_islands]



_islands = [Island(i['name'], i['island'], i['x'], i['y']) for i in _islands]
_islands_idx = {island.id: island for island in _islands}


_town_list = re.compile("var towns = \\[[\\s\\{\\w' :,\\}-]*\\];").search(island_js)

if _town_list is None:
    raise Exception('Cound not parse islands from js')

_town_list = _town_list.group()

_parsed_towns = re.compile('\\{[\\w\\d\\s.\':,-]*\\}').findall(_town_list)

_villages = [ast.literal_eval(p) for p in _parsed_towns]



_villages = [Village(town['name'], _islands_idx[town['island']], town['x'], town['y']) for town in _villages]

for village in _villages:
    village._houses = scrape_village(village)
    village.get_island()._villages.append(village)

def get_islands() -> List[Island]:
    return _islands

def get_villages() -> List[Village] :
    return _villages





__all__ = ['get_islands', 'get_villages']