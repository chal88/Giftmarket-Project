"""Giftmarket Shop API Views"""

from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import Store, Product, Review
from .serializers import (
    StoreSerializer,
    ProductSerializer,
    ReviewSerializer
)
from .permissions import IsVendor
from .twitter_service import post_tweet


# -----------------------------
# VENDOR: CREATE STORE
# -----------------------------
class StoreCreateView(generics.CreateAPIView):
    """Vendor creates a new store."""
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated, IsVendor]

    def perform_create(self, serializer):
        """Save the store and post a tweet."""
        store = serializer.save(
            vendor=self.request.user.vendor_profile
            )

        # Build tweet text
        tweet_text = (
            f"🛍️ New store launched on Giftmarket!\n\n"
            f"{store.name}\n\n"
            f"{store.description}"
            )

        # Optional image (logo)
        image_url = store.logo.url if store.logo else None

        # Post tweet
        post_tweet(text=tweet_text, image_url=image_url)


# -----------------------------
# VENDOR: CREATE PRODUCT
# -----------------------------


class ProductCreateView(generics.CreateAPIView):
    """Vendor adds a product to their store."""
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsVendor]

    def perform_create(self, serializer):
        """Save the product and post a tweet."""
        store = get_object_or_404(
            Store,
            id=self.kwargs['store_id'],
            vendor=self.request.user.vendor_profile
        )

        product = serializer.save(store=store)

        # Build tweet text
        tweet_text = (
            f"🆕 New product added to {store.name}!\n\n"
            f"{product.name}\n\n"
            f"{product.description}"
        )

        # Optional image
        image_url = product.image.url if product.image else None

        # Post tweet
        post_tweet(text=tweet_text, image_url=image_url)


# -----------------------------
# VENDOR: VIEW REVIEWS
# -----------------------------
class VendorReviewListView(generics.ListAPIView):
    """Vendor retrieves reviews for their products."""
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsVendor]

    def get_queryset(self):
        """ Get reviews for products owned by the vendor. """
        return Review.objects.filter(
            product__store__vendor=self.request.user.vendor_profile
        )


# -----------------------------
# VENDOR: VIEW OWN STORES
# -----------------------------
class VendorStoreListView(generics.ListAPIView):
    """Vendor retrieves their stores."""
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated, IsVendor]

    def get_queryset(self):
        """ Get stores owned by the vendor. """
        return Store.objects.filter(
            vendor=self.request.user.vendor_profile
        )


# -----------------------------
# PUBLIC: LIST ALL STORES
# -----------------------------
class StoreListView(generics.ListAPIView):
    """Public endpoint: list all stores."""
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.AllowAny]


# -----------------------------
# PUBLIC: LIST PRODUCTS IN STORE
# -----------------------------
class StoreProductListView(generics.ListAPIView):
    """Public endpoint: list products in a store."""
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """"" Get products for the specified store. """
        return Product.objects.filter(
            store_id=self.kwargs['store_id']
        )


class PublicVendorStoreListView(generics.ListAPIView):
    """
    Public API view:
    List all stores for a specific vendor.
    """
    serializer_class = StoreSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """ Get stores for the specified vendor. """
        return Store.objects.filter(
            vendor_id=self.kwargs['vendor_id']
        )
