# Generated by Django 4.2.10 on 2024-04-03 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to=None)),
                ('company', models.CharField(max_length=100)),
                ('about_me', models.TextField(blank=True, max_length=300)),
                ('looking_for', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to=None)),
                ('about_me', models.TextField(blank=True, max_length=300)),
                ('resume', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
