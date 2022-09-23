from typing import List, Optional

from apps.common.exception import NotFoundError
from apps.restaurant.models import Restaurant


def create_restaurant(data) -> Optional[Restaurant]:
    return Restaurant.objects.create(data)


def get_restaurant(id) -> Optional[Restaurant]:
    fetched_restaurant: Optional[Restaurant] = Restaurant.objects.filter(id=id).first()
    if fetched_restaurant in None:
        raise NotFoundError()
    return fetched_restaurant


def get_restaurant_list() -> Optional[List[Restaurant]]:
    fetched_restaurant: Optional[Restaurant] = Restaurant.objects.all()
    if fetched_restaurant in None:
        raise NotFoundError()
    return fetched_restaurant


def update_restaurant(id, new_restaurant_data) -> Optional[Restaurant]:
    fetched_restaurant: Optional[Restaurant] = get_restaurant(id=id)
    updated_restaurant: Optional[Restaurant] = Restaurant.objects.update(
        fetched_restaurant,
        new_restaurant_data
    )
    return updated_restaurant


def delete_restaurant(id):
    fetched_restaurant: Optional[Restaurant] = get_restaurant(id=id)
    return fetched_restaurant.delete()
