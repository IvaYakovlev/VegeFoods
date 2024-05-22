from decimal import Decimal

from django.shortcuts import render
from django.views import View

from apps.cart_shop.models import Product
from apps.cart_shop.views import fill_card_in_session


class ViewCheckout(View):
   def get(self, request):
       cart = fill_card_in_session(request)
       products = Product.objects.filter(id__in=cart.keys())
       data = [{"product": product, "quantity": cart[str(product.id)], "id": product.id} for product in products]
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
       return render(request, 'checkout/checkout.html', context)