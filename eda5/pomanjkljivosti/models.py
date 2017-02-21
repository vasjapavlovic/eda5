from django.db import models
from django.core.urlresolvers import reverse

from .managers import PomanjkljivostManager

# Core
from eda5.core.models import TimeStampedModel, IsLikvidiranModel, PrioritetaModel

# Deli
from eda5.deli.models import ProjektnoMesto

# Zahtevek
from eda5.zahtevki.models import Zahtevek


class Pomanjkljivost(TimeStampedModel, IsLikvidiranModel, PrioritetaModel):
    # ---------------------------------------------------------------------------------------
    ###########################################################################
    # ATRIBUTES
    ###########################################################################

    ''' Navezavo na točen element uredi administrator. 
    Posamezni uporabniki podatke vpisujejo ročno. '''

    # Osnovni podatki za vnos iz strani zunanjih

    oznaka = models.CharField(
        max_length=20)

    opis_text = models.TextField(
        blank=True, null=True,
        verbose_name='Problem')

    ugotovljeno_dne = models.DateField(
        verbose_name='datum ugotovitve')

    prijavil_text = models.CharField(
        max_length=255, 
        verbose_name='prijavil')

    element_text = models.CharField(
        max_length=255, blank=True, null=True, 
        verbose_name='element opisno')

    etaza_text = models.CharField(
        max_length=50, blank=True, null=True, 
        verbose_name='etaža opisno')

    lokacija_text = models.CharField(
        max_length=255, blank=True, null=True, 
        verbose_name='lokacija opisno')


    # Dodatni podatki za administratorja

    ''' Točni podatki o nazivu pomanjkljivosti '''

    naziv = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name='naziv pomanjkljivosti')

    opis = models.TextField(
        blank=True, null=True, 
        verbose_name='opis pomanjkljivosti')

    ''' Projektno mesto je del dela stavbe, ima lokacijo 
    (etaža, površina, stavba) '''

    element = models.ManyToManyField(
        ProjektnoMesto, blank=True, 
        verbose_name='element')

    ''' Navezava na zahtevek kjer se pomanjkljivost 
    rešuje '''
     
    zahtevek = models.ForeignKey(
        Zahtevek, blank=True, null=True, 
        verbose_name='zahtevek')

    
    ###########################################################################
    # OBJECT MANAGER
    ###########################################################################

    objects = PomanjkljivostManager()

    ###########################################################################
    # CUSTOM PROPERTIES
    ###########################################################################

    ###########################################################################
    # METHODS
    ###########################################################################

    def get_absolute_url(self):
        return reverse('moduli:pomanjkljivosti:pomanjkljivost_list')

    ###########################################################################
    # META AND STRING
    ###########################################################################

    class Meta:
        verbose_name = "pomanjkljivost"
        verbose_name_plural = "pomanjkljivosti"

    def __str__(self):
        return "(%s) %s" % (self.oznaka, self.opis_text)


