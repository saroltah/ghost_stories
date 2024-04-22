from django.db import models
from django.utils import timezone
from profiles.models import Writer
from django.urls import reverse
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify

# Create your models here.

class Story(models.Model):
  author = models.CharField(max_length=100)	
  title	= models.CharField(max_length=100)	
  slug = AutoSlugField (unique=True, populate_from='title')
  story_text = models.TextField(default='')
  teaser = models.TextField(max_length=500)
  keywords	= models.CharField(max_length=100, default='')	
  image	= models.ImageField(blank=True, upload_to=None, height_field=None, width_field=None)	
  created_on	= models.DateTimeField(auto_now_add=True)
  edited = models.DateTimeField	(auto_now=True)
  

  class Meta:
    ordering = ["-created_on"]

  def __str__(self):
    return f"{self.title} written by {self.author}"

  
  def get_absolute_url(self):
    return reverse("one_story", kwargs={"slug": self.slug})

  def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.title} written by {self.author}"

  
  def get_absolute_url(self):
    return reverse("one_story", kwargs={"slug": self.slug})

class Comment(models.Model):
  author = models.ForeignKey(Writer, on_delete=models.CASCADE)
  content	= models.TextField()		
  created_on	= models.DateTimeField(auto_now_add=True)
  commented_story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="comments")

  class Meta:
    ordering = ["-created_on"]

  def __str__(self):
    return f"{self.author} says: {self.content}."

  def number_of_comments(self):
    return self.content.count


class Like(models.Model):
  user = models.OneToOneField(Writer, on_delete=models.CASCADE)
  liked_story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="likes")

  def number_of_likes(self):
    return self.content.count