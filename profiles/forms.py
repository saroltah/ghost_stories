from django import forms
from .models import Writer


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Writer
    fields = 'name', 'email', 'photo', 'about_me', 'resume'