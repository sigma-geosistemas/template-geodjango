from .base import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []

# removing the browsable API
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ('rest_framework.renderers.JSONRenderer',)