from django.db import models
from django.core.urlresolvers import reverse


from . import managers

from eda5.core.models import TimeStampedModel, IsActiveModel

from eda5.arhiv.models import Arhiviranje


class VeljavnostDokumenta(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    arhiviranje = models.OneToOneField(Arhiviranje, verbose_name='arhiviranje')
    #   Mandatory
    velja_od = models.DateField(verbose_name='velja od')
    velja_do = models.DateField(blank=True, null=True, verbose_name='velja do')

    #   Optional
    # OBJECT MANAGER
    objects = managers.VeljavnostDokumentaManager()
    # CUSTOM PROPERTIES
    # METHODS
    def get_absolute_url(self):
        return reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': self.arhiviranje.zahtevek.pk})
    # META AND STRING
    def __str__(self):
        return "%s | %s" % (self.arhiviranje.dokument.oznaka, self.arhiviranje.dokument.naziv)
