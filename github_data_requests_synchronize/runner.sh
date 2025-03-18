#!/bin/bash

set -e

python3.11 -m github_data_requests_synchronize.synchronize --email $GITHUB_SYNCHRONIZE_APP_USER_EMAIL --password $GITHUB_SYNCHRONIZE_APP_USER_PASSWORD