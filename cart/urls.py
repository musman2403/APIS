from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),   # POST
    path('update-quantity/<uuid:product_id>/', views.update_quantity, name='update_quantity'),  # PUT
    path('clear-cart/', views.clear_cart, name='clear_cart'),  # DELETE
    path('view-cart/', views.view_cart, name='view_cart'),  # GET
]
