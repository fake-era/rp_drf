from typing import Tuple

from decouple import config

CELERY_BROKER_URL: str = config("CELERY_BROKER_URL", cast=str)
CELERY_RESULT_BACKEND: str = config("CELERY_RESULT_BACKEND", cast=str)
CELERY_TIMEZONE: str = config("CELERY_TIMEZONE", cast=str)
CELERY_ENABLE_UTC: bool = True
CELERY_ACCEPT_CONTENT: Tuple = ("application/json",)
CELERY_TASK_SERIALIZER: str = "json"
CELERY_RESULT_SERIALIZER: str = "json"
CELERY_TASK_ACKS_LATE: bool = True
