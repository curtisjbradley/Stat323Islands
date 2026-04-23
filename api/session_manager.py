import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')
_BASE_URL= 'https://islands.smp.uq.edu.au'

_session = requests.sessions.Session()

_login_url = f'{_BASE_URL}/login.php'
_r = _session.post(_login_url, data={'email': os.getenv('login'), 'word': os.getenv('password'), 'Sign In': 'Sign In'})

if _r.url == _login_url:
    raise Exception('Error With Authentication')

def make_request(page):
    res = _session.get(f'{_BASE_URL}/{page}')
    if res.status_code != 200:
        raise Exception(f'Error with fetching the desired page. Status code: {res.status_code} Reason: {res.reason}')
    res.encoding = "utf-8"
    return res.text

__all__ = ['make_request']