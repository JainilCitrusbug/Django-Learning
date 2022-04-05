
from application.models import *
from rest_framework import serializers

class Userserializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)

class ProductSerializers(serializers.ModelSerializer):
    # product_name = serializers.CharField(max_length=100)
    # product_description = serializers.CharField(max_length=500)
    # product_price = serializers.IntegerField()
    # product_image = serializers.ImageField()
    # product_category = serializers.CharField(max_length=100)
    # user = Userserializers()
    # soft_delete = serializers.BooleanField()

    class Meta:
        model = Product
        # fields = ['product_name','product_description','product_price','product_image','product_category','user','soft_delete']
        fields = '__all__'

    def create(self, validated_data):
        print('*************************Create*********************************')
        new_product = Product.objects.create(**validated_data)
        return new_product

    def update(self, instance, validated_data):
        print('*************************Update*********************************')
        return super().update(instance, validated_data)