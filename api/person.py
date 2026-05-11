"""
Person and PersonManager classes for the Islands API.

Person wraps an islander's profile, lazily fetching data from the site on
first access. PersonManager acts as an identity map so the same islander is
never represented by two different objects.
"""
from .session_manager import _session, _BASE_URL, make_request
from .tasks import TaskResult, Task

import regex as re
from bs4 import BeautifulSoup
from typing import List

# ---------------------------------------------------------------------------
# Compiled regex constants
# ---------------------------------------------------------------------------
_RE_AWAKE    = re.compile(r"var awake = (\d+);")
_RE_CONSENTED = re.compile(r"var consented = (\d+);")
_RE_AGE      = re.compile(r'\d+')
_RE_VILLAGE  = re.compile(r'Lives in (.*) \d+')


class Person:
    """Represents a single islander."""

    def __init__(
        self,
        _id: str,
        name: str = None,
        age: int = None,
        village: str = None,
        consented: bool = None,
        completed_tasks: List[TaskResult] = None,
        awake: bool = None,
    ):
        self._id: str = _id
        self._name: str = name
        self._age: int = age
        self._village: str = village
        self._consented: bool = consented
        self._tasks = completed_tasks
        self._awake = awake

    def __repr__(self):
        return "Person: Id {}".format(self._id)

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------

    def request_consent(self) -> bool:
        """Ask the islander for consent. Returns True if they accepted."""
        res = _session.get(
            f'{_BASE_URL}/php/consent.php?id={self._id}',
            headers={'Referer': f'{_BASE_URL}/islander.php?id={self._id}'},
        )
        if res.status_code != 200:
            raise Exception("Error with consent request")
        return 'accept' in res.text

    def toggle_contact(self) -> bool:
        """Toggle the contact status for this islander. Returns True if added."""
        res = _session.get(
            f'{_BASE_URL}/php/contact.php?id={self._id}',
            headers={'referer': f'{_BASE_URL}/islander.php?id={self._id}'},
        )
        if res.status_code != 200:
            raise Exception("Error with toggle contact request")
        return 'added' in res.text

    def do_task(self, task: Task) -> dict | None:
        """
        Submit a task for this islander.

        Returns a dict with task timing/result fields, or None if the task
        is not currently available for this islander.
        """
        if not isinstance(task, Task):
            raise Exception("Invalid task type")

        res = _session.get(
            f'{_BASE_URL}/task.php?id={self._id}&code={task.code()}',
            headers={'referer': f'{_BASE_URL}/islander.php?id={self._id}'},
        )
        if res.status_code != 200:
            raise Exception("Error with task request")
        if res.text == 'Not available' or res.text == 'Busy':
            return None

        lines = res.text.splitlines()
        if len(lines) < 5:
            raise Exception(f"Unexpected task response for id={self._id}: {res.text!r}")
        return {
            "start_time": float(lines[0]),
            "end_time":   float(lines[1]),
            "category":   lines[2],
            "number":     lines[3],
            "text":       lines[4],
        }

    # ------------------------------------------------------------------
    # Lazy-loaded accessors
    # ------------------------------------------------------------------

    def get_name(self) -> str:
        """Return the islander's display name."""
        if self._name is None:
            self.update_person()
        return self._name

    def get_village(self) -> str:
        """Return the name of the village this islander lives in."""
        if self._village is None:
            self.update_person()
        return self._village

    def get_age(self) -> int:
        """Return the islander's age."""
        if self._age is None:
            self.update_person()
        return self._age

    def get_id(self) -> str:
        """Return the islander's unique ID string."""
        return self._id

    def is_awake(self) -> bool:
        """Return whether the islander is currently awake."""
        if self._awake is None:
            self.update_person()
        return self._awake

    def has_consented(self) -> bool:
        """Return whether the islander has given consent."""
        if self._consented is None:
            self.update_person()
        return self._consented

    def get_task_results(self) -> List[TaskResult]:
        """Return the list of completed task results for this islander."""
        if self._tasks is None:
            self.update_person()
        return self._tasks

    # ------------------------------------------------------------------
    # Profile scraping
    # ------------------------------------------------------------------

    def update_person(self) -> None:
        """Fetch and refresh all profile data from the islander's page."""
        parsed = BeautifulSoup(make_request(f'islander.php?id={self._id}'), 'html.parser')

        awake_match = _RE_AWAKE.search(parsed.find('body').find('script').text)
        if awake_match is None:
            raise Exception(f"Could not parse awake status for id={self._id}")
        self._awake = int(awake_match.group(1)) == 1

        self._name = parsed.title.text.replace("<br>", " ")

        info_tab = parsed.find('div', id='t1')
        rows = [list(row.children)[0] for row in info_tab.find('table').find_all('tr')]
        rows = rows[1 : ['id' in row.attrs for row in rows].index(True) - 1]
        self._age = int(_RE_AGE.findall(rows[0].text)[0])

        village_match = _RE_VILLAGE.search(parsed.text)
        if village_match is None:
            raise Exception(f"Could not parse village for id={self._id}")
        self._village = village_match.group(1)

        tasks_div = parsed.find('div', id='t2')
        consent_match = _RE_CONSENTED.search(tasks_div.find("script").text)
        if consent_match is None:
            raise Exception(f"Could not parse consent status for id={self._id}")
        self._consented = int(consent_match.group(1)) == 1

        self._tasks = [
            self._parse_result(t)
            for t in tasks_div.find_all('div', class_='taskresult')
            if t.text.strip() != ''
        ]

    @staticmethod
    def _parse_result(task) -> TaskResult | None:
        """Parse a single taskresult div into a TaskResult object."""
        if task.text is None:
            return None
        if task.find('div', class_='taskresulttask') is None:
            # TODO: Support for tax records
            return TaskResult(task.find('div', class_='taskresulttd').text.strip(), "NYI", None)

        result_div = task.find('div', class_='taskresultresult')
        return TaskResult(
            task.find('div', class_='taskresulttd').text.strip(),
            task.find('div', class_='taskresulttask').text.strip(),
            result_div.text if result_div is not None else None,
        )


class PersonManager:
    """
    Identity map for Person objects.

    Ensures that each islander ID maps to exactly one Person instance,
    preventing duplicate objects for the same islander.
    """

    def __init__(self):
        self._persons: dict[str, Person] = {}

    def get_person(self, _id: str) -> Person:
        """Return the Person for the given ID, creating a stub if not yet known."""
        if _id not in self._persons:
            self._persons[_id] = Person(_id)
        return self._persons[_id]

    def register_person(self, person: Person) -> None:
        """Add a Person to the registry if not already present."""
        if person.get_id() not in self._persons:
            self._persons[person.get_id()] = person


manager = PersonManager()
__all__ = ['Person', 'manager']
