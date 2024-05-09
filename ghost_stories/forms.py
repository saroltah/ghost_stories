from allauth.account.forms import SignupForm
from django import forms 
 
GOAL_CHOICES = (
    ("Writer", "Writer"),
    ("Editor", "Editor"),
   )

class CustomSignupForm(SignupForm):
  
  goal = forms.ChoiceField(choices=GOAL_CHOICES, initial="Writer")
  def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.goal = self.cleaned_data['goal']
        user.save()
        return user