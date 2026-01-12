"""Views for the Giftmarket shop application."""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.db.models import Avg
from .twitter_service import post_tweet

from .models import Product, Order, OrderItem, Review, Store, VendorProfile, User
from .forms import (
    BuyerSignupForm,
    VendorSignupForm,
    OrderItemForm,
    ProductForm,
    ProductUpdateForm)
from shop.models import VendorProfile, Store, Product


# -----------------------------
# PRODUCT LIST / DETAIL
# -----------------------------


def product_list(request):
    """Display list of all products."""
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})


def product_detail(request, product_id):
    """Display product details and reviews."""
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()
    average_rating = reviews.aggregate(avg=Avg('rating'))['avg']
    average_rating = round(average_rating, 1) if average_rating else None

    user_has_reviewed = False
    if request.user.is_authenticated:
        user_has_reviewed = reviews.filter(user=request.user).exists()

    return render(request, 'shop/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'average_rating': average_rating,
        'user_has_reviewed': user_has_reviewed,
    })


# -----------------------------
# CART / ORDER
# -----------------------------

@login_required
def view_cart(request):
    """Display user's cart items."""
    cart_items = OrderItem.objects.filter(order__buyer=request.user,
                                          order__status='pending')
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'shop/cart.html',
                  {'cart_items': cart_items, 'total': total})


@login_required
def add_to_cart(request, product_id):
    """Add a product to the buyer's cart."""

    product = get_object_or_404(Product, id=product_id)

    # Get or create pending order
    order, created = Order.objects.get_or_create(
        buyer=request.user,
        status='pending'
    )

    # Get or create order item
    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        product=product,
        defaults={
            'quantity': 1,
            'price': product.price
            }
    )

    if not created:
        order_item.quantity += 1
        order_item.save()

    messages.success(request, "Product added to cart.")
    return redirect('view_cart')


@login_required
def increase_quantity(request, item_id):
    """Increase quantity of an item in the cart."""
    item = get_object_or_404(OrderItem, id=item_id, order__buyer=request.user)
    item.quantity += 1
    item.save()
    return redirect('view_cart')


@login_required
def decrease_quantity(request, item_id):
    """Decrease quantity of an item in the cart."""
    item = get_object_or_404(OrderItem, id=item_id, order__buyer=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('view_cart')


@login_required
def remove_from_cart(request, item_id):
    """Remove an item from the cart."""
    item = get_object_or_404(OrderItem, id=item_id, order__buyer=request.user)
    item.delete()
    return redirect('view_cart')


@login_required
def checkout(request):
    """Process the checkout of the cart."""
    order = Order.objects.filter(buyer=request.user, status='pending').first()
    if not order or not order.items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('product_list')

    order.status = 'processing'
    order.total_price = sum(
        item.product.price * item.quantity for item in order.items.all())
    order.save()

    subject = f"Invoice for Order #{order.id}"
    message = render_to_string('shop/email_invoice.html',
                               {'order': order, 'user': request.user})
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
              [request.user.email], fail_silently=False)

    messages.success(request,
                     f"Order #{order.id} placed successfully."
                     f"Invoice sent to your email.")
    return redirect('order_history')


@login_required
def order_history(request):
    """Display past orders for the user."""
    orders = Order.objects.filter(buyer=request.user).exclude(status='pending').order_by('-created_at')
    return render(request, 'shop/order_history.html', {'orders': orders})


# -----------------------------
# REVIEWS
# -----------------------------

@login_required
def submit_review(request, product_id):
    """Submit a review for a product."""
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        rating = int(request.POST.get('rating', 5))
        comment = request.POST.get('comment', '').strip()

        if not comment:
            messages.error(request, "Comment cannot be empty.")
            return redirect('product_detail', product_id=product.id)

        if Review.objects.filter(product=product, user=request.user).exists():
            messages.warning(request, "You have already reviewed this product.")
            return redirect('product_detail', product_id=product.id)

        purchased = OrderItem.objects.filter(
            order__buyer=request.user,
            order__status__in=['processing', 'shipped', 'completed'],
            product=product
        ).exists()

        Review.objects.create(
            product=product,
            user=request.user,
            rating=rating,
            comment=comment,
            verified_purchase=purchased
        )

        messages.success(request, "Your review has been submitted.")

    return redirect('product_detail', product_id=product.id)


# -----------------------------
# USER SIGNUP
# -----------------------------

def buyer_signup(request):
    """Handle buyer signup."""
    if request.user.is_authenticated:
        messages.warning(request,
                         "Please log out before creating a new account.")
        return redirect('product_list')

    form = BuyerSignupForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('product_list')

    return render(request, 'shop/buyer_signup.html', {'form': form})


def vendor_signup(request):
    """Handle vendor signup."""
    if request.user.is_authenticated:
        messages.warning(request,
                         "Please log out before creating a new account.")
        return redirect('product_list')

    form = VendorSignupForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.role = 'vendor'
        user.save()

        # Create VendorProfile
        VendorProfile.objects.create(
            user=user,
            store_name=form.cleaned_data['store_name']
        )

        login(request, user)
        return redirect('vendor_dashboard')

    return render(request, 'shop/vendor_signup.html', {'form': form})


# -----------------------------
# VENDOR DASHBOARD / PRODUCT MANAGEMENT
# -----------------------------


@login_required
def vendor_dashboard(request):
    """Vendor dashboard showing stores and products.
    Allows store creation if none exists."""
    vendor_profile = None
    stores = []
    products = []

    try:
        vendor_profile = VendorProfile.objects.get(user=request.user)

        # HANDLE STORE CREATION
        if request.method == "POST":
            store_name = request.POST.get("store_name")
            if store_name:
                Store.objects.create(
                    vendor=vendor_profile,
                    name=store_name
                )
                return redirect("vendor_dashboard")

        stores = Store.objects.filter(vendor=vendor_profile)
        products = Product.objects.filter(store__in=stores)

    except VendorProfile.DoesNotExist:
        pass

    context = {
        "vendor_profile": vendor_profile,
        "stores": stores,
        "products": products,
    }

    return render(request, "shop/vendor_dashboard.html", context)


@login_required
def add_product(request):
    """Add a new product for the vendor."""

    if not hasattr(request.user, 'vendor_profile'):
        messages.error(request, "You must complete vendor signup first.")
        return redirect('vendor_signup')

    vendor_profile = request.user.vendor_profile
    store = vendor_profile.stores.first()

    if not store:
        messages.error(request, "Create a store first.")
        return redirect('vendor_dashboard')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.store = store
            product.save()
            messages.success(request, "Product added successfully.")
            return redirect('vendor_dashboard')
    else:
        form = ProductForm()

    # ✅ ALWAYS return a response
    return render(request, 'shop/add_product.html', {
        'form': form,
        'store': store
    })


@login_required
def edit_product(request, product_id):
    """Edit an existing product for the vendor."""
    product = get_object_or_404(Product, id=product_id)
    if product.store.vendor != request.user.vendor_profile:
        messages.error(request, "Not authorized.")
        return redirect('product_list')

    form = ProductUpdateForm(request.POST or None,
                             request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, "Product updated.")
        return redirect('vendor_dashboard')

    return render(request, 'shop/edit_product.html',
                  {'form': form, 'product': product})


@login_required
def delete_product(request, product_id):
    """Delete a product for the vendor."""
    product = get_object_or_404(Product, id=product_id)
    if product.store.vendor != request.user.vendor_profile:
        messages.error(request, "Not authorized to delete this product.")
        return redirect('product_list')

    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted.")
        return redirect('vendor_dashboard')

    return render(request, 'shop/delete_product.html', {'product': product})
