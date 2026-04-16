from house import House
from typing import List

class Village:
    pass

class Island:
    def __init__(self, name, int_id, x, y,):
        self._name = name
        self._id = int_id
        self._x = x
        self._y = y
        self._villages = []
    def get_name(self) -> str:
        return self._name
    def __repr__(self):
        return "Island - {}".format(self._name)
    def get_villages(self):
        return self._villages

    @property
    def id(self):
        return self._id

class Village:
    def __init__(self, name,island, x,y):
        self._name = name
        self._island = island
        self._x = x
        self._y = y
        self._houses = []
    def get_name(self) -> str:
        return self._name
    def get_island(self) -> Island:
        return self._island
    def get_location(self) -> tuple:
        return self._x, self._y
    def get_houses(self) -> List[House]:
        return self._houses
    def __repr__(self):
        return "Village - {} on {}".format(self.get_name(), self._island.get_name())


__all__ = [
    'Island',
    'Village',
    'House',
]