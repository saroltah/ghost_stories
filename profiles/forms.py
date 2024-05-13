from django import forms
from .models import Writer
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField,\
     SummernoteTextField


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = ('name', 'goal', 'email', 'phone', 'about_me',
                  'facebook_link', 'instagram_link', 'linkedin_link', 'vis')
        widgets = {
          'about_me': SummernoteWidget(), }
