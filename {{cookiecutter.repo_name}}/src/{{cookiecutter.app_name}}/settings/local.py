from .base import *

DEBUG = True

SECRET_KEY = 'local'

ALLOWED_HOSTS = []

INSTALLED_APPS += ('debug_toolbar',
                   'django_extensions', )
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.     PostGIS => django.contrib.gis.db.backends.postgis
        'NAME': "{{cookiecutter.app_name}}",
        'USER': get_env_variable("PGUSER"),
        'PASSWORD':  get_env_variable("PGPASS"),
        'HOST': 'localhost',
        'PORT': '5432',                       # Set to empty string for default.
    }
}
