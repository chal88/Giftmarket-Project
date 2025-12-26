"""Giftmarket Shop Serializers"""
from rest_framework import serializers
from .models import Store
from .models import Product
from .models import Review


class StoreSerializer(serializers.ModelSerializer):
    """Serializer for Store model"""
    class Meta:
        """Meta class for StoreSerializer"""
        model = Store
        fields = '__all__'
        read_only_fields = ['vendor']


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model"""
    class Meta:
        """Meta class for ProductSerializer"""
        model = Product
        fields = '__all__'
        read_only_fields = ['store']


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review model"""
    class Meta:
        """Meta class for ReviewSerializer"""
        model = Review
        fields = '__all__'
        read_only_fields = ['buyer']
