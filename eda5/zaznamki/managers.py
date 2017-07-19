from django.db import models


class ZaznamekManager(models.Manager):

    def create_zaznamek(
        self,
        tekst=None,
        datum=None,
        ura=None,
        zahtevek=None,
        delovninalog=None,
        razdelilnik=None,
        reklamacija=None,
        dobava=None,
        sestanek=None,
        povprasevanje=None,
    ):

        zaznamek = self.model(
            tekst=tekst,
            datum=datum,
            ura=ura,
            zahtevek=zahtevek,
            delovninalog=delovninalog,
            razdelilnik=razdelilnik,
            reklamacija=reklamacija,
            dobava=dobava,
            sestanek=sestanek,
            povprasevanje=povprasevanje,
        )

        zaznamek.save(using=self._db)
        return zaznamek
