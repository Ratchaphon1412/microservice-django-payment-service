#!/bin/bash
poetry run python3 manage.py collectstatic --noinput
poetry run python3 manage.py makemigrations 
poetry run python3 manage.py migrate
poetry run gunicorn --bind 0.0.0.0:8023 djangopayment.wsgi
poetry run poetry run python3 manage.py ConsumerCommand --topic create_user --group auth 
