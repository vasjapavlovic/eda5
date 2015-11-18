from django.db import models
from django.core.urlresolvers import reverse

from eda5.core.models import TimeStampedModel, IsLikvidiranModel


class Pomanjkljivost(TimeStampedModel, IsLikvidiranModel):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    oznaka = models.CharField(max_length=20)
    naziv = models.TextField(verbose_name='prijave - sporočilo')
    prijavil = models.CharField(max_length=255)
    datum_ugotovitve = models.DateField()
    element = models.CharField(max_length=255)
    etaza = models.CharField(max_length=50)
    lokacija = models.CharField(max_length=255)
    
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES

    # METHODS
    def get_absolute_url(self):
        return reverse('moduli:pomanjkljivosti:pomanjkljivost_detail', kwargs={"pk": self.pk})

    # META AND STRING
    class Meta:
        verbose_name = "pomanjkljivost"
        verbose_name_plural = "pomanjkljivosti"

    def __str__(self):
        return "%s (%s)" % (self.naziv, self.oznaka)
