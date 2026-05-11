"""
IslandsAPI — top-level entry point for the Islands wrapper.

Provides access to islands, villages, and study participants. All HTTP
communication is handled by the underlying session_manager; this class
composes the other modules into a single convenient interface.

Usage::

    from api.API import IslandsAPI
    api = IslandsAPI()
    participants = api.get_study_participants()
"""
from .data_loader import get_islands, get_villages
from .person import manager, Person
from bs4 import BeautifulSoup
import regex as re
from .session_manager import make_request
import ast


class IslandsAPI:
    """High-level interface for interacting with the Islands simulation site."""

    def __init__(self):
        self._islands = get_islands()
        self._towns = get_villages()
        self._PersonManager = manager

    def get_villages(self):
        """Return the flat list of all villages across all islands."""
        return self._towns

    def get_islands(self):
        """Return the list of all islands."""
        return self._islands

    def get_person_manager(self):
        """Return the shared PersonManager (identity map for islanders)."""
        return self._PersonManager

    def get_study_participants(self):
        """
        Fetch the current project's participant list from project.php.

        Parses the embedded JavaScript to extract islander IDs and names,
        registers each with the PersonManager, and returns the Person objects.
        """
        res = make_request('project.php')

        script_blocks = BeautifulSoup(res, features="html.parser").find_all('script')
        # Find the script block that contains the 'heads' array
        heads_script = script_blocks[
            ['heads' in s.text for s in script_blocks].index(True)
        ]

        # Each participant is encoded as: heads[N] = { id: ..., name: ... }
        head_pattern = re.compile(
            r"heads\[\d+\] = (\{[.'\d\w:,<>\[\]\s-#]+\})"
        )
        heads = [
            ast.literal_eval(m.group(1))
            for m in head_pattern.finditer(heads_script.text)
        ]

        for head in heads:
            self._PersonManager.register_person(
                Person(head['id'], head['name'].replace("<br>", " "))
            )
        return [self._PersonManager.get_person(head['id']) for head in heads]
