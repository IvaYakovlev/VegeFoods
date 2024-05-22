
from django.urls import path, include
from .views import IndexShopView, AboutShopView, ContactShopView

app_name = 'home'
urlpatterns = [
    path('', IndexShopView.as_view(), name='index'),
    path('about/', AboutShopView.as_view(), name='about'),
    path('contact/', ContactShopView.as_view(), name='contact'),
]