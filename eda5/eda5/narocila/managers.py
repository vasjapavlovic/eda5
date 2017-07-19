from django.db import models
from django.utils import timezone


class NarociloManager(models.Manager):

    use_for_related_fields = True

    ''' Prikaži samo veljavna naročila '''
    def veljavna(self, **kwargs):
        return self.filter(datum_veljavnosti__gte=timezone.now(), **kwargs)

    ''' Izdela novo naročilo '''
    def create_narocilo(
        self,
        zahtevek=None,
        narocnik=None,
        izvajalec=None,
        oznaka=None,
        predmet=None,
        datum_narocila=None,
        datum_veljavnosti=None,
        vrednost=None,
        narocilo_telefon=None,

    ):
        narocilo_model = self.model(
            zahtevek=zahtevek,
            narocnik=narocnik,
            izvajalec=izvajalec,
            oznaka=oznaka,
            predmet=predmet,
            datum_narocila=datum_narocila,
            datum_veljavnosti=datum_veljavnosti,
            vrednost=vrednost,
            narocilo_telefon=narocilo_telefon,

        )
        narocilo_model.save(using=self._db)
        return narocilo_model


class NarociloTelefonManager(models.Manager):

    def create_narocilo_telefon(
        self,
        dogovor_text=None,
        dogovor_date=None,
        dogovor_time=None,
        dogovor_person=None,
        dogovor_phonenumber=None,
    ):
        narocilo_telefon_model = self.model(
            dogovor_text=dogovor_text,
            dogovor_date=dogovor_date,
            dogovor_time=dogovor_time,
            dogovor_person=dogovor_person,
            dogovor_phonenumber=dogovor_phonenumber,
        )
        narocilo_telefon_model.save(using=self._db)
        return narocilo_telefon_model


class NarociloDokumentManager(models.Manager):

    use_for_related_fields = True

    def create_narocilo_dokument(
        self,
        vrsta_dokumenta=None,
        dokument=None,
        narocilo=None,
    ):
        narocilo_dokument_model = self.model(
            vrsta_dokumenta=vrsta_dokumenta,
            dokument=dokument,
            narocilo=narocilo,
        )
        narocilo_dokument_model.save(using=self._db)
        return narocilo_dokument_model
