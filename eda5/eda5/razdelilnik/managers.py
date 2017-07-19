from django.db import models


class RacunRazdelilnikManager(models.Manager):



    def create_racunrazdelilnik(
        self,
        razdelilnik=None,
        racun=None,
    ):

        racunrazdelilnik = self.model(
            razdelilnik=razdelilnik,
            racun=racun,
        )

        racunrazdelilnik.save(using=self._db)
        return racunrazdelilnik

    # zahtevki v reševanju
    def status_vresevanju(self, **kwargs):
        return self.filter(status=3).order_by('-id')

    # zaključeni zahtevki
    def status_zakljuceno(self, **kwargs):
        return self.filter(status=4).order_by('-id')
