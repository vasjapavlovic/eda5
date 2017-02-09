from django.db import models
from django.core.urlresolvers import reverse

from . import managers

from eda5.core.models import IsActiveModel, StatusModel, TimeStampedModel
from eda5.partnerji.models import Oseba, Partner
from eda5.deli.models import Element


class Zahtevek(IsActiveModel, TimeStampedModel, StatusModel):
    # ---------------------------------------------------------------------------------------
    # STATUS
    draft = 0
    # vCakanju = 1
    # vPlanu = 2
    vResevanju = 3
    zakljuceno = 4

    STATUS = (
        (draft, 'draft'),
        (vResevanju, 'V Reševanju'),
        (zakljuceno, 'Zaključeno'),
        )

    VRSTE_ZAHTEVKOV = (
        (1, 'Škodni Dogodek'),
        (2, 'Sestanek'),
        (3, 'Izvedba del'),
        (4, 'Predaja Lastnine'),
        (5, 'Analiza Zahtevka'),
        (6, 'Povpraševanje'),
        (7, 'Reklamacija'),
    )

    # ATRIBUTES
    # ***Relations***
    zahtevek_parent = models.ForeignKey("self", null=True, blank=True)
    nosilec = models.ForeignKey(Oseba)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    vrsta = models.IntegerField(choices=VRSTE_ZAHTEVKOV)
    naziv = models.CharField(max_length=255)
    rok_izvedbe = models.DateField()
    # ***Optional***
    # OBJECT MANAGER
    objects = managers.ZahtevekManager()
    # CUSTOM PROPERTIES

    # METHODS
    def get_absolute_url(self):
        # return reverse('moduli:zahtevki:zahtevek_list')
        return reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': self.pk})

    # META AND STRING
    class Meta:
        verbose_name = "zahtevek"
        verbose_name_plural = "zahtevki"
        ordering = ("-pk",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)

  

class ZahtevekSkodniDogodek(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    zahtevek = models.OneToOneField(Zahtevek)
    poskodovane_stvari = models.ManyToManyField(Element, blank=True)
    #     dokumenti

    # zaznamki ZAVAROVALNICA
    #   Mandatory
    datum_nastanka_skode = models.DateField(blank=True, null=True, verbose_name="datum nastanka škode")
    vzrok_skode = models.TextField(blank=True, verbose_name="vzrok škode")
    #   Optional
    is_prijava_policiji = models.NullBooleanField(verbose_name="prijavljeno policiji")
    povzrocitelj = models.CharField(max_length=255, blank=True, verbose_name="povzročitelj (opisno)")
    #     oblika: 99999.99
    predvidena_visina_skode = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True,
                                                  verbose_name="predvidena višina škode")
    # OBJECT MANAGER
    # CUSTOM PROPERTIES

    # METHODS
    def get_absolute_url(self):
        # return reverse('moduli:zahtevki:zahtevek_list')
        return reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': self.zahtevek.pk})

    # META AND STRING
    class Meta:
        verbose_name = "škodni dogodek"
        verbose_name_plural = "škodni dogodki"
        ordering = ("datum_nastanka_skode",)

    def __str__(self):
        return "%s" % (self.zahtevek.oznaka)


class ZahtevekSestanek(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    zahtevek = models.OneToOneField(Zahtevek)
    sklicatelj = models.ForeignKey(Partner, null=True, blank=True)
    udelezenci = models.ManyToManyField(Oseba, blank=True, verbose_name="udeleženci")
    #   Mandatory
    datum = models.DateField(null=True, blank=True)
    #   Optional
    # OBJECT MANAGER
    objects = managers.ZahtevekSestanekManager()
    # CUSTOM PROPERTIES

    # METHODS
    def get_absolute_url(self):
        # return reverse('moduli:zahtevki:zahtevek_list')
        return reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': self.zahtevek.pk})

    # META AND STRING
    class Meta:
        verbose_name = "sestanek"
        verbose_name_plural = "sestanki"
        ordering = ("-zahtevek__oznaka", )

    def __str__(self):
        return "%s" % (self.zahtevek.oznaka)


class ZahtevekIzvedbaDela(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    zahtevek = models.OneToOneField(Zahtevek)
    #   Mandatory
    #   Optional
    is_zakonska_obveza = models.NullBooleanField(verbose_name='zakonska obveza')
    # OBJECT MANAGER
    objects = managers.ZahtevekIzvedbaDelaManager()
    # CUSTOM PROPERTIES

    # METHODS
    def get_absolute_url(self):
        # return reverse('moduli:zahtevki:zahtevek_list')
        return reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': self.zahtevek.pk})

    # META AND STRING
    class Meta:
        verbose_name = "izvedba dela"
        verbose_name_plural = "izvedba del"
        ordering = ("-zahtevek__oznaka", )

    def __str__(self):
        return "%s" % (self.zahtevek.oznaka)


class ZahtevekAnaliza(models.Model):
    pass
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS
    # META AND STRING


class ZahtevekPovprasevanje(models.Model):
    pass
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS
    # META AND STRING


class ZahtevekReklamacija(models.Model):
    pass
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS
    # META AND STRING
