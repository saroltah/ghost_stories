from . import views
from django.urls import path
from .views import ViewProfile

urlpatterns = [
    path('<slug:slug>/', views.ViewProfile.as_view(), name='view_profile'),
]