from django.db import models

# Create your models here.

DEFAULT_IMAGE = 'img/product.png'

class Product(models.Model):
    title = models.CharField(max_length=50, null=False, unique=True)
    price = models.FloatField(null=False)
    discount_price = models.FloatField(null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=False)
    description = models.TextField(null=True)
    image = models.FileField(upload_to='img/', null=False)


    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    adress = models.CharField(max_length=200)
    contact = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    