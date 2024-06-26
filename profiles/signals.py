from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Writer
from django.utils.text import slugify


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Writer.objects.create(user=instance, username=instance.username),
