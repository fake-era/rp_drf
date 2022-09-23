import uuid

from django.db import models


class UUIDModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True,
        editable=False
    )
