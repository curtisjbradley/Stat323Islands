"""
Task definitions and result types for the Islands API.

Tasks represent actions that can be performed on islanders (e.g. measuring
blood pressure, consuming food/drink). TaskResult holds the outcome of a
completed task as scraped from an islander's profile page.
"""
from typing import Final


class TaskResult:
    """Represents a completed task entry on an islander's profile."""

    def __init__(self, time: str, name: str, result: str):
        self._time = time
        self._name = name
        self._result = result

    def time(self) -> str:
        """Return the timestamp string of when the task was completed."""
        return self._time

    def name(self) -> str:
        """Return the display name of the task."""
        return self._name  # was incorrectly returning self._result

    def result(self) -> str:
        """Return the result/measurement value of the task."""
        return self._result

    def __repr__(self):
        return f'{self._name} @ {self._time} - ({self._result})'


class Task:
    """Represents a task that can be assigned to an islander."""

    def __init__(self, code: str):
        self._code = code

    def code(self) -> str:
        """Return the URL code used to submit this task."""
        return self._code


# ---------------------------------------------------------------------------
# Task Definitions
# ---------------------------------------------------------------------------

MEASURE_BLOOD_GLUCOSE: Final[Task] = Task('bloodglucose')
"""Measure blood glucose levels."""

MEASURE_BLOOD_PRESSURE: Final[Task] = Task('bloodpressure')
"""Measure blood pressure levels."""

CHOCOLATE_DARK_40: Final[Task] = Task('chocdark')
"""Consume 50g of 40% cocoa chocolate."""

CHOCOLATE_DARK_70: Final[Task] = Task('chocdark70')
"""Consume 50g of 70% cocoa chocolate."""

CHOCOLATE_DARK_85: Final[Task] = Task('chocdark85')
"""Consume 50g of 85% cocoa chocolate."""

CHOCOLATE_DARK_99: Final[Task] = Task('chocdark99')
"""Consume 50g of 99% cocoa chocolate."""

SIT_TEMP_NEG20: Final[Task] = Task('freezer')
"""Sit at -20°C for 10 minutes."""

SIT_TEMP_40: Final[Task] = Task('heat40')
"""Sit at 40°C for 10 minutes."""

SIT_TEMP_5: Final[Task] = Task('cold')
"""Sit at 5°C for 10 minutes."""

DRINK_WATER_250: Final[Task] = Task('water250')
"""Drink 250 ml of water."""

DRINK_WATER_60: Final[Task] = Task('water60')  # was a duplicate of DRINK_WATER_250
"""Drink 60 ml of water."""

EAT_FRIED_CHIPS: Final[Task] = Task('fries')
"""Eat 50g of fried chips."""

__all__ = [name for name in globals() if not name.startswith('_')]
