from django.db import models
from eda5.partnerji.models import Partner
from eda5.etaznalastnina.models import LastniskaEnotaInterna


class PredajaLastnine(models.Model):
    TIPI_PREDAJE = (
        ('A', 'predaja v last'),
        ('B', 'predaja v najem'),
    )

    oznaka = models.CharField(max_length=3)
    datum = models.DateField()
    tip_predaje = models.CharField(max_length=1, choices=TIPI_PREDAJE, verbose_name='ti predaje etažne lastnine')
    prodajalec = models.ForeignKey(Partner, related_name="prodajalec")
    kupec = models.ForeignKey(Partner, related_name="kupec")
    lastniska_enota_interna = models.ForeignKey(LastniskaEnotaInterna, verbose_name="Interna lastniška enota")
    trajanje = models.CharField(max_length=50)
    dokument = models.CharField(max_length=50)

    class Meta:
        verbose_name = "predaja lastnine"
        verbose_name_plural = "predaje lastnine"

    def __str__(self):
        return "001 | Predaja v last | 10330" % (self.oznaka, self.tip_predaje, self.lastniska_enota_interna.oznaka)


class Daljinec(models.Model):
    pass


class PredajaDaljinca(models.Model):
    pass
