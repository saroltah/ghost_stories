from . import views
from django.urls import path

urlpatterns = [
    path('writer/<slug:slug>/', views.Writer_details.as_view(), name='writer_detail'),
]