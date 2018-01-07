from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.JSONField(binary=True)

    class Meta:
        model = Order
        fields = ('id', 'user_name', 'item', 'checkout_date')

