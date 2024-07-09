from django.contrib import admin

from ecomapp.models import Product, Variant, Image, Collection, Category

# Register your models here.

admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(Image)
admin.site.register(Collection)
admin.site.register(Category)