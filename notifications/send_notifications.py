import os

import requests

BASE_ROUTE = 'https://data-sources-v2.pdap.io/api'

def login(email: str, password: str) -> str:
    login_route = f'{BASE_ROUTE}/login'
    payload = {'email': email, 'password': password}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(login_route, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['access_token']

def call_notifications_endpoint(jwt_token: str):
    notifications_route = f'{BASE_ROUTE}/notifications'
    headers = {'Authorization': f'Bearer {jwt_token}'}
    response = requests.post(notifications_route, headers=headers)
    response.raise_for_status()
    print(response.json())

def send_notifications(email: str, password: str):
    jwt_token = login(email, password)
    try:
        call_notifications_endpoint(jwt_token)
    except requests.exceptions.HTTPError as e:
        print(f"Error with email {email} and password {password}")
        print(e)


if __name__ == '__main__':
    # Get values from environment
    email = os.environ['NOTIFICATIONS_APP_USER_EMAIL']
    password = os.environ['NOTIFICATIONS_APP_USER_PASSWORD']

    send_notifications(email, password)