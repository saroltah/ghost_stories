from . import views
from django.urls import path
from .views import AddStory

urlpatterns = [
    path('', views.StoryList.as_view(), name='stories'),
    path('add_story/', views.AddStory.as_view(), name='add_story'),
    path('<slug:slug>/', views.OneStory.as_view(), name='one_story'),
]