from django.urls import path, include
from . import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('products', viewset=views.ProductViewSet)
router.register('collection', viewset=views.CollectionViewSet)



app_name = 'product'

urlpatterns = [
    # router for products and collections
    path('', include(router.urls))
]
