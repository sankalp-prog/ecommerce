# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from app.models import User,Product,CartItem

SANKALP = 1


def index(request):
    return render(request, "index.html", {
        "product_feed": Product.objects.all()[:15]
    })

def product(request, id):
    response = "you are looking at the products Page"
    product = Product.objects.get(id=id)
    return render(request, "product.html",{"product": product})

def cart(request):
    cart = CartItem.objects.filter(user__exact=SANKALP)
    return render(request, "cart.html", {"cart": cart})

def user(request):
    user = User.objects.get(id=SANKALP)
    return render(request, "user.html",{"user": user})

def search(request,text):
    search = Product.objects.filter(name__icontains=text)
    return render(request, "search.html",{"search_text": text, "product_search_results": search})

def add_to_cart(request, product_id):
    cart_item = CartItem(user_id=SANKALP, product_id=product_id, quantity = 1)
    cart_item.save()
    return HttpResponse(cart_item.id)

def signup(request, email_id, password):
    print(email_id, password)
    user = User(email=email_id, password=password, first_name='', last_name='', location='')
    user.save()
    return HttpResponse(request, "index.html")

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