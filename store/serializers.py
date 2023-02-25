from rest_framework import serializers
from .models import *

from decimal import Decimal

class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField(
        method_name='get_price_with_tax'
    )
    collection = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'unit_price', 'price_with_tax', 'inventory', 'collection']


    def get_price_with_tax(self, obj: Product):
        return obj.unit_price * Decimal(1.1)