from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("cart/", views.cart, name="cart"),
    path("add-to-cart/<int:pid>/", views.add_to_cart, name="add_to_cart"),
]
