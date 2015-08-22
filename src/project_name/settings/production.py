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