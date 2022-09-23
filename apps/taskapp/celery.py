import os

from celery import Celery
from django.conf import settings

if not settings.configured:
    os.environ.setdefault(
        "DAJNGO_SETTINGS_MODULE", "configs.settings"
    )

app = Celery("app")
app.config_from_object("django.conf.settings")
app.autodiscover_tasks()

app.conf.timezone = "Asia/Almaty"

app.conf.worker_max_tasks_per_child = 100
