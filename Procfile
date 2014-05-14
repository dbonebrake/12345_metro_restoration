web: gunicorn --workers=4 --bind=0.0.0.0:$PORT metro-restoration/settings.py
worker: python metro-restoration/manage.py celeryd -E -B --loglevel=INFO