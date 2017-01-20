from django.db import models
from django.core.urlresolvers import reverse

from .managers import *

from eda5.arhiv.models import Arhiviranje
from eda5.core.models import TimeStampedModel, IsActiveModel, Opombe
from eda5.etaznalastnina.models import LastniskaEnotaElaborat, LastniskaEnotaInterna
from eda5.partnerji.models import SkupinaPartnerjev
from eda5.zahtevki.models import Zahtevek


class PredajaLastnine(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    zahtevek = models.OneToOneField(Zahtevek, blank=True, null=True)
    prodajalec = models.ForeignKey(SkupinaPartnerjev, related_name="prodajalec")
    kupec = models.ForeignKey(SkupinaPartnerjev, related_name="kupec")
    #   Mandatory
    oznaka = models.CharField(max_length=20, unique=True)  # LST-2016-1
    #   Optional
    # OBJECT MANAGER
    objects = PredajaLastnineManager()
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


class ProdajaLastnine(Opombe):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    predaja_lastnine = models.ForeignKey(PredajaLastnine)
    lastniska_enota = models.ForeignKey(LastniskaEnotaElaborat, blank=True, null=True, verbose_name="LE")

    #   Mandatory
    placnik = models.ForeignKey(SkupinaPartnerjev)
    datum_predaje = models.DateField()
    zapisnik_izrocitev = models.ForeignKey(Arhiviranje, blank=True, null=True, related_name="prodaja_izrocitev_zapisnik")

    #   Optional
    # OBJECT MANAGER
    objects = ProdajaLastnineManager()
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


class NajemLastnine(Opombe):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    predaja_lastnine = models.ForeignKey(PredajaLastnine)
    lastniska_enota = models.ForeignKey(LastniskaEnotaInterna, blank=True, null=True, verbose_name="LE")

    #   Mandatory
    najemna_pogodba = models.ForeignKey(Arhiviranje, blank=True, null=True, related_name="najemna_pogodba")
    placnik = models.ForeignKey(SkupinaPartnerjev)
    predaja_datum = models.DateField()
    veljavnost_datum = models.DateField(blank=True, null=True)
    veljavnost_trajanje_opisno = models.CharField(max_length=255, blank=True, null=True, verbose_name="trajanje pogodbe - opisno")
    zapisnik_izrocitev = models.ForeignKey(Arhiviranje, blank=True, null=True, related_name="najem_izrocitev_zapisnik")
    vracilo_datum = models.DateField(blank=True, null=True)
    vracilo_zapisnik = models.ForeignKey(Arhiviranje, blank=True, null=True, related_name="najem_vracilo_zapisnik")
    vracilo_posebnosti = models.CharField(max_length=255, blank=True, null=True)
    #   Optional
    # OBJECT MANAGER
    objects = NajemLastnineManager()
    # CUSTOM PROPERTIES
    # METHODS
    def get_absolute_url(self):
        return reverse("moduli:zahtevki:zahtevek_detail", kwargs={'pk': self.predaja_lastnine.zahtevek.pk})


    # META AND STRING
    class Meta:
        verbose_name = "najem lastnine"
        verbose_name_plural = "najem lastnine"

    def __str__(self):
        return "%s | %s | %s" % (
            self.predaja_lastnine.oznaka,
            self.lastniska_enota.oznaka,
            self.predaja_datum,
            )
