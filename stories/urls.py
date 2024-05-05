from . import views
from django.urls import path
from .views import StoryList, AddStory, OneStory, EditStory, DeleteStory, AddComment, EditComment, DeleteComment, LikeStory

urlpatterns = [
    path('', views.StoryList.as_view(), name='stories'),
    path('filter_stories/', views.filter_stories, name='filter_stories'),
    path('add_story/', views.AddStory.as_view(), name='add_story'),
    path('<slug:slug>/', views.OneStory.as_view(), name='one_story'),
    path('<slug:slug>/edit_story/', views.EditStory.as_view(), name='edit_story'),
    path('<slug:slug>/delete_story/', views.DeleteStory.as_view(), name='delete_story'),
    path('<slug:slug>/add_comment/', views.AddComment.as_view(), name='add_comment'),
    path('<slug:slug>/edit_comment/', views.EditComment.as_view(), name='edit_comment'),
    path('<slug:slug>/delete_comment/', views.DeleteComment.as_view(), name='delete_comment'),
    path('<slug:slug>/like/', LikeStory, name='like_story'),

]