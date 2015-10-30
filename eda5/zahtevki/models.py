from django.db import models

from eda5.core.models import TimeStampedModel
from eda5.narocila.models import Narocilo
from eda5.partnerji.models import Oseba
from eda5.posta.models import Dokument


class Zahtevek(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    narocilo = models.ForeignKey(Narocilo)  # ***izbira samo med veljavnimi naročili****
    nosilec = models.ForeignKey(Oseba)
    zahtevek_skodni_dogodek = models.OneToOneField("ZahtevekSkodniDogodek")
    # zahtevek_zbor_lastnikov = models.OneToOneField(ZahtevekZborLastnikov)
    # zahtevek_sestanek = models.OneToOneField(ZahtevekSestanek)
    # zahtevek_izvedba_dela = models.OneToOneField(ZahtevekIzvedbaDela)
    # zahtevek_reklamacija_nabave = models.OneToOneField(ZahtevekReklamacijaNabave)
    # zahtevek_reklamacija_prodaje = models.OneToOneField(ZahtevekReklamacijaProdaje)
    # zaznamki SPLOŠNO
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    predmet = models.CharField(max_length=255)
    rok_izvedbe = models.DateField()
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "zahtevek"
        verbose_name_plural = "zahtevki"
        ordering = ("oznaka",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.predmet)


class ZahtevekSkodniDogodek(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #     dokumenti
    dokument_prijava_skode = models.ForeignKey(Dokument, related_name="dokument_prijava_skode", verbose_name="prijava škode")
    dokument_zapisnik_ogleda = models.ForeignKey(Dokument, related_name="dokument_zapisnik_ogleda",verbose_name="zapisnik o ogledu škode")
    dokument_poravnava = models.ForeignKey(Dokument, related_name="dokument_poravnava",verbose_name="poravnava škode")
    # zaznamki ZAVAROVALNICA
    #   Mandatory
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "škodni dogodek"
        verbose_name_plural = "škodni dogodki"

    def __str__(self):
        return "%s" % (self.dokument_prijava_skode)
