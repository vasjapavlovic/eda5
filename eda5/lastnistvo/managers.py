from django.db import models


class PredajaLastnineManager(models.Manager):

    def create_predaja_lastnine(
        self,
        oznaka=None,
        prodajalec=None,
        kupec=None,
        zahtevek=None
        ):

        predaja_lastnine = self.model(
            oznaka=oznaka,
            prodajalec=prodajalec,
            kupec=kupec,
            zahtevek=zahtevek,
            )

        predaja_lastnine.save(using=self._db)
        return predaja_lastnine


class ProdajaLastnineManager(models.Manager):

    def create_prodaja_lastnine(
        self,
        lastniska_enota=None,
        placnik=None,
        datum_predaje=None,
        predaja_lastnine=None,
        ):

        prodaja_lastnine = self.model(
            lastniska_enota=lastniska_enota,
            placnik=placnik,
            datum_predaje=datum_predaje,
            predaja_lastnine=predaja_lastnine,
            )

        prodaja_lastnine.save(using=self._db)
        return prodaja_lastnine


class NajemLastnineManager(models.Manager):

    def create_najem_lastnine(
        self,
        lastniska_enota=None,
        placnik=None,
        datum_predaje=None,
        datum_veljavnosti=None,
        predaja_lastnine=None,
        ):

        najem_lastnine = self.model(
            lastniska_enota=lastniska_enota,
            placnik=placnik,
            datum_predaje=datum_predaje,
            datum_veljavnosti=datum_veljavnosti,
            predaja_lastnine=predaja_lastnine,
            )

        najem_lastnine.save(using=self._db)
        return najem_lastnine
