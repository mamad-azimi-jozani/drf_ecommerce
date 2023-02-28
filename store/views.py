from django.shortcuts import get_object_or_404

from .models import *

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *

from .filters import ProductFilter



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['collection_id']
    filterset_class = ProductFilter

    def delete(self):
        pass

    # def perform_destroy(self, instance):
    #     if OrderItem.objects.filter(product_id=self.kwargs['pk']).count() > 0:
    #         raise serializers.ValidationError({'error': 'product can not be deleted'})
    #     instance.delete()


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('product')).all()
    serializer_class = CollectionSerializer


class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs.get('product_pk'))

    def perform_create(self, serializer):
        try:
            serializer.save(product_id=self.kwargs['product_pk'])
        except:
            raise serializers.ValidationError({'error': 'product is not present :|'})






