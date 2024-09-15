from django.http import HttpResponse
from django.shortcuts import render
from .models import Catalog

def index(request):
    context = {
    }
    return render(request, 'catalog/index.html', context)

def catalog(request):
    items = Catalog.objects.all()
    context = {
        'items': items
    }
    return render(request, 'catalog/catalog.html', context)

def reviews(request):
    context = {
    }
    return render(request, 'catalog/reviews.html', context)

def coffee(request):
    context = {
    }
    return render(request, 'catalog/coffee.html', context)

def contact(request):
    context = {
    }
    return render(request, 'catalog/contact.html', context)
