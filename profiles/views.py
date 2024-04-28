from django.views import generic
from .models import Writer
from .forms import ProfileForm


class ViewProfile(generic.DetailView):
    model = Writer
    template_name = "view_profile.html"

class EditProfile(generic.UpdateView):
    model = Writer
    template_name = "edit_profile.html"
    form_class = ProfileForm