from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Cart(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.user}"


class Product(models.Model):
   name = models.CharField(max_length=255)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   description = models.TextField()
   image = models.ImageField(upload_to='static/products/', null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def save(self, *args, **kwargs):
      super().save(*args, **kwargs)

      img = Image.open(self.image.path)
      img = img.resize((150, 150), Image.ANTIALIAS)
      img.save(self.image.path)

   def __str__(self):
       return self.name





class CartItem(models.Model):
   cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.cart}_{self.product}"

