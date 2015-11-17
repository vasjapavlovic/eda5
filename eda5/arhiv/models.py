from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

from . import managers

from eda5.core.models import TimeStampedModel
from eda5.deli.models import DelStavbe, Element
from eda5.delovninalogi.models import DelovniNalog
from eda5.katalog.models import ModelArtikla
from eda5.narocila.models import Narocilo
from eda5.partnerji.models import Oseba
from eda5.posta.models import Dokument
from eda5.zahtevki.models import Zahtevek


class Arhiv(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    oznaka = models.CharField(max_length=10, verbose_name='oznaka')
    naziv = models.CharField(max_length=255, verbose_name='naziv')
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "arhiv"
        verbose_name_plural = "arhivi"

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)


class ArhivMesto(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    arhiv = models.ForeignKey(Arhiv)
    #   Mandatory
    oznaka = models.CharField(max_length=10, verbose_name='oznaka')
    naziv = models.CharField(max_length=255, verbose_name='naziv')
    #   Optional
    # OBJECT MANAGER
    objects = managers.ArhivMestoManager()
    # CUSTOM PROPERTIES

    # METHODS
    @receiver(post_save, sender=Zahtevek)
    def create_delovninalog_za_novo_opravilo(sender, created, instance, **kwargs):

        # Arhiv
        '''v končni fazi bo arhiv = objektu '''
        arhiv = Arhiv.objects.get(id=1)

        # izdelava Arhivskega Mesta v bazi
        if created:
            dn = ArhivMesto(oznaka=instance.oznaka, naziv=instance.naziv, arhiv=arhiv, zahtevek=instance)
            dn.save()

    # META AND STRING
    class Meta:
        verbose_name = "arhivsko mesto"
        verbose_name_plural = "arhivska mesta"

    def __str__(self):
        return "%s - %s" % (self.oznaka, self.naziv)


class Arhiviranje(TimeStampedModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    dokument = models.OneToOneField(Dokument, blank=True, null=True)

    zahtevek = models.ForeignKey(Zahtevek, blank=True, null=True)
    delovninalog = models.ForeignKey(DelovniNalog, blank=True, null=True)
    delstavbe = models.ForeignKey(DelStavbe, blank=True, null=True)
    element = models.ForeignKey(Element, blank=True, null=True)
    narocilo = models.ForeignKey(Narocilo, blank=True, null=True)
    artikel = models.ForeignKey(ModelArtikla, blank=True, null=True)

    arhiviral = models.ForeignKey(Oseba)
    lokacija_hrambe = models.ForeignKey(ArhivMesto, blank=True, null=True, verbose_name="lokacija hrambe")
    #   Mandatory
    elektronski = models.BooleanField(default=True, verbose_name="elektronski hramba")
    fizicni = models.BooleanField(default=False, verbose_name="fizični hramba")
    #   Optional

    # OBJECT MANAGER
    objects = managers.ArhiviranjeManager()
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "arhiviranje"
        verbose_name_plural = "arhiviranje"

    def __str__(self):
        return "%s | %s" % (self.dokument, self.lokacija_hrambe)



