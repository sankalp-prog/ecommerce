

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from app.models import User,Product,CartItem

SANKALP = 1


def index(request):
    return render(request, "index.html",{"thing": 20})

def product(request, id):
    response = "you are looking at the products Page"
    product = Product.objects.get(id=id)
    return render(request, "product.html",{"product": product})

def cart(request):
    cart = CartItem.objects.filter(user__exact=SANKALP)
    return HttpResponse(cart)

def user(request):
    user = User.objects.get(id=SANKALP)
    return render(request, "user.html",{"user": user})

def search(request,text):
    search = Product.objects.filter(name__icontains=text)
    return render(request, "search.html",{"product_search_results": search})

def add_to_cart(request, product_id):
    cart_item = CartItem(user_id=SANKALP, product_id=product_id, quantity = 1)
    cart_item.save()
    return HttpResponse(cart_item.id)