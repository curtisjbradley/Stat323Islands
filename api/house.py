"""
House class for the Islands API.

A House belongs to a Village and contains zero or more resident islanders.
Resident data is fetched lazily on first access.
"""
from .person import Person, manager
from .session_manager import _session, _BASE_URL
from bs4 import BeautifulSoup


class House:
    """Represents a single house within a village."""

    def __init__(self, house_style, house_index, house_type, is_big, village, village_index):
        self._house_style = house_style   # TODO: Map to an enum
        self._house_index = house_index
        self._house_type = house_type     # TODO: Map to ghost house etc.
        self._is_big = is_big == 1
        self._village = village
        self._village_index = village_index
        self._residents = None            # Lazily populated by get_residents()

    def get_village(self):
        """Return the Village this house belongs to."""
        return self._village

    def is_empty(self) -> bool:
        """Return True if the house has no residents (index is 'empty')."""
        return self._house_index == 'empty'

    def get_residents(self) -> list:
        """
        Return the list of Person objects living in this house.

        Fetches resident data from the site on first call; subsequent calls
        return the cached result.
        """
        if self._residents is not None:
            return self._residents

        house_request = _session.get(
            f'{_BASE_URL}/house.php?v={self._village_index}&h={self._house_index}',
            headers={'Referer': f'{_BASE_URL}/village.php?{self.get_village().get_name()}'},
        )
        if house_request.status_code != 200:
            raise Exception("Unable to fetch house data")

        resident_list = (
            BeautifulSoup(house_request.content, 'html.parser')
            .find('table', class_='residents')
            .find_all('tr')
        )

        self._residents = []
        for row in resident_list:
            link = row.find('a')
            if link is None:
                continue

            _id = link.attrs['href'][16:]  # strip 'islander.php?id='

            # Re-use existing Person from the manager if already known;
            # otherwise create one with the name/age visible in the table.
            if _id in manager._persons:
                self._residents.append(manager._persons[_id])
            else:
                person = Person(_id, link.text, int(row.find('td', class_='age').text))
                manager.register_person(person)
                self._residents.append(person)

        return self._residents

    def __repr__(self):
        return "House - {} in {}".format(self._house_index, self._village.get_name())


__all__ = ['House']
