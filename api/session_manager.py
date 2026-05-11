"""
Session manager for the Islands API.

Handles authentication and provides make_request() for all HTTP GET calls
to the Islands site. The session is authenticated once at import time using
credentials from the .env file.
"""
import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')

_BASE_URL = 'https://islands.smp.uq.edu.au'
_session = requests.sessions.Session()

# Authenticate immediately; raise if credentials are wrong
_login_url = f'{_BASE_URL}/login.php'
_r = _session.post(
    _login_url,
    data={'email': os.getenv('login'), 'word': os.getenv('password'), 'Sign In': 'Sign In'},
)
if _r.url == _login_url:
    raise Exception('Authentication failed: check login/password in .env')


def make_request(page: str) -> str:
    """
    Perform an authenticated GET request to *page* on the Islands site.

    Returns the response body as a UTF-8 string.
    Raises an Exception if the server returns a non-200 status code.
    """
    res = _session.get(f'{_BASE_URL}/{page.lstrip("/")}')
    if res.status_code != 200:
        raise Exception(
            f'Error fetching page "{page}". '
            f'Status: {res.status_code} Reason: {res.reason}'
        )
    res.encoding = 'utf-8'
    return res.text


__all__ = ['make_request']
