from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.pizza.serializers import (
    PizzaInputAndOutputSerializer,
    PizzaUpdateSerializer
)

from apps.pizza.selectors import (
    create_pizza,
    get_pizza,
    get_pizza_list,
    update_pizza,
    delete_pizza
)


class PizzaListApi(APIView):
    def get(self, request, *args, **kwargs):
        pizza = get_pizza_list()
        serializer = PizzaInputAndOutputSerializer(pizza, many=True)
        return Response(
            serializer.data
        )


class PizzaDetailApi(APIView):
    def get(self, request, pizza_id):
        pizza = get_pizza(id=pizza_id)
        serializer = PizzaInputAndOutputSerializer(pizza)
        return Response(
            serializer.data
        )


class PizzaCreateApi(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PizzaInputAndOutputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pizza = create_pizza(serializer.data)
        return Response(
            PizzaInputAndOutputSerializer(pizza).data
        )


class PizzaUpdateApi(APIView):
    def post(self, request, pizza_id):
        serializer = PizzaUpdateSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        updated_pizza = update_pizza(id=pizza_id, **serializer.validated_data)
        return Response(
            PizzaInputAndOutputSerializer(updated_pizza).data
        )


class PizzaDeleteApi(APIView):
    def post(self, request, pizza_id):
        delete_pizza(pizza_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
