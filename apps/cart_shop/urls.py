from django.urls import path
from .views import *
app_name = 'cart_shop'


urlpatterns = [
    path('', ViewCart.as_view(), name='cart'),
    path('wishlist/', ViewWishList.as_view(), name='wishlist'),
    path('buy/<int:product_id>', ViewCartBuy.as_view(), name='buy'),
    path('del/<int:item_id>', ViewCartDel.as_view(), name='del_from_cart'),
    path('add/<int:product_id>', ViewCartAdd.as_view(), name='add_to_cart'),
    path('addwishlist/<int:product_id>', ViewWishlistAdd.as_view(), name='wishlist_add'),
    path('update_item/<int:item_id>/', ViewCartUpdate.as_view(), name='update_item'),
    path('del_wish/<int:item_id>', ViewWishlistDel.as_view(), name='del_from_wishlist'),
]