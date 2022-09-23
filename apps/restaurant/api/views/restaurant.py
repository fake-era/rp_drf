from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.restaurant.serializers import (
    RestaurantInputAndOutputSerializer,
    RestaurantUpdateSerializer
)

from apps.restaurant.selectors import (
    create_restaurant,
    get_restaurant,
    get_restaurant_list,
    update_restaurant,
    delete_restaurant
)


class RestaurantListApi(APIView):
    def get(self, request, *args, **kwargs):
        restaurant = get_restaurant_list()
        serializer = RestaurantInputAndOutputSerializer(restaurant, many=True)
        return Response(
            serializer.data
        )


class RestaurantDetailApi(APIView):
    def get(self, request, restaurant_id):
        restaurant = get_restaurant(id=restaurant_id)
        serializer = RestaurantInputAndOutputSerializer(restaurant)
        return Response(
            serializer.data
        )


class RestaurantCreateApi(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RestaurantInputAndOutputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        restaurant = create_restaurant(serializer.data)
        return Response(
            RestaurantInputAndOutputSerializer(restaurant).data
        )


class RestaurantUpdateApi(APIView):
    def post(self, request, restaurant_id):
        serializer = RestaurantUpdateSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        updated_restaurant = update_restaurant(id=restaurant_id, **serializer.validated_data)
        return Response(
            RestaurantInputAndOutputSerializer(updated_restaurant).data
        )


class RestaurantDeleteApi(APIView):
    def post(self, request, restaurant_id):
        delete_restaurant(restaurant_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
