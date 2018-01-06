import json
from .models import Order
from .serializers import OrderSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from auth.permissions import IsSSOAuthenticated
from .custom_throttling import PerUserRateThrottle


class OrderList(APIView):
    permission_classes = (IsSSOAuthenticated,)
    throttle_classes = (PerUserRateThrottle,)

    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        order = {'item': json.dumps(request.data)}
        serializer = OrderSerializer(data=order)
        if serializer.is_valid():
            serializer.save(user_name=request.session.get('username'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
    permission_classes = (IsSSOAuthenticated,)
    throttle_classes = (PerUserRateThrottle,)

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        order_modified = {'item': json.dumps(request.data)}
        serializer = OrderSerializer(order, data=order_modified)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)