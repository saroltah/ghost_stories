# Generated by Django 4.2.10 on 2024-04-16 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_editor_slug_writer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_stories', to=settings.AUTH_USER_MODEL),
        ),
    ]
