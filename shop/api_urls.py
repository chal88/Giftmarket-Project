"""Giftmarket Shop API URLs"""

from django.urls import path
from . import api_views

urlpatterns = [

    # -----------------------------
    # VENDOR (AUTHENTICATED)
    # -----------------------------
    path(
        'vendor/stores/',
        api_views.StoreCreateView.as_view(),
        name='api_vendor_create_store'
    ),
    path(
        'vendor/stores/<int:store_id>/products/',
        api_views.ProductCreateView.as_view(),
        name='api_vendor_create_product'
    ),
    path(
        'vendor/reviews/',
        api_views.VendorReviewListView.as_view(),
        name='api_vendor_reviews'
    ),
    path(
        'vendor/my-stores/',
        api_views.VendorStoreListView.as_view(),
        name='api_vendor_store_list'
    ),

    # -----------------------------
    # PUBLIC (READ-ONLY)
    # -----------------------------
    path(
        'stores/',
        api_views.StoreListView.as_view(),
        name='api_store_list'
    ),
    path(
        'vendors/<int:vendor_id>/stores/',
        api_views.PublicVendorStoreListView.as_view(),
        name='api_vendor_store_public'
    ),
    path(
        'stores/<int:store_id>/products/',
        api_views.StoreProductListView.as_view(),
        name='api_store_products'
    ),
]
