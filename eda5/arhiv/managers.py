from django.db import models


class ArhiviranjeManager(models.Manager):

    def create_arhiviranje(
                self,
                dokument=None,
                arhiviral=None,
                lokacija_hrambe=None,
                elektronski=None,
                fizicni=None,
                ):

        arhiviranje = self.model(
            dokument=dokument,
            arhiviral=arhiviral,
            lokacija_hrambe=lokacija_hrambe,
            elektronski=elektronski,
            fizicni=fizicni,
        )

        arhiviranje.save(using=self._db)
        return arhiviranje


class ArhivMestoManager(models.Manager):

    def create_arhiv_mesto(
        self=None,
        arhiv=None,
        zahtevek=None,
        oznaka=None,
        naziv=None,
    ):

        arhiv_mesto = self.model(
            arhiv=arhiv,
            zahtevek=zahtevek,
            oznaka=oznaka,
            naziv=naziv,
        )

        arhiv_mesto.save(using=self._db)
        return arhiv_mesto
