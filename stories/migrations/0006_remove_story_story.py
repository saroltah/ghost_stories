# Generated by Django 4.2.10 on 2024-04-16 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_story_slug_alter_comment_commented_story_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='story',
        ),
    ]
