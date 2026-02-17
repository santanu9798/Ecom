from django.shortcuts import render
from django.views import View
from urllib import request
from .models import Product
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "app/home.html")

class CategoryView(View):
    def get(self, request,val):
        product = Product.objects.filter(category=val)
        return render(request, "app/category.html", {"product": product, "val": val})