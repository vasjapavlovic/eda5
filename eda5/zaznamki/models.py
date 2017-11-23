from django.db import models
from django.core.urlresolvers import reverse

# Managers
from . import managers

# Models
from eda5.delovninalogi.models import DelovniNalog
from eda5.dogodki.models import Dogodek
from eda5.povprasevanje.models import Povprasevanje
from eda5.razdelilnik.models import Razdelilnik
from eda5.reklamacije.models import Reklamacija
from eda5.sestanki.models import Sestanek
from eda5.skladisce.models import Dobava
from eda5.zahtevki.models import Zahtevek


class Zaznamek(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    delovninalog = models.ForeignKey(DelovniNalog, blank=True, null=True)
    dobava = models.ForeignKey(Dobava, blank=True, null=True)
    dogodek = models.ForeignKey(Dogodek, blank=True, null=True)
    povprasevanje = models.ForeignKey(Povprasevanje, blank=True, null=True)
    razdelilnik = models.ForeignKey(Razdelilnik, blank=True, null=True)
    reklamacija = models.ForeignKey(Reklamacija, blank=True, null=True)
    sestanek = models.ForeignKey(Sestanek, blank=True, null=True)
    zahtevek = models.ForeignKey(Zahtevek, blank=True, null=True)

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

        if self.delovninalog:
            return reverse("moduli:delovninalogi:dn_detail", kwargs={'pk': self.delovninalog.pk})

        if self.dobava:
            return reverse("moduli:skladisce:dobava_detail", kwargs={'pk': self.dobava.pk})

        if self.dogodek:
            return reverse("moduli:dogodki:dogodek_detail", kwargs={'pk': self.dogodek.pk})

        if self.povprasevanje:
            return reverse("moduli:povprasevanje:povprasevanje_detail", kwargs={'pk': self.povprasevanje.pk})

        if self.razdelilnik:
            return reverse("moduli:razdelilnik:razdelilnik_detail", kwargs={'pk': self.razdelilnik.pk})

        if self.reklamacija:
            return reverse("moduli:reklamacije:reklamacija_detail", kwargs={'pk': self.reklamacija.pk})

        if self.sestanek:
            return reverse("moduli:sestanki:sestanek_detail", kwargs={'pk': self.sestanek.pk})

        if self.zahtevek:
            return reverse("moduli:zahtevki:zahtevek_detail", kwargs={'pk': self.zahtevek.pk})


    # META AND STRING
    class Meta:
        verbose_name = 'Zaznamek'
        verbose_name_plural = 'Zaznamki'

    def __str__(self):
        return '%s - %s' % (self.datum, self.tekst)
