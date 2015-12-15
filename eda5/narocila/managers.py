from django.db import models
from django.utils import timezone


class NarociloManager(models.Manager):

    use_for_related_fields = True

    def veljavna(self, **kwargs):
        return self.filter(datum_veljavnosti__gte=timezone.now(), **kwargs)

    def create_narocilo(
        self,
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
        oseba=None,
        telefonska_stevilka=None,
        datum_klica=None,
        cas_klica=None,
        telefonsko_sporocilo=None,
    ):
        narocilo_telefon_model = self.model(
            oseba=oseba,
            telefonska_stevilka=telefonska_stevilka,
            datum_klica=datum_klica,
            cas_klica=cas_klica,
            telefonsko_sporocilo=telefonsko_sporocilo,
        )
        narocilo_telefon_model.save(using=self._db)
        return narocilo_telefon_model
