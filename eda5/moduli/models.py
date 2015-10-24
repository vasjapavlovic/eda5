from django.db import models
from eda5.core.models import TimeStampedModel


class Modul(TimeStampedModel):

    oznaka = models.CharField(max_length=10)
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    url_name = models.CharField(max_length=500)

    def __str__(self):
        return "(%s) %s" % (self.oznaka, self.naziv)
