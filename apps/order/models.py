from django.db import models
from apps.common.models import BaseModel

from apps.common.enums.order_status import ORDER_STATUS


class Order(BaseModel):
    class Meta:
        verbose_name = "Order"

    pizza = models.ManyToManyField(
        "pizza.Pizza",
        related_name="Pizza"
    )
    details = models.CharField(max_length=64, blank=True)
    status = models.IntegerField(default=0, choices=ORDER_STATUS)
    task_id = models.CharField(max_length=64, blank=True)
