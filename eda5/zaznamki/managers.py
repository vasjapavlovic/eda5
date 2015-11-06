from django.db import models


class ZaznamekManager(models.Managers):
    def create_zaznamek(self,
                        tekst=None,
                        datum=None,
                        ura=None,
                        zahtevek=None,
                        ):

        zaznamek = self.model(tekst=None,
                              datum=None,
                              ura=None,
                              zahtevek=None,
                              )

        zaznamek.save(using=self._db)
        return zaznamek
