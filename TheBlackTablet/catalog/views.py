from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
    }
    return render(request, 'catalog/index.html', context)

def catalog(request):
    context = {
    }
    return render(request, 'catalog/catalog.html', context)

def reviews(request):
    context = {
    }
    return render(request, 'catalog/reviews.html', context)
