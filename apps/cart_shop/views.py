
from .models import CartItemShop, Product, Wishlist
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from decimal import Decimal
from ..cart.models import Cart


def fill_card_in_session(request):
    """ Проверяет есть ли параметр cart в сессии, если параметр пустой,
    то обращаемся к БД и заполняем его товарами из корзины в БД
    Т.о. заполнив один раз за сессию, к БД можно далее не обращаться """

    cart = request.session.get('cart', {})
    if request.user.is_authenticated and not cart:
        cart_items = CartItemShop.objects.filter(cart__user=request.user)
        for item in cart_items:
            cart[item.product.id] = item.quantity
        request.session['cart'] = cart
    return cart

def fill_id_card_in_session(request):
    """ Проверяет есть ли параметр id_cart в сессии,
    если он пустой, обращаемся к БД и заполняем id корзины в БД """

    id_cart = request.session.get('id_cart', None)
    if request.user.is_authenticated and not id_cart:
        id_cart = Cart.objects.get(user=request.user).id
        request.session['id_cart'] = id_cart
    return id_cart


def save_product_in_cart(request, product_id):
    """ Проверяет наличие параметра cart в сесии,
    если он пуст, то заполняем его id из корзины """

    cart = fill_card_in_session(request)
    if request.user.is_authenticated:
        cart_items = CartItemShop.objects.filter(cart__user=request.user, product_id=product_id)

        if cart_items:
            cart_item = cart_items[0]
            cart_item.quantity += 1
        else:
            product = get_object_or_404(Product, id=product_id)
            cart_user = get_object_or_404(Cart, user=request.user)
            cart_item = CartItemShop(cart=cart_user, product=product)
        cart_item.save()

    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart

class ViewCart(View):
    def get(self, request):
        cart = fill_card_in_session(request)
        if cart:
            products = Product.objects.filter(id__in=cart.keys())
            data = [{"product": product, "quantity": cart[str(product.id)], "id": product.id} for product in products]
        else:
            data=[]

        total_price_no_discount = sum(item['product'].price * item['quantity'] for item in data)
        total_discount = sum(item['product'].price * item['product'].discount * item['quantity']
                             for item in data if item['product'].discount is not None) / 100
        if not total_discount:
            total_discount = Decimal('0.00')
        total_sum = total_price_no_discount - total_discount
        context = {'cart_items': data,
                   'total_price_no_discount': total_price_no_discount,
                   'total_discount': total_discount,
                   'total_sum': total_sum,
                   }
        return render(request, "cart_shop/cart.html", context)

class ViewCartUpdate(View):
    def get(self, request, item_id):
        cart = fill_card_in_session(request)
        cart_id = fill_id_card_in_session(request)
        if request.user.is_authenticated:
            cart_item = get_object_or_404(CartItemShop, cart__id=cart_id, product__id=item_id)
            cart_item.quantity += int(request.GET.get('quantity'))
        cart[str(item_id)] += int(request.GET.get('quantity'))
        print(cart)
        request.session['cart'] = cart
        return redirect("cart_shop:cart")



class ViewCartBuy(View):
    def get(self, request, product_id):
        save_product_in_cart(request, product_id)
        return redirect('cart_shop:cart')

class ViewCartDel(View):
    def get(self, request, item_id):
        cart = fill_card_in_session(request)
        cart_id = fill_id_card_in_session(request)

        if request.user.is_authenticated:
            cart_item = get_object_or_404(CartItemShop, cart__id=cart_id, product__id=item_id)
            cart_item.delete()
        cart.pop(str(item_id))
        request.session['cart'] = cart
        return redirect("cart_shop:cart")

class ViewCartAdd(View):
    def get(self, request, product_id):
        save_product_in_cart(request, product_id)
        return redirect('home:index')





class ViewWishList(View):
    """Отображение списка избранного"""
    def get(self, request):

        if request.user.is_authenticated:
            wishlist_item = Wishlist.objects.filter(wishlist__user=request.user)
            data = list(wishlist_item)

            context = {'wishlist_item': data
                       }
            return render(request, 'cart_shop/wishlist.html', context)
        else:
            return redirect('auth_shop:login')





class ViewWishlistAdd(View):
    """ Добавление в список избранного """

    def get(self, request, product_id):

        if request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(wishlist__user=request.user, product=product_id)
            if wishlist:
                wishlist_item = wishlist[0]
            else:
                product = get_object_or_404(Product, id=product_id)
                wishlist_user = get_object_or_404(Cart, user=request.user)
                wishlist_item = Wishlist(wishlist=wishlist_user, product=product)
                wishlist_item.save()
            return redirect('home:index')
        else:
            return redirect('auth_shop:login')



class ViewWishlistDel(View):
    """Удаление из списка избранного"""
    def get(self, request, item_id):

        wishlist_item = get_object_or_404(Wishlist, id=item_id)
        wishlist_item.delete()
        return redirect('cart_shop:wishlist')

