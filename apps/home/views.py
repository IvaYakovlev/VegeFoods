from django.shortcuts import render
from django.views import View
from apps.cart_shop.models import Product, Wishlist
from apps.cart_shop.views import fill_id_card_in_session, fill_card_in_session

class IndexShopView(View):
    def get(self, request):
        fill_id_card_in_session(request)
        fill_card_in_session(request)
        data = Product.objects.all()
        cart = fill_card_in_session(request)
        products = Product.objects.filter(id__in=cart.keys())

        cart_items = [{"product": product, "quantity": cart[str(product.id)], "id": product.id} for product in products]
        if request.user.is_authenticated:
            wishlist_item = list(Wishlist.objects.filter(wishlist__user=request.user))
            wishlist = []
            for item in wishlist_item:
                wishlist.append(item.product)

            context = {'data': data,
                   'cart_items': cart_items,
                   'wishlist': wishlist}
        else:
            context = {'data': data,
                       'cart_items': cart_items,}
        return render(request, 'home/index.html', context)





class AboutShopView(View):
    def get(self, request):
        return render(request, 'home/about.html')

class ContactShopView(View):
    def get(self, request):
        return render(request, 'home/contact.html')