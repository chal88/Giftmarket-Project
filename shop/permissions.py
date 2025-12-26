"""Giftmarket Shop Permissions"""
from rest_framework.permissions import BasePermission


class IsVendor(BasePermission):
    """Custom permission to only allow vendors to access certain views."""
    def has_permission(self, request, view):
        """Check if the user is a vendor."""
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'vendor_profile')
        )


class IsVendorOwner(BasePermission):
    """Custom permission to only allow owners of a vendor profile to edit it."""
    def has_object_permission(self, request, view, obj):
        """Check if the user is the owner of the vendor profile."""
        return obj.vendor == request.user.vendor_profile
