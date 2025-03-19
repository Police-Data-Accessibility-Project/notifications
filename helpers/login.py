import requests

from helpers.miscellaneous_functions import get_base_route


def login(email: str, password: str) -> str:
    base_route = get_base_route()
    login_route = f'{base_route}/auth/login'
    payload = {'email': email, 'password': password}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(login_route, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['access_token']
