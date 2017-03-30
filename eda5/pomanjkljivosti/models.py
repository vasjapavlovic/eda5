
# Python

# Django
from django.db import models
from django.core.urlresolvers import reverse

# Models
from eda5.core.models import TimeStampedModel, IsLikvidiranModel, PrioritetaModel, StatusModel
from eda5.deli.models import ProjektnoMesto
from eda5.partnerji.models import Oseba
from eda5.zahtevki.models import Zahtevek

# Forms

# Managers
from .managers import PomanjkljivostManager, NalogaManager



class Pomanjkljivost(TimeStampedModel, IsLikvidiranModel, PrioritetaModel, StatusModel):
    # ---------------------------------------------------------------------------------------
    ###########################################################################
    # ATRIBUTES
    ###########################################################################

    ''' 
    Navezavo na točen element uredi administrator. 
    Posamezni uporabniki podatke vpisujejo ročno. 
    '''


    # def dokument_directory_path(instance, filename):
    #     # file will be uploaded to MEDIA_ROOT/prejeta_posta/<vrsta_dokumenta>/<new_filename>
    #     old_filename_raw = filename.split(".")
    #     ext = '.' + old_filename_raw[-1]
    #     filename_parameters = ('media/pomanjkljivosti', str(instance.oznaka_baza))
    #     new_filename = '/'.join(filename_parameters)
    #     return '{0}'.format(new_filename + ext)  # output=  media/5.pdf

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

    # priponka = models.FileField(
    #     upload_to=dokument_directory_path, 
    #     verbose_name='Fotograija')


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
    rok = models.DateField(
        verbose_name='rok za izvedbo')

    # Navezava na zahtevek kjer se naloga rešuje
    zahtevek = models.ForeignKey(
        Zahtevek, blank=True, null=True, 
        verbose_name='zahtevek')

    '''
    Navezava na uporabnike, ki nalogo vidijo.
    Ob izdelavi se avtomatsko doda obstoječi uporabnik.
    Nato po želji obstoječi uporabnik lahko nalogo
    dodeli tudi ostalim
    '''
    oseba = models.ManyToManyField(
        Oseba,
        verbose_name="Za Osebe")


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

    #def get_absolute_url(self):
    #    return reverse('moduli:pomanjkljivosti:naloga_list')

    ###########################################################################
    # META AND STRING
    ###########################################################################

    class Meta:
        verbose_name = "naloga"
        verbose_name_plural = "naloge"

    def __str__(self):
        return "(%s) %s" % (self.oznaka, self.naziv)



