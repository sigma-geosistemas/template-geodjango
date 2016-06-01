from .base import *

SECRET_KEY = 'test'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
    }
}

INSTALLED_APPS += ('test_without_migrations',)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'