from django.urls import path
from .views import *


app_name = 'product'

urlpatterns = [
    path('products/', product_list, name='product-lists'),
    path('products/<int:id>/', product_detail, name='product-detail')
]
