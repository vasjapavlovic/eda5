from django.db import models
from django.core.urlresolvers import reverse
from decimal import Decimal

from eda5.core.models import TimeStampedModel, ObdobjeLeto, ObdobjeMesec, IsLikvidiranModel
from eda5.etaznalastnina.models import LastniskaSkupina
from eda5.posta.models import Dokument
from eda5.delovninalogi.models import DelovniNalog
from eda5.narocila.models import Narocilo


from .managers import RacunManager, StrosekManager


class Racun(TimeStampedModel, IsLikvidiranModel):
    # ---------------------------------------------------------------------------------------
    DAVCNA_KLASIFIKACIJA = (
        (0, "podjetje"),
        (1, "razdelilnik"),
    )
    # ATRIBUTES
    # ***Relations***
    obdobje_obracuna_leto = models.ForeignKey(ObdobjeLeto)
    obdobje_obracuna_mesec = models.ForeignKey(ObdobjeMesec)
    narocilo = models.ForeignKey(Narocilo, blank=True, null=True)
    # ***Mandatory***
    davcna_klasifikacija = models.IntegerField(choices=DAVCNA_KLASIFIKACIJA)
    datum_storitve_od = models.DateField()
    datum_storitve_do = models.DateField()
    # ***Optional***
    osnova_0 = models.DecimalField(decimal_places=2, max_digits=7,
                                   blank=True, null=True, verbose_name="osnova brez ddv")
    osnova_1 = models.DecimalField(decimal_places=2, max_digits=7,
                                   blank=True, null=True, verbose_name="osnova nižja stopnja")
    osnova_2 = models.DecimalField(decimal_places=2, max_digits=7,
                                   blank=True, null=True, verbose_name="osnova višja stopnja")

    # OBJECT MANAGER
    objects = RacunManager()

    # CUSTOM PROPERTIES
    @property
    def dokument(self):
        ''' podatke o dokumentu pridobimo iz arhiviranja Prejete ali Izdane Pošte
        Pošta:Aktivnost:Dokument --> Arhiviranje:ArhivMesto --> Racun:Racunovodstvo'''
        return self.arhiviranje.dokument

    @property
    def vrednost_brez_ddv(self):
        if self.osnova_0:
            osnova_0 = self.osnova_0
        else:
            osnova_0 = 0
        if self.osnova_1:
            osnova_1 = self.osnova_1
        else:
            osnova_1 = 0
        if self.osnova_2:
            osnova_2 = self.osnova_2
        else:
            osnova_2 = 0
        vrednost_brez_ddv = Decimal(osnova_0) + Decimal(osnova_1) + Decimal(osnova_2)
        return "%.2f" % (vrednost_brez_ddv)

    @property
    def vrednost_z_ddv(self):
        if self.osnova_0:
            osnova_0 = self.osnova_0
        else:
            osnova_0 = 0
        if self.osnova_1:
            osnova_1 = self.osnova_1
        else:
            osnova_1 = 0
        if self.osnova_2:
            osnova_2 = self.osnova_2
        else:
            osnova_2 = 0
        vrednost_z_ddv = Decimal(osnova_0) + Decimal(osnova_1) * (1 + Decimal(0.095)) +\
                        Decimal(osnova_2) * (1 + Decimal(0.22))
        return "%.2f" % (vrednost_z_ddv)



    # METHODS
    def get_absolute_url(self):
        return reverse("moduli:racunovodstvo:home")

    # META AND STRING
    class Meta:
        verbose_name = 'račun'
        verbose_name_plural = "računi"

    def __str__(self):
        return "%s | %s" % (self.dokument.oznaka, self.dokument.naziv)


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

    STOPNJE_DDV = (
        (0, "neobdavčeno"),
        (1, "nižja stopnja"),
        (2, "višja stopnja"),
    )

    # ATRIBUTES
    # ***Relations***
    racun = models.ForeignKey(Racun)
    vrsta_stroska = models.ForeignKey("VrstaStroska")
    lastniska_skupina = models.ForeignKey(LastniskaSkupina, blank=True, null=True)
    delovni_nalog = models.ForeignKey(DelovniNalog, blank=True, null=True)
    obdobje_obracuna_leto = models.ForeignKey(ObdobjeLeto)
    obdobje_obracuna_mesec = models.ForeignKey(ObdobjeMesec)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=200)
    datum_storitve_od = models.DateField()
    datum_storitve_do = models.DateField()
    # vrednosti do 99.999,99 EUR (na dve decimalni mesti natančno)
    osnova = models.DecimalField(decimal_places=2, max_digits=7, verbose_name='osnova za ddv')
    # 0.22(22%) in 0.095(9,5%) | 0.000
    stopnja_ddv = models.IntegerField(choices=STOPNJE_DDV, verbose_name="stopnja DDV")
    delilnik_vrsta = models.CharField(blank=True, max_length=50, choices=DELILNIK_VRSTA)
    delilnik_kljuc = models.CharField(blank=True, max_length=50, choices=DELILNIK_KLJUC)
    is_strosek_posameznidel = models.NullBooleanField(verbose_name="strosek na posameznem delu")
    # ***Optional***

    # OBJECT MANAGER
    objects = StrosekManager()

    # CUSTOM PROPERTIES
    def stopnja_ddv_output(self):
        # določimo ddv
        if self.stopnja_ddv == 0:
            stopnja_ddv = 0.000
        if self.stopnja_ddv == 1:
            stopnja_ddv = 0.095
        if self.stopnja_ddv == 2:
            stopnja_ddv = 0.220

        return "{0:.2f}%".format(stopnja_ddv * 100)

    @property
    def strosek_z_ddv(self):
        # določimo ddv
        if self.stopnja_ddv == 0:
            stopnja_ddv = 0.000
        if self.stopnja_ddv == 1:
            stopnja_ddv = 0.095
        if self.stopnja_ddv == 2:
            stopnja_ddv = 0.220

        strosek_z_ddv = Decimal(self.osnova) * (1 + Decimal(stopnja_ddv))

        return "%.2f" % (strosek_z_ddv)

    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'strošek'
        verbose_name_plural = 'stroški'
        ordering = ("oznaka",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class Konto(models.Model):

    # ATRIBUTES
    # ***Relations***
    # ***Mandatory***
    oznaka = models.CharField(max_length=10, unique=True)
    naziv = models.CharField(max_length=50)
    # ***Optional***
    zap_st = models.IntegerField(default=0, verbose_name="zaporedna Številka",)
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'konto'
        verbose_name_plural = "konti"
        ordering = ("zap_st",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class PodKonto(models.Model):
    # ---------------------------------------------------------------------------------------

    # ATRIBUTES
    # ***Relations***
    skupina = models.ForeignKey(Konto)
    # ***Mandatory***
    oznaka = models.CharField(max_length=10, unique=True)
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
    oznaka = models.CharField(max_length=20, unique=True)
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
    oznaka = models.CharField(max_length=20, unique=True)
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
