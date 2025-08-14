from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('products/', views.product_list, name='product_list'),  # GET all products
    path('add-to-cart/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),  # POST
    path('cart/', views.view_cart, name='view_cart'),  # GET
    path('update-quantity/<uuid:product_id>/', views.update_quantity, name='update_quantity'),  # PUT
    path('clear-cart/', views.clear_cart, name='clear_cart'),  # DELETE
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
