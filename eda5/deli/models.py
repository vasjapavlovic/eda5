# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models

from . import managers

# Core
from eda5.core.models import IsActiveModel, TimeStampedModel

# Etažna lastnina
from eda5.etaznalastnina.models import LastniskaSkupina

# Katalog
from eda5.katalog.models import ModelArtikla, TipArtikla, ObratovalniParameter

# Lokacije
from eda5.lokacija.models import Prostor




class Stavba(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------

    # ATRIBUTES
    #===================================


    oznaka = models.CharField(
        max_length=20, unique=True,
        verbose_name="Oznaka")

    naziv = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="Naziv")

    opis = models.TextField(
        blank=True, null=True,
        verbose_name="Opis")


    # META AND STRING
    #===================================
    class Meta:
        verbose_name = "Stavba"
        verbose_name_plural = "Stavbe"
        ordering = ["oznaka", ]

    def __str__(self):
        return "%s. %s" % (self.oznaka, self.naziv)


class Etaza(TimeStampedModel, IsActiveModel):


    # ATRIBUTES
    #===================================

    oznaka = models.CharField(
        max_length=50, unique=True,
        verbose_name="Oznaka")

    naziv = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="Naziv")

    opis = models.TextField(
        blank=True, null=True,
        verbose_name="Opis")

    elevation = models.DecimalField(
        decimal_places=5, max_digits=20, blank=True, null=True,
        verbose_name="Višinska kota Etaže")

    #R STAVBA Relacija na Stavbo
    stavba = models.ForeignKey(
        Stavba,
        verbose_name="Stavba")


    # META AND STRING
    #===================================
    class Meta:
        verbose_name = "Etaža"
        verbose_name_plural = "Etaže"
        ordering = ["oznaka", ]

    def __str__(self):
        return "%s. %s" % (self.oznaka, self.naziv)


class Lokacija(TimeStampedModel, IsActiveModel):

    # ATRIBUTES
    #===================================

    prostor = models.OneToOneField(
        "DelStavbe",
        verbose_name='Prostor'
    )

    etaza = models.ForeignKey(
        Etaza,
        verbose_name="Etaža"
    )

    # META AND STRING
    #===================================
    class Meta:
        verbose_name = "Lokacija"
        verbose_name_plural = "Lokacije"
        ordering = ["prostor__oznaka", ]

    def __str__(self):
        return "Prostor: %s | Etaža: %s" % (self.prostor.oznaka, self.etaza.oznaka)



class Skupina(TimeStampedModel, IsActiveModel):

    # ---------------------------------------------------------------------------------------
    # Skupina delov stavbe združuje dele stavbe (glej spodaj deli stavbe) glede na vrsto.
    # npr. Sistem, Naprava, Gradbeni element, Prostor, Oprema
    # ---------------------------------------------------------------------------------------

    # ATRIBUTES
    #===================================

    # oznaka skupina
    oznaka = models.CharField(
        max_length=20, unique=True,
    )

    # naziv skupina
    naziv = models.CharField(
        max_length=255,
    )


    # OBJECT MANAGER
    #===================================
    objects = managers.SkupinaDelovManagers()

    # CUSTOM PROPERTIES
    #===================================
    @property
    def sorted_podskupinadelov_set(self):
        return self.podskupina_set.order_by('oznaka')
    # METHODS

    # META AND STRING
    #===================================
    class Meta:
        ordering = ['oznaka']
        verbose_name = 'skupina delov'
        verbose_name_plural = 'skupine delov'

    def __str__(self):
        return "(%s)%s" % (self.oznaka, self.naziv)


