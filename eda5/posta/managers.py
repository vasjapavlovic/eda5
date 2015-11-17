from django.db import models


class AktivnostManager(models.Manager):

    def create_aktivnost(
                        self,
                        id_1=None,
                        izvajalec=None,
                        vrsta_aktivnosti=None,
                        datum=None,
                        ):

        aktivnost_model = self.model(
            id_1=id_1,
            izvajalec=izvajalec,
            vrsta_aktivnosti=vrsta_aktivnosti,
            datum=datum,
        )

        aktivnost_model.save(using=self._db)
        return aktivnost_model


class DokumentManager(models.Manager):

    def create_dokument(
                        self,
                        aktivnost=None,
                        vrsta_dokumenta=None,
                        avtor=None,
                        naslovnik=None,
                        oznaka=None,
                        naziv=None,
                        datum=None,
                        priponka=None,
                        ):

        dokument_model = self.model(
            aktivnost=aktivnost,
            vrsta_dokumenta=vrsta_dokumenta,
            avtor=avtor,
            naslovnik=naslovnik,
            oznaka=oznaka,
            naziv=naziv,
            datum=datum,
            priponka=priponka,
        )

        dokument_model.save(using=self._db)
        return dokument_model
