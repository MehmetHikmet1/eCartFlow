from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ElectronicDeviceSerializer, FashionProductSerializer, FurnitureProductSerializer, CartSerializer, CartItemSerializer
from shop.models import ElectronicDevices, FashionProducts, FurnitureProduct, Cart, CartItem
from django.db.models import Q, F
from django.db import transaction

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
    
class ProductFilterView(APIView):
    def get(self, request):
        product_type = request.GET.get("product_type")
        query = Q()

        if 'brand' in request.GET:
            query &= Q(brand=request.GET['brand'])
        if 'min_price' in request.GET:
            query &= Q(price__gte=request.GET['min_price'])
        if 'max_price' in request.GET:
            query &= Q(price__lte=request.GET['max_price'])

        if product_type == "electronics":
            products = ElectronicDevices.objects.filter(query)
            serializer = ElectronicDeviceSerializer(products, many=True)
        elif product_type == "fashion":
            products = FashionProducts.objects.filter(query)
            serializer = FashionProductSerializer(products, many=True)
        elif product_type == "furniture":
            products = FurnitureProduct.objects.filter(query)
            serializer = FurnitureProductSerializer(products, many=True)
        else:
            return Response({"error": "Invalid product type"}, status=400)

        return Response(serializer.data)
    
class CartView(APIView):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @transaction.atomic
    def post(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartItemSerializer(data=request.data)
        
        if serializer.is_valid():
            product_type = serializer.validated_data['product_type']
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']

            cart_item, item_created = CartItem.objects.select_for_update().get_or_create(
                cart=cart,
                product_type=product_type,
                product_id=product_id,
                defaults={'quantity': quantity}
            )

            if not item_created:
                cart_item.quantity = F('quantity') + quantity
                cart_item.save()

            return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)