class Podskupina(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
    # Podskupina delov stavbe združuje dele stavbe (glej spodaj deli stavbe) glede na
    # funkcionalnost. Npr. Ogrevanje in haljenje, Vodovod in kanalizacija, Streha, Fasada,...
    # ---------------------------------------------------------------------------------------

    # ATRIBUTES
    #===================================
    # ***Relations***
    skupina = models.ForeignKey(
        Skupina
    )

    # oznaka podskupine
    oznaka = models.CharField(
        max_length=20, unique=True,
    )

    # naziv podskupine
    naziv = models.CharField(
        max_length=255,
    )
    # ***Optional***

    # OBJECT MANAGER
    #===================================
    objects = managers.PodskupinaDelovManagers()

    # CUSTOM PROPERTIES
    #===================================
    @property
    def sorted_delstavbe_set(self):
        return self.delstavbe_set.order_by('oznaka')

    # METHODS
    #===================================

    # META AND STRING
    #===================================
    class Meta:
        ordering = ['oznaka']
        verbose_name = 'podskupina delov'
        verbose_name_plural = 'podskupine delov'

    def __str__(self):
        return "(%s)%s" % (self.oznaka, self.naziv)


class DelStavbe(TimeStampedModel, IsActiveModel):

    shema_directory_path = ""

    # ---------------------------------------------------------------------------------------
    # Del stavbe predstavlja sistem, napravo, prostor, gradbeni element ali opremo, ki je
    # definirana oziroma oblikovana glede na (1) zaradi skupnega lastništva (2) smiselno po
    # funkcionalnosti-razdelitev na več delov tudi v primeru enega lastnika zaradi smiselne
    # funkcionalnosti. Del stabe združuje projektna mesta na katerih se vodi servisna knjiga,
    # imajo planirane aktivnosti, ki so del plana obratovanja in vzdrževanja.
    # ---------------------------------------------------------------------------------------

    # ATRIBUTES
    #===================================

    # oznaka dela stavbe
    oznaka = models.CharField(
        max_length=50, unique=True,
    )

    # naziv dela stavbe
    naziv = models.CharField(
        max_length=255,
    )

    # funkcijo dela stavbe (sistema)
    funkcija = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="funkcija sistema"
    )

    # BIM ID. Navezava na BIM program
    bim_id = models.CharField(
        max_length=100, blank=True, null=True,
        verbose_name='BIM ID'
    )

    #R# lastniška skupina - kdo je lastnik
    lastniska_skupina = models.ForeignKey(
        LastniskaSkupina, blank=True, null=True,
        verbose_name="lastniška skupina",
    )

    #R# klasifikacija v podskupino
    podskupina = models.ForeignKey(
        Podskupina,
    )

    #R# klasifikacija v podskupino
    stavba = models.ForeignKey(
        Stavba,
        blank=True,
        null=True,
    )


    # OBJECT MANAGER
    #===================================
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
    #===================================
    def get_absolute_url(self):
        return reverse('moduli:deli:del_detail', kwargs={'pk': self.pk})

    # META AND STRING
    #===================================
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
    # Projektno mesto definira pozicijo v stavbi kamor se vgrajujejo elementi ( glej spodaj
    # models Element. Projektno mesto določajo oznaka, naziv ter funkcija elementa, ki bo tu
    # vgrajen ter tudi kateri tip elementa se bo tu vgradil.)
    #
    # POMEMBNO - Uporabljen Django Signals tako, da se splošno projektno mesto avtomatsko izdela
    # ko se izdela nov DelStavbe.
    # ---------------------------------------------------------------------------------------

    # ATRIBUTES
    #===================================

    # OZNAKA projektnega mesta: npr. 09AA25 kjer pomeni 09 (deveti) element
    # v sistemu z oznako AA25
    oznaka = models.CharField(
        max_length=20, unique=True,
        verbose_name="Oznaka")

    # NAZIV projektnega mesta : npr. Toplotna črpalka ST
    naziv = models.CharField(
        max_length=255,
        verbose_name="Naziv")

    # FUNKCIJA s katerim definiramo zakaj se bo ta element potreboval
    funkcija = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="Funkcija Elementa")

    #R TIP ELEMENTA. Definira relacijo na TipArtikla. npr. Toplotna Črpalka
    # tip_elementa = models.ForeignKey(
    #     TipArtikla, blank=True, null=True,
    #     verbose_name='Tip Elementa')

    #R DEL STAVBE. Definiramo relacijo na DEL STAVBE, ki ga sestavlja več
    # projektnih mest
    del_stavbe = models.ForeignKey(
        DelStavbe,
        verbose_name='Del Stavbe')

    # BIM ID. Navezava na BIM program
    bim_id = models.CharField(
        max_length=100, blank=True, null=True,
        verbose_name='BIM ID')

    # LOKACIJA. Definiramo lokacijo projektnega mesta v stavbi (Prostor, Zemljišče -->Etaža-->Stavba)
    lokacija = models.ForeignKey(
        Lokacija, blank=True, null=True,
        verbose_name='Lokacija v Stavbi')


    # OBJECT MANAGER
    #===================================
    objects = managers.ProjektnoMestoManagers()

    # CUSTOM PROPERTIES
    #===================================
    @property
    def aktiven_element(self):  # element ki je trenutno aktiven pod posameznim projektnim mestom
        element = self.element_set.filter(is_active=True)[0]
        return element

    # METHODS

    # PROJEKTNO MESTO - !!!AVTO. Ob izdelavi dela stavbe se avtomatsko
    # izdela splošno projektno mesto ki je potrebno za funkcioniranje
    # informacijskega sistema

    @receiver(post_save, sender=DelStavbe)
    def create_projektnomesto_from_delstavbe(sender, created, instance, **kwargs):

        if created:

            # oznaka dela stavbe
            delstavbe = DelStavbe.objects.get(pk=instance.pk)
            oznaka_dela_stavbe = delstavbe.oznaka
            oznaka_projektnega_mesta = "S-" + oznaka_dela_stavbe

            projektno_mesto = ProjektnoMesto(
                oznaka=oznaka_projektnega_mesta,
                naziv="splošno",
                funkcija="-",
                del_stavbe=instance
                )

            projektno_mesto.save()

    def get_absolute_url(self):
        return reverse('moduli:deli:del_detail', kwargs={'pk': self.del_stavbe.pk})

    # META AND STRING
    #===================================
    class Meta:
        ordering = ["oznaka", ]
        verbose_name = "projektno mesto"
        verbose_name_plural = "projektna mesta"

    def __str__(self):
        return "(%s)%s - %s" % (
            self.oznaka,
            self.naziv,
            self.del_stavbe.naziv,
            )


