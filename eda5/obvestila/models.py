from django.db import models

from eda5.core.models import TimeStampedModel
from eda5.users.models import User


class Obvestilo(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    user = models.ForeignKey(User)
    #   Mandatory
    onaka = models.CharField(max_length=50)
    naziv = models.CharField(max_length=255)
    vsebina = models.TextField()
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "obvestilo"
        verbose_name_plural = "obvestila"
        ordering = "created"

    def __str__(self):
        return "(%s) %s" % (self.oznaka, self.naziv)


class Komentar(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    vsebina = models.TextField()
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "komentar"
        verbose_name_plural = "komentarji"
        ordering = "created"

    def __str__(self):
        return "(%s) %s" % (self.naziv)
