from django.shortcuts import render
from django.views import generic
from .models import Story


class StoryList(generic.ListView):
    queryset = Story.objects.all()
    template_name = "story_list.html"