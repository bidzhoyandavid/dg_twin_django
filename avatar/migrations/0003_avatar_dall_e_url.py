# Generated by Django 5.0.2 on 2025-03-01 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avatar', '0002_remove_avatar_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='dall_e_url',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
