from django.db import models


class ZaznamekManager(models.Manager):

    def create_zaznamek(
        self,
        tekst=None,
        datum=None,
        ura=None,
        zahtevek=None,
        delovninalog=None,
    ):

        zaznamek = self.model(
            tekst=tekst,
            datum=datum,
            ura=ura,
            zahtevek=zahtevek,
            delovninalog=delovninalog,
        )

        zaznamek.save(using=self._db)
        return zaznamek
