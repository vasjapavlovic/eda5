from django.db import models


class Sestanek(models.Model):
	pass
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    zahtevek = models.OneToOneField()
    #   Mandatory
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS
    # META AND STRING
    class Meta:
    	verbose_name = ""
    	verbose_name_plural = ""

    def __str__(self):
    	return "%s" % (self.zahtevek.oznaka)
