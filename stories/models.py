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

  class Meta:
    ordering = ["-created_on"]

  def __str__(self):
    return f"{self.title} written by {self.author}. {self.teaser}"

class Comment(models.Model):
  author = models.OneToOneField(Writer, on_delete=models.CASCADE)
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