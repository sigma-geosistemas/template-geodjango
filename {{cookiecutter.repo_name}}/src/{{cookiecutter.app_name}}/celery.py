# coding: utf-8
"""Configuração inicial do Celery"""
import os
from __future__ import absolute_import
from celery import Celery
from settings.utils import get_env_variable

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{0}'.format(get_env_variable('DJANGO_SETTINGS_MODULE')))

from django.conf import settings

app = Celery('{{cookiecutter.app_name}}')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
