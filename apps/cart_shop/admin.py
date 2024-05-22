from django.contrib import admin

from .models import CartItemShop, Product, Wishlist

admin.site.register(CartItemShop)
admin.site.register(Product)
admin.site.register(Wishlist)
