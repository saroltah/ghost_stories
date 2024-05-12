from django.db import models
from django.utils import timezone
from profiles.models import Writer
from django.urls import reverse
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Story(models.Model):
    author = models.ForeignKey(Writer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(unique=True, populate_from='title')
    story_text = models.TextField(default='')
    teaser = models.TextField(max_length=500)
    keywords = models.CharField(max_length=100, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="liked_stories")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("one_story", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    author = models.ForeignKey(Writer, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    ccommented_story = models.ForeignKey(
                       Story,
                       on_delete=models.CASCADE,
                       related_name="comments",
                       )

    def get_absolute_url(self):
        return reverse("one_story", kwargs={"slug": self.story.slug})

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.author} says: {self.content}."

    def number_of_comments(self):
        return self.content.count()
