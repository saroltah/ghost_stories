from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Story, Comment
from django.urls import reverse_lazy, reverse
from .forms import StoryForm, CommentForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages



class StoryList(generic.ListView):
    queryset = Story.objects.all()
    template_name = "story_list.html"
    paginate_by = 6

class OneStory(generic.DetailView):
    model = Story
    template_name = "one_story.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(commented_story=self.object)
        
        one_story_slug = self.kwargs.get('slug')
        likes = get_object_or_404(Story, slug=one_story_slug)
        number_of_likes = likes.number_of_likes()
        context['number_of_likes'] = number_of_likes
        
        return context

def LikeStory(request, slug):
    story = get_object_or_404(Story, slug=request.POST.get('story_slug'))
    story.likes.add(request.user)
    return HttpResponseRedirect(reverse('one_story', kwargs={'slug':slug}))


class AddStory(generic.CreateView):
    model = Story
    form_class = StoryForm
    template_name = "add_story.html"
    success_url = reverse_lazy('stories')
    #fields = '__all__'
    def form_valid(self, form):
        messages.success(self.request, 'Your story is posted!')
        return super().form_valid(form)
 

class EditStory(generic.UpdateView):
    model = Story
    form_class = StoryForm
    template_name = "edit_story.html"
    #fields = ['title', 'story_text', 'teaser', 'keywords', 'image']
    def form_valid(self, form):
        messages.success(self.request, 'Story edited')
        return super().form_valid(form)

class DeleteStory(generic.DeleteView):
    model = Story
    template_name = "delete_story.html"
    success_url = reverse_lazy('stories')
    def form_valid(self, form):
        messages.success(self.request, 'Story deleted!')
        return super().form_valid(form)
    

class FilterStory(generic.ListView):
    model = Story
    template_name = 'filter_story.html'

class AddComment(generic.CreateView):
   model  = Comment
   template_name = "add_comment.html"
   fields = '__all__'
   def get_success_url(self):
      return reverse_lazy('one_story', kwargs={'slug': self.object.commented_story.slug})
   def form_valid(self, form):
        messages.success(self.request, 'Comment added')
        return super().form_valid(form)


class EditComment(generic.UpdateView):
    model = Comment
    template_name = "edit_comment.html"
    fields = ['content']

    def get_object(self, queryset=None):
        story_slug = self.kwargs.get('slug')
        comment_id = self.kwargs.get('comment_id', None)
        if comment_id:
            comment = get_object_or_404(Comment, id=comment_id, commented_story__slug=story_slug)
        else:
            comment = get_object_or_404(Comment, commented_story__slug=story_slug)

class DeleteComment(generic.DeleteView):
    model = Comment
    template_name = "delete_story.html"
    success_url = reverse_lazy ('one_story') 