class Element(TimeStampedModel, IsActiveModel):

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
    #===================================

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
    #===================================
    objects = managers.ElementManagers()

    # CUSTOM PROPERTIES
    #===================================

    # METHODS
    #===================================

    # META AND STRING
    #===================================
    class Meta:
        verbose_name = 'element'
        verbose_name_plural = 'elementi'

    def __str__(self):
        return "(%s)%s" % (self.projektno_mesto.oznaka,
                              self.projektno_mesto.naziv
                              )


class Nastavitev(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #===================================
    #   Relations
    element = models.ForeignKey(Element)
    obratovalni_parameter = models.ForeignKey(ObratovalniParameter)
    #   Mandatory
    ''' datum nastavitve kasneje vzami iz zahtevka. Dodati je relacijo na zahtevek'''
    datum_nastavitve = models.DateField()
    vrednost = models.CharField(max_length=20)
    #   Optional
    # OBJECT MANAGER
    #===================================
    # CUSTOM PROPERTIES
    #===================================
    # METHODS
    #===================================

    # META AND STRING
    #===================================
    class Meta:
        verbose_name = "nastavitev"
        verbose_name_plural = "nastavitve"

    def __str__(self):
        return "%s | %s | %s" % (self.obratovalni_parameter.oznaka,
                                 self.vrednost,
                                 self.datum_nastavitve
                                 )
