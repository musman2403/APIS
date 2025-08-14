from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

# List all products
@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# Add products to cart (session-based)
@api_view(["POST"])
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, id=product_id)

    product_id_str = str(product_id)
    cart[product_id_str] = cart.get(product_id_str, 0) + 1
    request.session['cart'] = cart

    return Response({"message": f"{product.name} added to cart", "cart": cart}, status=status.HTTP_200_OK)

# View cart
@api_view(["GET"])
def view_cart(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    cart_items = []
    total_price = 0
    for product in products:
        quantity = int(cart.get(str(product.id), 1))
        total_price += product.price * quantity
        cart_items.append({
            "products": ProductSerializer(product).data,
            "quantity": quantity,
            "total_price": product.price * quantity
        })

    return Response({
        "items": cart_items,
        "total_cart_price": total_price
    })

# Update quantity
@api_view(["PUT"])
def update_quantity(request, product_id):
    quantity = int(request.data.get("quantity", 1))
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)] = quantity
        request.session['cart'] = cart
        return Response({"message": "Quantity updated", "cart": cart})
    else:
        return Response({"error": "Product not in cart"}, status=status.HTTP_404_NOT_FOUND)

# Clear cart
@api_view(["DELETE"])
def clear_cart(request):
    request.session['cart'] = {}
    return Response({"message": "Cart cleared"})
