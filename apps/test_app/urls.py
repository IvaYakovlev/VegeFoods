from django.urls import path

from .views import  RandomNumber

urlpatterns = [path('random/', RandomNumber.as_view()),
                ]