from django.db import models

from eda5.core.models import StatusModel, TimeStampedModel
from eda5.narocila.models import Narocilo
from eda5.partnerji.models import Oseba, Partner
from eda5.posta.models import Dokument
from eda5.deli.models import DelStavbe, Element


class Zahtevek(TimeStampedModel, StatusModel):
    # ---------------------------------------------------------------------------------------
    # STATUS
    draft = 0
    # vCakanju = 1
    # vPlanu = 2
    vResevanju = 3
    zakljuceno = 4

    STATUS = (
        (draft, 'draft'),
        (vResevanju, 'V Reševanju'),
        (zakljuceno, 'Zaključeno'),
        )

    # ATRIBUTES
    # ***Relations***
    narocilo = models.ForeignKey(Narocilo)  # ***izbira samo med veljavnimi naročili****
    nosilec = models.ForeignKey(Oseba)
    zahtevek_skodni_dogodek = models.OneToOneField("ZahtevekSkodniDogodek", blank=True, null=True)
    # zahtevek_zbor_lastnikov = models.OneToOneField(ZahtevekZborLastnikov)
    zahtevek_sestanek = models.OneToOneField("ZahtevekSestanek", blank=True, null=True)
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
    poskodovane_stvari = models.ManyToManyField(Element, blank=True)
    #     dokumenti
    dokument_prijava_skode = models.ForeignKey(Dokument, related_name="dokument_prijava_skode",
                                               blank=True, null=True, verbose_name="prijava škode")
    dokument_zapisnik_ogleda = models.ForeignKey(Dokument, related_name="dokument_zapisnik_ogleda",
                                                 blank=True, null=True, verbose_name="zapisnik o ogledu škode")
    dokument_poravnava = models.ForeignKey(Dokument, related_name="dokument_poravnava",
                                           blank=True, null=True, verbose_name="poravnava škode")
    dokazno_gradivo = models.ForeignKey(Dokument, blank=True, null=True, related_name="dokazno_gradivo")
    # zaznamki ZAVAROVALNICA
    #   Mandatory
    datum_nastanka_skode = models.DateField(verbose_name="datum nastanka škdoe")
    vzrok_skode = models.TextField(blank=True, verbose_name="vzrok škode")
    #   Optional
    is_prijava_policiji = models.BooleanField(blank=True, verbose_name="prijavljeno policiji")
    povzrocitelj = models.CharField(max_length=255, blank=True, verbose_name="povzročitelj")
    #     oblika: 99999.99
    predvidena_visina_skode = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True,
                                                  verbose_name="predvidena višina škode")
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "škodni dogodek"
        verbose_name_plural = "škodni dogodki"
        ordering = ("datum_nastanka_skode",)

    def __str__(self):
        return "%s" % (self.datum_nastanka_skode)


class ZahtevekSestanek(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    sklicatelj = models.ForeignKey(Partner)
    udelezenci = models.ManyToManyField(Oseba, verbose_name="udeleženci")
    zapisnik = models.ForeignKey(Dokument, null=True, blank=True)
    #   Mandatory
    datum = models.DateField()
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "sestanek"
        verbose_name_plural = "sestanki"
        ordering = ("datum",)

    def __str__(self):
        return "%s | %s" % (self.datum, self.sklicatelj)
