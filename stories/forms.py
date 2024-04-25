from django import forms
from .models import Story, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField 

class StoryForm(forms.ModelForm):
  class Meta:
    model = Story
    fields = 'title', 'author', 'story_text', 'teaser', 'keywords', 'image',
    widgets = {
      'story_text': SummernoteWidget(),
    }

#class StoryForm(forms.ModelForm):
#    class Meta:
#        model = Story
#        fields = ['story_text']
#        widgets = {
#            'story_text': SummernoteWidget(),
#        }

#class StoryForm(forms.ModelForm):
 # story_text = forms.TextField(widget=SummernoteWidget())
 # class Meta:
 #   model=Story
 #   fields=['story_text']

#class StoryForm(forms.ModelForm):
#    story_text = SummernoteTextField()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','content',)

        widgets = {'author': forms.TextInput,
        'content':forms.Textarea}
