"""URL configurations for the Giftmarket shop application."""
from django.urls import path
from shop import views


urlpatterns = [
    # Home / Public
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail,
         name='product_detail'),

    # Buyer URLs
    path('buyer/signup/', views.buyer_signup, name='buyer_signup'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart,
         name='add_to_cart'),
    path('cart/increase/<int:item_id>/', views.increase_quantity,
         name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', views.decrease_quantity,
         name='decrease_quantity'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart,
         name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='order_history'),

    # Review URLs
    path('product/<int:product_id>/review/', views.submit_review,
         name='submit_review'),

    # Vendor URLs
    path('vendor/signup/', views.vendor_signup, name='vendor_signup'),
    path('vendor/dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('vendor/add-product/', views.add_product, name='add_product'),
    path('vendor/edit-product/<int:product_id>/', views.edit_product,
         name='edit_product'),
    path('vendor/delete-product/<int:product_id>/', views.delete_product,
         name='delete_product'),
]
