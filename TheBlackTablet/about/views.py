from django.shortcuts import render

from django.views.generic.base import TemplateView


class AboutCompanyView(TemplateView):
    template_name = 'about/company.html'