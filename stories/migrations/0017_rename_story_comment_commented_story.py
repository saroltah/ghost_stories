# Generated by Django 4.2.10 on 2024-04-29 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0016_alter_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='story',
            new_name='commented_story',
        ),
    ]