from PIL import Image
from django.db import models
from apps.cart.models import Cart


class Product(models.Model):
   name = models.CharField(max_length=255)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   discount = models.IntegerField(null=True, blank=True)
   description = models.TextField()
   image = models.ImageField(upload_to='static/shop/images/', null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return self.name


class CartItemShop(models.Model):
   cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.cart}_{self.product}"



class Wishlist(models.Model):
   wishlist = models.ForeignKey(Cart, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   #quantity = models.IntegerField(default=1)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.wishlist}_{self.product}"

