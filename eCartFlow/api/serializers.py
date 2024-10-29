from rest_framework import serializers
from shop.models import ElectronicDevices, FashionProducts, FurnitureProduct

class ProductBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'price', 'brand', 'color', 'description', 'created_at', 'updated_at']

class ElectronicDeviceSerializer(ProductBaseSerializer):
    class Meta(ProductBaseSerializer.Meta):
        model = ElectronicDevices
        fields = ProductBaseSerializer.Meta.fields + ['model', 'storage_capacity']

class FashionProductSerializer(ProductBaseSerializer):
    class Meta(ProductBaseSerializer.Meta):
        model = FashionProducts
        fields = ProductBaseSerializer.Meta.fields + ['size', 'material']

class FurnitureProductSerializer(ProductBaseSerializer):
    class Meta(ProductBaseSerializer.Meta):
        model = FurnitureProduct
        fields = ProductBaseSerializer.Meta.fields + ['material', 'dimensions']
