from django.db import models


class ArhiviranjeManager(models.Manager):


    def create_arhiviranje(
            self,

            artikel=None,
            delovninalog=None,
            delstavbe=None,
            dobava=None,
            dogodek=None,
            dokument=None,
            element=None,
            pomanjkljivost=None,
            povprasevanje=None,
            sestanek=None,
            racun=None,
            razdelilnik=None,
            reklamacija=None,
            zahtevek=None,

            arhiviral=None,
            lokacija_hrambe=None,
            elektronski=None,
            fizicni=None,
            ):

        arhiviranje = self.model(

            artikel=artikel,
            delovninalog=delovninalog,
            delstavbe=delstavbe,
            dobava=dobava,
            dogodek=dogodek,
            dokument=dokument,
            element=element,
            pomanjkljivost=pomanjkljivost,
            povprasevanje=povprasevanje,
            sestanek=sestanek,
            racun=racun,
            razdelilnik=razdelilnik,
            reklamacija=reklamacija,
            zahtevek=zahtevek,

            arhiviral=arhiviral,
            lokacija_hrambe=lokacija_hrambe,
            elektronski=elektronski,
            fizicni=fizicni,
        )

        arhiviranje.save(using=self._db)
        return arhiviranje


class ArhivMestoManager(models.Manager):

    def create_arhiv_mesto(
        self=None,
        arhiv=None,
        zahtevek=None,
        oznaka=None,
        naziv=None,
    ):

        arhiv_mesto = self.model(
            arhiv=arhiv,
            zahtevek=zahtevek,
            oznaka=oznaka,
            naziv=naziv,
        )

        arhiv_mesto.save(using=self._db)
        return arhiv_mesto
