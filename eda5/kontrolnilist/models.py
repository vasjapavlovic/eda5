from django.db import models

from eda5.core.models import OsnovnaKombinacija
from eda5.delovninalogi.models import Opravilo
from eda5.delovninalogi.models import DelovniNalog
from eda5.deli.models import ProjektnoMesto



# KONTROLNI objekt_list
class Aktivnost(OsnovnaKombinacija):

    opravilo = models.ForeignKey(
        Opravilo,
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

    VREDNOST_VRSTA = (
        (tip_check, 'check'),
        (tip_vrednost, 'text'),
        (tip_select, 'select'), # Zaloga vrednosti --> OpcijeSelect model
        )

    vrednost_vrsta = models.IntegerField(
        choices=VREDNOST_VRSTA,
        default=1,
        verbose_name='vrsta vrednosti',
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


class KontrolaVrednost(OsnovnaKombinacija):
    '''
    Dokumentacija:
    http://eda5.readthedocs.io/en/latest/kontrolni_list/kontrolni_list.html#projektno-mesto
    '''

    kontrola_specifikacija = models.ForeignKey(
        KontrolaSpecifikacija,
        verbose_name='specifikacija kontrole'
    )

    delovni_nalog = models.ForeignKey(
        DelovniNalog,
        verbose_name='delovni nalog'
    )

    projektno_mesto = models.ManyToManyField(
        ProjektnoMesto,
        blank=True,
        verbose_name='projektno mesto'
    )

    vrednost_check = models.BooleanField(
        blank=True,
        default=False,
        verbose_name="vrednost check"
    )

    vrednost_text = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name="vrednost text"
    )

    vrednost_select = models.ForeignKey(
        KontrolaSpecifikacijaOpcijaSelect,
        blank=True,
        null=True,
        verbose_name="vrednost select"
    )


    class Meta:
        verbose_name = 'vrednost kontrole'
        verbose_name_plural = 'vrednosti kontrol'
