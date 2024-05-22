from django.urls import path
from . import views

app_name = 'app.cart'

urlpatterns = [
   path('', views.view_cart, name='view_cart'),
   path('update_item/<int:item_id>/', views.update_item, name='update_item'),
   path('remove_item/<int:item_id>/', views.remove_item, name='remove_item'),
   path('checkout/', views.checkout, name='checkout'),
]
