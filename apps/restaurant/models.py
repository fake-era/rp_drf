from django.db import models


class Restaurant(models.Model):
    class Meta:
        verbose_name = "Restaurant"

    name = models.CharField(
        max_length=30
    )
    address = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.name
