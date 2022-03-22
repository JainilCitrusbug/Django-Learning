from django.contrib import admin
from .models import student, info, Category, Product
# Register your models here.

@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'roll', 'name', 'course']

@admin.register(info)
class InfoData(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'number' ,'course']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_description', 'product_price', 'product_category']

