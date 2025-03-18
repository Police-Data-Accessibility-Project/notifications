import requests
import argparse

from helpers.miscellaneous_functions import get_base_route
from helpers.login import login


def call_notifications_endpoint(jwt_token: str):
    base_root = get_base_route()
    notifications_route = f'{base_root}/notifications'
    headers = {'Authorization': f'Bearer {jwt_token}'}
    response = requests.post(notifications_route, headers=headers)
    response.raise_for_status()
    print(response.json())

def send_notifications(email: str, password: str):
    jwt_token = login(email, password)
    call_notifications_endpoint(jwt_token)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', type=str, required=True)
    parser.add_argument('--password', type=str, required=True)
    args = parser.parse_args()

    email = args.email
    password = args.password

    send_notifications(email, password)