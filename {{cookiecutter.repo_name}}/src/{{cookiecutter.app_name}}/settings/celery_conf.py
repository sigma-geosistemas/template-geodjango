# coding: utf-8
from importlib import import_module
from .utils import generate_celery_schedule

# configuracao default redis
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# preencha esta informação para saber de quais apps iremos gerar um schedule
SCHEDULERS = []
if len(SCHEDULERS) > 0:
	CELERYBEAT_SCHEDULE = generate_celery_schedule(SCHEDULERS)
else:
	CELERYBEAT_SCHEDULE = {}}