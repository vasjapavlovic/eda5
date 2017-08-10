# Django
from django.db import models
from django.core.urlresolvers import reverse

# Models
from eda5.core.models import TimeStampedModel, ObdobjeLeto, ObdobjeMesec, IsLikvidiranModel, StatusModel
from eda5.deli.models import Stavba
from eda5.etaznalastnina.models import LastniskaEnotaInterna, LastniskaSkupina
from eda5.racunovodstvo.models import Strosek, Racun
from eda5.zahtevki.models import Zahtevek

# Managers
from eda5.razdelilnik.managers import RazdelilnikManager, StrosekRazdelilnikManager, StrosekRazdelilnikPostavkaManager, StrosekLEManager


class Razdelilnik(StatusModel):

    # ATRIBUTES
    # ------------------------------------------------------

    # Oznaka razdelilnika
    # npr. "1" . Zaporedna št. Avtomatska generacija
    oznaka = models.CharField(max_length=20, blank=True, null=True)
    # avtomatsko generirana standardna oznaka
    oznaka_gen = models.CharField(max_length=20, blank=True, null=True)
    
    # Naziv razdelilnika
    # npr. "2304-3037 / 2017-07" . Avtomatska generacija
    naziv = models.CharField(max_length=255)

    # Razdelilnik se izdela za vsako stavbo posebej
    stavba = models.ForeignKey(Stavba)
     
    # Razdelilnike se odpira v zahtevkih
    zahtevek = models.ForeignKey(Zahtevek, blank=True, null=True, verbose_name="zahtevek")

    # Specifika razdelilnika
    # Obdobje obračuna
    obdobje_obracuna_leto = models.ForeignKey(ObdobjeLeto)
    obdobje_obracuna_mesec = models.ForeignKey(ObdobjeMesec)


    # OBJECT MANAGER
    objects = RazdelilnikManager()

    # META AND STRING
    # ------------------------------------------------------
    class Meta:
        verbose_name = 'Razdelilnik'
        verbose_name_plural = 'Razdelilniki'
        ordering = ('-obdobje_obracuna_leto', "-obdobje_obracuna_mesec")

    # Željen izpis
    # "RAZDELILNIK / 2304-3037 / 2017-07"
    def __str__(self):
        return "%s / %s-%s" % (
            self.stavba.oznaka, 
            self.obdobje_obracuna_leto.oznaka, 
            self.obdobje_obracuna_mesec.oznaka,
            )


class StrosekDelitevVrsta(models.Model):

    # ATRIBUTES
    # ------------------------------------------------------

    # Splošni atributi
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    skrajsan_naziv = models.CharField(max_length=50, blank=True, null=True)

    # META AND STRING
    # ------------------------------------------------------
    class Meta:
        verbose_name = 'Vrsta delitve stroška'
        verbose_name_plural = 'Vrsta delitve stroška'


    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)    


class StrosekKljucDelitve(models.Model):

    # ATRIBUTES
    # ------------------------------------------------------

    # Splošni atributi
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    skrajsan_naziv = models.CharField(max_length=50, blank=True, null=True)

    # META AND STRING
    # ------------------------------------------------------
    class Meta:
        verbose_name = 'Ključ delitve stroška'
        verbose_name_plural = 'Ključ delitve stroška'


    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)    



class StrosekRazdelilnik(models.Model):

    # ATRIBUTES
    # ------------------------------------------------------

    # Razširitev EDA5:Racunovodstvo:Strosek
    strosek = models.OneToOneField(Strosek)

    # Ta del razširitve je tudi relacija na razdelilnik
    razdelilnik = models.ForeignKey(Razdelilnik)

    # status in datum ko je strošek razdeljen --> evidenca
    is_razdeljen = models.BooleanField(default=False)
    razdeljen_datum = models.DateField(blank=True, null=True)


    # OBJECT MANAGER
    objects = StrosekRazdelilnikManager()

    def get_absolute_url(self):
        return reverse('moduli:razdelilnik:razdelilnik_detail', kwargs={'pk': self.razdelilnik.pk})

    # META AND STRING
    # ------------------------------------------------------
    class Meta:
        verbose_name = 'StrosekRazdelilnik'
        verbose_name_plural = 'StrosekRazdelilnik'
        # ordering = ('-razdelilnik.obdobje_obracuna_leto', '-razdelilnik.obdobje_obracuna_mesec')

    def __str__(self):
        return "%s | %s-%s-%s" % (
            self.razdelilnik.oznaka, 
            self.strosek.racun.racunovodsko_leto, 
            self.strosek.racun.oznaka, 
            self.strosek.oznaka,
            )


