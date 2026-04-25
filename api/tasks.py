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

BLOOD_GLUCOSE : Final[Task] = Task('bloodglucose')
"""Measure blood glucose levels"""

CHOCOLATE_DARK_40 : Final[Task] = Task('chocdark')
"""Consume 50g of 40% cocoa chocolate"""

CHOCOLATE_DARK_70 : Final[Task] = Task('chocdark70')
"""Consume 50g of 70% cocoa chocolate"""

CHOCOLATE_DARK_85 : Final[Task] = Task('chocdark85')
"""Consume 50g of 85% cocoa chocolate"""

CHOCOLATE_DARK_99 : Final[Task] = Task('chocdark99')
"""Consume 50g of 99% cocoa chocolate"""



__all__ = [name for name in globals() if not name.startswith('_')]