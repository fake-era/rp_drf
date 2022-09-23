from django.urls import path

from apps.restaurant.api.views.restaurant import (
    RestaurantCreateApi,
    RestaurantListApi,
    RestaurantDetailApi,
    RestaurantUpdateApi,
    RestaurantDeleteApi
)

urlpatterns = [
    path("create/", RestaurantCreateApi.as_view()),
    path('', RestaurantListApi.as_view()),
    path('<int:id>/', RestaurantDetailApi.as_view()),
    path("<int:id>/update/", RestaurantUpdateApi.as_view()),
    path("<int:id>/delete/", RestaurantDeleteApi.as_view()),
]
