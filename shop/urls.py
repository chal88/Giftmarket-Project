"""URL configurations for the Giftmarket shop application."""
from django.urls import path
from . import views

urlpatterns = [

    # Public / Buyer

    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail,
         name='product_detail'),

    path('signup/buyer/', views.buyer_signup, name='buyer_signup'),
    path('signup/vendor/', views.vendor_signup, name='vendor_signup'),

    # Cart / Orders

    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/increase/<int:item_id>/', views.increase_quantity,
         name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', views.decrease_quantity,
         name='decrease_quantity'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart,
         name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='order_history'),

    # Reviews

    path('review/<int:product_id>/', views.submit_review,
         name='submit_review'),

    # Vendor Dashboard

    path('vendor/dashboard/', views.vendor_dashboard, name='vendor_dashboard'),

    # Vendor Store CRUD

    path('vendor/stores/', views.vendor_store_list, name='vendor_store_list'),
    path('vendor/stores/create/', views.create_store, name='create_store'),
    path('vendor/stores/<int:store_id>/edit/', views.update_store,
         name='update_store'),
    path('vendor/stores/<int:store_id>/delete/', views.delete_store,
         name='delete_store'),

    # Vendor Products

    path('vendor/products/add/', views.add_product, name='add_product'),
    path('vendor/products/<int:product_id>/edit/', views.edit_product,
         name='edit_product'),
    path('vendor/products/<int:product_id>/delete/', views.delete_product,
         name='delete_product'),
]
