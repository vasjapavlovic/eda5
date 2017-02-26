# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models

from . import managers

from eda5.core.models import IsActiveModel, TimeStampedModel

from eda5.katalog.models import ModelArtikla, TipArtikla, ObratovalniParameter
from eda5.etaznalastnina.models import LastniskaSkupina


class Skupina(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    # ***Mandatory***
    oznaka = models.CharField(max_length=20, unique=True)
    naziv = models.CharField(max_length=255)
    # ***Optional***

    # OBJECT MANAGER
    objects = managers.SkupinaDelovManagers()

    # CUSTOM PROPERTIES
    @property
    def sorted_podskupinadelov_set(self):
        return self.podskupina_set.order_by('oznaka')
    # METHODS

    # META AND STRING
    class Meta:
        ordering = ['oznaka']
        verbose_name = 'skupina delov'
        verbose_name_plural = 'skupine delov'

    def __str__(self):
        return "(%s)%s" % (self.oznaka, self.naziv)


class Podskupina(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    skupina = models.ForeignKey(Skupina)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20, unique=True)
    naziv = models.CharField(max_length=255)
    # ***Optional***

    # OBJECT MANAGER
    objects = managers.PodskupinaDelovManagers()

    # CUSTOM PROPERTIES
    @property
    def sorted_delstavbe_set(self):
        return self.delstavbe_set.order_by('oznaka')

    # METHODS

    # META AND STRING
    class Meta:
        ordering = ['oznaka']
        verbose_name = 'podskupina delov'
        verbose_name_plural = 'podskupine delov'

    def __str__(self):
        return "(%s)%s" % (self.oznaka, self.naziv)


class DelStavbe(models.Model):
    # ---------------------------------------------------------------------------------------

    def shema_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/deli/<del_oznaka>/<new_filename>
        new_filename_raw = filename.split(".")
        ext = '.' + new_filename_raw[1]

        parametri_imena = (instance.oznaka, "shema")
        new_filename = "_".join(parametri_imena)

        return 'deli/{0}/{1}'.format(instance.oznaka, new_filename + ext)

    # ATRIBUTES
    # ***Relations***
    podskupina = models.ForeignKey(Podskupina)
    lastniska_skupina = models.ForeignKey(LastniskaSkupina, blank=True, null=True, verbose_name="lastniška skupina",)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20, unique=True)
    naziv = models.CharField(max_length=255)
    # dodaj funkcijo dela stavbe (sistema)
    # ***Optional***
    funkcija = models.CharField(max_length=255, blank=True, null=True, verbose_name="funkcija sistema")
    shema = models.FileField(upload_to=shema_directory_path, blank=True, verbose_name="shema sistema")

    # OBJECT MANAGER
    objects = managers.DelManagers()

    # CUSTOM PROPERTIES
    @property
    def projektna_mesta_all(self):
        projektno_mesto = self.projektnomesto_set.all()
        return projektno_mesto

    @property
    def projektna_mesta_aktivna(self):
        projektna_mesta = self.projektnomesto_set.filter(is_active=True)
        return projektna_mesta


    # METHODS
    def get_absolute_url(self):
        return reverse('moduli:deli:del_detail', kwargs={'pk': self.pk})

    # META AND STRING
    class Meta:
        ordering = ['oznaka']
        verbose_name = 'del stavbe'
        verbose_name_plural = 'deli stavbe'

    def __str__(self):
        return "(%s)%s" % (self.oznaka,
                           self.naziv
                           )


