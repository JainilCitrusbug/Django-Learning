
from application.models import *
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # username = serializers.CharField(max_length=100)
    # first_name = serializers.CharField(max_length=100)
    # last_name = serializers.CharField(max_length=100)
    # email = serializers.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','password']

    def create(self, validated_data):
        print('*************************Create*********************************')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        print('*************************Update*********************************')
        return super().update(instance, validated_data)

class CategorySerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id','category_name']

    def create(self, validated_data):
        print('*************************Create*********************************')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        print('*************************Update*********************************')
        return super().update(instance, validated_data)

class ProductSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    soft_delete = serializers.BooleanField(read_only=True)
    # product_name = serializers.CharField(max_length=100)
    # product_description = serializers.CharField(max_length=500)
    # product_price = serializers.IntegerField()
    # product_image = serializers.ImageField()
    # product_category = CategorySerializers()
    # user = UserSerializers()

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        print('*************************Create*********************************')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        print('*************************Update*********************************')
        return super().update(instance, validated_data)