from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# /products -> index
# url: uniform resource Locators(Address)


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('new product list')