class ProjektnoMesto(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    tip_elementa = models.ForeignKey(TipArtikla)
    del_stavbe = models.ForeignKey(DelStavbe)
    #   Mandatory
    oznaka = models.CharField(max_length=20, unique=True)
    naziv = models.CharField(max_length=255)
    #   Optional
    funkcija = models.CharField(max_length=255, blank=True, null=True, verbose_name="funkcija elementa")


    @receiver(post_save, sender=DelStavbe)
    def create_projektnomesto_from_delstavbe(sender, created, instance, **kwargs):

        if created:

            # oznaka dela stavbe
            delstavbe = DelStavbe.objects.get(pk=instance.pk)
            oznaka_dela_stavbe = delstavbe.oznaka
            oznaka_projektnega_mesta = "S-" + oznaka_dela_stavbe

            #splošni tip elementa
            splosni_tip_elementa = TipArtikla.objects.get(oznaka="splosno")

            projektno_mesto = ProjektnoMesto(oznaka=oznaka_projektnega_mesta, naziv="Splošni del stavbe", funkcija="Splošni del stavbe", tip_elementa=splosni_tip_elementa, del_stavbe=instance)

            projektno_mesto.save()



    # OBJECT MANAGER

    # CUSTOM PROPERTIES
    @property
    def aktiven_element(self):  # element ki je trenutno aktiven pod posameznim projektnim mestom
        elementi = self.element_set.filter(is_active=True)
        return elementi[0]

    # METHODS
    def get_absolute_url(self):
        return reverse('moduli:deli:del_detail', kwargs={'pk': self.del_stavbe.pk})

    # META AND STRING
    class Meta:
        ordering = ["oznaka", ]
        verbose_name = "projektno mesto"
        verbose_name_plural = "projektna mesta"

    def __str__(self):
        return "(%s)%s - %s - %s" % (
            self.oznaka,
            self.naziv,
            self.tip_elementa.naziv,
            self.del_stavbe.naziv,
            )


class Element(IsActiveModel):

    # ---------------------------------------------------------------------------------------
    # Element predstavlja dejansko vgrajeno "Napravo" s serijsko in tovarniško številko,
    # ter ima vezavo na Katalog kjer se definira točno za kateri model določenega proizvajalca
    # gre.
    #
    # ELEMENT bi moral imeti OneToOneRelacijo glede na projektno mesto.
    # Vendar, ker bo lahko  na projektnem mestu v življenski dobi bilo registriranih več 
    # elementov je potrebna OneToMany relacija.Projektno mesto bo pa vedno imelo aktiven samo
    # en element do katerega se dostopa z ukazom
    # element = ProjektnoMesto.objects.filter(is_active=True)[0]
    # ---------------------------------------------------------------------------------------

    # ATRIBUTES

    # TOVARNIŠKA ŠTEVILKA proizvajalca predstavlja točno številko izdelanega proizvoda
    tovarniska_st = models.CharField(
        max_length=100, blank=True,
        verbose_name='Tovarniška Številka')

    # SERIJSKA ŠTEVILKA proizvajalca predstavlja številko v seriji.
    serijska_st = models.CharField(
        max_length=100, blank=True,
        verbose_name='Serijska Številka')

    #R PROJEKTNO MESTO. Relacija na projektno mesto
    projektno_mesto = models.ForeignKey(
        ProjektnoMesto, 
        verbose_name='projektno mesto')

    #R ARTIKEL. Relacija na model artikla iz kataloga
    artikel = models.ForeignKey(
        ModelArtikla, blank=True, null=True, 
        verbose_name='Model',)


    # OBJECT MANAGER
    objects = managers.ElementManagers()

    # CUSTOM PROPERTIES

    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'element'
        verbose_name_plural = 'elementi'

    def __str__(self):
        return "(%s)%s %s" % (self.projektno_mesto.oznaka,
                              self.projektno_mesto.tip_elementa.naziv,
                              self.projektno_mesto.naziv
                              )


class Nastavitev(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    element = models.ForeignKey(Element)
    obratovalni_parameter = models.ForeignKey(ObratovalniParameter)
    #   Mandatory
    ''' datum nastavitve kasneje vzami iz zahtevka. Dodati je relacijo na zahtevek'''
    datum_nastavitve = models.DateField()
    vrednost = models.CharField(max_length=20)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "nastavitev"
        verbose_name_plural = "nastavitve"

    def __str__(self):
        return "%s | %s | %s" % (self.obratovalni_parameter.oznaka,
                                 self.vrednost,
                                 self.datum_nastavitve
                                 )
