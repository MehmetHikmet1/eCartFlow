from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LogoutView
from .views import CartView, ElectronicDeviceViewSet, FashionProductViewSet, FurnitureProductViewSet, ProductFilterView, UserRegisterView, UserLoginView, IndexView

router = DefaultRouter()
router.register(r'electronic-devices', ElectronicDeviceViewSet)
router.register(r'fashion-products', FashionProductViewSet)
router.register(r'furniture-products', FurnitureProductViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('', include(router.urls)),
    path('cart/', CartView.as_view(), name='cart'),
    path('products/filter/', ProductFilterView.as_view(), name='product-filter'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]