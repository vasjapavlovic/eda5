from django.db import models

from .managers import *

from eda5.core.models import IsActiveModel, TimeStampedModel
from eda5.etaznalastnina.models import LastniskaEnotaElaborat, LastniskaEnotaInterna
from eda5.partnerji.models import SkupinaPartnerjev
from eda5.posta.models import Dokument


class Prodaja(IsActiveModel, TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    kupec = models.ForeignKey(SkupinaPartnerjev)
    lastniska_enota = models.ManyToManyField(LastniskaEnotaElaborat, verbose_name="lastniška enota")
    zapisnik_predaje = models.ForeignKey(Dokument, verbose_name="zapisnik predaje v posest")
    #   Mandatory
    datum_predaje = models.DateField(verbose_name="datum predaje v posest")
    #   Optional
    datum_vpisa = models.DateField(blank=True, null= True, verbose_name="datum vpisa v zemljiško knjigo")
    # OBJECT MANAGER

    # CUSTOM PROPERTIES
    @property
    def aktiven(self):
        if self.is_active:
            status = "Aktiven"
        else:
            status = "Neaktiven"
        return status

    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "prodaja"
        verbose_name_plural = "prodaja"

    def __str__(self):
        return "%s | %s | %s" % (self.datum_predaje, self.kupec, self.aktiven)


class Najem(IsActiveModel, TimeStampedModel):
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

    PLACNIK = (
               (1, "lastnik"),
               (2, "najemnik")
               )

    # ATRIBUTES
    #   Relations
    najemnik = models.ForeignKey(SkupinaPartnerjev)
    lastniska_enota = models.ManyToManyField(LastniskaEnotaInterna, verbose_name="lastniška enota")
    najemna_pogodba = models.ForeignKey(Dokument, verbose_name="najemna pogodba")
    #   Mandatory
    datum_predaje = models.DateField(verbose_name="datum predaje v najem")
    trajanje_enota = models.CharField(max_length=5, choices=ENOTE, verbose_name="enota trajanja najema")
    trajanje_kolicina = models.IntegerField(verbose_name="količina trajanja/enota")
    placnik_stroskov = models.CharField(max_length=8, choices=PLACNIK, verbose_name="plačnik stroškov")
    #   Optional
    
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    @property
    def aktiven(self):
        if self.is_active:
            status = "Aktiven"
        else:
            status = "Neaktiven"
        return status

    # METHODS
    
    # META AND STRING
    class Meta:
        verbose_name = "najem"
        verbose_name_plural = "najem"

    def __str__(self):
        return "%s | %s | %s" % (self.datum_predaje, self.najemnik, self.aktiven)


