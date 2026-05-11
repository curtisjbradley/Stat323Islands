"""
Core domain objects for the Islands API: Island, Village, and House.

Islands contain Villages, which contain Houses. These objects are populated
at startup by data_loader.py and village_scraper.py.
"""
from __future__ import annotations

from .house import House
from typing import List


class Island:
    """Represents one of the islands in the simulation."""

    def __init__(self, name: str, int_id: int, x: float, y: float):
        self._name = name
        self._id = int_id
        self._x = x
        self._y = y
        self._villages: List[Village] = []

    def get_name(self) -> str:
        """Return the island's display name."""
        return self._name

    def get_villages(self) -> List[Village]:
        """Return the list of villages on this island."""
        return self._villages

    @property
    def id(self) -> int:
        """Numeric island ID used in the site's JS data."""
        return self._id

    def __repr__(self):
        return "Island - {}".format(self._name)


class Village:
    """Represents a village on an island."""

    def __init__(self, name: str, island: Island, x: float, y: float):
        self._name = name
        self._island = island
        self._x = x
        self._y = y
        self._houses: List[House] = []

    def get_name(self) -> str:
        """Return the village's display name."""
        return self._name

    def get_island(self) -> Island:
        """Return the island this village belongs to."""
        return self._island

    def get_location(self) -> tuple:
        """Return the (x, y) map coordinates of the village."""
        return self._x, self._y

    def get_houses(self) -> List[House]:
        """Return the list of houses in this village."""
        return self._houses

    def __repr__(self):
        return "Village - {} on {}".format(self.get_name(), self._island.get_name())


__all__ = ['Island', 'Village', 'House']
