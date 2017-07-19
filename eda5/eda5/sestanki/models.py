# Django
from django.db import models
from django.core.urlresolvers import reverse

# Models
from . import managers
from eda5.core.models import ZaporednaStevilka, TimeStampedModel, IsActiveModel, StatusModel, IsLikvidiranModel
from eda5.partnerji.models import Partner, Oseba
from eda5.zahtevki.models import Zahtevek



''' 
V modulu Sestanki se beležijo zbori lastnikov, sestanki s
predstavniki etažnih lastnikov, individualni sestanki.
Na podlagi vnosov se lahko opredelijo tudi naloge, katerim 
se lahko opravlja sledenje

Primer:
SESTANEK
Oznaka: ZHT-2016-11
Naziv: Zbor etažnih lastnikov Eda center

Sklicatelj: EDAFM d.o.o.
Prisotni: Vasja, Tomaž, Kristina, Jože
Namen: Redni zbor etažnih lastnikov leto 2016

Dnevni red:
    -Točka 1: Abc
    -Točka 2: Def
    -Točka 3: razno

Zapisnik:
- Točka 1:
    Zadeva 1 --> Tema y
    - Sklep 1 (zadeva 1)
    - Sklep 2 (zadeva 1)
    - Sklep 3 (zadeva 1)

- Točka 2:
    Zadeva 2 --> Tema y
    - Sklep 1 (zadeva 2)
    - Sklep 2 (zadeva 2)
    - Sklep 3 (zadeva 2)

- Točka 3:
    Zadeva 1 --> Tema y
    - Sklep 1 (tema 1)
    Zadeva 2 --> Tema y
    - Sklep 2 (tema 2)
    - Sklep 3 (tema 2)
'''


class Sestanek(TimeStampedModel, IsActiveModel, IsLikvidiranModel, StatusModel):
    ''' 
    Ko želimo zabeležiti sestanek odpremo nov Zahtevek in
    registriramo sestanek, ki mu dodelimo potrebne podatke
    za pripravo zapisnika
    '''
    #=================================================
    # ATRIBTUI
    #-------------------------------------------------

    #=================================================
    # osnovni podatki
    #-------------------------------------------------
    # oznaka, oznaka reklamacije. Oblika Leto+zap.št.
    # naziv, kratko ime (naziv sestanka)
    # opis, namen sestanka
    # datum, datum sestanka
    # sklicatelj, Relacija na Osebo iz Partnerji
    # prisotni, relacija na osebe iz partnerji (many to many)
    # status (v reševanju, zaključeno ...)

    #=================================================
    # relacije z zahtevki, delovni nalogi,
    #-------------------------------------------------
    # zahtevek, sestanek je del zahtevka


    oznaka = models.CharField(
        max_length=255,
        verbose_name="oznaka",)
 
    naziv = models.CharField(
        max_length=255,
        verbose_name="naziv",)

    opis = models.TextField(
        verbose_name="namen",)

    datum = models.DateField(
        verbose_name="datum sestanka",)

    sklicatelj = models.ForeignKey(
        Partner,
        verbose_name="sklical",)
 
    prisotni = models.ManyToManyField(
        Oseba,
        blank=True, # blank in null ker se prisotni dodajo kasneje v .views
        verbose_name="prisotni",)

    zahtevek = models.ForeignKey( 
        Zahtevek,
        blank=True, null=True,
        verbose_name="zahtevek")
    
    #---------------------------------------------------------
    # OBJECT MANAGER
    # ========================================================
    objects = managers.SestanekManager()

    def get_absolute_url(self):
        return reverse('moduli:sestanki:sestanek_detail', kwargs={'pk': self.pk})

    #---------------------------------------------------------
    # META and STR
    # ========================================================
    class Meta:
        verbose_name = "sestanek"
        verbose_name_plural = "sestanki"
        ordering = ['-datum']

    def __str__(self):
        return "%s | %s | %s" % (self.oznaka, self.datum, self.zahtevek.oznaka)


