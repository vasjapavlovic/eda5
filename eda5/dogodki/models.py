from django.db import models
from django.apps import apps
from django.core.urlresolvers import reverse


from . import managers

from eda5.core.models import IsActiveModel, StatusModel, TimeStampedModel
from eda5.pomanjkljivosti.models import Pomanjkljivost
from eda5.zahtevki.models import Zahtevek


class Dogodek(IsActiveModel, TimeStampedModel, StatusModel):
# ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    zahtevek = models.ForeignKey(Zahtevek)  # OneToOneField = pod zahtevek se rašuje samo en dogodek
    #   Mandatory
    datum_dogodka = models.DateField(verbose_name="datum dogodka")
    opis_dogodka = models.TextField(verbose_name="opis dogodka")
    is_potrebna_prijava_policiji = models.NullBooleanField(verbose_name="potrebna prijava policiji?")
    is_nastala_skoda = models.NullBooleanField(verbose_name="Je nastala škoda?")
    povzrocitelj = models.CharField(max_length=255, blank=True, verbose_name="povzročitelj (opisno)")
    #   Optional
    cas_dogodka = models.TimeField(blank=True, null=True, verbose_name="okvirni čas dogodka")
    predvidena_visina_skode = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True, verbose_name="predvidena višina škode")
    prijava_skode = models.ForeignKey('arhiv.Arhiviranje', blank=True, null=True, related_name="prijava_skode")
    prijava_policiji = models.ForeignKey('arhiv.Arhiviranje', blank=True, null=True, related_name="prijava_policiji")
    racun_za_popravilo = models.ForeignKey('arhiv.Arhiviranje', blank=True, null=True, related_name="racun_za_popravilo")
    poravnava_skode = models.ForeignKey('arhiv.Arhiviranje', blank=True, null=True, related_name="poravnava_skode")

    pomanjkljivost = models.ManyToManyField(Pomanjkljivost, blank=True)

    # OBJECT MANAGER
    objects = managers.DogodekManager()
    # CUSTOM PROPERTIES
    # METHODS

    def get_absolute_url(self):
        return reverse('moduli:dogodki:dogodek_detail', kwargs={'pk': self.pk})

    #---------------------------------------------------------
    # META and STR
    # ========================================================
    # META AND STRING
    class Meta:
        verbose_name="dogodek"
        verbose_name_plural="dogodki"

    def __str__(self):
        return "%s | %s | %s" % (self.pk, self.opis_dogodka, self.datum_dogodka)

#class ZahtevekSkodniDogodek2(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    #'''Datum dogodka ali datum nastanka škode'''
    #datum_dogodka = models.DateField(verbose_name="datum dogodka ali nastanka škode")
    #'''opis dogodka, vzrok škode'''
    #opis_dogodka = models.TextField(verbose_name="opis dogodka ali vzroka nastanka škode")
    #visina_skode_ocena = models.DecimalField(
    #    decimal_places=10, max_digits=12, verbose_name="ocena višine škode")

    # === PRIJAVA POLICIJI ========================================================
    #'''v primeru, da je potrebno dogodek prijaviti policiji se izpolni naslednje'''
    #is_potrebna_prijava_policiji = models.NullBooleanField(verbose_name="potrebna prijava policiji")


    #osnova = models.DecimalField(decimal_places=5, max_digits=10, verbose_name='osnova za ddv')
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS
    # META AND STRING
