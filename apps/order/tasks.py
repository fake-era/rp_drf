from celery import shared_task

from apps.order.selectors import change_status_order

from random import randint


@shared_task
def start_order():
    duration = randint(2, 5)
    
