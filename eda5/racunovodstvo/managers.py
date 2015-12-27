from django.db import models


class RacunManager(models.Manager):
    def create_racun(
        self,
        davcna_klasifikacija=None,
        datum_storitve_od=None,
        datum_storitve_do=None,
        obdobje_obracuna_leto=None,
        obdobje_obracuna_mesec=None,
        narocilo=None,
        osnova_0=None,
        osnova_1=None,
        osnova_2=None,
        ):

        racun = self.model(
            davcna_klasifikacija=davcna_klasifikacija,
            datum_storitve_od=datum_storitve_od,
            datum_storitve_do=datum_storitve_do,
            obdobje_obracuna_leto=obdobje_obracuna_leto,
            obdobje_obracuna_mesec=obdobje_obracuna_mesec,
            narocilo=narocilo,
            osnova_0=osnova_0,
            osnova_1=osnova_1,
            osnova_2=osnova_2,
        )

        racun.save(using=self._db)
        return racun
