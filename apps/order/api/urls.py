from django.urls import path

from apps.order.api.views.order import (
    OrderListApi,
    OrderCreateApi,
    OrderDetailApi,
    OrderChangeStatusApi,
    OrderDeleteApi
)

urlpatterns = [
    path("create/", OrderCreateApi.as_view()),
    path("", OrderListApi.as_view()),
    path("<int:id>/", OrderDetailApi.as_view()),
    path("<int:id>/change_status/", OrderChangeStatusApi.as_view()),
    path("<int:id>/delete/", OrderDeleteApi.as_view()),
]
