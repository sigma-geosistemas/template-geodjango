from .base import *

INSTALLED_APPS += ('debug_toolbar',
                   'django_extensions', )
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'