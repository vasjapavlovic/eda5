from django.db import models


class PlaniranoOpraviloManager(models.Manager):

    use_for_related_fields = True

    def nezapadla(self, **kwargs):
        return self.filter(datum_naslednjega_opravila__gte=timezone.now()).order_by('do_naslednjega_opravila_dni')

    def zapadla(self, **kwargs):
        return self.filter(datum_naslednjega_opravila__lt=timezone.now()).order_by('do_naslednjega_opravila_dni')



    def create_planirano_opravilo(
        self,
        oznaka=None,
        naziv=None,
        namen=None,
        obseg=None,
        perioda_predpisana_enota=None,
        perioda_predpisana_enota_kolicina=None,
        perioda_predpisana_kolicina_na_enoto=None,
        datum_prve_izvedbe=None,
        opomba=None,
        zmin=None,
        plan=None,
    ):

        planirano_opravilo = self.model(
            oznaka=oznaka,
            naziv=naziv,
            namen=namen,
            obseg=obseg,
            perioda_predpisana_enota=perioda_predpisana_enota,
            perioda_predpisana_enota_kolicina=perioda_predpisana_enota_kolicina,
            perioda_predpisana_kolicina_na_enoto=perioda_predpisana_kolicina_na_enoto,
            datum_prve_izvedbe=datum_prve_izvedbe,
            opomba=opomba,
            zmin=zmin,
            plan=plan,
        )

        planirano_opravilo.save(using=self._db)
        return planirano_opravilo

