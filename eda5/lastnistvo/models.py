from django.db import models

from .managers import *


class Program(models.Model):

    # ATRIBUTES
    # ***Relations***
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    zap_st = models.IntegerField(default=0, verbose_name="zaporedna Številka",)
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programi"
        ordering = ("zap_st",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class LastniskaSkupina(models.Model):

    # ATRIBUTES
    # ***Relations***
    program = models.ForeignKey(Program)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    opis = models.CharField(max_length=255, blank=True)
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "lastniška skupina"
        verbose_name_plural = "lastniške skupine"
        ordering = ("oznaka",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)
