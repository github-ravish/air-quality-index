#!/bin/sh

set -e

echo "Making database migrations"
python manage.py makemigrations user_account
echo "Database migrations complete"

echo "Applying migrations"
python manage.py migrate
echo "Applying migrations complete"

echo "Creating superuser account"
python manage.py createsuperuser_if_not_exists
echo "Superuser created"

echo "Collecting static files"
python manage.py collectstatic --noinput
echo "Staticfiles collected"

python manage.py runserver 0.0.0.0:8000

