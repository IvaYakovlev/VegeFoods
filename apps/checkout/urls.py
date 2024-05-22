from django.urls import path
from .views import ViewCheckout

app_name = 'checkout'


urlpatterns = [
    path('', ViewCheckout.as_view(), name='checkout')
]