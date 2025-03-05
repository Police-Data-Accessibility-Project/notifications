import os

import requests
import argparse

BASE_ROUTE = 'https://data-sources-v2.pdap.io/api'

def login(email: str, password: str) -> str:
    login_route = f'{BASE_ROUTE}/auth/login'
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
    call_notifications_endpoint(jwt_token)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', type=str, required=True)
    parser.add_argument('--password', type=str, required=True)
    args = parser.parse_args()

    email = args.email
    password = args.password

    send_notifications(email, password)