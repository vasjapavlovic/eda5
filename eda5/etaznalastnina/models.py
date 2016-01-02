from django.db import models
from django.db.models import Max

from eda5.partnerji.models import SkupinaPartnerjev, Partner, Posta


class Program(models.Model):

    # ATRIBUTES
    # ***Relations***
    # ***Mandatory***
    oznaka = models.CharField(max_length=20, unique=True)
    naziv = models.CharField(max_length=255)
    zap_st = models.IntegerField(default=0, verbose_name="zaporedna Številka",)
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programi"
        ordering = ("zap_st",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class LastniskaEnotaElaborat(models.Model):
    # ATRIBUTES
    # __Relations
    program = models.ForeignKey(Program, blank=True, null=True)
    posta = models.ForeignKey(Posta, verbose_name='pošta')
    # __Mandatory
    oznaka = models.CharField(max_length=4, unique=True, verbose_name='številka dela stavbe')
    naslov = models.CharField(max_length=255)
    opis = models.CharField(max_length=255, blank=True)
    povrsina_tlorisna_neto = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='neto tlorisna površina')
    lastniski_delez = models.DecimalField(decimal_places=4, max_digits=5, blank=True, null=True, verbose_name="lastniški delež")

    # __Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    @property
    def id_stevilka(self):
        id_stevilka = int(self.oznaka)
        return id_stevilka

    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "lastniška enota elaborat"
        verbose_name_plural = "lastniške enote elaborat"
        ordering = ("id",)

    def __str__(self):
        return "%s | %s, %s" % (self.oznaka, self.naslov, self.posta)


class LastniskaEnotaInterna(models.Model):
    # ATRIBUTES
    # __Relations
    elaborat = models.ForeignKey(LastniskaEnotaElaborat)
    # __Mandatory
    oznaka = models.CharField(max_length=5, unique=True, verbose_name='interna številka dela stavbe')
    # __Optional
    #______delež v obliki :  0.9999
    lastniski_delez = models.DecimalField(decimal_places=4, max_digits=5, blank=True, verbose_name="lastniški delež")
    povrsina_tlorisna_neto = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='neto tlorisna površina')
    st_oseb = models.DecimalField(max_digits=2, decimal_places=1, blank=True, verbose_name="število oseb")
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    @property
    def prodaja(self):
        lastniska_enota = LastniskaEnotaInterna.objects.get(id=self.id)
        prodaje_lastnine = lastniska_enota.elaborat.prodajalastnine_set.all()
        zadnja_prodaja = prodaje_lastnine.latest('datum_predaje')
        prodaja = zadnja_prodaja
        return prodaja

    @property
    def najem(self):
        lastniska_enota = LastniskaEnotaInterna.objects.get(id=self.id)
        najem_lastnine = lastniska_enota.najemlastnine_set.filter(is_active=True)
        zadnji_najem = najem_lastnine.latest('datum_predaje')  # vrniti bi moralo samo en vnos (zaenkrat pustim še vedno latest)
        najem = zadnji_najem
        return najem

    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "lastniška enota interna"
        verbose_name_plural = "lastniške enote interna"
        ordering = ("oznaka",)

    def __str__(self):
        return "%s" % (self.oznaka)


class LastniskaSkupina(models.Model):

    # ATRIBUTES
    # ***Relations***
    program = models.ForeignKey(Program)
    lastniska_enota = models.ManyToManyField(LastniskaEnotaElaborat, blank=True)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20, unique=True)
    naziv = models.CharField(max_length=255)
    opis = models.CharField(max_length=255, blank=True)
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "lastniška skupina"
        verbose_name_plural = "lastniške skupine"
        ordering = ("oznaka",)

    def __str__(self):
        return "%s | %s | %s" % (self.oznaka, self.program.naziv, self.naziv)


class InternaDodatno(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    interna = models.OneToOneField(LastniskaEnotaInterna, verbose_name="interna LE")
    # lastnik = models.ForeignKey(SkupinaPartnerjev, blank=True, null=True, related_name='lastnik')
    # najemnik = models.ForeignKey(SkupinaPartnerjev, blank=True, null=True, related_name='najemnik')
    # placnik = models.ForeignKey(SkupinaPartnerjev, blank=True, null=True, related_name='placnik')
    uporabno_dovoljenje = models.ForeignKey("UporabnoDovoljenje", blank=True, null=True)
    #   Mandatory
    stanje_prostora = models.CharField(max_length=255, blank=True, null=True)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "dodatek interni LE"
        verbose_name_plural = "dodatki internim LE"
        ordering = ['interna',]

    def __str__(self):
        return "%s" % (self.interna.oznaka)


class UporabnoDovoljenje(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    oznaka = models.CharField(max_length=20, unique=True)
    st_dokumenta = models.CharField(max_length=50, unique=True)
    datum = models.DateField()
    objekt = models.CharField(max_length=255)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "uporabno dovoljenje"
        verbose_name_plural = "uporabna dovoljenja"
        ordering = ['datum',]

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.datum)
