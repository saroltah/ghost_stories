from django.db import models
from django.utils import timezone

# Create your models here.

class Writer(models.Model):
  name	= models.CharField(max_length=50)
  username = models.CharField(max_length=50)
  email	= models.EmailField(max_length=100)
  phone =	models.IntegerField
  photo	= models.ImageField(blank=True, upload_to=None, height_field=None, width_field=None)
  about_me = models.TextField(blank=True, max_length=300)	
  resume = models.FileField(blank=True)
		

class Editor(models.Model):
  name = models.CharField(max_length=50)
  username = models.CharField(max_length=50)
  email	= models.EmailField(max_length=100)
  phone =	models.IntegerField
  photo	= models.ImageField(blank=True, upload_to=None, height_field=None, width_field=None)	
  company	= models.CharField(max_length=100)
  about_me = models.TextField(blank=True, max_length=300)
  looking_for	= models.TextField(blank=True)	