from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "index.html"


class About(TemplateView):
    template_name = "about.html"


class Terms(TemplateView):
    template_name = "terms.html"


def error_404_view(request, exception):
    return render(request, 'page_not_found.html')

def error_500_view(request):
    return render(request, 'wrong_data.html')
