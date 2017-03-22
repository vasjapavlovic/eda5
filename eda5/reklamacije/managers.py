from django.db import models


class ReklamacijaManager(models.Manager):

    # oznaka, oznaka reklamacije. Oblika Leto+zap.št.
    # naziv, kratko ime reklamacije
    # opis, daljši opis vsebine reklamacije
    # datum, kdaj se je reklamacija vložila
    # narocnik, reklamira blago ali storitev
    # izvajalec, se mu reklamira blago ali storitev
    # status
    # okvirni_strosek, evidenca ISO 9001

    #=================================================
    # relacije z zahtevki, delovni nalogi,
    #-------------------------------------------------
    # zahtevek, reklamacija je del zahtevka
    # delovninalog, reklamira se delovni nalog

    def create_reklamacija(
        self,
        oznaka=None,
        naziv=None,
        opis=None,
        datum=None,
        narocnik=None,
        izvajalec=None,
        okvirni_strosek=None,
        zahtevek=None,
        delovninalog=None,
    ):

        reklamacija = self.model(
            oznaka=oznaka,
            naziv=naziv,
            opis=opis,
            datum=datum,
            narocnik=narocnik,
            izvajalec=izvajalec,
            okvirni_strosek=okvirni_strosek,
            zahtevek=zahtevek,
            delovninalog=delovninalog,
        )

        reklamacija.save(using=self._db)
        return reklamacija

    # zahtevki v reševanju
    def status_vresevanju(self, **kwargs):
        return self.filter(status=3).order_by('-id')

    # zaključeni zahtevki
    def status_zakljuceno(self, **kwargs):
        return self.filter(status=4).order_by('-id')
