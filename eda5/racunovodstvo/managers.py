from django.db import models

class RacunManager(models.Manager):
    def create_racun(
        self,
        racunovodsko_leto=None,
        oznaka=None,
        davcna_klasifikacija=None,
        datum_storitve_od=None,
        datum_storitve_do=None,
        valuta=None,
        povracilo_stroskov_zaposlenemu=None,
        je_reprezentanca=None,
        reprezentanca_opis=None,
        zavrnjen=None,
        zavrnjen_datum=None,
        zavrnjen_obrazlozitev_text=None,
        ):

        racun = self.model(
            racunovodsko_leto=racunovodsko_leto,
            oznaka=oznaka,
            davcna_klasifikacija=davcna_klasifikacija,
            datum_storitve_od=datum_storitve_od,
            datum_storitve_do=datum_storitve_do,
            valuta=valuta,
            povracilo_stroskov_zaposlenemu=povracilo_stroskov_zaposlenemu,
            je_reprezentanca=je_reprezentanca,
            reprezentanca_opis=reprezentanca_opis,
            zavrnjen=zavrnjen,
            zavrnjen_datum=zavrnjen_datum,
            zavrnjen_obrazlozitev_text=zavrnjen_obrazlozitev_text,
        )

        racun.save(using=self._db)
        return racun


class StrosekManager(models.Manager):

    def create_strosek(
        self,
        oznaka=None,
        naziv=None,
        datum_storitve_od=None,
        datum_storitve_do=None,
        obdobje_obracuna_leto=None,
        obdobje_obracuna_mesec=None,
        delovni_nalog=None,
        osnova=None,
        stopnja_ddv=None,
        vrsta_stroska=None,
        racun=None,
        ):

        strosek = self.model(
            oznaka=oznaka,
            naziv=naziv,
            datum_storitve_od=datum_storitve_od,
            datum_storitve_do=datum_storitve_do,
            obdobje_obracuna_leto=obdobje_obracuna_leto,
            obdobje_obracuna_mesec=obdobje_obracuna_mesec,
            delovni_nalog=delovni_nalog,
            osnova=osnova,
            stopnja_ddv=stopnja_ddv,
            vrsta_stroska=vrsta_stroska,
            racun=racun,
        )

        strosek.save(using=self._db)
        return strosek
