#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn  pitblog.wsgi:application --bind 0.0.0.0:8000
