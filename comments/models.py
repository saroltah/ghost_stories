from django.db import models
from django.utils import timezone
from profiles.models import Writer, Editor

# Create your models here.

class Comments(models.Model):
  author = models.OneToOneField(Writer, on_delete=models.CASCADE)
  content	= models.TextField()		
  created_on	= models.DateTimeField(auto_now_add=True)