from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200,blank=True)
    # email = models.CharField(max_length=200, default="blank")
    # password = models.CharField(max_length=200, default="blank")
    # first_name = models.CharField(max_length=200,blank=True)
    # last_name = models.CharField(max_length=200,blank=True)
    # location = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f"User({self.first_name}, {self.last_name}, {self.location}, {self.email}, {self.password})"

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    img_url = models.CharField(max_length=200)
    prod_desc = models.CharField(max_length=400)

    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.img_url}, {self.prod_desc})"

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"CartItem({self.user}, {self.product}, {self.quantity})"




