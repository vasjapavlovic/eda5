from django.db import models
from django.core.urlresolvers import reverse

from eda5.core.models import TimeStampedModel, ZaporednaStevilka, OsnovniPodatki
from eda5.partnerji.models import Oseba, Partner

from . import managers


class Aktivnost(TimeStampedModel):



    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    izvajalec = models.ForeignKey(Oseba, related_name="izvajalec", verbose_name="izvajalec poštne storitve")
    #   Mandatory

    datum_aktivnosti = models.DateField()
    #   Optional

    # OBJECT MANAGER
    objects = managers.AktivnostManager()
    # CUSTOM PROPERTIES
    @property
    def date_created(self):
        aktivnost_date_created = self.created.date()
        return aktivnost_date_created

    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "aktivnost"
        verbose_name_plural = "aktivnosti"

    def __str__(self):
        return "%s" % (self.datum_aktivnosti)


class Dokument(TimeStampedModel):
    # ---------------------------------------------------------------------------------------

    def dokument_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/prejeta_posta/<vrsta_dokumenta>/<new_filename>
        old_filename_raw = filename.split(".")
        ext = '.' + old_filename_raw[-1]
        filename_parameters = ('media', str(instance.oznaka_baza))
        new_filename = '/'.join(filename_parameters)
        return '{0}'.format(new_filename + ext)  # output=  media/5.pdf

    # ATRIBUTES
    #   Relations
    aktivnost = models.OneToOneField(Aktivnost)
    vrsta_dokumenta = models.ForeignKey('VrstaDokumenta', verbose_name="vrsta dokumenta")
    avtor = models.ForeignKey(Partner, related_name="avtor")
    naslovnik = models.ForeignKey(Partner, related_name="naslovnik")
    #   Mandatory
    oznaka_baza = models.IntegerField(blank=True, null=True)
    oznaka = models.CharField(max_length=50, verbose_name='številka dokumenta')
    naziv = models.CharField(max_length=255, verbose_name="naziv")
    datum_dokumenta = models.DateField()
    kraj_izdaje = models.CharField(max_length=100, blank=True)
    priponka = models.FileField(upload_to=dokument_directory_path)
    #   Optional

    # OBJECT MANAGER
    objects = managers.DokumentManager()
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "dokument"
        verbose_name_plural = "dokumenti"
        unique_together = (('oznaka', 'avtor', 'vrsta_dokumenta', 'datum_dokumenta',),)

    def get_year_date(self):
        return self.datum_dokumenta.year

    def get_month_date(self):
        return self.datum_dokumenta.month

    def get_day_date(self):
        return self.datum_dokumenta.day

    def get_absolute_url(self):
        return reverse("moduli:posta:list_likvidacija")

    def __str__(self):
        return "(%s) %s | %s" % (self.oznaka, self.naziv, self.datum_dokumenta, )


class SkupinaDokumenta(ZaporednaStevilka):
    oznaka = models.CharField(max_length=3, unique=True, verbose_name='oznaka')
    naziv = models.CharField(max_length=255, verbose_name='naziv')

    class Meta:
        verbose_name = "Skupina Dokumentov"
        verbose_name_plural = "Skupine Dokumentov"
        ordering = ('zap_st', )

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)


class VrstaDokumenta(ZaporednaStevilka):
    skupina = models.ForeignKey(SkupinaDokumenta, verbose_name='Skupina Dokumentov')
    oznaka = models.CharField(max_length=3, unique=True, verbose_name='oznaka')
    naziv = models.CharField(max_length=255, verbose_name='naziv')

    class Meta:
        verbose_name = "Vrsta Dokumenta"
        verbose_name_plural = "Vrste Dokumentov"
        ordering = ('oznaka', )

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)


class KlasifikacijaDokumenta(OsnovniPodatki, ZaporednaStevilka, TimeStampedModel):
    vrsta_dokumenta = models.ForeignKey(VrstaDokumenta, verbose_name='Vrsta dokumenta')

    proces_oznaka = models.CharField(max_length=10, unique=True, verbose_name='Oznaka procesa')
    proces_naziv = models.CharField(max_length=255, verbose_name='Naziv procesa')

    postopek_oznaka = models.CharField(max_length=10, unique=True, verbose_name='Oznaka postopka')
    postopek_naziv = models.CharField(max_length=255, verbose_name='Naziv postopka')

    class Meta:
        verbose_name = "Klasifikacija dokumenta"
        verbose_name_plural = "Klasifikacija dokumentov"
        ordering = ('oznaka', )

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)
