import os
from .utils import get_env_variable

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    # 3rd party apps
    'rest_framework',
    'rest_framework.auth',
    'rest_framework_gis',
    # our apps
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = '{{cookiecutter.app_name}}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
            # the below line is optional. we configure if you have an separate frontend
            # MVC app (such as react, angular, etc) that you'd like to include.
            {% if cookiecutter.js_frontend %}
            os.path.join(BASE_DIR, "..", "..", "..", "{{cookie_cutter.app_name}}-app"),
            {% endif %}
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '{{cookiecutter.app_name}}.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '{{cookiecutter.app_name}}',
        'USER': get_env_variable("PGUSER"),
        'PASSWORD': get_env_variable("PGPASS"),
        'HOST': "localhost",
        'PORT': "5432",
    }
}

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = (

)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_INTERMEDIARY = os.path.join(BASE_DIR, "..", "..", "..", "{{cookiecutter.app_name}}-static")
STATIC_ROOT = os.path.abspath(os.path.join(STATIC_INTERMEDIARY, "static"))
MEDIA_ROOT = os.path.abspath(os.path.join(STATIC_INTERMEDIARY, "media"))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'addresses': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    },
}

if len(sys.argv) > 1 and sys.argv[1] == 'test':
    logging.disable(logging.CRITICAL)

CELERY_TASK_ALWAYS_EAGER = True

MAINTENANCE_MODE_STATE_FILE_PATH = 'maintenance_mode_state.txt'

try:
    from .drf import *
except ImportError:
    pass