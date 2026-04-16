from data_loader import get_islands, get_villages
from person import manager
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

