from django.db import models
from django.core.urlresolvers import reverse

from . import managers

from eda5.zahtevki.models import Zahtevek
from eda5.delovninalogi.models import DelovniNalog


class Zaznamek(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    zahtevek = models.ForeignKey(Zahtevek, blank=True, null=True)
    delovninalog = models.ForeignKey(DelovniNalog, blank=True, null=True)
    #   Mandatory
    tekst = models.TextField(verbose_name='Tekst')
    datum = models.DateField(verbose_name='Datum')
    ura = models.TimeField(verbose_name='Ura')
    #   Optional

    # OBJECT MANAGER
    objects = managers.ZaznamekManager()
    # CUSTOM PROPERTIES
    # METHODS
    def get_absolute_url(self):

        if self.zahtevek:
            return reverse("moduli:zahtevki:zahtevek_detail", kwargs={'pk': self.zahtevek.pk})

        if self.delovninalog:
            return reverse("moduli:delovninalogi:dn_detail", kwargs={'pk': self.delovninalog.pk})

    # META AND STRING
    class Meta:
        verbose_name = 'Zaznamek'
        verbose_name_plural = 'Zaznamki'

    def __str__(self):
        return '%s - %s' % (self.datum, self.tekst)
