from django.urls import path

from apps.pizza.api.views.pizza import (
    PizzaCreateApi,
    PizzaListApi,
    PizzaDetailApi,
    PizzaUpdateApi,
    PizzaDeleteApi
)

urlpattern = [
    path("create/", PizzaCreateApi.as_view()),
    path("", PizzaListApi.as_view()),
    path("<int:id>/", PizzaDetailApi.as_view()),
    path("<int:id>/update/", PizzaUpdateApi.as_view()),
    path("<int:id>/delete/", PizzaDeleteApi.as_view()),
]
