import pytest

from django.urls import reverse

from .models import *

from .serializers import ProductSerializer

from rest_framework import status

@pytest.mark.django_db
def test_list_product(client):
    url = reverse('product:product-lists')
    response = client.get(url)

    products = Product.objects.all()
    expected_data = ProductSerializer(products, many=True)


    assert response.status_code == status.HTTP_200_OK
    assert expected_data.data == response.data


# @pytest.mark.django_db
# def test_detail_product(client, product: Product):
#     url = reverse('product:product-detail', kwargs={'pk': product.pk})
#     response = client.get(url)
#
#     product = Product.objects.get(pk=product.pk)
#     serializer = ProductSerializer(product)
#
#     assert response.status_code == 200
#     assert response.data == serializer.data

