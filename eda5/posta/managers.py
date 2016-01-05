from django.db import models


class AktivnostManager(models.Manager):

    def create_aktivnost(
                        self,
                        izvajalec=None,
                        vrsta_aktivnosti=None,
                        datum_aktivnosti=None,
                        ):

        aktivnost_model = self.model(
            izvajalec=izvajalec,
            vrsta_aktivnosti=vrsta_aktivnosti,
            datum_aktivnosti=datum_aktivnosti,
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
                        oznaka_baza=None,
                        oznaka=None,
                        naziv=None,
                        datum_dokumenta=None,
                        priponka=None,
                        ):

        dokument_model = self.model(
            aktivnost=aktivnost,
            vrsta_dokumenta=vrsta_dokumenta,
            avtor=avtor,
            naslovnik=naslovnik,
            oznaka_baza=oznaka_baza,
            oznaka=oznaka,
            naziv=naziv,
            datum_dokumenta=datum_dokumenta,
            priponka=priponka,
        )

        dokument_model.save(using=self._db)
        return dokument_model

