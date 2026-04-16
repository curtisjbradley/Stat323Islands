from session_manager import _session, _BASE_URL, make_request
import regex as re
from bs4 import BeautifulSoup

class Person:
    def __init__(self,_id,name,age, village):
        self._id = _id
        self.name = name
        self.age = age
        self.village = village
    def __repr__(self):
        return "Person {} - Id {} - Of {}".format(self.name, self._id, self.village.get_name())

    def request_consent(self):
        res = _session.get(
            f'{_BASE_URL}/php/consent.php?id={self._id}',
            headers={'Referer': f'{_BASE_URL}/islander.php?id={self._id}'})
        if res.status_code != 200:
            raise Exception("Error with consent request")
        return 'accept' in res.text
    def toggle_contact(self):
        res = make_request(f'php/contact.php?id={self._id}')
        if res.status_code != 200:
            raise Exception("Error with contact request")
        return 'added' in res.text


class PersonManager:
    def __init__(self):
        self._persons = {}
    def get_person(self, id) -> Person:
        if id in self._persons:
            return self._persons[id]
        else:
            island_raw = make_request(f'/islander.php?id={id}')
            parsed = BeautifulSoup(island_raw, 'html.parser')
            name = parsed.title.text

            rows = [list(row.children)[0] for row in parsed.find('table').find_all('tr')]
            rows = rows[1:['id' in row.attrs for row in rows].index(True) - 1]
            age = int(re.compile('\d+').findall(rows[0].text)[0])
            village = re.compile('Lives in (.*) \d+').search(rows[2].text).group(1)

            person = Person(id, name, age[0],None)#TODO: FIX
            self._persons[id] = person
            return self._persons[id]


manager = PersonManager()
__all__ = ['Person', 'manager']