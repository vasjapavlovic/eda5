from django.db import models


class DnevnikManager(models.Manager):

    def create_dnevnik(
        self,
        dobava=None,
        artikel=None,
        delovninalog=None,
        likvidiral=None,
        kom=None,
        cena=None,
        stopnja_ddv=None,
    ):

        dnevnik = self.model(
            dobava=dobava,
            artikel=artikel,
            delovninalog=delovninalog,
            likvidiral=likvidiral,
            kom=kom,
            cena=cena,
            stopnja_ddv=stopnja_ddv
        )

        dnevnik.save(using=self._db)
        return dnevnik
