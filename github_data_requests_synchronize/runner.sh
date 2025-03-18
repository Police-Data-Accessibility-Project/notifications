#!/bin/bash

set -e

python3.11 github_data_requests_synchronize/synchronize.py --email $GITHUB_SYNCHRONIZE_APP_USER_PASSWORD --password $GITHUB_SYNCHRONIZE_APP_USER_PASSWORD