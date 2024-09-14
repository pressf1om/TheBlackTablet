from django.urls import path
from . import views


app_name = 'about'

urlpatterns = [
    path('company/', views.AboutCompanyView.as_view(), name='company'),
]