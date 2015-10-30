from django.db import models

from eda5.core.models import TimeStampedModel
from eda5.partnerji.models import Partner, SkupinaPartnerjev
from eda5.posta.models import Dokument


class Narocilo(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    narocnik = models.ForeignKey(SkupinaPartnerjev, related_name="narocnik")
    izvajalec = models.ForeignKey(Partner, related_name="izvajalec")
    narocilo_pogodba = models.OneToOneField("NarociloPogodba", blank=True, null=True)
    # narocilo_narocilnica = models.OneToOneField("NarociloNarocilnica", blank=True, null=True)
    # narocilo_eposta = models.OneToOneField("NarociloEposta", blank=True, null=True)
    narocilo_telefon = models.OneToOneField("NarociloTelefon", blank=True, null=True)
    # narocilo_ustno = models.OneToOneField("NarociloUstno", blank=True, null=True)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20, verbose_name='oznaka')
    predmet = models.CharField(max_length=255, verbose_name='predmet')
    datum_narocila = models.DateField(verbose_name="datum naročila")
    datum_veljavnosti = models.DateField(verbose_name="velja do")
    # ____max = 99999.99 EUR
    vrednost = models.DecimalField(decimal_places=2, max_digits=7)
    # ***Optional***
    dodatna_dokumentacija = models.ManyToManyField(Dokument, blank=True)
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'Naročilo'
        verbose_name_plural = 'Naročila'

    def __str__(self):
        return '%s - %s' % (self.oznaka, self.predmet)


class NarociloPogodba(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    st_pogodbe = models.CharField(max_length=20, verbose_name="številka pogodbe")
    predmet_pogodbe = models.CharField(max_length=255, verbose_name="številka pogodbe")
    pogodba = models.ForeignKey(Dokument)
    # ***Mandatory***
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'pogodbeno naročilo'
        verbose_name_plural = 'pogodbena naročila'

    def __str__(self):
        return '%s' % (self.st_pogodbe)


class NarociloTelefon(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    # ***Mandatory***
    telefonska_stevilka = models.CharField(max_length=20)
    datum_klica = models.DateField()
    cas_klica = models.TimeField()
    telefonsko_sporocilo = models.CharField(max_length=255)
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'naročilo po telefonu'
        verbose_name_plural = 'naročila po telefonu'

    def __str__(self):
        return '%s - %s' % (self.datum_klica, self.telefonska_stevilka)
