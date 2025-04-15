from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(upload_to="category_img", black=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField()
    image = models.ImageField(upload_to="product_img", black=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.name
