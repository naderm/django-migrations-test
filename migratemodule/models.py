from django.db import models

# Create your models here.
class ModelTest(models.Model):
    SPRING = "Sp"
    SUMMER = "Su"
    FALL = "Fa"
    SEASON_CHOICES =(
        (SPRING, "Spring"),
        (SUMMER, "Summer"),
        (FALL, "Fall"),
        )
    season = models.CharField(
        max_length=2,
        choices=SEASON_CHOICES,
        default=SPRING,
        )
    year = models.PositiveSmallIntegerField(
        max_length=4,
        )

    class Meta:
        unique_together = ("season", "year")
