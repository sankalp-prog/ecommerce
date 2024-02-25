from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:id>/", views.product, name="product"),
    path("cart/", views.cart, name="cart"),
    path("user/", views.user_page, name="user"),
    path("search/<str:text>", views.search, name="search"),
    path("add_to_cart/<product_id>", views.add_to_cart, name="add_to_cart"),
    path("signup/", views.signup, name="signup"),
    path("signup_form/", views.signup_form, name="signup_form"),
    path("product_form/", views.product_form, name="product_form"),
    path("add_product/", views.add_product, name="add_product"),
    path("login/", views.login, name="login"),
    path("login_form/", views.login_form, name="login_form"),
    path("logout/", views.logout, name="logout"),
]