from typing import Final
class TaskResult:
    def __init__(self, time : str, name : str, result : str):
        self._time = time
        self._result = result
        self._name = name

    def time(self) -> str:
        return self._time
    def name(self) -> str:
        return self._result
    def result(self) -> str:
        return self._result
    def __repr__(self):
        return f'{self._name} @ {self._time} - ({self._result})'

class Task:
    def __init__(self, code : str):
        self._code = code
    def code(self) -> str:
        return self._code


# Task Definitions

MEASURE_BLOOD_GLUCOSE : Final[Task] = Task('bloodglucose')
"""Measure blood glucose levels"""

MEASURE_BLOOD_PRESSURE : Final[Task] = Task('bloodpressure')
"""Measure blood pressure levels"""

CHOCOLATE_DARK_40 : Final[Task] = Task('chocdark')
"""Consume 50g of 40% cocoa chocolate"""

CHOCOLATE_DARK_70 : Final[Task] = Task('chocdark70')
"""Consume 50g of 70% cocoa chocolate"""

CHOCOLATE_DARK_85 : Final[Task] = Task('chocdark85')
"""Consume 50g of 85% cocoa chocolate"""

CHOCOLATE_DARK_99 : Final[Task] = Task('chocdark99')
"""Consume 50g of 99% cocoa chocolate"""

SIT_TEMP_NEG20 : Final[Task] = Task('freezer')
"""Sit at -20 C for 10 mins"""

SIT_TEMP_40: Final[Task] = Task('heat40')
"""Sit at 40 C for 10 mins"""

SIT_TEMP_5: Final[Task] = Task('cold')
"""Sit at 5 C for 10 mins"""

DRINK_WATER_250: Final[Task] = Task('water250')
"""Drink 250 ml of Water"""

DRINK_WATER_250: Final[Task] = Task('water60')
"""Drink 60 ml of Water"""

EAT_FRIED_CHIPS : Final[Task] = Task('fries')
"""Eat 50g of Fried Chips"""


__all__ = [name for name in globals() if not name.startswith('_')]