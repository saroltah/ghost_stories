from django.db import models
from django.utils import timezone

# Create your models here.

class Writer(models.Model):
  name	= models.CharField(on_delete=models.CASCADE,max_length=50)
  username = models.CharField(max_length=50)
  email	= models.EmailField(max_length=100,	class EmailValidator(message=None, code=None, allowlist=None))
  phone =	models.IntegerField(Blank=True)
  photo	= models.ImageField(Blank=True upload_to=None, height_field=None, width_field=None)
  about_me = models.TextField(Blank=True max_length=300)	
  resume = models.FileField(Blank=True)
  my_stories	= ForeignKey(stories.story, on_delete=models.CASCADE)			

class Editor(models.Model):
  name = models.CharField(max_length=50)
  username = models.CharField(max_length=50)
  email	= models.EmailField(max_length=100,	class EmailValidator(message=None, code=None, allowlist=None))
  phone =	models.IntegerField(Blank=True)
  photo	= models.ImageField(Blank=True, upload_to=None, height_field=None, width_field=None)	
  company	= models.CharField(max_length=100)
  about_me = models.TextField(Blank=True max_length=300)
  looking_for	= models.TextField(Blank=True)	