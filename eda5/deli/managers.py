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



class ProjektnoMestoManagers(models.Manager):

    def create_projektno_mesto(
                   self,
                   oznaka=None,
                   naziv=None,
                   funkcija=None,
                   bim_id=None,
                   tip_elementa=None,
                   lokacija=None,
                   del_stavbe=None,
                   ):

        projektnomesto = self.model(
                   oznaka=oznaka,
                   naziv=naziv,
                   funkcija=funkcija,
                   bim_id=bim_id,
                   tip_elementa=tip_elementa,
                   lokacija=lokacija,
                   del_stavbe=del_stavbe,
                   )

        projektnomesto.save(using=self._db)

        return projektnomesto


class ElementManagers:
    pass
                        # 'oznaka',
                        # 'naziv',
                        # 'funkcija',
                        # 'bim_id',
                        # 'tip_elementa',
                        # 'lokacija',
                        # 'del_stavbe',