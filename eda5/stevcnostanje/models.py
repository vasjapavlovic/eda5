from django.db import models

from eda5.core.models import ObdobjeLeto, ObdobjeMesec, TimeStampedModel, ZaporednaStevilka
from eda5.deli.models import ProjektnoMesto
from eda5.partnerji.models import Partner, Oseba
from . import managers


class Stevec(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   __lokacija
    projektno_mesto = models.ForeignKey(ProjektnoMesto, null=True, blank=True)
    upravljavec = models.ForeignKey(Partner)
    # lokacija stevca !!!!!!
    #   Mandatory
    oznaka = models.CharField(max_length=13, unique=True)
    naziv = models.CharField(max_length=255)
    is_distribucija = models.BooleanField(verbose_name="distribucijski števec")
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "števec"
        verbose_name_plural = "števci"
        ordering = ("oznaka",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class StevecStatus(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    stevec = models.ForeignKey(Stevec)
    #   Mandatory
    v_okvari = models.BooleanField()
    v_delovanju = models.BooleanField()  # ventili pred ali za števcem odprti
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "status števca"
        verbose_name_plural = "status števcev"
        ordering = ("updated",)

    def __str__(self):
        return "%s | %s" % (self.updated, self.stevec)


class MeritevVrsta(ZaporednaStevilka):
    # --------------------------------------------------------------------------------------
    # ATRIBUTES
    oznaka = models.CharField(max_length=13, unique=True)
    naziv = models.CharField(max_length=255)

    # META AND STRING
    class Meta:
        verbose_name = "vrsta meritve"
        verbose_name_plural = "vrste meritev"
        ordering = ("zap_st",)

    def __str__(self):
        return "%s | %s" % (self.stevec, self.oznaka)



class Delilnik(models.Model):
    # ---------------------------------------------------------------------------------------

    MERITEV = (
        (1, "Toplota [MWh]"),
        (2, "Hlad [MWh]"),
        (3, "Topla voda [m3]"),
        (4, "Hladna voda [m3]"),
        (5, "Elektrika [kWh]"),
        )

    # ATRIBUTES
    #   Relations

    #   Mandatory
    oznaka = models.CharField(max_length=20, unique=True)
    naziv = models.CharField(max_length=255, blank=True, null=True)
    meritev_vrsta = models.ForeignKey(MeritevVrsta, blank=True, null=True)

    # Relacija na števec ( en števec ima lahko več delilnikov)
    stevec = models.ForeignKey(Stevec)

    # ODSTRANI - potrebne so bile zaradi migracije
    meritev = models.IntegerField(choices=MERITEV)
    opis = models.CharField(max_length=255, blank=True, null=True)


    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "delilnik"
        verbose_name_plural = "delilniki"
        ordering = ("stevec",)

    def __str__(self):
        return "%s | %s" % (self.stevec, self.oznaka)


class Odcitek(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    delilnik = models.ForeignKey(Delilnik)
    obdobje_leto = models.ForeignKey(ObdobjeLeto)
    obdobje_mesec = models.ForeignKey(ObdobjeMesec)
    odcital = models.ForeignKey(Oseba, null=True, blank=True, verbose_name="odčital")
    #   Mandatory
    datum_odcitka = models.DateField()
    stanje_staro = models.DecimalField(max_digits=15, decimal_places=3)
    stanje_novo = models.DecimalField(max_digits=15, decimal_places=3)
    #   Optional

    # OBJECT MANAGER
    objects = managers.OdcitekManager()

    # CUSTOM PROPERTIES
    @property
    def poraba(self):
        return (self.stanje_novo - self.stanje_staro)

    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "odcitek"
        verbose_name_plural = "odcitki"
        ordering = ("delilnik", "datum_odcitka", )
        unique_together = ("delilnik", "obdobje_leto", "obdobje_mesec")

    def __str__(self):
        return "%s | %s-%s" % (self.delilnik, self.obdobje_leto, self.obdobje_mesec)
