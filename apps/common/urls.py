from django.urls import path

from .views import CurrentDataView, Hello, IndexView

urlpatterns = [
               path('', IndexView.as_view()),
               path('datetime/', CurrentDataView.as_view()),
               path('hello/', Hello.as_view()),
                ]