import os
from .base import *
from .utils import get_env_variable

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ["{{cookiecutter.app_name}}.sigmageosistemas.com.br", ]

INSTALLED_APPS += ("opbeat.contrib.django",
                   "dbbackup",)

# removing the browsable API - comment this if you WANT the browsable API in production.
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ('rest_framework.renderers.JSONRenderer',)

SECRET_KEY = get_env_variable("SECRET_KEY")

OPBEAT = {
    'ORGANIZATION_ID': get_env_variable('OPBEAT_ORG_ID'),
    'APP_ID': get_env_variable('OPBEAT_APP_ID'),
    'SECRET_TOKEN': get_env_variable('OPBEAT_SECRET_TOKEN')
}
CELERY_BROKER_URL = 'redis://{0}:{1}/{2}'.format(get_env_variable("REDIS_HOST"),
                                                 get_env_variable("REDIS_PORT"),
                                                 get_env_variable("REDIS_DB"))
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

# django dbbackup
DBBACKUP_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DBBACKUP_STORAGE_OPTIONS = {
    'oauth2_access_token': get_env_variable('DBBACKUP_OAUTH2_TOKEN')
}
HOSTNAME = ALLOWED_HOSTS[0]

EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = get_env_variable("MAILGUN_ACCESS_KEY")
MAILGUN_SERVER_NAME = get_env_variable("MAILGUN_SERVER_NAME")

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': get_env_variable("PGDATABASE"),
        'USER': get_env_variable("PGUSER"),
        'PASSWORD':  get_env_variable("PGPASS"),
        'HOST': get_env_variable('DBHOST'),
        'PORT': '5432',
    }
}
