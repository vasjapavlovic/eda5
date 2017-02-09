from django.db import models
from django.db.models import get_model
from django.utils import timezone

from . import managers

from eda5 import arhiv
from eda5.core.models import TimeStampedModel
from eda5.partnerji.models import Partner, Oseba
from eda5.zahtevki.models import Zahtevek


class Narocilo(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    zahtevek = models.ForeignKey(Zahtevek, null=True, blank=True)
    narocnik = models.ForeignKey(Partner, related_name="narocnik")
    izvajalec = models.ForeignKey(Partner, related_name="izvajalec")
    
    # narocilo_narocilnica = models.OneToOneField("NarociloNarocilnica", blank=True, null=True)
    # narocilo_eposta = models.OneToOneField("NarosciloEposta", blank=True, null=True)
    narocilo_telefon = models.OneToOneField("NarociloTelefon", blank=True, null=True)
    # narocilo_ustno = models.OneToOneField("NarociloUstno", blank=True, null=True)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20, unique=True)
    predmet = models.CharField(max_length=255)
    datum_narocila = models.DateField(verbose_name="datum naročila")
    datum_veljavnosti = models.DateField(verbose_name="velja do")
    # ____max = 99999.99 EUR
    vrednost = models.DecimalField(decimal_places=2, max_digits=7, blank=True, null=True)
    # ***Optional***
    # OBJECT MANAGER
    objects = managers.NarociloManager()

    # CUSTOM PROPERTIES
    @property
    def status(self):
        if self.datum_veljavnosti <= timezone.now().date():
            return "veljavno"
        else:
            return "neveljavno"
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'naročilo'
        verbose_name_plural = 'naročila'

    def __str__(self):
        return '%s - %s' % (self.oznaka, self.predmet)


class NarociloDokument(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # tipi dokumentov za naročanje
    TIPI_DOKUMENTOV = (
        (1, 'e-pošta'),
        (2, 'naročilnica'),
        (3, 'pogodba'),
    )
    # ATRIBUTES
    # ***Relations***
    narocilo = models.OneToOneField(Narocilo, blank=True, null=True)
    tip_dokumenta = models.IntegerField(choices=TIPI_DOKUMENTOV)
    # ***Mandatory***


    dokument = models.ForeignKey('arhiv.Arhiviranje', blank=True, null=True)
    # ***Optional***

    # OBJECT MANAGER
    objects = managers.NarociloDokumentManager()
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'naročilo z dokumentom'
        verbose_name_plural = 'naročilo z dokumentom'

    def __str__(self):
        return '%s' % (self.narocilo.oznaka)


class NarociloTelefon(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    oseba = models.ForeignKey(Oseba, blank=True, null=True)
    # ***Mandatory***
    telefonska_stevilka = models.CharField(max_length=20)
    datum_klica = models.DateField()
    cas_klica = models.TimeField()
    telefonsko_sporocilo = models.CharField(max_length=255)
    # ***Optional***
    # OBJECT MANAGER
    objects = managers.NarociloTelefonManager()
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'naročilo po telefonu'
        verbose_name_plural = 'naročila po telefonu'

    def __str__(self):
        return '%s' % (self.narocilo.oznaka)
