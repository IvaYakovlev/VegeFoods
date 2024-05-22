from django.urls import path

from .views import LoginView

urlpatterns = [
               path('auth_shop/', LoginView.as_view()),
                ]