class StrosekRazdelilnikPostavka(models.Model):

    # ATRIBUTES
    # ------------------------------------------------------

    # Splošni atributi
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)

    # Razdelitev stroška na poljubno postavk
    # Znotraj ene lastniške skupine
    # Ta strošek se nato razdeli med posamezne lastniške enote
    strosek_razdelilnik = models.ForeignKey(StrosekRazdelilnik)

    # Lastniška skupina = Skupina lastniških enot med katere se strošek
    # prerazporedi
    lastniska_skupina = models.ForeignKey(LastniskaSkupina, blank=True, null=True)

    # Ključ razdelitve po kateremu se strošek razdeli med lastniške enote
    # znotraj lastniške skupine. Npr. Lastniški delež, število uporabnikov...
    delilnik_kljuc = models.ForeignKey(StrosekKljucDelitve, blank=True, null=True)

    # Razdelitev samo med lastniške enote z določenem statusom (v uporabi, na vse, ...)
    delitev_vrsta = models.ForeignKey(StrosekDelitevVrsta, blank=True, null=True)


    # lastniški-delež: 0.0000 ,  površina: 0000.00 , enota: 0, oseba: 0, | 0000.0000
    delilnik_vrednost = models.DecimalField(decimal_places=4, max_digits=8)
    # Dodaj še ali se strošek razdeli na LASTNIKE/UPORABNIKE

    # Strošek na posameznemu delu - V določenih primerih bi se uporabniku
    # zaračunalo samo strošek, ki odpade na posamezni del
    is_strosek_posameznidel = models.NullBooleanField(verbose_name="strosek na posameznem delu")


    # OBJECT MANAGER
    objects = StrosekRazdelilnikPostavkaManager()

    def get_absolute_url(self):
        return reverse('moduli:razdelilnik:razdelilnik_detail', kwargs={'pk': self.strosek_razdelilnik.pk})

    # META AND STRING
    # ------------------------------------------------------
    class Meta:
        verbose_name = 'StrosekRazdelilnikPostavka'
        verbose_name_plural = 'StrosekRazdelilnikPostavke'
        ordering = ('oznaka',)

    def __str__(self):
        return "%s-%s-%s" % (
            self.strosek_razdelilnik.strosek.racun.racunovodsko_leto, 
            self.strosek_razdelilnik.strosek.racun.oznaka, 
            self.oznaka
            )


class StrosekLE(models.Model):
    # ATRIBUTES
    # ***Relations***
    strosek_razdelilnik = models.ForeignKey(StrosekRazdelilnik)
    lastniska_enota_interna = models.ForeignKey(LastniskaEnotaInterna)

    # ***Mandatory***
    # lastniški-delež: 0.0000 ,  površina: 0000.00 , enota: 0, oseba: 0, | 0000.0000
    delilnik_vrednost = models.DecimalField(decimal_places=4, max_digits=8)
    # ***Optional***

    # OBJECT MANAGER
    objects = StrosekLEManager()

    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'strošek na LE'
        verbose_name_plural = 'stroški na LE'

    def __str__(self):
        return "%s-%s-%s-%s | %s" % (
            self.strosek_razdelilnik.razdelilnik.oznaka,
            self.strosek_razdelilnik.strosek.racun.racunovodsko_leto, 
            self.strosek_razdelilnik.strosek.racun.oznaka, 
            self.strosek_razdelilnik.strosek.oznaka,
            self.lastniska_enota_interna.oznaka,
            )
