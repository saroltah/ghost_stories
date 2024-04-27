from . import views
from django.urls import path
from .views import WriterDetails

urlpatterns = [
    path('<slug:slug>/', views.WriterDetails.as_view(), name='profile'),
]