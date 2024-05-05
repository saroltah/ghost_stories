from django.db import models
from django.utils import timezone
from django.urls import reverse
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.contrib.auth.models import User


class Writer(models.Model):
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  name	= models.CharField(max_length=50)
  username = models.CharField (max_length=50, primary_key=True)
  slug = models.SlugField (unique=True)
  GOAL_CHOICES = (
    ("WRITER", "Writer"),
    ("EDITOR", "Editor"),
   )
  goal = models.CharField(max_length=9,
                  choices=GOAL_CHOICES,
                  default="Writer")
  email	= models.EmailField(max_length=100)
  phone =	models.IntegerField
  photo	= models.ImageField(blank=True, default='example.jpg')
  about_me = models.TextField(blank=True, max_length=300)
  facebook_link = models.CharField(blank=True, max_length=100)
  instagram_link = models.CharField(blank=True, max_length=100)
  linkedin_link = models.CharField(blank=True, max_length=100)

  def __str__(self):
    return str(self.user)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.username)
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse("view_profile", kwargs={"slug": self.slug})
    
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