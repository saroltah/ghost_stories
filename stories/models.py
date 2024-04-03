from django.db import models
from django.utils import timezone
from profiles.models import Writer

# Create your models here.

class Story(models.Model):
  author = models.OneToOneField(Writer, on_delete=models.CASCADE)
  title	= models.CharField(max_length=100)	
  teaser = models.TextField(max_length=500)
  story	= models.TextField()
  image	= models.ImageField(blank=True, upload_to=None, height_field=None, width_field=None)	
  created_on	= models.DateTimeField(auto_now_add=True)
  edited = models.DateTimeField	(auto_now=True)