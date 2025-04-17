from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'image' 'price']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = ['id', 'name', 'image']