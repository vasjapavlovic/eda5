from django.db import models

from eda5.core.models import ZaporednaStevilka


class PredpisSklop(ZaporednaStevilka):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    oznaka = models.CharField(max_length=25, unique=True)
    naziv = models.CharField(max_length=255)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "sklop predpisov"
        verbose_name_plural = "sklopi predpisov"
        ordering = ("zap_st",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class PredpisPodsklop(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    predpis_sklop = models.ForeignKey(PredpisSklop, blank=True, null=True)
    #   Mandatory
    oznaka = models.CharField(max_length=25, unique=True)
    naziv = models.CharField(max_length=255)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "podsklop predpisov"
        verbose_name_plural = "podsklopi predpisov"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class PredpisOpravilo(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    predpis_podsklop = models.ForeignKey(PredpisPodsklop, blank=True, null=True)
    predpis = models.ManyToManyField("Predpis", blank=True)
    #   Mandatory
    oznaka = models.CharField(max_length=25, unique=True)
    naziv = models.CharField(max_length=255)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "predpisano opravilo"
        verbose_name_plural = "predpisana opravila"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class Predpis(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    oznaka = models.CharField(max_length=25, unique=True)
    naziv = models.CharField(max_length=255)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "predpis"
        verbose_name_plural = "predpisi"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)
