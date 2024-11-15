from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from shop.models import ElectronicDevices, FashionProducts, FurnitureProduct, Cart, CartItem
import re

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
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True}
        }

    def validate_confirm_password(self, value):
        password = self.initial_data.get('password')
        if value != password:
            raise serializers.ValidationError("Şifreler uyuşmuyor.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Bu email adresi zaten kullanılıyor.")
        return value

    def validate_password(self, value):
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("Şifre en az bir büyük harf içermelidir.")
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError("Şifre en az bir küçük harf içermelidir.")
        if not re.search(r'[0-9]', value):
            raise serializers.ValidationError("Şifre en az bir rakam içermelidir.")
        return value
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Geçersiz giriş bilgileri")
        return {'user': user}