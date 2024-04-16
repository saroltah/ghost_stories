from django.shortcuts import render
from django.views import generic
from .models import Story


class StoryList(generic.ListView):
    queryset = Story.objects.all()
    template_name = "story_list.html"

class OneStory(generic.DetailView):
    model = Story
    template_name = "one_story.html"
    
class AddStory(generic.CreateView):
    model = Story
    template_name = "add_story.html"
    fields = '__all__'