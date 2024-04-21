from django.shortcuts import render
from django.views import generic
from .models import Story, Comment
from django.urls import reverse_lazy


class StoryList(generic.ListView):
    queryset = Story.objects.all()
    template_name = "story_list.html"

class OneStory(generic.DetailView):
    model = Story
    template_name = "one_story.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(commented_story=self.object)
        return context
    
class AddStory(generic.CreateView):
    model = Story
    template_name = "add_story.html"
    fields = '__all__'

class EditStory(generic.UpdateView):
    model = Story
    template_name = "edit_story.html"
    fields = ['title', 'slug', 'story_text', 'teaser', 'keywords', 'image']

class DeleteStory(generic.DeleteView):
    model = Story
    template_name = "delete_story.html"
    success_url = reverse_lazy('stories') 

class AddComment(generic.CreateView):
    model  = Comment
    template_name = "add_comment.html"
    fields = '__all__'
    success_url = reverse_lazy ('one_story') 

class EditComment(generic.UpdateView):
    model = Comment
    template_name = "edit_comment.html"
    fields = ['content']

class DeleteComment(generic.DeleteView):
    model = Comment
    template_name = "delete_story.html"
    success_url = reverse_lazy ('one_story') 