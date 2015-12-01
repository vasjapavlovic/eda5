from django.db import models

from eda5.posta.models import Dokument
from eda5.core.models import TimeStampedModel, IsActiveModel


class SklopPlanov(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    oznaka = models.CharField(max_length=25)
    naziv = models.CharField(max_length=255)
    #   Optional
    zap_st = models.IntegerField(default=0, verbose_name="zaporedna številka")
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "sklop planov"
        verbose_name_plural = "sklopi planov"
        ordering = ("zap_st",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class Plan(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    sklop = models.ForeignKey(SklopPlanov)
    #   Mandatory
    oznaka = models.CharField(max_length=25)
    naziv = models.CharField(max_length=255)
    #   Optional
    zap_st = models.IntegerField(default=0, verbose_name="zaporedna številka")
    opis = models.CharField(max_length=255)
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "plan"
        verbose_name_plural = "plani"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class PlanIzdaja(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    plan = models.ForeignKey(Plan)
    '''dodaj, da je potrebna potrditvena dokumentacija za plan'''
    #   Mandatory
    oznaka = models.CharField(max_length=20, blank=True)
    datum_izdaje = models.DateField()
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "izdaja plana"
        verbose_name_plural = "izdaje planov"

    def __str__(self):
        return "%s | %s(%s)" % (self.datum_izdaje, self.plan.naziv, self.plan.oznaka)


class PlanOpravilo(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
    dan = 'dan'
    teden = 'teden'
    mesec = 'mesec'
    leto = 'leto'

    ENOTE = (
        (dan, "Dan"),
        (teden, "Teden"),
        (mesec, "Mesec"),
        (leto, "Leto")
        )
    # ATRIBUTES
    #   Relations
    plan = models.ForeignKey(PlanIzdaja, verbose_name="izdaja plana")
    #   Mandatory
    oznaka = models.CharField(max_length=25)
    naziv = models.CharField(max_length=255)
    namen = models.CharField(max_length=255)
    obseg = models.TextField()
    perioda_predpisana_enota = models.CharField(max_length=5, choices=ENOTE, verbose_name="enota periode")
    perioda_predpisana_enota_kolicina = models.IntegerField(verbose_name="kolicina enote periode")
    perioda_predpisana_kolicina_na_enoto = models.IntegerField(verbose_name="kolicina na enoto periode")
    #   Optional
    opomba = models.TextField(blank=True)
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "planirano opravilo"
        verbose_name_plural = "planirana opravila"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)
