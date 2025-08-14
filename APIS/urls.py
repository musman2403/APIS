from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from cart import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', lambda request: redirect('product_list')),
    path('add-to-cart/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('api/products/', include('products.urls')),
    path('api/accounts/', include('allauth.urls')),
    path('api/users/', include('accounts.urls')),
    path('api/cart/', include('cart.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
