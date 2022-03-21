from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=70)
    course = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class info(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    course = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_description = models.CharField(max_length=100, blank=True, null=True)
    product_price = models.IntegerField(blank=True, null=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.product_name