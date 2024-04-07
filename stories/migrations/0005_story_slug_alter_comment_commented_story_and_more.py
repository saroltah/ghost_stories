# Generated by Django 4.2.10 on 2024-04-06 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_alter_story_options_like_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='stories.story'),
        ),
        migrations.AlterField(
            model_name='like',
            name='liked_story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='stories.story'),
        ),
    ]