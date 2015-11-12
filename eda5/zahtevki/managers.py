from django.db import models


class ZahtevekManager(models.Manager):

    def create_zahtevek(
        self,
        oznaka=None,
        predmet=None,
        rok_izvedbe=None,
        narocilo=None,
        nosilec=None,
        zahtevek_skodni_dogodek=None,
        zahtevek_sestanek=None,
        zahtevek_izvedba_dela=None,
        zahtevek_parent=None,
        ):

        zahtevek = self.model(
            oznaka=oznaka,
            predmet=predmet,
            rok_izvedbe=rok_izvedbe,
            narocilo=narocilo,
            nosilec=nosilec,
            zahtevek_skodni_dogodek=zahtevek_skodni_dogodek,
            zahtevek_sestanek=zahtevek_sestanek,
            zahtevek_izvedba_dela=zahtevek_izvedba_dela,
            zahtevek_parent=zahtevek_parent,
            )

        zahtevek.save(using=self._db)
        return zahtevek

