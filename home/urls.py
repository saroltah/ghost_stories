from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('about/', views.Index.as_view(), name='about'),
    path('terms/', views.Index.as_view(), name='terms'),
]