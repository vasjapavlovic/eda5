from django.db import models


class ZahtevekManager(models.Manager):

    def create_zahtevek(
        self,
        oznaka=None,
        vrsta=None,
        naziv=None,
        rok_izvedbe=None,
        narocilo=None,
        nosilec=None,
        zahtevek_parent=None,
    ):

        zahtevek = self.model(
            oznaka=oznaka,
            vrsta=vrsta,
            naziv=naziv,
            rok_izvedbe=rok_izvedbe,
            narocilo=narocilo,
            nosilec=nosilec,
            zahtevek_parent=zahtevek_parent,
        )

        zahtevek.save(using=self._db)
        return zahtevek


class ZahtevekSestanekManager(models.Manager):

    def create_zahtevek_sestanek(
        self,
        zahtevek=None,
        sklicatelj=None,

        datum=None,
    ):

        zahtevek_sestanek = self.model(
            zahtevek=zahtevek,
            sklicatelj=sklicatelj,
            # udelezenci=udelezenci,
            datum=datum,
        )
        zahtevek_sestanek.save(using=self._db)
        return zahtevek_sestanek


class ZahtevekIzvedbaDelaManager(models.Manager):

    def create_zahtevek_sestanek(
        self,
        zahtevek=None,
        is_zakonska_obveza=None,
    ):

        zahtevek_izvedba_del = self.model(
            zahtevek=zahtevek,
            is_zakonska_obveza=is_zakonska_obveza,
        )
        zahtevek_izvedba_del.save(using=self._db)
        return zahtevek_izvedba_del
