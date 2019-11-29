from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mydjango.settings')

app = Celery('mydjango')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
