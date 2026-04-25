from .person import Person, manager

from .session_manager import _session, _BASE_URL

from bs4 import BeautifulSoup

class House:
    def __init__(self, house_style, house_index, house_type, is_big, village, village_index):
        self._house_style = house_style #TODO: Map these to an enum
        self._house_index = house_index
        self._house_type = house_type #TODO: Map this to ghost house and such
        self._is_big = is_big == 1
        self._village = village
        self._village_index = village_index
        self._residents = None
    def get_village(self):
        return self._village
    def is_empty(self) -> bool:
        return self._house_index == 'empty'

    def get_residents(self) -> list:
        if self._residents is not None:
            return self._residents
        house_request = _session.get(
            f'{_BASE_URL}/house.php?v={self._village_index}&h={self._house_index}',
            headers={'Referer': f'https://islands.smp.uq.edu.au/village.php?{self.get_village().get_name()}'})
        if house_request.status_code != 200:
            raise Exception("Unable to make request to retrieve house data")

        resident_list = BeautifulSoup(house_request.content, 'html.parser').find('table', class_='residents').find_all(
            'tr')
        self._residents = []
        for res in resident_list:

            person_id = res.find('a')

            if person_id is None:
                continue
            _id = person_id.attrs['href'][16:]

            if _id in manager._persons:
                self._residents.append(manager._persons[_id])
                continue
            person = Person(_id, res.find('a').text, int(res.find('td', class_='age').text))
            manager.register_person(person)
            self._residents.append(person)
        return self._residents

    def __repr__(self):
        return "House - {} in {}".format(self._house_index, self._village.get_name())
__all__ = ['House']