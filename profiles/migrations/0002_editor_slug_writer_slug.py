# Generated by Django 4.2.10 on 2024-04-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='editor',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='writer',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]