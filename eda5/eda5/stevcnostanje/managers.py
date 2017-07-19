from django.db import models


class OdcitekManager(models.Manager):
    def create_odcitek(self, delilnik=None, obdobje_leto=None, obdobje_mesec=None,
                       odcital=None, datum_odcitka=None, stanje_staro=None, stanje_novo=None):
        if not delilnik:
            raise ValueError("Izbrati delilnik")

        odcitek = self.model(
            delilnik=delilnik,
            obdobje_leto=obdobje_leto,
            obdobje_mesec=obdobje_mesec,
            odcital=odcital,
            datum_odcitka=datum_odcitka,
            stanje_staro=stanje_staro,
            stanje_novo=stanje_novo,
            )

        odcitek.save(using=self._db)
        return odcitek
