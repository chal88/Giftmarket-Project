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


# -----------------------------
# VENDOR: CREATE STORE
# -----------------------------
class StoreCreateView(generics.CreateAPIView):
    """Vendor creates a new store."""
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated, IsVendor]

    def perform_create(self, serializer):
        """Save the store with the current vendor as the owner."""
        serializer.save(vendor=self.request.user.vendor_profile)


# -----------------------------
# VENDOR: CREATE PRODUCT
# -----------------------------
class ProductCreateView(generics.CreateAPIView):
    """Vendor adds a product to their store."""
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsVendor]

    def perform_create(self, serializer):
        """Save the product under the specified store owned by the vendor."""
        store = get_object_or_404(
            Store,
            id=self.kwargs['store_id'],
            vendor=self.request.user.vendor_profile
        )
        serializer.save(store=store)


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
