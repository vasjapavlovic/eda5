from django.db import models

from eda5.core.models import OsnovnaKombinacija
from eda5.delovninalogi.models import Opravilo
from eda5.deli.models import ProjektnoMesto



# KONTROLNI objekt_list
class Aktivnost(OsnovnaKombinacija):

    opravilo = models.ForeignKey(
        Opravilo,
        blank=True,
        null=True,
        verbose_name='opravilo'
        )

    projektno_mesto = models.ManyToManyField(
        ProjektnoMesto,
        blank=True,
        verbose_name='projektno mesto'
        )


    class Meta:
        verbose_name='Aktivnost'
        verbose_name_plural='Aktivnosti'
        ordering=('oznaka',)


    def __str__(self):
        return '(%s)%s' % (self.oznaka, self.naziv)


class KontrolaSpecifikacija(OsnovnaKombinacija):

    aktivnost = models.ForeignKey(
        Aktivnost,
        verbose_name='aktivnost'
        )

    tip_check = 1
    tip_vrednost = 2
    tip_select = 3

    VRSTE_VNOSA = (
        (tip_check, 'check'),
        (tip_vrednost, 'text'),
        (tip_select, 'select'), # Zaloga vrednosti --> OpcijeSelect model
        )

    vrsta_vnosa = models.IntegerField(
        choices=VRSTE_VNOSA,
        default=1,
        verbose_name='vrsta vnosa',
        )


    class Meta:
        ordering = ['oznaka']


class KontrolaSpecifikacijaOpcijaSelect(OsnovnaKombinacija):

    kontrola_specifikacija = models.ForeignKey(
        KontrolaSpecifikacija,
        verbose_name='specifikacija kontrole'
        )

    def __str__(self):
        return "(%s)%s" % (self.oznaka, self.naziv)
