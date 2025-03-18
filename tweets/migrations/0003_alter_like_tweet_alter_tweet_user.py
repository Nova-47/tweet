# Generated by Django 5.1.7 on 2025-03-18 06:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tweets", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="tweet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="likes",
                to="tweets.tweet",
            ),
        ),
        migrations.AlterField(
            model_name="tweet",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tweets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
