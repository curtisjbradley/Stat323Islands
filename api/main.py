from .data_loader import get_islands, get_villages
from .person import manager,Person
from bs4 import BeautifulSoup
import regex as re
from .session_manager import make_request
import ast
class IslandsAPI:
    def __init__(self):
        self._islands = get_islands()
        self._towns = get_villages()
        self._PersonManager = manager

    def get_villages(self):
        return self._towns
    def get_islands(self):
        return self._islands
    def get_person_manager(self):
        return self._PersonManager
    def get_study_participants(self):
        res = make_request('project.php')

        script_blocks = BeautifulSoup(res,features="html.parser").find_all('script')
        heads_script = script_blocks[['heads' in s.text for s in script_blocks].index(True)]

        heads = [g.group() for g in
                 (re.compile("heads\\[\\d+\\] = (\\{[.'\\d\\w:,<>\\[\\]\\s-#]+\\})").finditer(heads_script.text))]
        persons = [Person(head['id'], head['name'].replace("<br>", " ")) for head in [ast.literal_eval(head[head.index('{'):]) for head in heads]]
        for p in persons:
            self._PersonManager.register_person(p)
        persons = [self._PersonManager.get_person(p.get_id())  for p in persons]
        return persons

