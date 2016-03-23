import os
import raven
from .base import *
from .utils import get_env_variable

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []

INSTALLED_APPS += ("raven.contrib.django.raven_compat",)

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