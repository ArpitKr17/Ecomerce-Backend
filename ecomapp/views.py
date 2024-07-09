from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from ecomapp.models import *


def products(request):

    products=Product.objects.prefetch_related('images').all()
    product_data=[]

    for product in products:
        product_data.append({
            'Title':product.title,
            'Description':product.description,
            'Created_at':product.created_at,
            'Updated_at':product.updated_at,
            'Images':[x.alt_text for x in product.images.all()]
        })
    return JsonResponse({'products': product_data})

def variants(request):

    variants=Variant.objects.all()
    variant_data=[]

    for variant in variants:
        variant_data.append({
            'Title':f"Product is {variant.product.title} and the variant is {variant.title} ",
            'Created_at':variant.created_at,
            'Updated_at':variant.updated_at,
            'Available_for_sale':variant.available_for_sale,
            'Price': variant.price,
            'Images': variant.image.alt_text,
        })
    return JsonResponse({'variants': variant_data})

def collections(request):

    collections=Collection.objects.all()
    collection_data=[]

    for collection in collections:
        collection_data.append({
            'Title': collection.title,
            'Published':collection.published,
            'Updated_at':collection.updated_at,
        })
    return JsonResponse({'collections': collection_data})

def products_in_collections(request, collection_ids):
    collection_ids_list = collection_ids.split(',')
    collections = Collection.objects.filter(id__in=collection_ids_list)
    products=Product.objects.prefetch_related('images', 'collections').filter(collections__in=collections).distinct()
    product_data=[]
    print(products)
    for product in products:
        product_data.append({
            'Title':product.title,
            'Description':product.description,
            'Created_at':product.created_at,
            'Updated_at':product.updated_at,
            'Images':[x.alt_text for x in product.images.all()]
        })
    return JsonResponse({'products': product_data})

def variants_in_collection(request,collection_id):
    collection = Collection.objects.get(id=collection_id)
    products=Product.objects.filter(collections=collection).distinct()
    variants=Variant.objects.select_related('image').filter(product__in=products)
    variant_data=[]

    for variant in variants:
        variant_data.append({
            'Title':f"Product is {variant.product.title} and the variant is {variant.title} ",
            'Created_at':variant.created_at,
            'Updated_at':variant.updated_at,
            'Available_for_sale':variant.available_for_sale,
            'Price': variant.price,
            'Images': variant.image.alt_text,
        })
    return JsonResponse({'variants': variant_data})

def variants_in_category(request,category_id):
    
    category = Category.objects.get(id=category_id)
    products=Product.objects.filter(category=category).distinct()
    variants=Variant.objects.select_related('image').filter(product__in=products)
    variant_data=[]

    for variant in variants:
        variant_data.append({
            'Title':f"Product is {variant.product.title} and the variant is {variant.title} ",
            'Created_at':variant.created_at,
            'Updated_at':variant.updated_at,
            'Available_for_sale':variant.available_for_sale,
            'Price': variant.price,
            'Images': variant.image.alt_text,
        })
    return JsonResponse({'variants': variant_data})
    
