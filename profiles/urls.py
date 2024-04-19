from . import views
from django.urls import path

urlpatterns = [
    path('writer/<slug:writer_slug>/', views.WriterDetails.as_view(), name='writer_details'),
]