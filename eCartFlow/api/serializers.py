from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from shop.models import ElectronicDevices, FashionProducts, FurnitureProduct, Cart, CartItem

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

class CartItemSerializer(serializers.ModelSerializer):
    product_type = serializers.ChoiceField(choices=[('electronic', 'Electronic'), ('fashion', 'Fashion'), ('furniture', 'Furniture')])
    
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product_type', 'product_id', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Geçersiz giriş bilgileri")
        return {'user': user}