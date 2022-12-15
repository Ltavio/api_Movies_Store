# Generated by Django 4.1.4 on 2022-12-15 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MovieOrder",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("buyed_ad", models.DateTimeField(auto_now_add=True)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movieOrders",
                        to="movies.movie",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="userMovieOrders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="movie",
            name="movieOrder",
            field=models.ManyToManyField(
                related_name="user_buy_movies",
                through="movies.MovieOrder",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
