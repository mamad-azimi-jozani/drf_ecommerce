from django.shortcuts import get_object_or_404

from .models import *

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import ProductSerializer



@api_view()
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
