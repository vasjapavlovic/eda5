from django.db import models
from eda5.partnerji.models import Partner, Posta


class LastniskaEnotaElaborat(models.Model):
    # ATRIBUTES
    # __Relations
    # __Mandatory
    oznaka = models.CharField(max_length=4, verbose_name='številka dela stavbe')
    povrsina_tlorisna_neto = models.CharField(max_length=4, verbose_name='neto tlorisna površina')
    '''************Dodaj Lastniški delež***********'''
    naslov = models.CharField(max_length=255)
    posta = models.ForeignKey(Posta, verbose_name='pošta')
    # __Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "lastniška enota elaborat"
        verbose_name_plural = "lastniške enote elaborat"
        ordering = ("oznaka",)

    def __str__(self):
        return "%s" % (self.oznaka)


class LastniskaEnotaInterna(models.Model):
    # ATRIBUTES
    # __Relations
    elaborat = models.ForeignKey(LastniskaEnotaElaborat)
    lastnik = models.ForeignKey(Partner, related_name="lastnik")
    najemnik = models.ForeignKey(Partner, null=True, blank=True, related_name="najemnik")
    placnik = models.ForeignKey(Partner, related_name="placnik")
    # __Mandatory
    oznaka = models.CharField(max_length=5, verbose_name='interna številka dela stavbe')

    '''************Dodati je še ostale atribute***********'''
    # __Optional
    #______delež v obliki :  0.9999
    lastniski_delez = models.DecimalField(decimal_places=4, max_digits=5, blank=True, verbose_name="lastniški delež")
    povrsina_tlorisna_neto = models.CharField(max_length=4, blank=True, verbose_name='neto tlorisna površina')
    st_oseb = models.IntegerField(blank=True, verbose_name="število oseb")
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS
    # META AND STRING
    class Meta:
        verbose_name = "lastniška enota interna"
        verbose_name_plural = "lastniške enote interna"
        ordering = ("oznaka",)

    def __str__(self):
        return "%s" % (self.oznaka)


class Program(models.Model):

    # ATRIBUTES
    # ***Relations***
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
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


class LastniskaSkupina(models.Model):

    # ATRIBUTES
    # ***Relations***
    program = models.ForeignKey(Program)
    lastniska_enota = models.ManyToManyField(LastniskaEnotaInterna, blank=True)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
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
        return "%s | %s" % (self.oznaka, self.naziv)
