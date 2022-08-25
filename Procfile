web: gunicorn setup.wsgi:application --log-file - --log-level debug
make requirements
python manage.py collectstatic --noinput
manage.py migrate