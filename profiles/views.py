from django.shortcuts import render
from django.views import generic
from .models import Writer


class Writer_details(generic.DetailView):
    model = Writer
    