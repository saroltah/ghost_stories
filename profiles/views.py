from django.shortcuts import render
from django.views import generic
from .models import Writer


class WriterDetails(generic.DetailView):
    model = Writer
    template_name = "writer_detail.html"
    