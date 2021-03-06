import urllib
from django.core.urlresolvers import reverse

from django.db import models
from eda5.core.models import TimeStampedModel, ZaporednaStevilka


class Modul(ZaporednaStevilka):

    oznaka = models.CharField(max_length=10, unique=True)
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    barva = models.CharField(max_length=500)
    url_ref = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'modul'
        verbose_name_plural = "moduli"
        ordering = ['zap_st', 'naziv', ]

    def __str__(self):
        return "(%s) %s" % (self.oznaka, self.naziv)


class Zavihek(ZaporednaStevilka):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    parent = models.ManyToManyField('self', blank=True)
    modul = models.ForeignKey(Modul)
    #   Mandatory
    oznaka = models.CharField(max_length=100, unique=True)
    naziv = models.CharField(max_length=200)
    url_ref = models.CharField(max_length=500, blank=True)
    #   Optional
    # OBJECT MANAGER

    # CUSTOM PROPERTIES
    @property
    def urlreference(self):
        link = self.url_ref
        if link:
            url = reverse('%s' % (link))
            return url
        else:
            return ""
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'zavihek'
        verbose_name_plural = "zavihki"
        ordering = ['zap_st', 'oznaka', ]

    def __str__(self):
        return "(%s) %s" % (self.oznaka, self.naziv)
