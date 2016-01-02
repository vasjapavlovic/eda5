from django.db import models

from .managers import *

from eda5.core.models import TimeStampedModel, IsActiveModel
from eda5.etaznalastnina.models import LastniskaEnotaElaborat, LastniskaEnotaInterna
from eda5.partnerji.models import SkupinaPartnerjev


class PredajaLastnine(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    prodajalec = models.ForeignKey(SkupinaPartnerjev, related_name="prodajalec")
    kupec = models.ForeignKey(SkupinaPartnerjev, related_name="kupec")
    #   Mandatory
    oznaka = models.CharField(max_length=20, unique=True)  # LST-2016-1
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "predaja lastnine"
        verbose_name_plural = "predaje lastnine"

    def __str__(self):
        return "%s | %s | %s" % (
            self.oznaka,
            self.prodajalec.naziv,
            self.kupec.naziv,
            )


class ProdajaLastnine(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    predaja_lastnine = models.ForeignKey(PredajaLastnine)
    lastniska_enota = models.ForeignKey(LastniskaEnotaElaborat, blank=True, null=True, verbose_name="LE")

    #   Mandatory
    placnik = models.ForeignKey(SkupinaPartnerjev)
    datum_predaje = models.DateField()

    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "prodaja lastnine"
        verbose_name_plural = "prodaja lastnine"

    def __str__(self):
        return "%s | %s | %s" % (
            self.predaja_lastnine.oznaka,
            self.lastniska_enota.oznaka,
            self.datum_predaje,
            )


class NajemLastnine(IsActiveModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    predaja_lastnine = models.ForeignKey(PredajaLastnine)
    lastniska_enota = models.ForeignKey(LastniskaEnotaInterna, blank=True, null=True, verbose_name="LE")

    #   Mandatory
    placnik = models.ForeignKey(SkupinaPartnerjev)
    datum_predaje = models.DateField()
    datum_veljavnosti = models.DateField(blank=True, null=True)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "najem lastnine"
        verbose_name_plural = "najem lastnine"

    def __str__(self):
        return "%s | %s | %s" % (
            self.predaja_lastnine.oznaka,
            self.lastniska_enota.oznaka,
            self.datum_predaje,
            )
