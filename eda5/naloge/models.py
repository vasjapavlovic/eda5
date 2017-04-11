
# Python

# Django
from django.db import models
from django.core.urlresolvers import reverse

# Models
from eda5.core.models import TimeStampedModel, IsLikvidiranModel, PrioritetaModel, StatusModel
from eda5.partnerji.models import Oseba
from eda5.sestanki.models import Sklep
from eda5.zahtevki.models import Zahtevek

# Forms

# Managers
from .managers import NalogaManager


class Naloga(TimeStampedModel, IsLikvidiranModel, PrioritetaModel, StatusModel):

    '''
    Definirana kot nekaj kar je potrebno izdelali.
    Kot nekakšen "Task". Vsak uporabnik ima svoje naloge,
    ki si jih vpiše, da jih mora rešiti. Naloge se 
    Rešujejo z opravili - zato, da je evidenca kje so bile rešene.
    Naloge se vežejo tudi na alinee po sestankih.
    '''

    ###########################################################################
    # ATRIBUTES
    ###########################################################################

    oznaka = models.CharField(
        max_length=20)

    naziv = models.CharField(
        max_length=255,
        verbose_name='naziv naloge')

    opis = models.TextField(
        blank=True, null=True, 
        verbose_name='opis naloge')

    # natančno omejeno trajanje
    rok_izvedbe = models.DateField(
        verbose_name='rok za izvedbo')

    # Navezava na zahtevek kjer se naloga rešuje
    zahtevek = models.ForeignKey(
        Zahtevek, blank=True, null=True, 
        verbose_name='Rešuje se pod Zahtevkom')
    '''
    Navezava na uporabnike, ki nalogo vidijo.
    Ob izdelavi se avtomatsko doda obstoječi uporabnik.
    Nato po želji obstoječi uporabnik lahko nalogo
    dodeli tudi ostalim
    '''
    nosilec = models.ForeignKey(
        Oseba,
        verbose_name="nosilec")

    '''
    Navezava na sestanek. Na podlagi sklepov sestanka se rešujejo
    oziroma določijo naloge
    '''
    sklep_sestanka = models.ForeignKey(
        Sklep,
        blank=True, null=True,
        verbose_name="sklep sestanka")


    ###########################################################################
    # OBJECT MANAGER
    ###########################################################################

    objects = NalogaManager()

    ###########################################################################
    # CUSTOM PROPERTIES
    ###########################################################################

    ###########################################################################
    # METHODS
    ###########################################################################

    def get_absolute_url(self):
        return reverse('moduli:naloge:naloga_list')

    ###########################################################################
    # META AND STRING
    ###########################################################################

    class Meta:
        verbose_name = "naloga"
        verbose_name_plural = "naloge"

    def __str__(self):
        return "(%s) %s" % (self.oznaka, self.naziv)



