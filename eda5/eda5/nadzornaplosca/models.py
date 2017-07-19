from django.db import models


class NadzorniSistem(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    oznaka = models.CharField(max_length=50)
    naziv = models.CharField(max_length=255)
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "nadzorni sistem"
        verbose_name_plural = "nadzorni sistemi"

    def __str__(self):
        return "(%s) %s" % (self.oznaka, self.naziv)


class NadzornaEnota(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    nadzorni_sistem = models.ForeignKey(NadzorniSistem)
    #   Mandatory
    oznaka = models.CharField(max_length=50)
    naziv = models.CharField(max_length=255)
    ip_naslov = models.CharField(max_length=255)
    #   Optional
    opis = models.TextField()
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = "nadzorna enota"
        verbose_name_plural = "nadzorne enote"
        ordering = ['oznaka',]

    def __str__(self):
        return "(%s) %s" % (self.oznaka, self.naziv)
