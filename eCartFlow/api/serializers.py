from rest_framework import serializers
from shop.models import ElectronicDevices, FashionProducts, FurnitureProduct


class ElectronicDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicDevices
        fields = '__all__'

class FashionProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionProducts
        fields = '__all__'

class FurnitureProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnitureProduct
        fields = '__all__'