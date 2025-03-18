#!/bin/bash

set -e

python3.11 -m  notifications.send_notifications --email $NOTIFICATIONS_APP_USER_EMAIL --password $NOTIFICATIONS_APP_USER_PASSWORD