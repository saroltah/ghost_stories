# Generated by Django 4.2.10 on 2024-04-27 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_remove_writer_id_alter_writer_username'),
        ('stories', '0013_alter_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.writer'),
        ),
    ]
