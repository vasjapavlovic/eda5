from django.db import models


class DogodekManager(models.Manager):

    def create_dogodek(
        self,
        datum_dogodka=None,
        cas_dogodka=None,
        opis_dogodka=None,
        is_potrebna_prijava_policiji=None,
        is_nastala_skoda=None,
        povzrocitelj=None,
        zahtevek=None,
        ):

        dogodek = self.model(
            datum_dogodka=datum_dogodka,
            cas_dogodka=cas_dogodka,
            opis_dogodka=opis_dogodka,
            is_potrebna_prijava_policiji=is_potrebna_prijava_policiji,
            is_nastala_skoda=is_nastala_skoda,
            povzrocitelj=povzrocitelj,
            zahtevek=zahtevek,
            )

        dogodek.save(using=self._db)
        return dogodek

        # zahtevki v reševanju
    def status_vresevanju(self, **kwargs):
        return self.filter(status=3).order_by('-id')

    # zaključeni zahtevki
    def status_zakljuceno(self, **kwargs):
        return self.filter(status=4).order_by('-id')
