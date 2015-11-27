from django.db import models

from eda5.core.models import TimeStampedModel


class Proizvajalec(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    # ***Mandatory***
    naziv = models.CharField(max_length=100, unique=True)
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'proizvajalec'
        verbose_name_plural = 'proizvajalci'
        ordering = ('naziv',)

    def __str__(self):
        return "%s" % (self.naziv)


class TipArtikla(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'tip artikla'
        verbose_name_plural = 'tipi artiklov'
        ordering = ('oznaka',)

    def __str__(self):
        return "(%s)%s" % (self.oznaka, self.naziv)


class ModelArtikla(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    proizvajalec = models.ForeignKey(Proizvajalec)
    # ***Mandatory***
    tip = models.ForeignKey(TipArtikla)
    naziv = models.CharField(max_length=255)
    # ***Optional***
    P1_title = models.CharField(max_length=255, verbose_name='P1 title',
                                null=True, blank=True,)
    P1_value = models.CharField(max_length=255, verbose_name='P1 value',
                                null=True, blank=True,)
    P2_title = models.CharField(max_length=255, verbose_name='P2 title',
                                null=True, blank=True,)
    P2_value = models.CharField(max_length=255, verbose_name='P2 value',
                                null=True, blank=True,)
    P3_title = models.CharField(max_length=255, verbose_name='P3 title',
                                null=True, blank=True,)
    P3_value = models.CharField(max_length=255, verbose_name='P3 value',
                                null=True, blank=True,)
    P4_title = models.CharField(max_length=255, verbose_name='P4 title',
                                null=True, blank=True,)
    P4_value = models.CharField(max_length=255, verbose_name='P4 value',
                                null=True, blank=True,)
    P5_title = models.CharField(max_length=255, verbose_name='P5 title',
                                null=True, blank=True,)
    P5_value = models.CharField(max_length=255, verbose_name='P5 value',
                                null=True, blank=True,)
    # OBJECT MANAGER

    # CUSTOM PROPERTIES
    @property
    def sorted_planov_set(self):
        return self.planov_set.order_by('oznaka')
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'model artikla'
        verbose_name_plural = 'modeli artiklov'
        ordering = ('naziv',)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class PlanOV(models.Model):
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
    # ***Relations***
    element = models.ForeignKey(ModelArtikla)
    # ***Mandatory***
    oznaka = models.CharField(max_length=25)
    naziv = models.CharField(max_length=255)
    perioda_predpisana_enota = models.CharField(max_length=5, choices=ENOTE, verbose_name="enota periode")
    perioda_predpisana_enota_kolicina = models.IntegerField(verbose_name="kolicina enote periode")
    perioda_predpisana_kolicina_na_enoto = models.IntegerField(verbose_name="kolicina na enoto periode")
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "Plan Obratovanja in Vzdrževanja"
        verbose_name_plural = "Plan Obratovanja in Vzdrževanja"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class RezervniDel(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    artikel = models.ForeignKey(ModelArtikla)
    # ***Mandatory***

    naziv = models.CharField(max_length=255)
    # ***Optional***
    oznaka = models.CharField(max_length=25, blank=True)
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "Rezervni Del"
        verbose_name_plural = "Rezervni Deli"

    def __str__(self):
        return "%s (%s)" % (self.naziv, self.oznaka)
