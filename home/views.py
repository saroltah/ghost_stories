from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "index.html"

class About(TemplateView):
    template_name = "about.html"

class Terms(TemplateView):
    template_name = "terms.html"
