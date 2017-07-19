from django.db import models


class AktivnostManager(models.Manager):

    def create_aktivnost(
                        self,
                        izvajalec=None,
                        datum_aktivnosti=None,
                        ):

        aktivnost_model = self.model(
            izvajalec=izvajalec,
            datum_aktivnosti=datum_aktivnosti,
        )

        aktivnost_model.save(using=self._db)
        return aktivnost_model


class DokumentManager(models.Manager):

    def __init__(self, *args, **kwargs):
        super(DokumentManager, self).__init__(*args, **kwargs)

    def arhivirano():
        return self.get_query_set().filter(arhiviranje__isnull=False).order_by('-aktivnost__datum_aktivnosti')[0]

    def za_arhiviranje():
        return self.get_query_set().filter(arhiviranje__isnull=True).order_by('-aktivnost__datum_aktivnosti')[0]



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
                        kraj_izdaje=None,
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
            kraj_izdaje=kraj_izdaje,
        )

        dokument_model.save(using=self._db)
        return dokument_model

