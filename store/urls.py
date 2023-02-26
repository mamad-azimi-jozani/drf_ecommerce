from django.urls import path
from .views import *


app_name = 'product'

urlpatterns = [
    # products endpoint => /store/products/
    path('products/', product_list, name='product-lists'),
    path('products/<int:id>/', product_detail, name='product-detail'),

    # collection endpoint => /store/collections/
    path('collections/', collection_list, name='collection-list'),
    path('collections/<int:id>/', collection_detail, name='collection-detail'),


]
