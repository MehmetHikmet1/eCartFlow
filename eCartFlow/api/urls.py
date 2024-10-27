from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElectronicDeviceViewSet, FashionProductViewSet, FurnitureProductViewSet

router = DefaultRouter()
router.register(r'electronic-devices', ElectronicDeviceViewSet)
router.register(r'fashion-products', FashionProductViewSet)
router.register(r'furniture-products', FurnitureProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]