from django.db import models

from eda5.core.models import TimeStampedModel
from eda5.predpisi.models import PredpisOpravilo


class TipArtikla(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    # ***Mandatory***
    oznaka = models.CharField(max_length=20, unique=True)
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


class Karakteristika(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    tip_artikla = models.ForeignKey(TipArtikla, blank=True, null=True)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    enota = models.CharField(max_length=20, blank=True)
    opis = models.CharField(max_length=255, blank=True, verbose_name="opis")
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'karakteristika artikla'
        verbose_name_plural = 'karakteristike artiklov'

    def __str__(self):
        return "(%s)%s[%s]" % (self.tip_artikla.naziv, self.oznaka, self.enota)


class ObratovalniParameter(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    tip_artikla = models.ForeignKey(TipArtikla, blank=True, null=True)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    enota = models.CharField(max_length=20, blank=True)
    opis = models.CharField(max_length=255, blank=True, verbose_name="opis")
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'obratovalni parameter'
        verbose_name_plural = 'obratovalni parametri'

    def __str__(self):
        return "(%s)%s[%s]" % (self.tip_artikla.naziv, self.oznaka, self.enota)


class Proizvajalec(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    # ***Mandatory***
    oznaka = models.CharField(max_length=20, unique=True)
    naziv = models.CharField(max_length=100)
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
        return "%s | %s" % (self.oznaka, self.naziv)


class ModelArtikla(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    proizvajalec = models.ForeignKey(Proizvajalec)
    tip_artikla = models.ForeignKey(TipArtikla)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20, unique=True)
    naziv = models.CharField(max_length=255)
    # ***Optional***
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
        return "%s-%s-%s" % (self.proizvajalec.naziv, self.naziv, self.tip_artikla.naziv)


class KarakteristikaVrednost(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    artikel = models.ForeignKey(ModelArtikla, blank=True, null=True)
    karakteristika = models.ForeignKey(Karakteristika)
    #   Mandatory
    vrednost = models.CharField(max_length=20)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "vrednost karakteristike"
        verbose_name_plural = "vrednosti karakteristik"

    def __str__(self):
        return "%s | %s | %s %s" % (self.artikel.naziv, self.karakteristika.oznaka, self.vrednost, self.karakteristika.enota)


class ArtikelPlan(models.Model):
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
    artikel = models.ForeignKey(ModelArtikla)
    predpis_opravilo = models.ForeignKey(PredpisOpravilo, blank=True, null=True)
    # ***Mandatory***
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
        return "%s | %s" % (self.artikel.naziv, self.naziv)


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
