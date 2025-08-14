from rest_framework import serializers
from .models import CartItem
from products.serializers import ProductSerializer  # to show products details

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=CartItem._meta.get_field('products').remote_field.model.objects.all(),
        source='products',
        write_only=True
    )

    class Meta:
        model = CartItem
        fields = ['id', 'user', 'products', 'product_id', 'quantity']
        read_only_fields = ['user']
