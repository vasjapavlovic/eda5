from django.db import models
from django.core.urlresolvers import reverse

from eda5.core.models import TimeStampedModel
from eda5.partnerji.models import Partner


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


class Dokument(TimeStampedModel):

    # upload_to settings
    def dokument_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/prejeta_posta/<vrsta_dokumenta>/<new_filename>
        new_filename_raw = filename.split(".")
        ext = '.' + new_filename_raw[1]

        parametri_imena = (str(instance.datum_prejema), instance.oznaka, instance.posiljatelj.davcna_st)
        new_filename = "_".join(parametri_imena)

        return 'prejeta_posta/{0}/{1}'.format(instance.vrsta_dokumenta.oznaka, new_filename + ext)

    vrsta_dokumenta = models.ForeignKey(VrstaDokumenta, verbose_name="vrsta dokumenta")
    posiljatelj = models.ForeignKey(Partner, verbose_name="avtor dokumenta")
    datum_prejema = models.DateField(verbose_name="datum prejema")
    oznaka = models.CharField(max_length=20, verbose_name='številka dokumenta')
    opis = models.CharField(max_length=255, verbose_name="opis")
    priponka = models.FileField(upload_to=dokument_directory_path)
    likvidiran = models.BooleanField(default=False)
    # definiraj upload_to="" za točno lokacijo
    # dokumenta, ki je morebiti vezana na vrsto dokumenta

    class Meta:
        verbose_name = "Dokument"
        verbose_name_plural = "Dokumenti"

    def get_absolute_url(self):
        return reverse("moduli:posta:list_likvidacija")

    def __str__(self):
        return "%s - %s" % (self.datum_prejema, self.opis)
