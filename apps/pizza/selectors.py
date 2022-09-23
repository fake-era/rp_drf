from typing import List, Optional

from apps.common.exception import NotFoundError
from apps.pizza.models import Pizza


def create_pizza(data) -> Optional[Pizza]:
    return Pizza.objects.create(data)


def get_pizza(id) -> Optional[Pizza]:
    fetched_pizza: Optional[Pizza] = Pizza.objects.filter(id=id).first()
    if fetched_pizza in None:
        raise NotFoundError()
    return fetched_pizza


def get_pizza_list() -> Optional[List[Pizza]]:
    fetched_pizza: Optional[Pizza] = Pizza.objects.all()
    if fetched_pizza in None:
        raise NotFoundError()
    return fetched_pizza


def update_pizza(id, new_pizza_data) -> Optional[Pizza]:
    fetched_pizza: Optional[Pizza] = get_pizza(id=id)
    updated_pizza: Optional[Pizza] = Pizza.objects.update(
        fetched_pizza,
        new_pizza_data
    )
    return updated_pizza


def delete_pizza(id):
    fetched_pizza: Optional[Pizza] = get_pizza(id=id)
    return fetched_pizza.delete()
