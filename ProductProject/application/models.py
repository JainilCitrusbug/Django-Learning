from django.db import models
from application.signals import *
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["-id"]

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_description = models.CharField(max_length=500, blank=True, null=True)
    product_price = models.PositiveIntegerField(blank=True, null=True)
    product_image = models.ImageField(upload_to="images/", blank=True, null=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    soft_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-id"]

    def __str__(self):
        return self.product_name