from unicodedata import category
from django.db import models

# Product(title, description, created_at, updated_at)
# Variant(title, created_at, updated_at, available_for_sale, price)
# Image(source, alt_text, updated_at)
# Collection(title, published, updated_at)
# Categories/subcategories (title, created_at, updated_at)

class Image(models.Model):
    source=models.TextField()
    alt_text=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now=True)

class Category(models.Model):
    title=models.CharField(max_length=100)
    subcategory = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ManyToManyField(Image)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)

class Variant(models.Model):
    title=models.CharField(max_length=100)
    available_for_sale=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    price=models.IntegerField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.OneToOneField(Image,on_delete=models.CASCADE)

class Collection(models.Model):
    title=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    product=models.ManyToManyField(Product)
