from django.urls import path, include

from . import views


from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register('products', viewset=views.ProductViewSet, basename='products')
router.register('collection', viewset=views.CollectionViewSet)

product_router = routers.NestedSimpleRouter(router, r'products', lookup='product')
product_router.register(r'reviews', viewset=views.ReviewViewSet, basename='product-reviews')

# router = SimpleRouter()




app_name = 'product'

urlpatterns = router.urls + product_router.urls
