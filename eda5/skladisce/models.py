from django.db import models

from eda5.core.models import TimeStampedModel
from eda5.delovninalogi.models import DelovniNalog
from eda5.partnerji.models import Oseba, Partner
from eda5.posta.models import Dokument


class Dobava(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    prevzel = models.ForeignKey(Oseba)
    dobavitelj = models.ForeignKey(Partner)
    dobavnica = models.OneToOneField(Dokument)
    #   Mandatory
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    datum = models.DateField(verbose_name='datum prevzema blaga')
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "dobava"
        verbose_name_plural = "dobave"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class Artikel(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    tip = models.ForeignKey("TipArtikla")
    dobava = models.ManyToManyField(Dobava, through="Dnevnik")
    #   Mandatory
    oznaka = models.CharField(max_length=50)
    naziv = models.CharField(max_length=255)
    #   Optional
    opis = models.CharField(blank=True, max_length=255)
    st_police = models.IntegerField(blank=True, null=True, verbose_name="številka police")
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "artikel"
        verbose_name_plural = "artikli"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class TipArtikla(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    sklop = models.ForeignKey("SklopArtikla")
    #   Mandatory
    oznaka = models.CharField(max_length=50)
    naziv = models.CharField(max_length=255)
    #   Optional
    opis = models.CharField(blank=True, max_length=255)
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "tip artikla"
        verbose_name_plural = "tipi artiklov"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class SklopArtikla(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    oznaka = models.CharField(max_length=50)
    naziv = models.CharField(max_length=255)
    #   Optional
    opis = models.CharField(blank=True, max_length=255)
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "sklop artikla"
        verbose_name_plural = "sklopi artiklov"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class Dnevnik(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    dobava = models.ForeignKey(Dobava, blank=True, null=True)
    artikel = models.ForeignKey(Artikel)
    delovninalog = models.ForeignKey(DelovniNalog, blank=True, null=True, verbose_name="delovni nalog")
    likvidiral = models.ForeignKey(Oseba, verbose_name="likvidiral blago")
    #   Mandatory
    kom = models.IntegerField()
    nabavna_vrednost = models.DecimalField(decimal_places=2, max_digits=6)  # zneski do 9999,99 EUR
    stopnja_ddv = models.DecimalField(decimal_places=3, max_digits=4)  # 0,095 :  0,200
    #   Optional
    # OBJECT MANAGER

    # CUSTOM PROPERTIES
    @property
    def vrsta(self):
        if self.dobava:
            return "poraba"
        if self.delovninalog:
            return "dobava"

    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "dnevnik"
        verbose_name_plural = "dnevnik"

    def __str__(self):
        return "%s | %s" % (self.artikel, self.likvidiral)
