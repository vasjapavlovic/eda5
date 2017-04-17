# Python
# Django
from django.db import models
# Models
# Forms
# Widgets


class PovprasevanjeManager(models.Manager):

    def create_povprasevanje(
        self,
        oznaka=None,
        naziv=None,
        opis=None,
        datum=None,
        zahtevek=None,
    ):

        povprasevanje = self.model(
            oznaka=oznaka,
            naziv=naziv,
            opis=opis,
            datum=datum,
            zahtevek=zahtevek,
        )

        povprasevanje.save(using=self._db)
        return povprasevanje


class PostavkaManager(models.Manager):

    def create_postavka(
        self,
        oznaka=None,
        opis=None,
        priloge=None,
        povprasevanje=None,
    ):

        postavka = self.model(
            oznaka=oznaka,
            opis=opis,
            priloge=priloge,
            povprasevanje=povprasevanje,
        )

        postavka.save(using=self._db)
        return postavka

class PonudbaPoPostavkiManager(models.Manager):
    
    def create_ponudbapopostavki(
        self,
        vrednost_za_izracun=None,
        vrednost_opis=None,
        postavka=None,
        ponudba=None,
    ):

        ponudbapopostavki = self.model(
            vrednost_za_izracun=vrednost_za_izracun,
            vrednost_opis=vrednost_opis,
            postavka=postavka,
            ponudba=ponudba,
        )

        ponudbapopostavki.save(using=self._db)
        return ponudbapopostavki


class PonudbaManager(models.Manager):

    def create_ponudba(
        self,
        oznaka=None,
        ponudnik=None,
        povprasevanje=None,
    ):

        ponudba = self.model(
            oznaka=oznaka,
            ponudnik=ponudnik,
            povprasevanje=povprasevanje,
        )

        ponudba.save(using=self._db)
        return ponudba

