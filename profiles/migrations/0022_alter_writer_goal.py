# Generated by Django 4.2.10 on 2024-05-09 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0021_alter_writer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='goal',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goals', to=settings.AUTH_USER_MODEL),
        ),
    ]