"""Giftmarket.shop.apps"""
from django.apps import AppConfig


class ShopConfig(AppConfig):
    """Configuration for the shop app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'

    def ready(self):
        # Import for side effects; suppress unused import warning
        _ = __import__('shop.signals')
