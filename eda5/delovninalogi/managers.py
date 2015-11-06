from django.db import models


class OpraviloManager(models.Manager):

    def create_opravilo(self,
                        oznaka=None,
                        naziv=None,
                        rok_izvedbe=None,
                        narocilo=None,
                        zahtevek=None,
                        ):
        if not zahtevek:
            raise ValueError("Izbran mora biti zahtevek")

        opravilo = self.model(oznaka=oznaka,
                              naziv=naziv,
                              rok_izvedbe=rok_izvedbe,
                              narocilo=narocilo,
                              # element=element,
                              zahtevek=zahtevek,
                              )

        opravilo.save(using=self._db)
        return opravilo
