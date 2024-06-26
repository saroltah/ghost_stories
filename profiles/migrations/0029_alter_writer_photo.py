# Generated by Django 4.2.10 on 2024-05-13 18:42

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0028_alter_writer_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
