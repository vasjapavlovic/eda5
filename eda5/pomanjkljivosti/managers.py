from django.db import models


class PomanjkljivostManager(models.Manager):

    def create_pomanjkljivost(
        self,

        # za uporabnika
        oznaka=None,
        opis_text=None,
        prijavil_text=None,
        ugotovljeno_dne=None,
        element_text=None,
        lokacija_text=None,

        # za administratorja
        naziv=None,
        opis=None,
        # element=None,
        prioriteta=None,
        zahtevek=None
    ):

        pomanjkljivost = self.model(

            # za uporabnika
            oznaka=oznaka,
            opis_text=opis_text,
            prijavil_text=prijavil_text,
            ugotovljeno_dne=ugotovljeno_dne,
            element_text=element_text,
            lokacija_text=lokacija_text,

            # za administratorja
            naziv=naziv,
            opis=opis,
            # element=element, se doda v updatu ko je pomanjkljivost izdelana
            prioriteta=prioriteta,
            zahtevek=zahtevek
        )

        pomanjkljivost.save(using=self.db)
        return pomanjkljivost

