from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from django.shortcuts import get_object_or_404

# Add products to cart (session-based)
@api_view(["POST"])
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    if not isinstance(cart, dict):
        cart = {}

    product = get_object_or_404(Product, id=product_id)
    product_id_str = str(product_id)

    cart[product_id_str] = cart.get(product_id_str, 0) + 1
    request.session['cart'] = cart

    return Response({
        "message": f"{product.name} added to cart",
        "cart": cart
    }, status=status.HTTP_200_OK)


# Clear cart
@api_view(["DELETE"])
def clear_cart(request):
    request.session['cart'] = {}
    return Response({"message": "Cart cleared"}, status=status.HTTP_200_OK)


# Update quantity
@api_view(["PUT"])
def update_quantity(request, product_id):
    cart = request.session.get('cart', {})
    quantity = request.data.get('quantity')

    if quantity is None or not str(quantity).isdigit() or int(quantity) < 1:
        return Response({"error": "Invalid quantity"}, status=status.HTTP_400_BAD_REQUEST)

    if str(product_id) in cart:
        cart[str(product_id)] = int(quantity)
        request.session['cart'] = cart
        return Response({"message": "Quantity updated", "cart": cart}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Product not in cart"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def view_cart(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    items = []
    total_price = 0
    for product in products:
        quantity = int(cart[str(product.id)])
        total = product.price * quantity
        items.append({
            "products": {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "image_url": product.image_url
            },
            "quantity": quantity,
            "total_price": total
        })
        total_price += total

    return Response({
        "items": items,
        "total_cart_price": total_price
    })
