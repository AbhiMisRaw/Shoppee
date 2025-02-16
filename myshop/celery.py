from django.conf import settings
import os
from celery import Celery

# setuping up django-settings for `celery` program
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myshop.settings")

# Create Celery application instance
app = Celery("myshop", broker='amqp://guest:guest@localhost:5672//')

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()