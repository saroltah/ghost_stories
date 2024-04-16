from . import views
from django.urls import path

urlpatterns = [
    path('writer/<slug:writer_slug>/', views.Writer_details.as_view(), name='writer_details'),
]