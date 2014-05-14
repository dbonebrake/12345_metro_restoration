web: bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT metro_restoration/settings.py
worker: bin/python metro_restoration/manage.py celeryd -E -B --loglevel=INFO