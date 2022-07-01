from django.db import models

# Create your models here.


class Accident(models.Model):
    year = models.CharField(max_length=6, default=2021)
    month = models.CharField(max_length=4, default=1)

    def __str__(self):
        return self.year
