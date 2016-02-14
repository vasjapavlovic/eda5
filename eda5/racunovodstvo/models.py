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
    racunovodsko_leto = models.ForeignKey(ObdobjeLeto)
    # ***Mandatory***
    oznaka = models.IntegerField()
    davcna_klasifikacija = models.IntegerField(choices=DAVCNA_KLASIFIKACIJA)
    valuta = models.DateField(blank=True, null=True)
    datum_storitve_od = models.DateField(blank=True, null=True)
    datum_storitve_do = models.DateField(blank=True, null=True)


    # OBJECT MANAGER
    objects = RacunManager()

    # CUSTOM PROPERTIES
    @property
    def dokument(self):
        ''' podatke o dokumentu pridobimo iz arhiviranja Prejete ali Izdane Pošte
        Pošta:Aktivnost:Dokument --> Arhiviranje:ArhivMesto --> Racun:Racunovodstvo'''
        return self.arhiviranje.dokument


    # METHODS
    def get_absolute_url(self):
        return reverse("moduli:racunovodstvo:home")

    # META AND STRING
    class Meta:
        verbose_name = 'račun'
        verbose_name_plural = "računi"
        ordering = ('-racunovodsko_leto', "-oznaka")

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
    osnova = models.DecimalField(decimal_places=5, max_digits=10, verbose_name='osnova za ddv')
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
    @property
    def visina_stroska(self):
        visina_stroska = 0
        for podkonto in self.podkonto_set.all():
            for skupina_vrste_stroska in podkonto.skupinavrstestroska_set.all():
                for vrsta_stroska in skupina_vrste_stroska.vrstastroska_set.all():
                    for strosek in vrsta_stroska.strosek_set.all():
                        visina_stroska += strosek.osnova
        return visina_stroska
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
    @property
    def visina_stroska(self):
        visina_stroska = 0
        for skupina_vrste_stroska in self.skupinavrstestroska_set.all():
            for vrsta_stroska in skupina_vrste_stroska.vrstastroska_set.all():
                for strosek in vrsta_stroska.strosek_set.all():
                    visina_stroska += strosek.osnova
        return visina_stroska
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
    @property
    def visina_stroska(self):
        visina_stroska = 0
        for vrsta_stroska in self.vrstastroska_set.all():
            for strosek in vrsta_stroska.strosek_set.all():
                visina_stroska += strosek.osnova
        return visina_stroska
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
    @property
    def visina_stroska(self):
        visina_stroska = 0
        for strosek in self.strosek_set.all():
            visina_stroska += strosek.osnova
        return visina_stroska
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'vrsta stroška'
        verbose_name_plural = "vrste stroškov"
        ordering = ("zap_st",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)
