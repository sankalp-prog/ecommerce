# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as django_logout
from app.models import Product,CartItem,Profile
from django.contrib.auth.models import User


def index(request):
    return render(request, "index.html", {
        "product_feed": Product.objects.all()[:15]
    })

def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, "product.html",{"product": product})

def cart(request):
    user = request.user
    if user.is_authenticated:
        # Show cart
        cart = CartItem.objects.filter(user__exact=user.id)
        return render(request, "cart.html", {"cart": cart})
    else:
        # Show log-in form
        return render(request, "login.html")

def user_page(request):
    user = request.user
    print(user)
    if user.is_authenticated:
        # Show user details
        profile = Profile.objects.get(user=user.id)
        return render(request, "user.html",{"user": user, "location": profile.location})
    else:
        # Show log-in form
        return render(request, "login.html")

def search(request,text):
    search = Product.objects.filter(name__icontains=text)
    return render(request, "search.html",{"search_text": text, "product_search_results": search})

def add_to_cart(request, product_id):
    cart_item = CartItem(user_id=request.user.id, product_id=product_id, quantity = 1)
    cart_item.save()
    return HttpResponse(cart_item.id)

def add_product(request):
    name = request.POST["name"]
    price = request.POST["price"]
    img_url = request.POST["img_url"]
    prod_desc = request.POST["prod_desc"]
    product = Product(name=name, price=price, img_url=img_url, prod_desc=prod_desc)
    product.save()
    return render(request, "product.html", {"product": product})

def product_form(request):
    return render(request, "product_form.html")

def login(request):
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(username = email, password = password)
    if user is not None:
        auth_login(request, user)
        return user_page(request)
    else:
        return HttpResponse("username/password is not in the database")

def login_form(request):
    return render(request, "login.html")

def logout(request):
    django_logout(request)
    return index(request)

def signup(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email_id = request.POST["email"]
    password = request.POST["password"]
    location = request.POST["location"]

    user = User.objects.create_user(username = email_id, password = password, first_name = first_name, last_name = last_name)
    auth_login(request, user)

    profile = Profile(user=user, location=location)
    profile.save()

    return render(request, "index.html", {
        "product_feed": Product.objects.all()[:15]
    })

def signup_form(request):
    return render(request, "signup.html") 
