from django import forms
from .models import Story, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField 

class StoryForm(forms.ModelForm):
  class Meta:
    model = Story
    fields = 'title', 'author', 'story_text', 'teaser', 'keywords', 
    widgets = {
      'author': forms.HiddenInput,
      'story_text': SummernoteWidget(),
    }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','content', 'commented_story')

        widgets = {'author': forms.HiddenInput,
        'content':forms.Textarea}