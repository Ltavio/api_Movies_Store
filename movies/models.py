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

    def __repr__(self) -> str:
        return f"<[{self.tittle}] - usuário:{self.user}>"
