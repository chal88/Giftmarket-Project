"""Signals for the Giftmarket shop application."""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, VendorProfile


@receiver(post_save, sender=User)
def create_vendor_profile(sender, instance, created, **kwargs):
    """
    Automatically create a VendorProfile when a vendor user is created.
    Prevents API crashes when accessing vendor stores.
    """
    if created and instance.role == 'vendor':
        VendorProfile.objects.get_or_create(
            user=instance,
            defaults={
                'store_name': f"{instance.username}'s Store"
            }
        )
