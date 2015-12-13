from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models

from eda5.core.models import TimeStampedModel, IsActiveModel
from eda5.users.models import User

from .managers import OsebaManager, TrrManager


''' POZOR !!! uporabljeni DJANGO-SIGNALS.
    Avtomatsko se izdelajo SkupinaPartnerjev. Glej spodaj'''


class Partner(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    user = models.OneToOneField(User, null=True, blank=True)
    # ***Mandatory***
    kratko_ime = models.CharField(max_length=100)
    naslov = models.CharField(max_length=255)
    posta = models.ForeignKey("Posta", verbose_name='pošta')
    is_pravnaoseba = models.BooleanField()
    davcni_zavezanec = models.BooleanField()
    # ***Optional***
    davcna_st = models.CharField(max_length=15, unique=True, blank=True)
    maticna_st = models.CharField(max_length=15, blank=True)
    dolgo_ime = models.CharField(max_length=255, blank=True)

    # OBJECT MANAGER
    # CUSTOM PROPERTIES

    # METHODS
    def get_absolute_url(self):
        return reverse("moduli:partnerji:detail", kwargs={"pk": self.pk})

    # META AND STRING
    class Meta:
        verbose_name = "partner"
        verbose_name_plural = "partnerji"
        ordering = ['kratko_ime',]

    def __str__(self):
        return "%s" % (self.kratko_ime)


class SkupinaPartnerjev(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    partner = models.ManyToManyField("Partner")
    # ***Mandatory***
    naziv = models.CharField(max_length=255)
    # ***Optional***
    oznaka = models.CharField(blank=True, max_length=20)

    @receiver(post_save, sender=Partner)
    def create_skupina_partnerjev_from_partner(sender, created, instance, **kwargs):

        if created:
            skupina_partnerjev = SkupinaPartnerjev(davcna_st=instance.davcna_st, naziv=instance.kratko_ime)
            skupina_partnerjev.save()
            skupina_partnerjev.partner.add(instance.pk)  # dodajanje k many-to-many

    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "skupina partnerjev"
        verbose_name_plural = "skupine partnerjev"
        ordering = ['naziv',]

    def __str__(self):
        return "%s" % (self.naziv)


class Drzava(models.Model):

    naziv = models.CharField(max_length=100)
    iso_koda = models.CharField(max_length=3, unique=True)

    class Meta:
        verbose_name = "Država"
        verbose_name_plural = "Države"

    def __str__(self):
        return "%s (%s)" % (self.naziv, self.iso_koda)



class Posta(TimeStampedModel, IsActiveModel):

    postna_stevilka = models.CharField(max_length=10, unique=True,
                                       verbose_name='poštna številka')
    naziv = models.CharField(max_length=100)
    drzava = models.ForeignKey(Drzava)

    class Meta:
        verbose_name = "Pošta"
        verbose_name_plural = "Pošte"

    def __str__(self):
        return "%s %s" % (self.postna_stevilka, self.naziv)


class Banka(TimeStampedModel, IsActiveModel):

    partner = models.OneToOneField(Partner, blank=True)
    bic_koda = models.CharField(max_length=8, unique=True)
    bancna_oznaka = models.CharField(max_length=2, unique=True)
    # Po možnosti dodaj "kratek_naziv", ki bi se izpisal pred IBANOM pod partnerji details

    class Meta:
        verbose_name = "Banka"
        verbose_name_plural = "Banke"

    def __str__(self):
        return "%s | %s" % (self.partner.kratko_ime, self.bic_koda)


class TRRacun(TimeStampedModel, IsActiveModel):

    iban = models.CharField(max_length=20, unique=True, verbose_name="stevilka računa")
    banka = models.ForeignKey(Banka)
    partner = models.ForeignKey(Partner, verbose_name='partner')

    objects = TrrManager()

    class Meta:
        verbose_name = "TR Račun"
        verbose_name_plural = "TR Računi"

    def __str__(self):
        return "%s - %s | %s" % (self.partner.kratko_ime, self.iban, self.banka.bic_koda)


'''
Pooblaščene osebe partnerja. Pooblaščena za naročila, Delavci, itd.
'''
class Oseba(TimeStampedModel, IsActiveModel):

    # STATUS
    # A. Pooblaščenec
    # B. Delavec

    STATUS = (
        ("A", 'pooblaščenec'),
        ("B", 'delavec'),
        )

    priimek = models.CharField(max_length=50)
    ime = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUS)
    kvalifikacije = models.TextField(blank=True)
    podjetje = models.ForeignKey(Partner)

    '''Dodaj Davčno Številko Osebam.'''

    objects = OsebaManager()

    class Meta:
        verbose_name = "Oseba"
        verbose_name_plural = "Osebe"

    def get_absolute_url(self):
        return reverse('moduli:partnerji:detail', kwargs={"pk": self.podjetje.pk})

    def __str__(self):
        return "%s %s - %s" % (self.priimek, self.ime, self.status)
