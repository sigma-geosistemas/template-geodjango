import os
import raven
from .base import *
from .utils import get_env_variable

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []

INSTALLED_APPS += ("raven.contrib.django.raven_compat",
                   "dbbackup",)

MIDDLEWARE_CLASSES = (
  'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
  'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
) + MIDDLEWARE_CLASSES

RAVEN_CONFIG = {
    'dsn': '__dsn__'
}

# removing the browsable API - comment this if you WANT the browsable API in production.
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ('rest_framework.renderers.JSONRenderer',)

SECRET_KEY = get_env_variable("SECRET_KEY")

# django dbbackup
token_fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dbtoken")
DBBACKUP_STORAGE = 'dbbackup.storage.dropbox_storage'
DBBACKUP_TOKENS_FILEPATH = token_fp
DBBACKUP_DROPBOX_APP_KEY = get_env_variable("DBBACKUP_DROP_APP_KEY")
DBBACKUP_DROPBOX_APP_SECRET = get_env_variable("DBBACKUP_DROPBOX_APP_SECRET")
HOSTNAME = ALLOWED_HOSTS[0]

EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = get_env_variable("MAILGUN_ACCESS_KEY")
MAILGUN_SERVER_NAME = get_env_variable("MAILGUN_SERVER_NAME")

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