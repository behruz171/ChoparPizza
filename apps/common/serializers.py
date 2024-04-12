from rest_framework import serializers
from .models import *


class ProductInfoSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name',)
    class Meta:
        model = ProductInfo
        fields = ['img','product_name', 'description', 'category']


class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name')
    img = serializers.CharField(source='product.img')
    description = serializers.CharField(source='product.description')
    category = serializers.CharField(source='product.category')

    class Meta:
        model = Product
        fields = ['product_name', 'img', 'description', 'price', 'category']


class CreateProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = ['img', 'product_name', 'description', 'category']


class CreateProduct(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'price', 'weight']


class UpdateProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = ['img', 'product_name', 'description', 'category']


class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'price', 'weight']


class KorzinkaListSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product.product_name')
    user = serializers.CharField(source='user.phone_number')
    class Meta:
        model = Korzinka
        fields = ['product_name', 'user']


class AddProductKorzinkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korzinka
        fields = ['product', 'user']


class UpdateProductKorzinkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korzinka
        fields = ['user', 'product']
    
