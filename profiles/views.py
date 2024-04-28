from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Writer


class ViewProfile(generic.DetailView):
    model = Writer
    template_name = "view_profile.html"
    