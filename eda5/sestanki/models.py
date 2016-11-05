from django.db import models

from eda5.core.models import ZaporednaStevilka
from eda5.zahtevki.models import Zahtevek
from eda5.partnerji.models import SkupinaPartnerjev, Oseba

'''
SESTANEK
Oznaka: ZHT-2016-11
Naziv: Zbor etažnih lastnikov Eda center

Sklicatelj: EDAFM d.o.o.
Udeleženi: Vasja, Tomaž, Kristina, Jože
Namen: Redni zbor etažnih lastnikov leto 2016

Dnevni red:
    -Tema sestanka A:
        -Točka 1 (tema A): Abc
        -Točka 2 (tema A): Def
    -Tema sestanka B:
        - Točka 3 (tema B): Ghj

Obravnava:
- Točka 1:
    - Alineja 1
    - Alineja 2
    - Alineja 3

- Točka 4:
    - Alineja 1
    - Alineja 2
    - Alineja 3
'''


class Sestanek(models.Model):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    zahtevek = models.OneToOneField(Zahtevek)
    sklicatelj = models.ForeignKey(SkupinaPartnerjev, null=True, blank=True)
    udelezenci = models.ManyToManyField(Oseba, blank=True, verbose_name="udeleženci")
    #   Mandatory
    datum = models.DateField(null=True, blank=True, verbose_name="datum sestanka")
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS
    # META AND STRING
    class Meta:
    	verbose_name = "sestanek"
    	verbose_name_plural = "sestanki"

    def __str__(self):
    	return "%s" % (self.zahtevek.oznaka)


class TemaSestankov(ZaporednaStevilka):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    #   Mandatory
    oznaka = models.CharField(max_length=20)
    naziv = models.CharField(max_length=255)
    predlagal = models.CharField(max_length=255)
    #   Optional
    opis = models.TextField(blank=True)
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS
    # META AND STRING
    class Meta:
        verbose_name = "tema sestankovanja"
        verbose_name_plural = "teme sestankovanja"

    def __str__(self):
        return "(%s)%s" % (self.oznaka, self.naziv)


class TockaSestanka(ZaporednaStevilka):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    tema_sestanka = models.ForeignKey(TemaSestankov, verbose_name="tema sestanka")
    #   Mandatory
    naziv_tocke = models.CharField(max_length=255)
    predlagal = models.ForeignKey(Oseba, verbose_name="predlagal")
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS
    # META AND STRING
    class Meta:
        verbose_name = "točka sestanka"
        verbose_name_plural = "točke sestanka"

    def __str__(self):
        return "(%s %s)%s" % (self.predlagal.ime, self.predlagal.priimek, self.naziv_tocke)


class AlinejaSestanka(ZaporednaStevilka):
    # ---------------------------------------------------------------------------------------
    # ATRIBUTES
    #   Relations
    tocka_sestanka = models.ForeignKey(TockaSestanka, verbose_name="točka")
    predlagal = models.ManyToManyField(Oseba, blank=True, related_name="predlagal", verbose_name="predlagal")
    proti_predlogu = models.ManyToManyField(Oseba, blank=True, related_name="proti_predlogu",  verbose_name="proti predlogu")
    #   Mandatory
    vsebina = models.TextField(verbose_name="vsebina alineje")
    #   Optional
    # OBJECT MANAGER
    # CUSTOM PROPERTIES
    # METHODS
    # META AND STRING
    class Meta:
        verbose_name = "alineja sestanka"
        verbose_name_plural = "alineje sestanka"

    def __str__(self):
        return "TE:%s(TČ:%s)AL:%s" % (self.tocka_sestanka.tema_sestanka.oznaka, self.tocka_sestanka.zap_st, self.zap_st)