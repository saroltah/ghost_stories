# Generated by Django 4.2.10 on 2024-04-03 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('stories', '0002_rename_xyz_stories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stories',
            new_name='Story',
        ),
    ]