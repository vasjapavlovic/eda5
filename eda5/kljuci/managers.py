from django.db import models


class PredajaKljucaManager(models.Manager):

    def create_predaja_kljuca(
        self,
        kljuc=None,
        datum_predaje=None,
        vrsta_predaje=None,
        predaja_lastnine=None,
        ):

        predaja_kljuca = self.model(
            kljuc=kljuc,
            datum_predaje=datum_predaje,
            vrsta_predaje=vrsta_predaje,
            predaja_lastnine=predaja_lastnine,
            )

        predaja_kljuca.save(using=self._db)
        return predaja_kljuca
