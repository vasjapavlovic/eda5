from django.db import models
from django.core.urlresolvers import reverse

from eda5.core.models import TimeStampedModel, IsLikvidiranModel
from eda5.partnerji.models import SkupinaPartnerjev, Oseba


class PostnaStoritev(TimeStampedModel):

    AKTIVNOSTI = (
        (1, "prejeta posta"),
        (2, "izdana pošta"),
        )

    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    dokument = models.OneToOneField('Dokument')
    izvajalec = models.ForeignKey(Oseba, verbose_name="izvajalec poštne storitve")
    #   Mandatory
    aktivnost = models.IntegerField(choices=AKTIVNOSTI)
    datum = models.DateField()
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "poštna storitev"
        verbose_name_plural = "poštne storitve"

    def __str__(self):
        return "%s - %s | %s" % (self.datum, self.aktivnost, self.izvajalec)


class Dokument(TimeStampedModel, IsLikvidiranModel):
    # ---------------------------------------------------------------------------------------

    def dokument_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/prejeta_posta/<vrsta_dokumenta>/<new_filename>
        new_filename_raw = filename.split(".")
        ext = '.' + new_filename_raw[1]

        parametri_imena = (str(instance.datum), instance.oznaka, instance.posiljatelj.davcna_st)
        new_filename = "_".join(parametri_imena)

        return 'prejeta_posta/{0}/{1}'.format(instance.vrsta_dokumenta.oznaka, new_filename + ext)
    # ATRIBUTES
    #   Relations
    vrsta_dokumenta = models.ForeignKey('VrstaDokumenta', verbose_name="vrsta dokumenta")
    posiljatelj = models.ForeignKey(SkupinaPartnerjev, related_name="posiljatelj", verbose_name="pošiljatelj")
    naslovnik = models.ForeignKey(SkupinaPartnerjev, related_name="naslovnik", verbose_name="naslovnik")
    #   Mandatory
    oznaka = models.CharField(max_length=20, verbose_name='številka dokumenta')
    datum = models.DateField()
    opis = models.CharField(max_length=255, verbose_name="opis")
    priponka = models.FileField(upload_to=dokument_directory_path)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "dokument"
        verbose_name_plural = "dokumenti"

    def get_absolute_url(self):
        return reverse("moduli:posta:list_likvidacija")

    def __str__(self):
        return "%s - %s | %s" % (self.datum, self.oznaka, self.opis)

class SkupinaDokumenta(TimeStampedModel):
    oznaka = models.CharField(max_length=3, verbose_name='oznaka')
    naziv = models.CharField(max_length=255, verbose_name='naziv')

    class Meta:
        verbose_name = "Skupina Dokumentov"
        verbose_name_plural = "Skupine Dokumentov"

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)


class VrstaDokumenta(TimeStampedModel):
    skupina = models.ForeignKey(SkupinaDokumenta, verbose_name='Skupina Dokumentov')
    oznaka = models.CharField(max_length=3, verbose_name='oznaka')
    naziv = models.CharField(max_length=255, verbose_name='naziv')
    zap_st = models.IntegerField(verbose_name="zaporedna številka")

    class Meta:
        verbose_name = "Vrsta Dokumenta"
        verbose_name_plural = "Vrste Dokumentov"

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)
