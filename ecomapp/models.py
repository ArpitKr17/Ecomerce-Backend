from unicodedata import category
from django.db import models

class Image(models.Model):
    source=models.TextField()
    alt_text=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.alt_text

class Category(models.Model):
    title=models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    images=models.ManyToManyField(Image, related_name='products', null=True, blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Variant(models.Model):
    title=models.CharField(max_length=100)
    available_for_sale=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    price=models.IntegerField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ForeignKey(Image,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Collection(models.Model):
    title=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    product=models.ManyToManyField(Product)

    def __str__(self):
        return self.title
