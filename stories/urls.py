from . import views
from django.urls import path

urlpatterns = [
    path('', views.StoryList.as_view(), name='stories'),
    path('<slug:slug>/', views.OneStory.as_view(), name='one_story'),
]