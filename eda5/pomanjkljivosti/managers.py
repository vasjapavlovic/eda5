from django.db import models


class PomanjkljivostManager(models.Manager):

    def create_pomanjkljivost(
        self,
        oznaka=None,
        naziv=None,
        prijavil_text=None,
        prijava_dne=None,
        element_text=None,
        etaza_text=None,
        lokacija_text=None,
        element=None,
        zahtevek=None
    ):

        pomanjkljivost = self.model(
            oznaka=oznaka,
            naziv=naziv,
            prijavil_text=prijavil_text,
            prijava_dne=prijava_dne,
            element_text=element_text,
            etaza_text=etaza_text,
            lokacija_text=lokacija_text,
            element=element,
            zahtevek=zahtevek
        )

        pomanjkljivost.save(using=self.db)
        return pomanjkljivost

