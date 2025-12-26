"""Forms for the Giftmarket application, including user registration,
product management, and order handling."""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, VendorProfile, Product, OrderItem

# -----------------------------
# Vendor Signup Form
# -----------------------------


class VendorSignupForm(UserCreationForm):
    """Form for vendor registration, extending the default user creation form."""
    store_name = forms.CharField(max_length=255, required=True)

    class Meta:
        """Meta class for VendorSignupForm."""
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # role set automatically

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'vendor'
        if commit:
            user.save()
            VendorProfile.objects.create(
                user=user,
                store_name=self.cleaned_data['store_name']
            )
        return user

# -----------------------------
# Buyer Signup Form
# -----------------------------


class BuyerSignupForm(UserCreationForm):
    """Form for buyer registration."""
    class Meta:
        """Meta class for BuyerSignupForm."""
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # role set automatically

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'buyer'
        if commit:
            user.save()
        return user

# -----------------------------
# Product Form
# -----------------------------


class ProductForm(forms.ModelForm):
    """Form for adding and editing products in the marketplace."""
    class Meta:
        """Meta class for ProductForm."""
        model = Product
        exclude = ['store']  # store is set in the view


class ProductUpdateForm(forms.ModelForm):
    """Form for vendors to update product info, including image."""
    class Meta:
        """Meta class for ProductUpdateForm."""
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'stock',
            'image',
            'personalized_text',
            'personalized_image'
        ]


# -----------------------------
# Order Item / Cart Form
# -----------------------------


class OrderItemForm(forms.ModelForm):
    """Form to add products to cart or update quantity/personalization."""
    class Meta:
        """Meta class for OrderItemForm."""
        model = OrderItem
        fields = ['quantity', 'personalized_text', 'personalized_image']

# -----------------------------
# Vendor Profile Update Form (Optional)
# -----------------------------


class VendorProfileForm(forms.ModelForm):
    """Form for vendors to update their store information."""
    class Meta:
        """Meta class for VendorProfileForm."""
        model = VendorProfile
        fields = ['store_name']  # Hide 'verified' from form
