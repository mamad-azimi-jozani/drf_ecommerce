from django.urls import path
from .views import *


app_name = 'product'

urlpatterns = [
    # products endpoint => /store/products/
    path('products/', ProductList.as_view(), name='product-lists'),
    path('products/<int:id>/', ProductDetail.as_view(), name='product-detail'),

    # collection endpoint => /store/collections/
    path('collections/', CollectionList.as_view(), name='collection-list'),
    path('collections/<int:id>/', collection_detail, name='collection-detail'),


]
