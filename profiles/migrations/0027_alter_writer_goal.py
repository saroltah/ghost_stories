# Generated by Django 4.2.10 on 2024-05-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0026_writer_vis_alter_writer_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='goal',
            field=models.CharField(choices=[('Writer', 'Writer'), ('Editor', 'Editor')], default='Writer', max_length=9),
        ),
    ]
