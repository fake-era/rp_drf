from django.db import models


class Pizza(models.Model):
    class Meta:
        verbose_name = "Pizza"

    name = models.CharField(
        max_length=30
    )
    description = models.CharField(
        max_length=255
    )
    restaurant = models.ForeignKey(
        "restaurant.Restaurant",
        on_delete=models.CASCADE,
        related_name="Restaurant"
    )

    def __str__(self):
        return self.name
