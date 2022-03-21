from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProductCategory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_category = models.CharField(max_length=100, primary_key=True)

class ProductDetails(models.Model):
    product_category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()