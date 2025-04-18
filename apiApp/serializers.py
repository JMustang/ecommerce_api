from rest_framework import serializers
from .models import Category, Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "slug", "image" "price"]


class CategorySerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        field = ["id", "name", "image", "products"]
