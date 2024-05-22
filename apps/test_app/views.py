from random import random

from django.http import HttpResponse
from django.views import View

class RandomNumber(View):
    def get(self, request):
        number = random()
        html = f"{number}"
        return HttpResponse(html)
