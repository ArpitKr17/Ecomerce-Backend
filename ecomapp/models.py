from django.db import models

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
    category=models.OneToOneField(Category,on_delete=models.CASCADE, null=True, blank=True, related_name='product')

    def __str__(self):
        return self.title

class Image(models.Model):
    source=models.TextField()
    alt_text=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now=True)
    product=models.ForeignKey(Product, related_name='images',on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.alt_text

class Variant(models.Model):
    title=models.CharField(max_length=100)
    available_for_sale=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    price=models.IntegerField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE, related_name='variants')
    image=models.ForeignKey(Image,on_delete=models.CASCADE, related_name='variants')

    def __str__(self):
        return self.title

class Collection(models.Model):
    title=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    products=models.ManyToManyField(Product, related_name='collections')
    published=models.BooleanField(default=True)

    def __str__(self):
        return self.title
