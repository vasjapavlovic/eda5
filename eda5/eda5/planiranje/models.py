from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

from eda5.posta.models import Dokument
from eda5.core.models import TimeStampedModel, IsActiveModel
from eda5.katalog.models import ArtikelPlan
from eda5.deli.models import Element
from eda5.zahtevki.models import Zahtevek

from . import managers


class SkupinaPlanov(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    oznaka = models.CharField(max_length=25)
    naziv = models.CharField(max_length=255)
    #   Optional
    zap_st = models.IntegerField(default=0, verbose_name="zaporedna številka")
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "skupina planov"
        verbose_name_plural = "skupine planov"
        ordering = ("zap_st",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class Plan(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    sklop = models.ForeignKey(SkupinaPlanov)
    zahtevek = models.ForeignKey(Zahtevek, blank=True, null=True)  # plan se izdela iz zahtevka
    #   Mandatory
    oznaka = models.CharField(max_length=25)
    naziv = models.CharField(max_length=255)
    #   Optional
    zap_st = models.IntegerField(default=0, verbose_name="zaporedna številka")
    opis = models.CharField(max_length=255)
    # OBJECT MANAGER
    # CUSTOM PROPERTIES

    # METHODS
    def get_absolute_url(self):
        return reverse("moduli:planiranje:plan_detail", kwargs={"pk": self.pk})

    # META AND STRING
    class Meta:
        verbose_name = "plan"
        verbose_name_plural = "plani"

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


# class PlanIzdaja(TimeStampedModel, IsActiveModel):
#     # ---------------------------------------------------------------------------------------
#     # ATRIBUTES
#     #   Relations
#     plan = models.ForeignKey(Plan)
#     '''dodaj, da je potrebna potrditvena dokumentacija za plan'''
#     #   Mandatory
#     oznaka = models.CharField(max_length=20, blank=True)
#     datum_izdaje = models.DateField()
#     #   Optional
#     # OBJECT MANAGER
#     # CUSTOM PROPERTIES
#     # METHODS

#     # META AND STRING
#     class Meta:
#         verbose_name = "izdaja plana"
#         verbose_name_plural = "izdaje planov"

#     def __str__(self):
#         return "%s | %s(%s)" % (self.datum_izdaje, self.plan.naziv, self.plan.oznaka)


class PlaniranoOpravilo(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
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
    # ATRIBUTES
    #   Relations
    plan = models.ForeignKey(Plan)
    #   Mandatory
    oznaka = models.CharField(max_length=25)
    naziv = models.CharField(max_length=255)
    namen = models.CharField(max_length=255)
    obseg = models.TextField()
    perioda_predpisana_enota = models.CharField(max_length=5, choices=ENOTE, verbose_name="enota periode")
    perioda_predpisana_enota_kolicina = models.IntegerField(verbose_name="kolicina enote periode")
    perioda_predpisana_kolicina_na_enoto = models.IntegerField(verbose_name="kolicina na enoto periode")
    datum_prve_izvedbe = models.DateField(blank=True, null=True)

    datum_izvedeno_dne = models.DateField(
        blank=True, null=True,
        verbose_name='Izvedeno dne')

    datum_naslednjega_opravila = models.DateField(
        blank=True, null=True,
        verbose_name='Naslednji pregled')

    # zaokrožitev minimalno minut
    zmin = models.IntegerField(
        default=15, 
        verbose_name='zaokrožitev [min]')
    
    #   Optional
    opomba = models.TextField(blank=True)
    # OBJECT MANAGER
    objects = managers.PlaniranoOpraviloManager()

    # CUSTOM PROPERTIES
    @property
    def do_naslednjega_opravila_dni(self):
        if self.datum_naslednjega_opravila:
            dni = self.datum_naslednjega_opravila - timezone.now().date()
            return dni.days

    @property
    def zapade_14dni(self):
        if self.do_naslednjega_opravila_dni:
            if self.do_naslednjega_opravila_dni <= 14:
                return True
            else:
                return False

    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "planirano opravilo"
        verbose_name_plural = "planirana opravila"
        ordering = ('oznaka', )

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class PlaniranaAktivnost(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    artikel_plan = models.ForeignKey(ArtikelPlan, blank=True, null=True)
    planirano_opravilo = models.ForeignKey(PlaniranoOpravilo, blank=True, null=True)
    element = models.ForeignKey(Element, blank=True, null=True)
    #   Mandatory
    naziv_opravila_izven_plana = models.CharField(max_length=255, blank=True)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "planirana aktivnost"
        verbose_name_plural = "planirane aktivnosti"

    def __str__(self):
        if self.artikel_plan:
            return "%s" % (self.artikel_plan.naziv)
        else:
            return "%s" % (self.naziv_opravila_izven_plana)