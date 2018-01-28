from django.db import models

from eda5.core.models import OsnovnaKombinacija, ZaporednaStevilka
from eda5.delovninalogi.models import Opravilo
from eda5.delovninalogi.models import DelovniNalog
from eda5.deli.models import ProjektnoMesto
from eda5.predpisi.models import PredpisSklop

from eda5.planiranje.models import PlanAktivnost, PlanKontrolaSkupina, PlanKontrolaSpecifikacija






# KONTROLNI objekt_list
class Aktivnost(OsnovnaKombinacija, ZaporednaStevilka):

    opravilo = models.ForeignKey(
        Opravilo,
        verbose_name='opravilo'
        )

    plan_aktivnost = models.ForeignKey(
        PlanAktivnost,
        blank=True,
        null=True
    )

    dan = 'dan'
    teden = 'teden'
    mesec = 'mesec'
    leto = 'leto'

    ENOTE = (
        (dan, "Dan"),
        (teden, "Teden"),
        (mesec, "Mesec"),
        (leto, "Leto")
        )

    perioda_enota = models.CharField(max_length=5, choices=ENOTE, verbose_name="Perioda ENOTA")
    perioda_enota_kolicina = models.IntegerField(verbose_name="Perioda KRATNIK ENOTE")
    perioda_kolicina_na_enoto = models.IntegerField(verbose_name="Perioda KOLIČINA NA ENOTO")



    class Meta:
        verbose_name='Aktivnost'
        verbose_name_plural='Aktivnosti'
        ordering=('oznaka',)


    def __str__(self):
        return '(%s)%s' % (self.oznaka, self.naziv)


class KontrolaSkupina(OsnovnaKombinacija, ZaporednaStevilka):

    aktivnost = models.ForeignKey(
        Aktivnost,
        verbose_name='aktivnost'
        )

    # potreben zaradi izdelave iz vzorcev opravil (planirana opravila)
    plan_kontrola_skupina = models.ForeignKey(
        PlanKontrolaSkupina,
        blank=True,
        null=True,
        verbose_name='planiranja skupina kontrol',
        )


    class Meta:
        ordering = ['oznaka']
        verbose_name = 'Skupina kontrol'

    def __str__(self):
        return "(%s)%s" % (self.oznaka, self.naziv)


class KontrolaSpecifikacija(OsnovnaKombinacija, ZaporednaStevilka):


    projektno_mesto = models.ManyToManyField(
        ProjektnoMesto,
        blank=True,
        verbose_name='projektno mesto'
        )

    kontrola_skupina = models.ForeignKey(
        KontrolaSkupina,
        blank=True,
        null=True,
        verbose_name='skupina kontrol',
    )

    plan_kontrola_specifikacija = models.ForeignKey(
        PlanKontrolaSpecifikacija,
        blank=True,
        null=True,
        verbose_name='planirana kontrola specifikacija',
    )

    tip_check = 1
    tip_vrednost_text = 2
    tip_select = 3
    tip_vrednost_number = 4
    tip_vrednost_yes_no = 5

    VREDNOST_VRSTA = (
        (tip_check, 'check'),
        (tip_vrednost_text, 'text'),
        (tip_vrednost_number, 'number'),
        (tip_vrednost_yes_no, 'yes_no'),
        (tip_select, 'select'), # Zaloga vrednosti --> OpcijeSelect model
        )

    vrednost_vrsta = models.IntegerField(
        choices=VREDNOST_VRSTA,
        default=1,
        verbose_name='vrsta vrednosti',
        )


    class Meta:
        ordering = ['oznaka']

    def __str__(self):
        return "(%s)%s" % (self.oznaka, self.naziv)


class KontrolaSpecifikacijaOpcijaSelect(OsnovnaKombinacija, ZaporednaStevilka):

    kontrola_specifikacija = models.ForeignKey(
        KontrolaSpecifikacija,
        verbose_name='specifikacija kontrole'
        )

    def __str__(self):
        return "%s" % (self.naziv)


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

    projektno_mesto = models.ForeignKey(
        ProjektnoMesto,
        verbose_name='projektno mesto'
    )

    vrednost_check = models.BooleanField(
        blank=True,
        default=False,
        verbose_name="vrednost check"
    )


    yes = 1
    no = -1

    VREDNOST = (
        (yes, 'DA'),
        (no, 'NE'),
        )

    vrednost_yes_no = models.IntegerField(
        choices=VREDNOST,
        blank=True,
        null=True,
        verbose_name='vrednost DA/NE',
        )

    vrednost_text = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name="vrednost text"
    )

    vrednost_number = models.DecimalField(
        decimal_places=2,
        max_digits=50,
        blank=True,
        null=True,
        max_length=255,
        verbose_name="vrednost število"
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
