from django.db import models
from django.core.urlresolvers import reverse

from. import managers

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
    def get_absolute_url(self):
        return reverse("moduli:skladisce:dobava_detail", kwargs={"pk": self.pk})

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
    dobavitelj = models.ForeignKey(Partner)
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
        return "%s(%s)" % (self.naziv, self.oznaka)


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
    # DDV = (
    #     (0.095, '9,5%'),
    #     (0.20, '22,0%'),
    # )

    # ATRIBUTES
    #   Relations
    dobava = models.ForeignKey(Dobava, blank=True, null=True)
    artikel = models.ForeignKey(Artikel)
    delovninalog = models.ForeignKey(DelovniNalog, blank=True, null=True, verbose_name="delovni nalog")
    likvidiral = models.ForeignKey(Oseba, verbose_name="likvidiral blago")
    #   Mandatory
    kom = models.IntegerField()
    #   Optional
    cena = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)  # zneski do 9999,99 EUR
    stopnja_ddv = models.DecimalField(blank=True, null=True, decimal_places=3, max_digits=4)  # 0,095 :  0,200

    # OBJECT MANAGER
    objects = managers.DnevnikManager()

    # CUSTOM PROPERTIES
    @property
    def datum(self):
        datum = self.created
        datum = datum.date()
        return datum

    @property
    def storitev(self):
        if self.dobava:
            return "dobava"
        if self.delovninalog:
            return "poraba"

    @property
    def cena_z_ddv(self):
        cena_z_ddv = self.cena * (1 + self.stopnja_ddv)
        return cena_z_ddv

    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "dnevnik"
        verbose_name_plural = "dnevnik"

    def __str__(self):
        if self.dobava:
            return "%s: %s | %s | %s %s" % ('dobava', self.datum, self.artikel,  self.kom, 'kom')
        if self.delovninalog:
            return "%s: %s | %s | %s %s" % ('poraba', self.datum, self.artikel, self.kom, 'kom')
