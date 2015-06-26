from .base import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []

# removing the browsable API - comment this if you WANT the browsable API in production.
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ('rest_framework.renderers.JSONRenderer',)