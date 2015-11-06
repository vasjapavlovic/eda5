from django.db import models
from django.core.urlresolvers import reverse

from eda5.core.models import TimeStampedModel, ObdobjeLeto, ObdobjeMesec, IsLikvidiranModel
from eda5.lastnistvo.models import LastniskaSkupina
from eda5.posta.models import Dokument
from eda5.delovninalogi.models import DelovniNalog


from .managers import RacunManager


class Racun(TimeStampedModel, IsLikvidiranModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    dokument = models.ForeignKey(Dokument)
    davcna_klasifikacija = models.ForeignKey("DavcnaKlasifikacija")
    obdobje_obracuna_leto = models.ForeignKey(ObdobjeLeto)
    obdobje_obracuna_mesec = models.ForeignKey(ObdobjeMesec)
    '''***DODAJ RELACIJO NA NAROČILA***'''
    # ***Mandatory***
    datum_storitve_od = models.DateField()
    datum_storitve_do = models.DateField()
    # ***Optional***

    # OBJECT MANAGER
    objects = RacunManager()
    # CUSTOM PROPERTIES

    # METHODS
    def get_absolute_url(self):
        return reverse("moduli:racunovodstvo:home")

    # META AND STRING
    class Meta:
        verbose_name = 'račun'
        verbose_name_plural = "računi"

    def __str__(self):
        return "%s" % (self.dokument.oznaka)


class DavcnaKlasifikacija(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    # ***Mandatory***
    oznaka = models.CharField(max_length=10)
    naziv = models.CharField(max_length=50)
    opis = models.CharField(max_length=255)
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'davčna klasifikacija'
        verbose_name_plural = "davčna klasifikacija"

    def __str__(self):
        return "%s" % (self.naziv)


class Konto(models.Model):

    # ATRIBUTES
    # ***Relations***
    # ***Mandatory***
    oznaka = models.CharField(max_length=10)
    naziv = models.CharField(max_length=50)
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'konto'
        verbose_name_plural = "konti"
        ordering = ("oznaka",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class PodKonto(models.Model):
    # ---------------------------------------------------------------------------------------

    # ATRIBUTES
    # ***Relations***
    skupina = models.ForeignKey(Konto)
    # ***Mandatory***
    oznaka = models.CharField(max_length=10)
    naziv = models.CharField(max_length=50)
    zap_st = models.IntegerField(default=0, verbose_name="zaporedna Številka",)
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'pod konto'
        verbose_name_plural = "pod konti"
        ordering = ("zap_st",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class SkupinaVrsteStroska(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    skupina = models.ForeignKey(PodKonto)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=200)
    zap_st = models.IntegerField(default=0, verbose_name="zaporedna Številka",)
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'skupina vrste stroška'
        verbose_name_plural = "skupine vrst stroškov"
        ordering = ("zap_st",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class VrstaStroska(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    skupina = models.ForeignKey(SkupinaVrsteStroska)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=200)
    zap_st = models.IntegerField(default=0, verbose_name="zaporedna Številka",)
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'vrsta stroška'
        verbose_name_plural = "vrste stroškov"
        ordering = ("zap_st",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class Strosek(models.Model):
    # ---------------------------------------------------------------------------------------
    DELILNIK_VRSTA = (
            ("fiksni", "fiksni strošek"),
            ("vuporabi", "LE v uporabi"),
            ("delilniki", "po priloženem delilniku"),
        )

    DELILNIK_KLJUC = (
            ("lastniski_delez", "lastniški delež"),
            ("povrsina", "površina enote"),
            ("st_enot", "število enot"),
            ("oseba", "število oseb"),
        )

    # ATRIBUTES
    # ***Relations***
    racun = models.ForeignKey(Racun)
    lastniska_skupina = models.ForeignKey(LastniskaSkupina)
    vrsta_stroska = models.ForeignKey(VrstaStroska)
    delovni_nalog = models.OneToOneField(DelovniNalog, blank=True, null=True)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=200)
    datum_storitve_od = models.DateField()
    datum_storitve_do = models.DateField()
    # vrednosti do 99.999,99 EUR (na dve decimalni mesti natančno)
    vrednost = models.DecimalField(decimal_places=2, max_digits=7)
    # 0.22(22%) in 0.095(9,5%) | 0.000
    stopnja_ddv = models.DecimalField(decimal_places=3, max_digits=4)
    delilnik_vrsta = models.CharField(max_length=50, choices=DELILNIK_VRSTA)
    delilnik_kljuc = models.CharField(max_length=50, choices=DELILNIK_KLJUC)
    is_strosek_posameznidel = models.BooleanField(verbose_name="strosek na posameznem delu")
    # ***Optional***
    # OBJECT MANAGER

    # CUSTOM PROPERTIES
    @property
    def strosek_z_ddv(self):
        strosek_z_ddv = self.vrednost * (1 + self.stopnja_ddv)
        return strosek_z_ddv

    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'strošek'
        verbose_name_plural = 'stroški'
        ordering = ("oznaka",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)
