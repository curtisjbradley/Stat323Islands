import ast
import session_manager
from islands_objects import Village, House
from bs4 import BeautifulSoup
import regex as re
from typing import List

def scrape_village(town : Village) -> List[House]:
    town_php = session_manager.make_request(f'village.php?{town.get_name()}')
    tags = BeautifulSoup(town_php, 'html.parser').findAll('script')

    village_script = list(filter(lambda tag: len(tag.attrs) == 0, tags))[0].text
    v_value_search = re.compile("var v=([\\d]*);").search(village_script)

    if v_value_search is None:
        raise Exception('Cound not find village number when scraping village')
    v = int(v_value_search.group(1))

    map_search = re.compile('var map=\\[.*\\];').search(village_script)
    if map_search is None:
        raise Exception('Cound not find village village map')

    village_map = ast.literal_eval(map_search.group()[8:-1])
    return [House(h[0], h[1], h[2], h[3],town,v) for h in village_map]