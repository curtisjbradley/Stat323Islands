from .session_manager import _session, _BASE_URL, make_request
from .tasks import TaskResult, Task

import regex as re
from bs4 import BeautifulSoup
from typing import List

class Person:
    def __init__(self,_id,name : str =None,age : int=None, village :str  =None, consented : bool = None,completed_tasks : List[TaskResult] = None, awake : bool = None ):
        self._id : str = _id
        self.name : str = name
        self._age : int = age
        self._village : str= village
        self._consented : bool = consented
        self._tasks = completed_tasks
        self._awake = awake

    def __repr__(self):
        return "Person: Id {}".format(self._id)

    def request_consent(self):
        res = _session.get(
            f'{_BASE_URL}/php/consent.php?id={self._id}',
            headers={'Referer': f'{_BASE_URL}/islander.php?id={self._id}'})
        if res.status_code != 200:
            raise Exception("Error with consent request")
        return 'accept' in res.text
    def toggle_contact(self):
        header ={'referer': f'{_BASE_URL}/islander.php?id={self._id}'}
        res = _session.get(
            f'{_BASE_URL}/php/contact.php?id={self._id}',headers=header)
        if res.status_code != 200:
            raise Exception("Error with toggle contact request")
        return 'added' in res.text
    def get_village(self) -> str:
        if self._village is None:
            self.update_person()
        return self._village
    def get_age(self) -> int:
        if self._age is None:
            self.update_person()
        return self._age
    def get_name(self) -> str:
        if self.name is None:
            self.update_person()
        return self.name
    def get_id(self) -> str:
        return self._id
    def is_awake(self):
        if self._awake is None:
            self.update_person()
        return self._awake

    def get_village(self) -> str:
        if self._village is None:
            self.update_person()
        return self._village
    def has_consented(self) -> bool:
        if self._consented is None:
            self.update_person()
        return self._consented
    def get_task_results(self):
        if self._tasks is None:
            self.update_person()
        return self._tasks
    def do_task(self, task : Task):
        if task is None or type(task) != Task :
            raise Exception("Invalid task type")

        header ={'referer': f'{_BASE_URL}/islander.php?id={self._id}'}
        res = _session.get(
            f'{_BASE_URL}/task.php?id={self._id}&code={task.code()}', headers=header)
        if res.status_code != 200:
            raise Exception("Error with toggle contact request")
        if res.text == 'Not available':
            return None
        split_lines = res.text.splitlines()
        return {"start_time": float(split_lines[0]), "end_time": float(split_lines[1]), "category": split_lines[2], "number?": split_lines[3], "text": split_lines[4]}



    def update_person(self) -> None:
        island_raw = make_request(f'islander.php?id={self._id}')
        parsed = BeautifulSoup(island_raw, 'html.parser')


        self._awake = int(re.compile("var awake = (\\d+);").search(parsed.find('body').find('script').text).group(1)) == 1

        info_tab = parsed.find('div', id='t1')
        self.name = parsed.title.text
        rows = [list(row.children)[0] for row in info_tab.find('table').find_all('tr')]
        rows = rows[1:['id' in row.attrs for row in rows].index(True) - 1]
        self._age = int(re.compile('\\d+').findall(rows[0].text)[0])
        self._village = re.compile('Lives in (.*) \\d+').search(parsed.text).group(1)

        tasks = parsed.find('div', id='t2')
        script = tasks.find("script")
        consent_match = re.compile("var consented = (\\d+);").search(script.text)
        if consent_match is None:
            raise Exception("Could not parse script field")
        self._consented = int(consent_match.group(1)) == 1

        tasks = [task for task in tasks.find_all('div', class_='taskresult') if task.text.strip() != '']

        def parse_result(task):
            if task.text is None:
                return None

            if task.find('div', class_='taskresulttask') is None:
                #TODO: Support for tax records
                return TaskResult(task.find('div', class_='taskresulttd').text.strip(), "NYI", None)

            result = None
            if task.find('div', class_="taskresultresult") is not None:
                result = task.find('div', class_="taskresultresult").text
            return TaskResult(task.find('div', class_='taskresulttd').text.strip(), task.find('div', class_='taskresulttask').text.strip(), result)

        self._tasks = [parse_result(task) for task in tasks]


class PersonManager:
    def __init__(self):
        self._persons = {}
    def get_person(self, _id) -> Person:
        if _id in self._persons:
            return self._persons[_id]
        else:
            person = Person(_id)
            try:
                self._persons[_id] = person
                return person
            except:
                return None
    def register_person(self, person: Person):
        if person.get_id() not in self._persons:
            self._persons[person.get_id()] = person

manager = PersonManager()
__all__ = ['Person', 'manager']