from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"User({self.first_name}, {self.last_name}, {self.location})"

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    img_url = models.CharField(max_length=200)
    prod_desc = models.CharField(max_length=400)

    def __str__(self):
        return f"User({self.name}, {self.price}, {self.img_url}, {self.prod_desc})"

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"User({self.user}, {self.product}, {self.quantity})"




