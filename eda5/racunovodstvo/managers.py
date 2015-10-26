from django.db import models


class RacunManager(models.Manager):
    def create_racun(self, dokument=None, davcna_klasifikacija=None, datum_storitve_od=None, datum_storitve_do=None, obdobje_obracuna_leto=None, obdobje_obracuna_mesec=None):
        if not dokument:
            raise ValueError("Izbrati dokument iz pošte")

        racun = self.model(
            dokument=dokument,
            davcna_klasifikacija=davcna_klasifikacija,
            datum_storitve_od=datum_storitve_od,
            datum_storitve_do=datum_storitve_do,
            obdobje_obracuna_leto=obdobje_obracuna_leto,
            obdobje_obracuna_mesec=obdobje_obracuna_mesec,
            )

        racun.save(using=self._db)
        return racun
