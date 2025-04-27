from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItem, Category, Product
from .serializers import (
    CartItemSerializer,
    CartSerializer,
    CategoryDetailSerializer,
    CategoryListSerializer,
    ProductDetailSerializer,
    ProductListSerializer,
)


@api_view(["GET"])
def product_list(request):
    products = Product.objects.filter(featured=True)
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_detail(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"error": "❌ Product not found!"})


@api_view(["GET"])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def category_detail(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)
    except Category.DoesNotExist:
        return Response({"error": "❌ Category not found!"})


@api_view(["POST"])
def add_to_cart(request):
    cart_code = request.data.get("cart_code")
    product_id = request.data.get("product_id")

    cart, created = Cart.objects.get_or_create(cart_code=cart_code)
    product = Product.objects.get(id=product_id)

    cartitem, created = CartItem.objects.get_or_create(product=product, cart=cart)
    cartitem.quantity = 1
    cartitem.save()

    serializer = CartSerializer(cart)
    return Response(serializer.data)


@api_view(["PUT"])
def update_cartitem_quantity(request):
    cartitem_id = request.data.get("item_id")
    quantity = request.data.get("quantity")

    try:
        cartitem = CartItem.objects.get(id=cartitem_id)
        cartitem.quantity = quantity
        cartitem.save()

        serializer = CartItemSerializer(cartitem)
        return Response(
            {"data": serializer.data, "message": "Cart item updated successfully!"}
        )
    except CartItem.DoesNotExist:
        return Response({"error": "❌ Cart item not found!"})
