from django.db import models
from django.db.models import Q


class OpraviloManager(models.Manager):

    use_for_related_fields = True

    def create_opravilo(self,
                        oznaka=None,
                        naziv=None,
                        rok_izvedbe=None,
                        narocilo=None,
                        zahtevek=None,
                        nosilec=None,
                        planirano_opravilo=None,
                        ):
        if not zahtevek:
            raise ValueError("Izbran mora biti zahtevek")

        opravilo = self.model(oznaka=oznaka,
                              naziv=naziv,
                              rok_izvedbe=rok_izvedbe,
                              narocilo=narocilo,
                              # element se doda kasneje pod ElementManager in OpraviloCreateView
                              zahtevek=zahtevek,
                              nosilec=nosilec,
                              planirano_opravilo=planirano_opravilo,
                              )

        opravilo.save(using=self._db)
        return opravilo


class VzorecOpravilaManager(models.Manager):

    def create_vzorec_opravila(self,
                               oznaka=None,
                               naziv=None,
                               rok_izvedbe=None,
                               narocilo=None,
                               nosilec=None,
                               planirano_opravilo=None,
                               ):

        vzorec_opravila = self.model(
                              oznaka=oznaka,
                              naziv=naziv,
                              rok_izvedbe=rok_izvedbe,
                              narocilo=narocilo,
                              nosilec=nosilec,
                              planirano_opravilo=planirano_opravilo,
                              )

        vzorec_opravila.save(using=self._db)
        return vzorec_opravila


class DelovniNalogManager(models.Manager):

    use_for_related_fields = True

    # nepopolno izpolnjeni delovni nalogi
    def dn_draft(self, **kwargs):
        return self.filter(status=0)

    # delovni nalogi v čakanju
    def dn_vcakanju(self, **kwargs):
        return self.filter(status=1)

    # delovni nalogi v planu
    def dn_vplanu(self, **kwargs):
        return self.filter(status=2)

    # delovni nalogi v reševanju
    def dn_vresevanju(self, **kwargs):
        return self.filter(status=3)

    # zaključeni delovni nalogi
    def dn_zakljuceni(self, **kwargs):
        return self.filter(status=4).order_by("opravilo__is_potrjen", "-datum_stop")

        '''
        razvrstitev:
        -nepotrjeni naprej
        -zadnje končani naprej
        '''


class DeloManager(models.Manager):

    use_for_related_fields = True

    def odprta_dela(self, **kwargs):
        return self.filter(time_stop__isnull=True)

    def koncana_dela(self, **kwargs):
        return self.filter(time_stop__isnull=False)

    def create_delo(
                    self,
                    oznaka=None,
                    naziv=None,
                    delavec=None,
                    datum=None,
                    vrsta_dela=None,
                    time_start=None,
                    delovninalog=None,
    ):

        if not delovninalog:
            raise ValueError("Izbran mora biti delovninalog")

        delo = self.model(
                          oznaka=oznaka,
                          naziv=naziv,
                          delavec=delavec,
                          datum=datum,
                          vrsta_dela=vrsta_dela,
                          time_start=time_start,
                          delovninalog=delovninalog,
        )

        delo.save(using=self._db)
        return delo

