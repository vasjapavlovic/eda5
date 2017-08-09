from django.db import models


class RazdelilnikManager(models.Manager):

    def create_razdelilnik(
        self,
        oznaka=None,
        naziv=None,
        stavba=None,
        zahtevek=None,
        obdobje_obracuna_leto=None,
        obdobje_obracuna_mesec=None,
    ):

        razdelilnik = self.model(
            oznaka=oznaka,
            naziv=naziv,
            stavba=stavba,
            zahtevek=zahtevek,
            obdobje_obracuna_leto=obdobje_obracuna_leto,
            obdobje_obracuna_mesec=obdobje_obracuna_mesec,
        )

        razdelilnik.save(using=self._db)
        return razdelilnik


class StrosekRazdelilnikManager(models.Manager):

    def create_strosekrazdelilnik(
        self,
        strosek=None,
        razdelilnik=None,
    ):

        strosekrazdelilnik = self.model(
            strosek=strosek,
            razdelilnik=razdelilnik,
        )

        strosekrazdelilnik.save(using=self._db)
        return strosekrazdelilnik



class StrosekRazdelilnikPostavkaManager(models.Manager):

    def create_strosekrazdelilnikpostavka(
        self,
        oznaka=None,
        naziv=None,
        strosek_razdelilnik=None,
        lastniska_skupina=None,
        delilnik_kljuc=None,
        delitev_vrsta=None,
        delilnik_vrednost=None,
        is_strosek_posameznidel=None,
    ):

        strosekrazdelilnikpostavka = self.model(
            oznaka=oznaka,
            naziv=naziv,
            strosek_razdelilnik=strosek_razdelilnik,
            lastniska_skupina=lastniska_skupina,
            delilnik_kljuc=delilnik_kljuc,
            delitev_vrsta=delitev_vrsta,
            delilnik_vrednost=delilnik_vrednost,
            is_strosek_posameznidel=is_strosek_posameznidel,
        )

        strosekrazdelilnikpostavka.save(using=self._db)
        return strosekrazdelilnikpostavka


class StrosekLEManager(models.Manager):

    def create_strosekLE(
        self,
        strosek_razdelilnik=None,
        lastniska_enota_interna=None,
        delilnik_vrednost=None,
    ):

        strosekLE = self.model(
            strosek_razdelilnik=strosek_razdelilnik,
            lastniska_enota_interna=lastniska_enota_interna,
            delilnik_vrednost=delilnik_vrednost,
        )

        strosekLE.save(using=self._db)
        return strosekLE

