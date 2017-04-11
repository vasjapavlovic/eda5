from django.db import models


class SestanekManager(models.Manager):
    #=================================================
    # osnovni podatki
    #-------------------------------------------------
    # oznaka, oznaka reklamacije. Oblika Leto+zap.št.
    # naziv, kratko ime (naziv sestanka)
    # opis, namen sestanka
    # datum, datum sestanka
    # sklicatelj, Relacija na Osebo iz Partnerji
    # prisotni, relacija na osebe iz partnerji (many to many)
    # status (v reševanju, zaključeno ...)

    #=================================================
    # relacije z zahtevki, delovni nalogi,
    #-------------------------------------------------
    # zahtevek, sestanek je del zahtevka

    def create_sestanek(
        self,
        oznaka=None,
        naziv=None,
        opis=None,
        datum=None,
        sklicatelj=None,
        zahtevek=None,
    ):

        sestanek = self.model(
            oznaka=oznaka,
            naziv=naziv,
            opis=opis,
            datum=datum,
            sklicatelj=sklicatelj,
            zahtevek=zahtevek,
        )

        sestanek.save(using=self._db)
        return sestanek

    # zahtevki v reševanju
    def status_vresevanju(self, **kwargs):
        return self.filter(status=3).order_by('-id')

    # zaključeni zahtevki
    def status_zakljuceno(self, **kwargs):
        return self.filter(status=4).order_by('-id')


class TemaManager(models.Manager):
    pass


class TockaManager(models.Manager):
    pass