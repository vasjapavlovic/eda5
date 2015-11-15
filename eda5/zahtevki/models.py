from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

from . import managers

from eda5.core.models import IsActiveModel, StatusModel, TimeStampedModel
from eda5.narocila.models import Narocilo
from eda5.partnerji.models import Oseba, Partner
from eda5.posta.models import Dokument
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
        # (4, 'Zbor Lastnikov'),
        # (5, 'Reklamacija Nabave'),
        # (6, 'Reklamacija Prodaje'),
    )

    # ATRIBUTES
    # ***Relations***
    zahtevek_parent = models.ForeignKey("self", null=True, blank=True)
    narocilo = models.ForeignKey(Narocilo)  # ***izbira samo med veljavnimi naročili****
    nosilec = models.ForeignKey(Oseba)
    dokument = models.ManyToManyField(Dokument, blank=True)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    vrsta = models.IntegerField(choices=VRSTE_ZAHTEVKOV)
    predmet = models.CharField(max_length=255)
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
        ordering = ("oznaka",)

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.predmet)


class ZahtevekSkodniDogodek(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    zahtevek = models.OneToOneField(Zahtevek)
    poskodovane_stvari = models.ManyToManyField(Element, blank=True)
    #     dokumenti
    dokument_prijava_skode = models.ForeignKey(Dokument, related_name="dokument_prijava_skode",
                                               blank=True, null=True, verbose_name="prijava škode")
    dokument_zapisnik_ogleda = models.ForeignKey(Dokument, related_name="dokument_zapisnik_ogleda",
                                                 blank=True, null=True, verbose_name="zapisnik o ogledu škode")
    dokument_poravnava = models.ForeignKey(Dokument, related_name="dokument_poravnava",
                                           blank=True, null=True, verbose_name="poravnava škode")
    dokazno_gradivo = models.ForeignKey(Dokument, blank=True, null=True, related_name="dokazno_gradivo")
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
    @receiver(post_save, sender=Zahtevek)
    def create_delovninalog_za_novo_opravilo(sender, created, instance, **kwargs):

        if instance.vrsta == 1:
            if created:
                sd = ZahtevekSkodniDogodek(zahtevek=instance)
                sd.save()

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
    zapisnik = models.ForeignKey(Dokument, null=True, blank=True)
    #   Mandatory
    datum = models.DateField(null=True, blank=True)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES

    # METHODS
    @receiver(post_save, sender=Zahtevek)
    def create_delovninalog_za_novo_opravilo(sender, created, instance, **kwargs):

        if instance.vrsta == 2:
            if created:
                ses = ZahtevekSestanek(zahtevek=instance)
                ses.save()

    def get_absolute_url(self):
        # return reverse('moduli:zahtevki:zahtevek_list')
        return reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': self.zahtevek.pk})

    # META AND STRING
    class Meta:
        verbose_name = "sestanek"
        verbose_name_plural = "sestanki"
        ordering = ("datum",)

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
    # CUSTOM PROPERTIES

    # # METHODS
    @receiver(post_save, sender=Zahtevek)
    def create_delovninalog_za_novo_opravilo(sender, created, instance, **kwargs):

        if instance.vrsta == 3:
            if created:
                izvedba_del = ZahtevekIzvedbaDela(zahtevek=instance)
                izvedba_del.save()

    def get_absolute_url(self):
        # return reverse('moduli:zahtevki:zahtevek_list')
        return reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': self.zahtevek.pk})

    # META AND STRING
    class Meta:
        verbose_name = "izvedba dela"
        verbose_name_plural = "izvedba del"

    def __str__(self):
        return "%s" % (self.zahtevek.oznaka)
