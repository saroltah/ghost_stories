# Generated by Django 3.2.4 on 2025-03-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0029_alter_writer_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
