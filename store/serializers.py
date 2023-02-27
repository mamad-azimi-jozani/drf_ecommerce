from rest_framework import serializers
from .models import *

from decimal import Decimal

from django.db.models import Count



class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField(
        method_name='get_price_with_tax'
    )
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection']


    def get_price_with_tax(self, obj: Product):
        return obj.unit_price * Decimal(1.1)

    # def validate(self, data):
    #     if data['title'] == data['slug']:
    #         raise serializers.ValidationError('title and slug are the same!')
    #     return data


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'date', 'product']


