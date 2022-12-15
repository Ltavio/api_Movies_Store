# Generated by Django 4.1.4 on 2022-12-14 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=127)),
                ("duration", models.CharField(default=None, max_length=10, null=True)),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("G", "Rated G"),
                            ("PG", "Rated Pg"),
                            ("PG-13", "Rated Pg 13"),
                            ("R", "Rated R"),
                            ("NC-17", "Rated Nc 17"),
                        ],
                        default="G",
                        max_length=20,
                    ),
                ),
                ("synopsis", models.TextField(default=None, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movies",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]