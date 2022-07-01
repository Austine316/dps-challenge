from django.db import models

# Create your models here.


class Accident(models.Model):
    year = models.CharField(max_length=6, null=True)
    month = models.CharField(max_length=4, null=True)

    def __str__(self):
        return self.year
