from django.db import models


class ZahtevekManager(models.Manager):

    def create_zahtevek(
        self,
        oznaka=None,
        vrsta=None,
        predmet=None,
        rok_izvedbe=None,
        narocilo=None,
        nosilec=None,
        zahtevek_parent=None,
    ):

        zahtevek = self.model(
            oznaka=oznaka,
            vrsta=vrsta,
            predmet=predmet,
            rok_izvedbe=rok_izvedbe,
            narocilo=narocilo,
            nosilec=nosilec,
            zahtevek_parent=zahtevek_parent,
            )

        zahtevek.save(using=self._db)
        return zahtevek
