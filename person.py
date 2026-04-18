from session_manager import _session, _BASE_URL, make_request
import regex as re
from bs4 import BeautifulSoup

class Person:
    def __init__(self,_id,name=None,age=None, village=None):
        self._id = _id
        self.name = name
        self._age = age
        self._village = village
    def __repr__(self):
        return "Person {} - Id {} - Of {}".format(self.name, self._id, self._village.get_name() if self._village else None)

    def request_consent(self):
        res = _session.get(
            f'{_BASE_URL}/php/consent.php?id={self._id}',
            headers={'Referer': f'{_BASE_URL}/islander.php?id={self._id}'})
        if res.status_code != 200:
            raise Exception("Error with consent request")
        return 'accept' in res.text
    def toggle_contact(self):
        header ={'referer': f'{_BASE_URL}/islander.php?id={self._id}'}
        res = _session.get(
            f'{_BASE_URL}/php/contact.php?id={self._id}',headers=header)
        if res.status_code != 200:
            raise Exception("Error with toggle contact request")
        return 'added' in res.text
    def get_village(self) -> str:
        if self._village is None:
            self.update_person()
        return self._village
    def get_age(self) -> int:
        if self._age is None:
            self.update_person()
        return self._age
    def get_name(self) -> str:
        if self.name is None:
            self.update_person()
        return self.name
    def update_person(self) -> None:
        island_raw = make_request(f'islander.php?id={self._id}')
        parsed = BeautifulSoup(island_raw, 'html.parser')
        self.name = parsed.title.text

        rows = [list(row.children)[0] for row in parsed.find('table').find_all('tr')]
        rows = rows[1:['id' in row.attrs for row in rows].index(True) - 1]

        self._age = int(re.compile('\\d+').findall(rows[0].text)[0])
        self._village = re.compile('Lives in (.*) \\d+').search(parsed.text).group(1)



class PersonManager:
    def __init__(self):
        self._persons = {}
    def get_person(self, id) -> Person:
        if id in self._persons:
            return self._persons[id]
        else:
            person = Person(id)
            try:
                self._persons[id] = person
                return person
            except:
                return None


manager = PersonManager()
__all__ = ['Person', 'manager']