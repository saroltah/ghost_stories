from django.db import models
from django.utils import timezone
from django.urls import reverse
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError


def validate_image_size(value):
    if isinstance(value, bool):
        return
    max_size = 10 * 1024 * 1024  # 1MB
    if value.size > max_size:
        raise ValidationError(f"Image size should be less than 10 MB.")


class Writer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True)
    slug = models.SlugField(unique=True)
    GOAL_CHOICES = (
        ("Writer", "Writer"),
        ("Editor", "Editor"),
    )
    goal = models.CharField(max_length=9,
                            choices=GOAL_CHOICES,
                            default="Writer")
    VIS_CHOICES = (
        ("Visible", "Visible"),
        ("Hidden", "Hidden"),
    )
    vis = models.CharField(max_length=9,
                           choices=VIS_CHOICES,
                           default="Visible")
    email = models.EmailField(max_length=100)
    phone = models.CharField(blank=True)
    photo = CloudinaryField('image',
                            default='placeholder',
                            blank=True,
                            validators=[validate_image_size]
                            )
    about_me = models.TextField(blank=True)
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
