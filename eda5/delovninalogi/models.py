from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime
from django.utils import timezone

from django.dispatch import receiver
from django.db.models.signals import post_save

from . import managers

from eda5.core.models import IsActiveModel, StatusModel, TimeStampedModel
from eda5.deli.models import Element
from eda5.narocila.models import Narocilo
from eda5.partnerji.models import Oseba
from eda5.zahtevki.models import Zahtevek


class Opravilo(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    zahtevek = models.ForeignKey(Zahtevek)
    narocilo = models.ForeignKey(Narocilo, verbose_name='naročilo')
    nadzornik = models.ForeignKey(Oseba)
    '''pod naročilo je odzadaj tudi relacija na naročnika in izvajalca'''
    # planirano_opravilo = models.ForeignKey(PlanOpravilo, blank=True, null=True)
    element = models.ManyToManyField(Element)
    #   Mandatory
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    rok_izvedbe = models.DateField()
    is_potrjen = models.BooleanField(default=False, verbose_name="Potrjeno iz strani nadzornika")
    #   Optional


    # OBJECT MANAGER
    objects = managers.OpraviloManager()

    # CUSTOM PROPERTIES

    @property
    def delovninalog_koncan_sorted_by_date(self):
        return self.delovninalog_set.exclude(datum_stop__isnull=True).order_by("datum_start")

    @property
    def delovninalog_vdelu_sorted_by_date(self):
        return self.delovninalog_set.exclude(datum_stop__isnull=False).order_by("datum_start")

    # METHODS
    def get_absolute_url(self):
        return reverse("moduli:delovninalogi:opravilo_detail", kwargs={'pk': self.pk})

    # META AND STRING
    class Meta:
        verbose_name = "Opravilo"
        verbose_name_plural = "Opravila"

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)


class DelovniNalog(TimeStampedModel, StatusModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    opravilo = models.ForeignKey(Opravilo)
    #   Mandatory
    oznaka = models.CharField(max_length=20)
    '''***naziv ni potreben-vsi podatki v opravilu. Preveri druge možnosti***'''
    naziv = models.CharField(max_length=255)
    #   Optional
    nosilec = models.ForeignKey(Oseba, blank=True, null=True)
    datum_plan = models.DateField(blank=True, null=True, verbose_name='V planu za dne')
    datum_start = models.DateField(blank=True, null=True, verbose_name="Začeto dne")
    datum_stop = models.DateField(blank=True, null=True, verbose_name="Končano dne")

    @receiver(post_save, sender=Opravilo)
    def create_delovninalog_za_novo_opravilo(sender, created, instance, **kwargs):

        # nova oznaka
        leto = timezone.now().date().year
        zap_st = DelovniNalog.objects.all().count()
        zap_st = zap_st + 1
        nova_oznaka = "DN-%s-%s" % (leto, zap_st)
        # naziv
        naziv = "Skladno z opravilom."

        if created:
            dn = DelovniNalog(opravilo=instance, oznaka=nova_oznaka, naziv=naziv, status=1)
            dn.save()


    # OBJECT MANAGER
    objects = managers.DelovniNalogManager()

    # CUSTOM PROPERTIES
    def get_absolute_url(self):
        return reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': self.pk})


 

    # @property
    # def delo_vdelu(self):
    #     return self.delo_set.filter(time_stop__isnull=True).order_by("-time_start")

    # @property
    # def delo_koncano(self):
    #     return self.delo_set.filter(time_stop__isnull=False).order_by("-time_stop")

    

    



    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "Delovni Nalog"
        verbose_name_plural = "Delovni Nalogi"

    def __str__(self):
        return "%s | %s (%s)" % (self.oznaka, self.opravilo.naziv, self.opravilo.oznaka,)


# DELO
class Delo(TimeStampedModel, StatusModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    delavec = models.ForeignKey(Oseba)
    delovninalog = models.ForeignKey(DelovniNalog, verbose_name="delovni nalog")
    vrsta_dela = models.ForeignKey('DeloVrsta', blank=True, null=True)
    #   Mandatory
    #   Optional
    datum = models.DateField(blank=True, null=True)
    '''****spremeni v DurationField*****'''
    time_start = models.TimeField(blank=True, null=True, verbose_name="Ura:Začeto")
    time_stop = models.TimeField(blank=True, null=True, verbose_name="Ura:Končano")

    # OBJECT MANAGER
    objects = managers.DeloManager()

    # CUSTOM PROPERTIES
    @property
    def porabljen_cas(self):
        t1 = str(self.time_start)
        t2 = str(self.time_stop)
        # time format
        FMT = '%H:%M:%S'
        # izračun razlike
        tdelta = datetime.strptime(t2, FMT) - datetime.strptime(t1, FMT)
        # output
        return tdelta

    # METHODS
    def get_absolute_url(self):
        return reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': self.delovninalog.pk})

    # META AND STRING
    class Meta:
        verbose_name = "Delo"
        verbose_name_plural = "Dela"

    def __str__(self):
        return "%s | %s %s | %s" % (self.datum, self.delavec.priimek, self.delavec.ime, self.delovninalog.oznaka)


class DeloVrsta(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    sklo = models.ForeignKey('DeloVrstaSklop')
    #   Mandatory
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    zap_st = models.IntegerField(default=99)
    # vrednosti do 99,99 EUR (na dve decimalni mesti natančno)
    cena = models.DecimalField(decimal_places=2, max_digits=4)
    # 0.22(22%) in 0.095(9,5%) | 0.000
    stopnja_ddv = models.DecimalField(decimal_places=3, max_digits=4)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "vrsta dela"
        verbose_name_plural = "vrste del"

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)


class DeloVrstaSklop(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    zap_st = models.IntegerField(default=99)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "sklop vrst del"
        verbose_name_plural = "sklopi vrst del"

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)
