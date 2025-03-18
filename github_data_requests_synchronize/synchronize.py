import argparse

import requests

from helpers.miscellaneous_functions import get_base_route
from helpers.login import login


def synchronize(email: str, password: str):
    base_route = get_base_route()
    access_token = login(
        email=email,
        password=password
    )
    synchronize_route = f'{base_route}/github/data-requests/synchronize'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.post(synchronize_route, headers=headers)
    response.raise_for_status()
    print(response.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', type=str, required=True)
    parser.add_argument('--password', type=str, required=True)
    args = parser.parse_args()

    email = args.email
    password = args.password

    synchronize(email, password)