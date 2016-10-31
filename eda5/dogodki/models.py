from django.db import models

from eda5.zahtevki.models import Zahtevek

class Dogodek(models.Model):
# ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    zahtevek = models.OneToOneField(Zahtevek)  # OneToOneField = pod zahtevek se rašuje samo en dogodek
    #   Mandatory
    datum_dogodka = models.DateField(verbose_name="datum dogodka")
    opis_dogodka = models.TextField(verbose_name="opis dogodka")
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS
    # META AND STRING  
    class Meta:
    	verbose_name="dogodek"
    	verbose_name_plural="dogodki"

    def __str__(self):
    	return "%s (%s)" % (self.zahtevek.naziv, self.zahtevek.oznaka)  # Oznaka dogodka je kar oznaka zahtevka glede na to,
    										  # da samo en dogodek lahko rešuje pod en zahtevek

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