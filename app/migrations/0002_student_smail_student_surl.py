# Generated by Django 4.1.7 on 2023-05-10 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="Smail",
            field=models.EmailField(default=0, max_length=254),
        ),
        migrations.AddField(
            model_name="student",
            name="Surl",
            field=models.URLField(default=0),
        ),
    ]