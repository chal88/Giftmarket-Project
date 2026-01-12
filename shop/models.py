"""Models for Giftmarket application including custom user model,
vendor profiles, products, orders, and reviews."""
from django.db import models
from django.contrib.auth.models import AbstractUser


# 1. Custom User Model
class User(AbstractUser):
    """Additional fields for user roles: buyer or vendor."""
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('vendor', 'Vendor'),
    )
    role = models.CharField(max_length=10, 
                            choices=ROLE_CHOICES, default='buyer')

    def is_vendor(self):
        """Check if the user is a vendor."""
        return self.role == 'vendor'

    def is_buyer(self):
        """Check if the user is a buyer."""
        return self.role == 'buyer'


# 2. Vendor Profile

class VendorProfile(models.Model):
    """Profile model for vendors."""
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='vendor_profile')
    store_name = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.store_name)

# 3. Store


class Store(models.Model):
    """Store owned by a vendor."""
    vendor = models.ForeignKey(
        VendorProfile,
        on_delete=models.CASCADE,
        related_name='stores'
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.vendor.store_name})"


# 3. Store Products

class Product(models.Model):
    """Product model for items sold in stores."""
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(
        upload_to='products/'
    )
    personalized_text = models.BooleanField(default=False)
    personalized_image = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} by {self.store.name}"

# 6. Cart Items


class CartItem(models.Model):
    """Items in a buyer's cart before checkout."""
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} ({self.user.username})"

    @property
    def price(self):
        """Return total price for this cart item."""
        return self.product.price * self.quantity


# 4. Orders and Order Items


class Order(models.Model):
    """Order model for purchases made by buyers."""
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    buyer = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='orders')
    total_price = models.DecimalField(max_digits=10, 
                                      decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id or 'unsaved'} by {self.buyer}"


class OrderItem(models.Model):
    """Order item model for individual products in an order."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    personalized_text = models.CharField(max_length=255, blank=True, null=True)
    personalized_image = models.ImageField(upload_to='personalized_images/',
                                           blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


# 5. Reviews
class Review(models.Model):
    """Review model for products."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField()
    # True if user purchased product
    verified_purchase = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Ensure a user can only leave one review per product."""
        unique_together = ('product', 'user')

    def __str__(self):
        status = "Verified" if self.verified_purchase else "Unverified"
        return f"{status} review by {self.user.username} for {self.product.name}"
