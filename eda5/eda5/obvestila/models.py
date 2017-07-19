from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

from eda5.core.models import TimeStampedModel, StatusModel, IsActiveModel
from eda5.partnerji.models import Oseba
from eda5.zahtevki.models import Zahtevek


class Obvestilo(TimeStampedModel, StatusModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    oseba = models.ForeignKey(Oseba)
    #   Mandatory
    oznaka = models.CharField(max_length=50)
    naziv = models.CharField(max_length=255)
    vsebina = models.TextField()
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    @property
    def objavljeno_danes(self):
        datum_danes = timezone.now().date()
        objavljeno = self.created.date()
        if objavljeno == datum_danes:
            objavljeno_danes = True
        else:
            objavljeno_danes = False
        return objavljeno_danes
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "obvestilo"
        verbose_name_plural = "obvestila"
        ordering = ["-created", ]

    def __str__(self):
        return "(%s) %s" % (self.oznaka, self.naziv)


class Povezava(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    obvestilo = models.ForeignKey(Obvestilo)
    #   Mandatory
    url_ref = models.CharField(max_length=500)
    naziv = models.CharField(max_length=255)
    predtext = models.CharField(max_length=255, blank=True)
    objavljeno = models.BooleanField(default=False)
    #   Optional
    url_detail = models.CharField(max_length=50, blank=True)
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    @property
    def urlreference(self):
        if self.url_detail:
            zahtevek_oznaka = self.url_detail
            zahtevek = Zahtevek.objects.get(oznaka=zahtevek_oznaka)
        link = self.url_ref
        if link:
            url = reverse('%s' % (link), kwargs={'pk': zahtevek.pk})
            return url
        else:
            return ""

    @property
    def url_zahtevek(self):
        if self.url_detail:
            zahtevek_oznaka = self.url_detail
            zahtevek = Zahtevek.objects.get(oznaka=zahtevek_oznaka)
            
            zahtevek_oznaka = "%s %s" % (zahtevek.oznaka, zahtevek.naziv)
            return zahtevek_oznaka
        else:
            return ""
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "povezava"
        verbose_name_plural = "povezave"

    def __str__(self):
        return "%s | %s" % (self.obvestilo.oznaka, self.naziv)




class Komentar(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    obvestilo = models.ForeignKey(Obvestilo)
    #   Mandatory
    vsebina = models.TextField()
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "komentar"
        verbose_name_plural = "komentarji"
        ordering = ["-created", ]

    def __str__(self):
        return "(%s) %s" % (self.naziv)
