from rest_framework import serializers
from apps.restaurant.models import Restaurant


class RestaurantInputAndOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class RestaurantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            "address"
        )
