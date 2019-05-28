#!/usr/bin/env bash
exec gunicorn --env DJANGO_SETTINGS_MODULE=TahrirBackend.settings TahrirBackend.wsgi \
    --name tahrir-gunicorn \
    --bind 0.0.0.0:5555 \
    --workers 3 \
    --timeout 10 \
    --log-level=info \
    --graceful-timeout 15 \
    --reload