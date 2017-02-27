from django.db import models

# Core
from eda5.core.models import TimeStampedModel, IsActiveModel


class Stavba(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------

    # ATRIBUTES


    oznaka = models.CharField(
        max_length=20, unique=True,
        verbose_name="Oznaka")

    naziv = models.CharField(
        max_length=255, blank=True, null=True, 
        verbose_name="Naziv")

    opis = models.TextField(
        blank=True, null=True, 
        verbose_name="Opis")


    # META AND STRING
    class Meta:
        verbose_name = "Stavba"
        verbose_name_plural = "Stavbe"
        ordering = ["oznaka", ]

    def __str__(self):
        return "%s. %s" % (self.oznaka, self.naziv)


class Etaza(TimeStampedModel, IsActiveModel):


    # ATRIBUTES

    oznaka = models.CharField(
        max_length=50, unique=True,
        verbose_name="Oznaka")

    naziv = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="Naziv")

    opis = models.TextField(
        blank=True, null=True, 
        verbose_name="Opis")

    #R STAVBA Relacija na Stavbo
    stavba = models.ForeignKey(
        Stavba, 
        verbose_name="Stavba")


    # META AND STRING
    class Meta:
        verbose_name = "Etaža"
        verbose_name_plural = "Etaže"
        ordering = ["oznaka", ]

    def __str__(self):
        return "%s. %s" % (self.oznaka, self.naziv)


class Prostor(TimeStampedModel, IsActiveModel):
    

    # ATRIBUTES


    oznaka = models.CharField(
        max_length=20, unique=True,
        verbose_name="Oznaka")

    naziv = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="Naziv")

    opis = models.TextField(
        blank=True, null=True, 
        verbose_name="Opis")

    #R ETAŽA. Relacija na etažo.
    etaza = models.ForeignKey(
        Etaza, 
        verbose_name="Etaža")

    # BIM ID. Navezava na BIM program
    bim_id = models.CharField(
        max_length=100, blank=True, null=True, 
        verbose_name='BIM ID')


    # META AND STRING
    class Meta:
        verbose_name = "Prostor"
        verbose_name_plural = "Prostori"
        ordering = ["oznaka", ]

    def __str__(self):
        return "%s. %s" % (self.oznaka, self.naziv)
