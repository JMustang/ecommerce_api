from django.contrib import admin
from .models import CustomUser, Product
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin:
    list_display = ("username", "email", "first_name", "last_name")


admin.site.register(CustomUser, UserAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "featured")


admin.site.register(ProductAdmin, Product)
