from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Lander(TemplateView):
    template_name = "thirdauth/index.html"