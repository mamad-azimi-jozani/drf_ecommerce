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
        fields = ['id', 'name', 'description', 'date']

    # def create(self, validated_data):
    #     product_id = self.context['product_id']
    #     return Review.objects.create(product_id=product_id, **validated_data)


class CustomProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']


class CartItemSerializer(serializers.ModelSerializer):
    product = CustomProductSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'total_price']

    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.unit_price



class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    id = serializers.UUIDField(read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']

    def get_total_price(self, cart: Cart):
        return sum([i.quantity * i.product.unit_price for i in cart.items.all()])





