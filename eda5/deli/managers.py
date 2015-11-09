from django.db import models


class SkupinaDelovManagers:
    pass


class PodskupinaDelovManagers:
    pass


class DelManagers(models.Manager):

    def create_del(
                   self,
                   podskupina=None,
                   oznaka=None,
                   naziv=None,
                   shema=None,
                   lastniska_skupina=None,
                   ):

        delstavbe = self.model(
                               podskupina=podskupina,
                               oznaka=oznaka,
                               naziv=naziv,
                               shema=shema,
                               lastniska_skupina=lastniska_skupina,
                               # prejeta_dokumentacija=prejeta_dokumentacija,
                               )

        delstavbe.save(using=self._db)

        return delstavbe


class ElementManagers:
    pass
