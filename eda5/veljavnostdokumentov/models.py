# Python
# Django
from django.db import models
from django.core.urlresolvers import reverse
# Models
from eda5.arhiv.models import Arhiviranje
from eda5.core.models import TimeStampedModel, IsActiveModel
from eda5.deli.models import Stavba
from eda5.planiranje.models import PlaniranoOpravilo
from eda5.racunovodstvo.models import VrstaStroska
# Managers
from . import managers
# Forms


class VeljavnostDokumenta(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES

    # Relacija na dokument, ki je arhiviran
    arhiviranje = models.OneToOneField(Arhiviranje, verbose_name='arhiviranje')

    # Veljavnost dokumenta
    velja_od = models.DateField(blank=True, null=True, verbose_name='velja od')
    velja_do = models.DateField(blank=True, null=True, verbose_name='velja do')

    # Stavba
    stavba = models.ForeignKey(Stavba, blank=True, null=True, verbose_name="stavba")

    # Stroškovno mesto
    vrsta_stroska = models.ForeignKey(VrstaStroska, blank=True, null=True, verbose_name="Vrsta Stroška")

    # Planirano opravilo
    planirano_opravilo = models.ForeignKey(PlaniranoOpravilo, blank=True, null=True, verbose_name="Planirano Opravilo")


    #   Optional
    # OBJECT MANAGER
    objects = managers.VeljavnostDokumentaManager()
    # CUSTOM PROPERTIES
    # METHODS
    def get_absolute_url(self):

        # Dokumenti arhivirani pod zahtevek
        if self.arhiviranje.zahtevek:
            return reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': self.arhiviranje.zahtevek.pk})

        # Dokumenti arhivirani pod Dobave
        if self.arhiviranje.dobava:
            return reverse('moduli:skladisce:dobava_detail', kwargs={'pk': self.arhiviranje.dobava.pk})

        # Dokumenti arhivirani pod Delovni nalog
        if self.arhiviranje.delovninalog:
            return reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': self.arhiviranje.delovninalog.pk})

        # Dokumenti arhivirani pod reklamacijami
        if self.arhiviranje.reklamacija:
            return reverse('moduli:reklamacije:reklamacija_detail', kwargs={'pk': self.arhiviranje.reklamacija.pk})

    # META AND STRING
    def __str__(self):
        return "%s | %s" % (self.arhiviranje.dokument.oznaka, self.arhiviranje.dokument.naziv)
