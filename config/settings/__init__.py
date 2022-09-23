from os import environ

import django_stubs_ext
from split_settings.tools import include

django_stubs_ext.monkeypatch()

environ.setdefault("DJANGO_ENV", "development")
_ENV = environ["DJANGO_ENV"]

_base_settings = (
    "components/common.py",
    "components/default_apps.py",
    "components/default_middleware.py",
    "components/rest_framework_settings.py",
)

include(*_base_settings)
