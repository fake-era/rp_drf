from rest_framework import serializers

from apps.order.models import Order


class OrderInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "pizza",
            "details",
            "task_id"
        )


class OrderChangeStatusSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "status"
        )


class OrderOutputSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
