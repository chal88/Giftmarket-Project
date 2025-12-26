"""django_project URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='home'),           # homepage
    path('shop/', include('shop.urls')),   # shop app urls
    path('accounts/', include('django.contrib.auth.urls')),  # auth urls
    path('api/', include('shop.api_urls')),


    # Optional: explicit login/logout
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Redirect /login to /accounts/login/
    path('login/', 
         RedirectView.as_view(url='/accounts/login/', permanent=False)),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
