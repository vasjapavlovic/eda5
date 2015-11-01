from django.db import models

from eda5.deli.models import Element
from eda5.partnerji.models import Oseba
from eda5.zahtevki.models import Zahtevek
from eda5.narocila.models import Narocilo
from eda5.core.models import TimeStampedModel


class Opravilo(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    zahtevek = models.ForeignKey(Zahtevek)
    narocilo = models.ForeignKey(Narocilo, verbose_name='naročilo')
    '''pod naročilo je odzadaj tudi relacija na naročnika in izvajalca'''
    element = models.ManyToManyField(Element)
    #   Mandatory
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    rok_izvedbe = models.DateField()
    #   Optional
    # OBJECT MANAGER

    # CUSTOM PROPERTIES
    @property
    def delovninalog_koncan_sorted_by_date(self):
        return self.delovninalog_set.exclude(datum_stop__isnull=True).order_by("datum_start")

    @property
    def delovninalog_vdelu_sorted_by_date(self):
        return self.delovninalog_set.exclude(datum_stop__isnull=False).order_by("datum_start")
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "Opravilo"
        verbose_name_plural = "Opravila"

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)


class DelovniNalog(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    opravilo = models.ForeignKey(Opravilo)
    nosilec = models.ForeignKey(Oseba)
    #   Mandatory
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    date_plan = models.DateField(verbose_name='V planu za dne')
    #   Optional
    datum_start = models.DateField(blank=True, null=True, verbose_name="Začeto dne")
    datum_stop = models.DateField(blank=True, null=True, verbose_name="Končano dne")
    # OBJECT MANAGER

    # CUSTOM PROPERTIES
    @property
    def delo_vdelu(self):
        return self.delo_set.filter(time_stop__isnull=True).order_by("-time_start")

    @property
    def delo_koncano(self):
        return self.delo_set.filter(time_stop__isnull=False).order_by("-time_stop")
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "Delovni Nalog"
        verbose_name_plural = "Delovni Nalogi"

    def __str__(self):
        return "%s | %s (%s)" % (self.oznaka, self.opravilo.naziv, self.opravilo.oznaka,)


# DELO
class Delo(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    delavec = models.ForeignKey(Oseba)
    delovninalog = models.ForeignKey(DelovniNalog, verbose_name="delovni nalog")
    #   Mandatory
    #   Optional
    datum = models.DateField(blank=True, null=True)
    time_start = models.TimeField(blank=True, null=True, verbose_name="Ura:Začeto")
    time_start = models.TimeField(blank=True, null=True, verbose_name="Ura:Končano")
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "Delo"
        verbose_name_plural = "Dela"

    def __str__(self):
        return "%s - %s" % (self.datum, self.delavec)
