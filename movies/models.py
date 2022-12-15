from django.db import models


class ParentalRules(models.TextChoices):
    Rated_G = "G"
    Rated_PG = "PG"
    Rated_PG_13 = "PG-13"
    Rated_R = "R"
    Rated_NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        choices=ParentalRules.choices,
        default=ParentalRules.Rated_G,
    )
    synopsis = models.TextField(null=True, default=None)

    user = models.ForeignKey(
        "users.Users",
        on_delete=models.CASCADE,
        related_name="movies",
    )

    movieOrder = models.ManyToManyField(
        "users.Users",
        through="movies.MovieOrder",
        related_name="user_buy_movies",
    )

    def __repr__(self) -> str:
        return f"<[{self.tittle}] - usuário:{self.user}>"


class MovieOrder(models.Model):
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movieOrders",
    )

    user = models.ForeignKey(
        "users.Users",
        on_delete=models.CASCADE,
        related_name="userMovieOrders",
    )

    price = models.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = models.DateTimeField(auto_now_add=True)
