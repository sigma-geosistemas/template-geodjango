from .base import *

SECRET_KEY = 'test'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.     PostGIS => django.contrib.gis.db.backends.postgis
        'NAME': get_env_variable("PGDATABASE"),                       # Or path to database file if using sqlite3.
        'USER': get_env_variable("PGUSER"),
        'PASSWORD':  get_env_variable("PGPASS"),
        'HOST': get_env_variable('DBHOST'),
        'PORT': '5432',                       # Set to empty string for default.
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'