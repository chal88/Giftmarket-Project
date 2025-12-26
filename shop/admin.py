"""module for registering admin models in the Giftmarket application."""
from django.contrib import admin
from .models import User, VendorProfile, Product, Order, OrderItem, Review

admin.site.register(User)
admin.site.register(VendorProfile)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
