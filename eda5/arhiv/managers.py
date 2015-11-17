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
