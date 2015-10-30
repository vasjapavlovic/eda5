from django.db import models

from eda5.racunovodstvo.models import Strosek
from eda5.etaznalastnina.models import LastniskaEnotaInterna


class StrosekLE(models.Model):
    # ATRIBUTES
    # ***Relations***
    strosek = models.ForeignKey(Strosek)
    lastniska_enota = models.ForeignKey(LastniskaEnotaInterna)

    # ***Mandatory***
    # lastniški-delež: 0.0000 ,  površina: 0000.00 , enota: 0, oseba: 0, | 0000.0000
    delilnik_vrednost = models.DecimalField(decimal_places=4, max_digits=8)
    # ***Optional***
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS

    # META AND STRING
    class Meta:
        verbose_name = 'strošek na LE'
        verbose_name_plural = 'stroški na LE'

    def __str__(self):
        return "%s - %s" % (self.strosek.oznaka, self.lastniska_enota.oznaka)