class Tema(TimeStampedModel, IsActiveModel, IsLikvidiranModel, StatusModel, ZaporednaStevilka):
    ''' 
    Tema združuje Zadeve v skupine (širše gledano) - npr. tema odprava pomanjkljivosti, pogodba o upravljanju
    '''
    #=================================================
    # ATRIBTUI
    #=================================================
    # osnovni podatki
    #-------------------------------------------------
    # oznaka, oznaka teme. zap.št.
    # naziv, naziv teme
    # opis, opis teme
    # status (če je izbrisana je ne prikaži ...)
    #=================================================
    # Relacije
    #-------------------------------------------------
    # tema sestanka

    oznaka = models.CharField(
        max_length=255,
        verbose_name="oznaka",)
 
    naziv = models.CharField(
        max_length=255,
        verbose_name="naziv",)

    opis = models.TextField(
        verbose_name="opis",)

    #---------------------------------------------------------
    # OBJECT MANAGER
    # ========================================================
    objects = managers.TemaManager()


    #---------------------------------------------------------
    # META and STR
    # ========================================================
    class Meta:
        verbose_name = "tema"
        verbose_name_plural = "teme"

    def __str__(self):
        return "(%s)%s" % (self.oznaka, self.naziv)




class Zadeva(TimeStampedModel, IsActiveModel, IsLikvidiranModel, StatusModel, ZaporednaStevilka):
    ''' 
    Zadeva združuje sklepe sestanka s skupnim problemom oziroma
    namenom.
    '''
    #=================================================
    # ATRIBTUI
    #=================================================
    # osnovni podatki
    #-------------------------------------------------
    # oznaka, oznaka teme. zap.št.
    # naziv, naziv teme
    # opis, opis teme
    # status (če je izbrisana je ne prikaži ...)


    oznaka = models.CharField(
        max_length=255,
        verbose_name="oznaka",)
 
    naziv = models.CharField(
        max_length=255,
        verbose_name="naziv",)

    opis = models.TextField(
        verbose_name="opis",)

    tema = models.ForeignKey(
        Tema,
        blank=True, null=True,
        verbose_name="tema",)

    #---------------------------------------------------------
    # OBJECT MANAGER
    # ========================================================
    objects = managers.ZadevaManager()


    #---------------------------------------------------------
    # META and STR
    # ========================================================
    class Meta:
        verbose_name = "zadeva"
        verbose_name_plural = "zadeve"

    def __str__(self):
        return "(%s)%s" % (self.oznaka, self.naziv)


class Tocka(TimeStampedModel, IsActiveModel, IsLikvidiranModel, StatusModel, ZaporednaStevilka):
    ''' 
    Točka dnevnega reda je namenjena samo objavi dnevnega reda in
    združevanju sklepov pri izpisu zapisnika sestanka
    '''
    #=================================================
    # ATRIBTUI
    #-------------------------------------------------

    #=================================================
    # osnovni podatki
    #-------------------------------------------------
    # oznaka
    # naziv

    #=================================================
    # relacije
    #-------------------------------------------------
    # sestanek

    oznaka = models.CharField(
        max_length=255,
        verbose_name="oznaka",)
 
    naziv = models.CharField(
        max_length=255,
        verbose_name="naziv",)

    sestanek = models.ForeignKey(
        Sestanek,
        verbose_name="sestanek",)

    #---------------------------------------------------------
    # OBJECT MANAGER
    # ========================================================
    objects = managers.TockaManager()


    #---------------------------------------------------------
    # META and STR
    # ========================================================
    class Meta:
        verbose_name = "tocka dnevnega reda"
        verbose_name_plural = "dnevni red"

    def __str__(self):
        return "(%s) %s" % (self.oznaka, self.naziv)


