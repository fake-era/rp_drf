from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.order import tasks

from apps.order.serializaers import (
    OrderInputSerializer,
    OrderOutputSerilizer,
    OrderChangeStatusSerilizer
)

from apps.order.selectors import (
    create_order,
    get_order,
    get_order_list,
    change_status_order,
    delete_order
)


class OrderCreateApi(APIView):
    def post(self, request):
        serializer = OrderInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # task = tasks.start_order()
        order = create_order(serializer.data)
        return Response(
            OrderOutputSerilizer(order).data
        )


class OrderChangeStatusApi(APIView):
    def post(self, request, order_id):
        serializer = OrderChangeStatusSerilizer(request.data)
        serializer.is_valid(raise_exception=True)
        updated_order = change_status_order(id=order_id, **serializer.validated_data)
        return Response(
            OrderOutputSerilizer(updated_order).data
        )


class OrderListApi(APIView):
    def get(self, request):
        order = get_order_list()
        serializer = OrderOutputSerilizer(order, many=True)
        return Response(
            serializer.data
        )


class OrderDetailApi(APIView):
    def get(self, request, order_id):
        order = get_order(id=order_id)
        serializer = OrderOutputSerilizer(order)
        return Response(
            serializer.data
        )


class OrderDeleteApi(APIView):
    def post(self, request, order_id):
        delete_order(order_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
