# Generated by Django 4.2.10 on 2024-05-09 22:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0027_alter_writer_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='photo',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]