from typing import List, Optional

from apps.common.exception import NotFoundError
from apps.order.models import Order


def create_order(data):
    return Order.objects.create(data)


def get_order(id) -> Optional[Order]:
    fetched_order: Optional[Order] = Order.objects.filter(id=id).first()
    if fetched_order in None:
        raise NotFoundError()
    return fetched_order


def get_order_list() -> Optional[List[Order]]:
    fetched_order: Optional[Order] = Order.objects.all()
    if fetched_order in None:
        raise NotFoundError()
    return fetched_order


def change_status_order(id, new_order_data) -> Optional[Order]:
    fetched_order: Optional[Order] = get_order(id=id)
    updated_order: Optional[Order] = Order.objects.update(
        fetched_order,
        new_order_data
    )
    return updated_order


def delete_order(id):
    fetched_order: Optional[Order] = get_order(id=id)
    return fetched_order.delete()
