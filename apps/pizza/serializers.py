from rest_framework import serializers
from apps.pizza.models import Pizza


class PizzaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = (
            "description"
        )


class PizzaInputAndOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = "__all__"
