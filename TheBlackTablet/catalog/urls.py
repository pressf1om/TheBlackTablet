from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('reviews/', views.reviews, name='reviews'),
    path('coffee/', views.coffee, name='coffee'),
    path('contact/', views.contact, name='contact'),
]