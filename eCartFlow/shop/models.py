from django.db import models
from django.conf import settings

class ProductBase(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 

class ElectronicDevices(ProductBase):
    model = models.CharField(max_length=100)
    storage_capacity = models.CharField(max_length=50)

class FashionProducts(ProductBase):
    size = models.CharField(max_length=10)
    material = models.CharField(max_length=100)

class FurnitureProduct(ProductBase):
    material = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product_type = models.CharField(max_length=50)
    product_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def get_product(self):
        if self.product_type == 'electronic':
            return ElectronicDevices.objects.get(id=self.product_id)
        elif self.product_type == 'fashion':
            return FashionProducts.objects.get(id=self.product_id)
        elif self.product_type == 'furniture':
            return FurnitureProduct.objects.get(id=self.product_id)
        return None