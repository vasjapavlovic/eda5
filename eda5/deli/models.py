# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

from . import managers

from eda5.katalog.models import ModelArtikla
from eda5.etaznalastnina.models import LastniskaSkupina
from eda5.posta.models import Dokument


class Skupina(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    # ***Optional***

    # OBJECT MANAGER
    objects = managers.SkupinaDelovManagers()

    # CUSTOM PROPERTIES
    @property
    def sorted_podskupinadelov_set(self):
        return self.podskupina_set.order_by('oznaka')
    # METHODS

    # META AND STRING
    class Meta:
        ordering = ['oznaka']
        verbose_name = 'skupina delov'
        verbose_name_plural = 'skupine delov'

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class Podskupina(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    # ***Relations***
    skupina = models.ForeignKey(Skupina)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    # ***Optional***

    # OBJECT MANAGER
    objects = managers.PodskupinaDelovManagers()

    # CUSTOM PROPERTIES
    @property
    def sorted_delstavbe_set(self):
        return self.delstavbe_set.order_by('oznaka')

    # METHODS

    # META AND STRING
    class Meta:
        ordering = ['oznaka']
        verbose_name = 'podskupina delov'
        verbose_name_plural = 'podskupine delov'

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class DelStavbe(models.Model):
    # ---------------------------------------------------------------------------------------

    def shema_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/deli/<del_oznaka>/<new_filename>
        new_filename_raw = filename.split(".")
        ext = '.' + new_filename_raw[1]

        parametri_imena = (instance.oznaka, "shema")
        new_filename = "_".join(parametri_imena)

        return 'deli/{0}/{1}'.format(instance.oznaka, new_filename + ext)

    # ATRIBUTES
    # ***Relations***
    podskupina = models.ForeignKey(Podskupina)
    lastniska_skupina = models.ForeignKey(LastniskaSkupina, blank=True, null=True, verbose_name="lastniška skupina",)
    prejeta_dokumentacija = models.ManyToManyField(Dokument, blank=True)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    # ***Optional***
    shema = models.FileField(upload_to=shema_directory_path, blank=True, verbose_name="shema sistema")

    # OBJECT MANAGER
    objects = managers.DelManagers()

    # CUSTOM PROPERTIES
    @property
    def elementi_vsi(self):
        return self.element_set.order_by('oznaka')

    # METHODS
    def get_absolute_url(self):
        return reverse('moduli:deli:del_detail', kwargs={'pk': self.pk})

    # META AND STRING
    class Meta:
        ordering = ['oznaka']
        verbose_name = 'del stavbe'
        verbose_name_plural = 'deli stavbe'

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)


class Element(models.Model):
    # ---------------------------------------------------------------------------------------

    def dokumentacija_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/deli/<del_oznaka>/<new_filename>
        new_filename_raw = filename.split(".")
        ext = '.' + new_filename_raw[1]
        new_filename = new_filename_raw[0]
        return 'deli/{0}/{1}/{2}'.format(instance.del_stavbe.oznaka, instance.oznaka, new_filename + ext)

    # ATRIBUTES
    # ***Relations***
    del_stavbe = models.ForeignKey(DelStavbe)
    model_artikla = models.ForeignKey(ModelArtikla, default=1, verbose_name='Model',)
    prejeta_dokumentacija = models.ManyToManyField(Dokument, blank=True)
    # ***Mandatory***
    oznaka = models.CharField(max_length=20, verbose_name='Oznaka',)
    naziv = models.CharField(max_length=255, verbose_name='Naziv',)
    # ***Optional***
    serijska_st = models.CharField(max_length=100, verbose_name='Serijska Številka', blank=True,)
    tovarniska_st = models.CharField(max_length=100, verbose_name='Tovarniška Številka', blank=True,)
    datum_prevzema_v_upravljanje = models.DateField(verbose_name='datum prevzema v upravljanje', blank=True,)
    dokumentacija = models.FileField(upload_to=dokumentacija_directory_path, blank=True, verbose_name="dokumentacija")

    # OBJECT MANAGER
    objects = managers.ElementManagers()

    # CUSTOM PROPERTIES

    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'element'
        verbose_name_plural = 'elementi'

    def __str__(self):
        return "%s | %s" % (self.oznaka, self.naziv)
