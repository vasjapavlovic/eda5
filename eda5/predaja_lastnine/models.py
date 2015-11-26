from django.db import models
from eda5.partnerji.models import Partner
from eda5.etaznalastnina.models import LastniskaEnotaInterna


class PredajaLastnine(models.Model):
    # ---------------------------------------------------------------------------------------
    TIPI_PREDAJE = (
        ('P', 'predaja v last'),
        ('N', 'predaja v najem'),
    )

    # ATRIBUTES
    #   Relations
    prodajalec = models.ForeignKey(Partner, related_name="prodajalec")
    kupec = models.ForeignKey(Partner, related_name="kupec")
    lastniska_enota_interna = models.ForeignKey(LastniskaEnotaInterna, verbose_name="Interna lastniška enota")
    daljinec = models.ManyToManyField(Daljinec, through="PredajaDaljinca")
    #   Mandatory
    oznaka = models.CharField(max_length=4)
    datum = models.DateField()
    tip_predaje = models.CharField(max_length=1, choices=TIPI_PREDAJE, verbose_name='tip predaje etažne lastnine')
    #   Optional
    trajanje = models.CharField(max_length=50, blank=True)
    dokument = models.CharField(max_length=50, blank=True)
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS
    # META AND STRING

    class Meta:
        verbose_name = "predaja lastnine"
        verbose_name_plural = "predaje lastnine"

    def __str__(self):
        return "%s | %s | %s" % (self.oznaka, self.get_tip_predaje_display(), self.lastniska_enota_interna.oznaka)


class Daljinec(models.Model):
    # ---------------------------------------------------------------------------------------
    STATUS_DALJINCA = (
        (1, "v uporabi"),
        (2, "izklopljen"),
    )

    # ATRIBUTES
    #   Relations
    #   Mandatory
    oznaka = models.CharField(max_length=4)
    status = models.IntegerField(default=1, choices=STATUS_DALJINCA)
    #   Optional
    stevilka = models.CharField(max_length=20, blank=True)
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "daljinec"
        verbose_name_plural = "daljinci"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.get_status_display())


class PredajaDaljinca(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    daljinec = models.ForeignKey(Daljinec)
    predaja_lastnine = models.ForeignKey(PredajaLastnine)
    #   Mandatory
    oznaka = models.CharField(max_length=4)
    datum = models.DateField()
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS
    # META AND STRING
    class Meta:
        verbose_name = "predaja daljinca"
        verbose_name_plural = "predaje daljincev"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.datum)
