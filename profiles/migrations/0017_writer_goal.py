# Generated by Django 4.2.10 on 2024-05-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_alter_writer_facebook_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='goal',
            field=models.CharField(choices=[('WRITER', 'Writer'), ('EDITOR', 'Editor')], default='Writer', max_length=9),
        ),
    ]
