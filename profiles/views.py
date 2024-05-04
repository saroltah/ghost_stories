from django.views import generic
from .models import Writer
from .forms import ProfileForm
from django.contrib import messages


class ViewProfile(generic.DetailView):
    model = Writer
    template_name = "view_profile.html"

class EditProfile(generic.UpdateView):
    model = Writer
    template_name = "edit_profile.html"
    form_class = ProfileForm
    def form_valid(self, form):
        messages.success(self.request, 'Your profile is updated!')
        return super().form_valid(form)