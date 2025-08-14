from rest_framework import serializers
from .models import Product, Offer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # includes id, name, price, stock, image_url

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'  # includes code, description, discount
