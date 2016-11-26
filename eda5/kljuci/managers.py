from django.db import models


class PredajaKljucaManager(models.Manager):

    def create_predaja_kljuca(
        self,
        kljuc=None,
        datum_predaje=None,
        vrsta_predaje=None,
        zahtevek=None,
        ):

        predaja_kljuca = self.model(
            kljuc=kljuc,
            datum_predaje=datum_predaje,
            vrsta_predaje=vrsta_predaje,
            zahtevek=zahtevek,
            )

        predaja_kljuca.save(using=self._db)
        return predaja_kljuca
