from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.products, name="products"),
    path("variants/", views.variants, name="variants"),
    path("collections/", views.collections, name="collections"),
    path("products_in_collections/<str:collection_ids>/", views.products_in_collections, name="products_in_collections"),
    path("variants_in_collection/<str:collection_id>/", views.variants_in_collection, name="variants_in_collection"),
    path("variants_in_category/<str:category_id>/", views.variants_in_category, name="variants_in_category")
]