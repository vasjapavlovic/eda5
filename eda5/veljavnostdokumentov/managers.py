from django.db import models


class VeljavnostDokumentaManager(models.Manager):

    def create_veljavnost_dokumenta(
        self,
        arhiviranje=None,
        stavba=None,
        vrsta_stroska=None,
        velja_od=None,
        velja_do=None,
    ):

        veljavnost_dokumenta = self.model(
            arhiviranje=arhiviranje,
            stavba=stavba,
            vrsta_stroska=vrsta_stroska,
            velja_od=velja_od,
            velja_do=velja_do,
        )

        veljavnost_dokumenta.save(using=self._db)
        return veljavnost_dokumenta