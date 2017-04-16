# Python
# Django
from django.db import models
# Models
from . import managers
from eda5.core.models import timestampedmodel
from eda5.partnerji.models import Partner
# Forms
# Widgets


class Povprasevanje(timestampedmodel):
    '''
    zbirnik ponudb, izvedba analize ponudb in
    izbira dobavitelja. Zaključek povpraševanja
    je izdaja naročilnice.
    '''

    #=================================================
    # ATRIBTUI
    #-------------------------------------------------
    oznaka = models.CharField(
        max_length=255,
        verbose_name="oznaka",)
 
    # naziv in opis tvorita predmet povpraševanja
    naziv = models.CharField(
        max_length=255,
        verbose_name="naziv",)

    opis = models.TextField(
        verbose_name="opis",)

    zahtevek = models.ForeignKey( 
        Zahtevek,
        blank=True, null=True,
        verbose_name="zahtevek")


    #---------------------------------------------------------
    # OBJECT MANAGER
    # ========================================================
    objects = managers.PovprasevanjeManager()

    def get_absolute_url(self):
        return reverse('moduli:povprasevanje:povprasevanje_detail', kwargs={'pk': self.pk})

    #---------------------------------------------------------
    # META and STR
    # ========================================================
    class Meta:
        verbose_name_plural = "povpraševanja"

    def __str__(self):
        return "%s | %s | %s" % (self.oznaka, self.naziv, self.zahtevek.oznaka)


class Postavka(timestampedmodel):
    '''
    postavka povpraševanja - popis
    '''

    # ===ATRIBUTI

    # način označevanja postavke v popisu
    oznaka = models.CharField(
        max_length=255,
        verbose_name="oznaka",
    )

    # opis postavke
    opis = models.TextField(
        verbose_name="opis",)

    # postavka je del povpraševanja
    povprasevanje = models.ForeignKey(
        Povprasevanje,
        verbose_name="povprasevanje",
    )

    #---------------------------------------------------------
    # OBJECT MANAGER
    # ========================================================
    objects = managers.PostavkaManager()

    def get_absolute_url(self):
        return reverse('moduli:povprasevanje:povprasevanje_detail', 
            kwargs={'pk': self.povprasevanje.pk})

    #---------------------------------------------------------
    # META and STR
    # ========================================================
    class Meta:
        verbose_name_plural = "postavke povpraševanja"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.povprasevanje.oznaka)


class Ponudba(timestampedmodel):
    '''
    dobavitelj, ki se ga v povpraševanju obravnava
    '''

    # ===ATRIBUTI
    oznaka = models.CharField(
        max_length=255,
        verbose_name="oznaka",
    )

    ponudnik = models.ForeignKey(
        Partner,
        verbose_name="ponudnik",
    )

    vrednost_postavke = models.ManyToManyField(
        Postavka,
        blank=True,
        through='PonudbaPoPostavki',
        verbose_name="vrednost postavke")

    # ponudba je del povpraševanja
    povprasevanje = models.ForeignKey(
        Povprasevanje,
        verbose_name="povprasevanje",
    )

    # povprasevanje_poslano_dne
    # ponudba_prejeta_dne
    # datum_ponudbe
    # veljavnost_dni
    # veljavnost_datum
    # ponudba (arhiviranje)

    #---------------------------------------------------------
    # OBJECT MANAGER
    # ========================================================
    objects = managers.PonudbaManager()

    def get_absolute_url(self):
        return reverse('moduli:povprasevanje:povprasevanje_detail', 
            kwargs={'pk': self.povprasevanje.pk})

    #---------------------------------------------------------
    # META and STR
    # ========================================================
    class Meta:
        verbose_name_plural = "ponudbe"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.ponudnik.kratko_ime)


class PonudbaPoPostavki(timestampedmodel):

    postavka = models.ForeignKey(Postavka)

    ponudba = models.ForeignKey(Ponudba)

    vrednost_za_izracun = models.DecimalField(
        max_digits=10, decimal_places=2,
        blank=True, null=True,
        verbose_name="vrednost za izračun cene"
    )

    vrednost_opis = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name="ponudba po postavkah",
    )

    #---------------------------------------------------------
    # OBJECT MANAGER
    # ========================================================
    objects = managers.PonudbaPoPostavkiManager()

    def get_absolute_url(self):
        return reverse('moduli:povprasevanje:povprasevanje_detail', 
            kwargs={'pk': self.postavka.povprasevanje.pk})

    #---------------------------------------------------------
    # META and STR
    # ========================================================
    class Meta:
        verbose_name_plural = "ponudbe po postavkah"

    def __str__(self):
        return "%s | %s" % (self.ponudba.oznaka, self.postavka.oznaka)


