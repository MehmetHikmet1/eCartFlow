from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ElectronicDeviceSerializer, FashionProductSerializer, FurnitureProductSerializer
from shop.models import ElectronicDevices, FashionProducts, FurnitureProduct

class ElectronicDeviceViewSet(viewsets.ModelViewSet):
    queryset = ElectronicDevices.objects.all()
    serializer_class = ElectronicDeviceSerializer
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs) 

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs) 

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs) 


class FashionProductViewSet(viewsets.ModelViewSet):
    queryset = FashionProducts.objects.all()
    serializer_class = FashionProductSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs) 

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs) 

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs) 

class FurnitureProductViewSet(viewsets.ModelViewSet):
    queryset = FurnitureProduct.objects.all()
    serializer_class = FurnitureProductSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs) 

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs) 

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs) 