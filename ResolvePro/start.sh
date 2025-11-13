#!/bin/bash
python manage.py col
lectstatic --noinput
python manage.py migrate
gunicorn ResolvePro.wsgi:application --bind 0.0.0.0:$PORT