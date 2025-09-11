from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "product_detail.html", {"product": product})

def cart(request):
    cart_items = request.session.get("cart", {})
    products = []
    total = 0
    for pid, qty in cart_items.items():
        p = Product.objects.get(id=pid)
        products.append({"product": p, "qty": qty, "subtotal": p.price * qty})
        total += p.price * qty
    return render(request, "cart.html", {"items": products, "total": total})

def add_to_cart(request, pid):
    cart = request.session.get("cart", {})
    cart[str(pid)] = cart.get(str(pid), 0) + 1
    request.session["cart"] = cart
    return redirect("cart")
