# Python
from datetime import datetime

# Django
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Models
from . import managers
from eda5.core.models import IsActiveModel, StatusModel, TimeStampedModel
from eda5.deli.models import ProjektnoMesto
from eda5.naloge.models import Naloga
from eda5.narocila.models import Narocilo
from eda5.partnerji.models import Oseba
from eda5.planiranje.models import PlaniranoOpravilo
from eda5.pomanjkljivosti.models import Pomanjkljivost
from eda5.zahtevki.models import Zahtevek





class Opravilo(TimeStampedModel, IsActiveModel, StatusModel):
    # ---------------------------------------------------------------------------------------
    #   RELATIONS

    zahtevek = models.ForeignKey(Zahtevek)
    narocilo = models.ForeignKey(Narocilo, verbose_name='naročilo')
    nosilec = models.ForeignKey(Oseba)
    planirano_opravilo = models.ForeignKey(PlaniranoOpravilo, blank=True, null=True)


    # Stroškovno mesto. Vsako opravilo se vmesti v posamezno stroškovno mesto.
    # Namen je finančno poročilo po posameznih stroškovnih mestih

    # vrsta_stroska = models.ForeignKey("racunovodstvo.VrstaStroska", blank=True, null=True, verbose_name="vrsta stroška")


    ''' Navezava na pomanjkljivosti, ki se v opravilu odpravljajo.
    V opravilu se lahko odpravlja več pomanjkljivosti. 
    Pomanjkljivost se lahko odpravlja v več opravilih za katerega
    je potrebno svoje naročilo. '''

    pomanjkljivost = models.ManyToManyField(Pomanjkljivost, blank=True)

    ''' Navezava na naloge, ki se v opravilu urejajo.
    V opravilu se lahko odpravlja več nalog. 
    Naloga se lahko odpravlja v več opravilih za katerega
    je potrebno svoje naročilo. '''

    naloga = models.ManyToManyField(Naloga, blank=True)

    '''Opravilo se izvaja na posameznih elementih stavbe, 
    ki se jih definira tukaj'''

    element = models.ManyToManyField(ProjektnoMesto, blank=True)


    #   MANDATORY
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    rok_izvedbe = models.DateField()
    is_potrjen = models.BooleanField(default=False, verbose_name="Potrjeno iz strani nadzornika")
    #   Optional

    ''' parameter za zaokroževanje porabljenega časa za dela,
    ki se opravljajo pod to opravilo'''

    # zaokrožitev minimalno minut
    zmin = models.IntegerField(
        default=15, 
        verbose_name='zaokrožitev [min]')


    # OBJECT MANAGER
    objects = managers.OpraviloManager()

    # CUSTOM PROPERTIES

    @property
    def delovninalog_koncan_sorted_by_date(self):
        return self.delovninalog_set.exclude(datum_stop__isnull=True).order_by("datum_start")

    @property
    def delovninalog_vdelu_sorted_by_date(self):
        return self.delovninalog_set.exclude(datum_stop__isnull=False).order_by("datum_start")

    @property
    def st_elementov(self):
        st_elementov = self.element.count()
        return st_elementov

    # METHODS
    def get_absolute_url(self):
        return reverse("moduli:delovninalogi:opravilo_detail", kwargs={'pk': self.pk})

    # META AND STRING
    class Meta:
        verbose_name = "Opravilo"
        verbose_name_plural = "Opravila"

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)


class VzorecOpravila(TimeStampedModel, IsActiveModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    narocilo = models.ForeignKey(Narocilo, verbose_name='naročilo')
    nosilec = models.ForeignKey(Oseba)
    planirano_opravilo = models.ForeignKey(PlaniranoOpravilo, blank=True, null=True)
    element = models.ManyToManyField(ProjektnoMesto)
    #   Mandatory
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    rok_izvedbe = models.DateField(blank=True, null=True)
    is_potrjen = models.BooleanField(default=False, verbose_name="Potrjeno iz strani nadzornika")
    #   Optional

    # OBJECT MANAGER
    objects = managers.VzorecOpravilaManager()

    # CUSTOM PROPERTIES

    # METHODS
    # def get_absolute_url(self):
    #    return reverse("moduli:delovninalogi:vzorec_opravila_detail", kwargs={'pk': self.pk})

    # META AND STRING
    class Meta:
        verbose_name = "vzorec opravila"
        verbose_name_plural = "vzorci opravil"

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)


class DelovniNalog(TimeStampedModel, StatusModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    opravilo = models.ForeignKey(
        Opravilo)
    #   Mandatory
    oznaka = models.CharField(
        max_length=20)
    '''***naziv ni potreben-vsi podatki v opravilu. Preveri druge možnosti***'''
    naziv = models.CharField(
        max_length=255)
    #   Optional
    nosilec = models.ForeignKey(
        Oseba, blank=True, null=True, 
        verbose_name="Izvajalec (kdo bo delo izvedel)")

    datum_plan = models.DateField(
        blank=True, null=True, 
        verbose_name='V planu za dne')

    datum_start = models.DateField(
        blank=True, null=True,
        verbose_name="Začeto dne")

    datum_stop = models.DateField(
        blank=True, null=True, 
        verbose_name="Končano dne")

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
    @property
    def racun_dokument(self):
        return self.strosek.racun.arhiviranje.dokument

    

    



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
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    #   Optional
    datum = models.DateField(blank=True, null=True)
    '''****spremeni v DurationField*****'''
    time_start = models.DurationField(blank=True, null=True, verbose_name="Ura:Začeto")
    time_stop = models.DurationField(blank=True, null=True, verbose_name="Ura:Končano")

    delo_cas_rac = models.DecimalField(
        decimal_places=2, max_digits=5,
        blank=True, null=True, 
        verbose_name="Porabljen čas [UR]"
    )

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
    skupina = models.ForeignKey('DeloVrstaSklop')
    #   Mandatory
    oznaka = models.CharField(max_length=20, unique=True)
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
    oznaka = models.CharField(max_length=20, unique=True)
    naziv = models.CharField(max_length=255)
    #   Optional
    zap_st = models.IntegerField(default=99)
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "sklop vrst del"
        verbose_name_plural = "sklopi vrst del"

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)



