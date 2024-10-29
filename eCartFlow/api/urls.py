from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartView, ElectronicDeviceViewSet, FashionProductViewSet, FurnitureProductViewSet, ProductFilterView

router = DefaultRouter()
router.register(r'electronic-devices', ElectronicDeviceViewSet)
router.register(r'fashion-products', FashionProductViewSet)
router.register(r'furniture-products', FurnitureProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cart/', CartView.as_view(), name='cart'),
    path('products/filter/', ProductFilterView.as_view(), name='product-filter'), 
]