from shop.models import Category, Order, Product
from django.contrib import admin

# Register your models here.

admin.site.site_header = "E-commerce"
admin.site.site_title = "Ma commerce"
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)