from django.db import models

from eda5.core.models import TimeStampedModel
from eda5.partnerji.models import Oseba
from eda5.posta.models import Dokument


class Arhiv(models.Model):
    oznaka = models.CharField(max_length=10, verbose_name='oznaka')
    naziv = models.CharField(max_length=255, verbose_name='naziv')

    class Meta:
        verbose_name = "arhiv"
        verbose_name_plural = "arhivi"

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)


class ArhivMesto(models.Model):

    arhiv = models.ForeignKey(Arhiv)
    oznaka = models.CharField(max_length=10, verbose_name='oznaka')
    naziv = models.CharField(max_length=255, verbose_name='naziv')

    class Meta:
        verbose_name = "arhivsko mesto"
        verbose_name_plural = "arhivska mesta"

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)


class Arhiviranje(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    dokument = models.OneToOneField(Dokument, blank=True, null=True)
    arhiviral = models.ForeignKey(Oseba)
    lokacija_hrambe = models.ForeignKey(ArhivMesto, blank=True, null=True, verbose_name="lokacija hrambe")
    #   Mandatory
    elektronski = models.BooleanField(default=True, verbose_name="elektronski hramba")
    fizicni = models.BooleanField(default=False, verbose_name="fizični hramba")
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "arhiviranje"
        verbose_name_plural = "arhiviranje"

    def __str__(self):
        return "%s | %s" % (self.dokument, self.lokacija_hrambe)
