from django.db import models
import jsonfield

# Create your models here.


class Accident(models.Model):
    year = models.CharField(max_length=6)
    month = models.CharField(max_length=4)

    def __str__(self):
        return self.year
