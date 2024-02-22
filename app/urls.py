from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:id>/", views.product, name="product"),
    path("cart/", views.cart, name="cart"),
    path("user/", views.user, name="user"),
    path("search/<str:text>", views.search, name="search"),
    path("add_to_cart/<product_id>", views.add_to_cart, name="add_to_cart"),
    path("signup/<str:email_id>/<str:password>", views.signup, name="signup"),
]