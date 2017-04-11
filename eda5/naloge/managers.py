from django.db import models


class NalogaManager(models.Manager):

    def create_naloga(
        self,
        oznaka=None,
        naziv=None,
        opis=None,
        rok_izvedbe=None,
        prioriteta=None,
        nosilec=None,
        zahtevek=None,
        sklep_sestanka=None  # navezava na sklep sestanka
    ):

        naloga = self.model(
            oznaka=oznaka,
            naziv=naziv,
            opis=opis,
            rok_izvedbe=rok_izvedbe,
            prioriteta=prioriteta,
            nosilec=nosilec,
            zahtevek=zahtevek,
            sklep_sestanka=sklep_sestanka  # navezava na sklep sestanka
            )

        naloga.save(using=self.db)
        return naloga

