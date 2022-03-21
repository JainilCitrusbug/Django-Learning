from django.contrib import admin
from .models import ProductCategory, ProductDetails
# Register your models here.

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'product_category']

@admin.register(ProductDetails)
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ['product_category', 'product_name', 'product_price']