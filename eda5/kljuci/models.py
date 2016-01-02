from django.db import models


from eda5.deli.models import Element
from eda5.lastnistvo.models import PredajaLastnine


class SklopKljucev(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    element = models.ForeignKey(Element, blank=True, null=True)  # relacija na kaj odpira. Projektno mesto?
    #   Mandatory
    oznaka = models.CharField(max_length=50, unique=True)
    naziv = models.CharField(max_length=255)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "ključ"
        verbose_name_plural = "ključi"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class Kljuc(models.Model):
    # ---------------------------------------------------------------------------------------
    VRSTA_KLJUCA = (
        (1, "ključ"),
        (2, "daljinec"),
    )

    STATUS_DALJINCA = (
        (1, "za uporabo"),
        (2, "odpisan"),  # zaradi izgube ali npr okvare daljinca
    )

    # ATRIBUTES
    #   Relations
    sklop_kljucev = models.ForeignKey(SklopKljucev, verbose_name="sklop ključev")
    #   Mandatory
    oznaka = models.CharField(max_length=50)
    vrsta_kljuca = models.IntegerField(choices=VRSTA_KLJUCA)
    status_kljuca = models.IntegerField(default=1, choices=STATUS_DALJINCA)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "ključ"
        verbose_name_plural = "ključi"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.get_vrsta_kljuca_display())


class PredajaKljucev(models.Model):

    ''' Predaja Ključev je ločena Ker se pričakuje Zapisnik o predaji, ki ni odvisen od
    Predaje Lastnine '''

    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    kljuc = models.ManyToManyField(Kljuc)
    predaja_lastnine = models.ForeignKey(PredajaLastnine, blank=True, null=True)
    #   Mandatory
    oznaka = models.CharField(max_length=20)
    datum_predaje_kljuca = models.DateField()
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "predaja kljuca"
        verbose_name_plural = "predaje kljucev"

    def __str__(self):
        return "%s | %s" % (self.kljuc.oznaka, self.datum_predaje_kljuca)
