from django.db import models
from django.utils import timezone
from django.urls import reverse
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class Writer(models.Model):
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  name	= models.CharField(max_length=50)
  username = models.CharField(max_length=50)
  slug = AutoSlugField (unique=True, populate_from='username')
  email	= models.EmailField(max_length=100)
  phone =	models.IntegerField
  photo	= models.ImageField(blank=True, upload_to=None, height_field=None, width_field=None)
  about_me = models.TextField(blank=True, max_length=300)	
  resume = models.FileField(blank=True)

  def __str__(self):
    return str(self.user)

  def get_absolute_url(self):
    return reverse("writer_details", kwargs={"writer_slug": self.slug})

#class Editor(models.Model):
#  name = models.CharField(max_length=50)
#  username = models.CharField(max_length=50)
#  slug = AutoSlugField (unique=True, populate_from='name')
#  email	= models.EmailField(max_length=100)
#  phone =	models.IntegerField
#  photo	= models.ImageField(blank=True, upload_to=None, height_field=None, width_field=None)	
#  company	= models.CharField(max_length=100)
#  about_me = models.TextField(blank=True, max_length=300)
#  looking_for	= models.TextField(blank=True)
#
#  def __str__(self):
#    return f"Editor: {self.name}"
#
#  def get_absolute_url(self):
#    return reverse("editor_detail", kwargs={"slug": self.slug})