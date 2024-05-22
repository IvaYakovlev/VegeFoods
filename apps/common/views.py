from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from datetime import datetime

class IndexView(View):
    def get(self, request):
        return render(request, 'common/index.html')

class CurrentDataView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)

class Hello(View):
    def get(self, request):
        html = f"<h1>Hello, World</h1>"
        return HttpResponse(html)



