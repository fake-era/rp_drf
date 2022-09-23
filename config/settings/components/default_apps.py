from typing import Tuple

from decouple import config

DEBUG: bool = config("DEBUG", default=True, cast=bool)

DJANGO_APPS: Tuple[str, ...] = (
    'django.contrib.sites',
    "django.contrib.admin",
    "django.contrib.staticfiles",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.auth",
)
SIDE_APPS: Tuple[str, ...] = (
    "corsheaders",
    "rest_framework",
)
DEBUG_APPS: Tuple[str, ...] = ("debug_toolbar",)

PROJECT_APPS: Tuple[str, ...] = (
    "apps.order.apps.OrderConfig",
    "apps.pizza.apps.PizzaConfig",
    "apps.taskapp.apps.TaskAppConfig",
    "apps.restaurant.apps.RestaurantConfig"
)
INSTALLED_APPS: Tuple[str, ...] = DJANGO_APPS + SIDE_APPS + PROJECT_APPS

if DEBUG:
    INSTALLED_APPS += DEBUG_APPS

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
