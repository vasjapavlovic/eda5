# Django
from django.db import models
from django.core.urlresolvers import reverse

# Models
from eda5.core.models import TimeStampedModel, ObdobjeLeto, ObdobjeMesec, IsLikvidiranModel, StatusModel
from eda5.deli.models import Stavba
from eda5.etaznalastnina.models import LastniskaEnotaInterna
from eda5.racunovodstvo.models import Strosek, Racun
from eda5.zahtevki.models import Zahtevek

# Managers
from eda5.razdelilnik.managers import RacunRazdelilnikManager


class StrosekLE(models.Model):
    # ATRIBUTES
    # ***Relations***
    strosek = models.ForeignKey(Strosek)
    lastniska_enota = models.ForeignKey(LastniskaEnotaInterna)

    # ***Mandatory***
    # lastniški-delež: 0.0000 ,  površina: 0000.00 , enota: 0, oseba: 0, | 0000.0000
    delilnik_vrednost = models.DecimalField(decimal_places=4, max_digits=8)
    # ***Optional***
    # OBJECT MANAGER

    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'strošek na LE'
        verbose_name_plural = 'stroški na LE'

    def __str__(self):
        return "%s - %s" % (self.strosek.oznaka, self.lastniska_enota.oznaka)


class Razdelilnik(StatusModel):

    # ATRIBUTES
    # ------------------------------------------------------

    # Splošni atributi
    oznaka = models.CharField(max_length=20)  # npr. "EDA-2017-07"
    naziv = models.CharField(max_length=255)  # npr. "Razdelilnik stroškov EDA CENTER 2017-07"

    # Razdelilnike se odpira v zahtevkih
    zahtevek = models.ForeignKey(Zahtevek, blank=True, null=True, verbose_name="zahtevek")

    # Specifika razdelilnika
    # Obdobje obračuna
    obdobje_obracuna_leto = models.ForeignKey(ObdobjeLeto)
    obdobje_obracuna_mesec = models.ForeignKey(ObdobjeMesec)

    # Stavba
    stavba = models.ForeignKey(Stavba)

    # META AND STRING
    # ------------------------------------------------------
    class Meta:
        verbose_name = 'Razdelilnik'
        verbose_name_plural = 'Razdelilniki'
        ordering = ('-obdobje_obracuna_leto', "-obdobje_obracuna_mesec")

    def __str__(self):
        return "%s | %s-%s" % (self.oznaka, self.obdobje_obracuna_leto.oznaka, self.obdobje_obracuna_mesec.oznaka)


class RacunRazdelilnik(models.Model):
    # ATRIBUTES
    # ------------------------------------------------------

    # Povemo kateri Račun se obračuna v posameznem Razdelilniku
    racun = models.OneToOneField(Racun)
    razdelilnik = models.ForeignKey(Razdelilnik)

    # Specifični atributi
    is_razdeljen = models.BooleanField(default=False)
    razdeljen_datum = models.DateField(blank=True, null=True)


    # OBJECT MANAGER
    objects = RacunRazdelilnikManager()

    def get_absolute_url(self):
        return reverse('moduli:razdelilnik:razdelilnik_detail', kwargs={'pk': self.razdelilnik.pk})

    # META AND STRING
    # ------------------------------------------------------
    class Meta:
        verbose_name = 'RacunRazdelilnik'
        verbose_name_plural = 'RacunRazdelilnik'
        # ordering = ('-razdelilnik.obdobje_obracuna_leto', '-razdelilnik.obdobje_obracuna_mesec')

    def __str__(self):
        return "%s | %s" % (self.razdelilnik.oznaka, self.racun.oznaka)