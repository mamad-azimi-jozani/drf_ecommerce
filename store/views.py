from django.shortcuts import get_object_or_404

from .models import *

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from .serializers import *



class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        collection_id = self.request.query_params.get('collection_id')
        if collection_id is not None:
            queryset = queryset.filter(collection_id=collection_id)
        return queryset

    def perform_destroy(self, instance):
        if OrderItem.objects.filter(product_id=self.kwargs['pk']).count() > 0:
            raise serializers.ValidationError({'error': 'product can not be deleted'})
        instance.delete()


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






