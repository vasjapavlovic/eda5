from django.db import models

from eda5.core.models import TimeStampedModel, ObdobjeLeto, ObdobjeMesec
from eda5.prejeta_posta.models import Dokument


class Racun(TimeStampedModel):

    dokument = models.ForeignKey(Dokument)
    davcna_klasifikacija = models.ForeignKey("DavcnaKlasifikacija")
    datum_storitve_od = models.DateField()
    datum_storitve_do = models.DateField()
    obdobje_obracuna_leto = models.ForeignKey(ObdobjeLeto)
    obdobje_obracuna_mesec = models.ForeignKey(ObdobjeMesec)

    class Meta:
        verbose_name = 'račun'
        verbose_name_plural = "računi"

    def __str__(self):
        return "%s" % (self.dokument.oznaka)


class DavcnaKlasifikacija(models.Model):

    oznaka = models.CharField(max_length=10)
    naziv = models.CharField(max_length=50)
    opis = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'davčna klasifikacija'
        verbose_name_plural = "davčna klasifikacija"

    def __str__(self):
        return "%s" % (self.naziv)
