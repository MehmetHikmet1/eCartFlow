from django.db import models

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
