from django.db import models

from eda5.partnerji.models import Partner


class NastavitevPartnerja(models.Model):
    partner = models.OneToOneField(Partner)

    class Meta:
        verbose_name = 'nastavitev'
        verbose_name_plural = "nastavitve"

    def __str__(self):
        return "(%s) %s" % (self.partner.davcna_st, self.partner.kratko_ime)
