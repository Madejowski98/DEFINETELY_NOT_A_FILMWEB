# Generated by Django 5.0.6 on 2024-06-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies_app", "0003_alter_movie_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="approved",
            field=models.BooleanField(default=False),
        ),
    ]
