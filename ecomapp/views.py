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