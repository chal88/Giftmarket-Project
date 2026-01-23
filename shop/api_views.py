"""Giftmarket Shop API Views"""

from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Store, Product, Review
from .serializers import (
    StoreSerializer,
    ProductSerializer,
    ReviewSerializer
)
from .permissions import IsVendor
from .twitter_service import post_tweet
from .models import VendorProfile
from rest_framework import generics, permissions
from .models import Store, Product, Review

# -----------------------------
# VENDOR: CREATE STORE
# -----------------------------


class StoreCreateView(generics.CreateAPIView):
    """Vendor creates a new store."""
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated, IsVendor]

    def perform_create(self, serializer):
        """
        Save the store safely for the logged-in vendor.
        Automatically creates a VendorProfile if missing.
        """

        # ✅ Safely get or create VendorProfile
        vendor_profile, created = VendorProfile.objects.get_or_create(
            user=self.request.user,
            defaults={'store_name': f"{self.request.user.username}'s Store"}
        )

        # ✅ Save the store linked to this vendor
        serializer.save(vendor=vendor_profile)


# -----------------------------
# VENDOR: CREATE PRODUCT
# -----------------------------


class ProductCreateView(generics.CreateAPIView):
    """Vendor adds a product to their store."""
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsVendor]

    def perform_create(self, serializer):
        """Save the product safely and post a tweet."""

        # ✅ Safely get or create VendorProfile
        vendor_profile, _ = getattr(self.request.user, 'vendor_profile', None), None
        if vendor_profile is None:
            from .models import VendorProfile
            vendor_profile, _ = VendorProfile.objects.get_or_create(
                user=self.request.user,
                defaults={'store_name': f"{self.request.user.username}'s Store"}
            )

        # ✅ Safely get store for this vendor
        store = get_object_or_404(
            Store,
            id=self.kwargs.get('store_id'),
            vendor=vendor_profile
        )

        # ✅ Save product linked to this store
        product = serializer.save(store=store)

        # ✅ Build tweet text
        tweet_text = (
            f"🆕 New product added to {store.name}!\n\n"
            f"{product.name}\n\n"
            f"{product.description}"
        )

        # ✅ Optional image URL (still supported by twitter_service)
        image_url = product.image.url if product.image else None

        # ✅ Post tweet safely (mentor requirement)
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
    """Vendor retrieves their own stores."""
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ Get stores owned by the authenticated vendor. """
        return Store.objects.filter(
            vendor__user=self.request.user
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