class Vnos(TimeStampedModel, IsActiveModel, IsLikvidiranModel, StatusModel, ZaporednaStevilka):
    ''' 
    Vnos predstavlja dogovor na sestanku, ki se zapiše
    in realizira. K sklepu se zapiše tudi kdo ga realizira/reši
    '''
    #=================================================
    # ATRIBTUI
    #-------------------------------------------------

    #=================================================
    # osnovni podatki
    #-------------------------------------------------
    # oznaka
    # vsebina
    # 

    #=================================================
    # relacije
    #-------------------------------------------------
    # tocka : relacija na točko dnenega reda sestanka
    # dopolnitev_sklepov : relacija na druge sklepe, ki jih ta dopolnjuje
    # zadeva : relacija na Zadevo o kateri se razpravlja
    # izvede : kdo bo sklep realiziral. Če sklep ni
    #          narave, da je potrebno kaj narediti se pusti mesto prazno
    # rok: do kdaj mora biti sklep realiziran
    # rok_opis: če se še opisno zapiše

    oznaka = models.CharField(
        max_length=255,
        verbose_name="oznaka",)
 
    opis = models.TextField(
        verbose_name="vsebina",)

    izvede = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name="izvede/realizira",)

    rok_izvedbe = models.DateField(
        blank=True, null=True,
        verbose_name="rok izvedbe")

    rok_izvedbe_opis = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name="rok izvedbe opisno",)

    tocka = models.ForeignKey(
        Tocka,
        verbose_name="točka sestanka",)

    dopolnitev_vnosov = models.ManyToManyField(
        "self",
        blank=True,
        verbose_name="dopolnitev vnosov",)

    zadeva = models.ForeignKey(
        Zadeva,
        blank=True, null=True,
        verbose_name="zadeva",)

    #---------------------------------------------------------
    # OBJECT MANAGER
    # ========================================================
    objects = managers.VnosManager()


    #---------------------------------------------------------
    # META and STR
    # ========================================================
    class Meta:
        verbose_name = "vnos sestanka"
        verbose_name_plural = "vnosi sestankov"

    def __str__(self):
        # sestanek-tocka-sklep = (ZHT-2017-1)1-1-1, (ZHT-2017-1)1-2-1, ...
        return "(%s)%s-%s-%s" % (self.tocka.sestanek.zahtevek.oznaka, self.tocka.sestanek.oznaka, self.tocka.oznaka, self.oznaka)

# UREDI ŠE GLASOVANJE ZA SKLEPE


class OpombaVnosa(TimeStampedModel, StatusModel):
    ''' 
    Sklep predstavlja dogovor na sestanku, ki se zapiše
    in realizira. K sklepu se zapiše tudi kdo ga realizira/reši
    '''
    #=================================================
    # ATRIBTUI
    #-------------------------------------------------

    #=================================================
    # osnovni podatki
    #-------------------------------------------------
    # oznaka
    # vsebina
    # 

    #=================================================
    # relacije
    #-------------------------------------------------
    # tocka : relacija na točko dnenega reda sestanka
    # dopolnitev_sklepov : relacija na druge sklepe, ki jih ta dopolnjuje
    # izvede : kdo bo sklep realiziral. Če sklep ni
    #          narave, da je potrebno kaj narediti se pusti mesto prazno
    # rok: do kdaj mora biti sklep realiziran
    # rok_opis: če se še opisno zapiše

    oznaka = models.CharField(
        max_length=255,
        verbose_name="oznaka",)
 
    opis = models.TextField(
        verbose_name="vsebina",)

    opomnil = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name="opomnil",)

    vnos = models.ForeignKey(
        Vnos,
        verbose_name="vnos sestanka",)

    #---------------------------------------------------------
    # OBJECT MANAGER
    # ========================================================
    objects = managers.OpombaVnosaManager()


    #---------------------------------------------------------
    # META and STR
    # ========================================================
    class Meta:
        verbose_name = "opomba vnosa"
        verbose_name_plural = "opombe vnosov"

    def __str__(self):
        # sestanek-tocka-vnos = (ZHT-2017-1)1-1-1, (ZHT-2017-1)1-2-1, ...
        return "(%s)%s-%s-%s" % (self.vnos.tocka.sestanek.zahtevek.oznaka, self.vnos.tocka.sestanek.oznaka, self.vnos.tocka.oznaka, self.oznaka)

# UREDI ŠE GLASOVANJE ZA SKLEPE