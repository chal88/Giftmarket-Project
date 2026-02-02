"""Signals for the Giftmarket shop application."""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import VendorProfile, Product, Store
from .twitter_service import post_tweet

User = get_user_model()


@receiver(post_save, sender=User)
def create_vendor_profile(sender, instance, created, **kwargs):
    """
    Automatically create a VendorProfile when a vendor user is created.

    This ensures a vendor always has a profile and prevents duplicate
    OneToOneField errors by centralising creation logic in signals.
    """
    if created and getattr(instance, "role", None) == "vendor":
        VendorProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=Store)
def tweet_when_store_created(sender, instance, created, **kwargs):
    """
    Send a tweet whenever a Store is created
    (Web UI, API, admin, shell).
    """
    if not created:
        return

    tweet_text = f"🏪 A new store has opened!\n\n{instance.name}"

    try:
        post_tweet(text=tweet_text)
    except Exception:
        # Tweet failure must not prevent store creation
        pass


@receiver(post_save, sender=Product)
def tweet_when_product_created(sender, instance, created, **kwargs):
    """
    Send a tweet whenever a Product is created
    (Web UI, API, admin, shell).
    """
    if not created:
        return

    store = instance.store

    tweet_text = (
        f"🆕 New product added to {store.name}!\n\n"
        f"{instance.name}\n\n"
        f"{instance.description}"
    )

    image_url = instance.image.url if instance.image else None

    try:
        post_tweet(text=tweet_text, image_url=image_url)
    except Exception:
        # Tweet failure must not prevent product creation
        pass
