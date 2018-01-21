from django.db import models


from eda5.core.models import OsnovnaKombinacija
from eda5.deli.models import ProjektnoMesto
from eda5.planiranje.models import PlanKontrolaSpecifikacija



class Parameter(OsnovnaKombinacija):

    # kateri kontrolo bomo spremljali
    plan_kontrola_specifikacija = models.ForeignKey(
        PlanKontrolaSpecifikacija,
        verbose_name='poročilo o rezultatu kontrole'
    )

    # za katero projektno mesto bomo spremljali
    projektno_mesto = models.ForeignKey(
        ProjektnoMesto,
        verbose_name='projektno mesto'
    )


    class Meta:
        verbose_name='Report maped PlanKontrolaSpeciikacija'


    def __str__(self):
        return 'PM:%s|PAR:%s' % (self.projektno_mesto.oznaka, self.plan_kontrola_specifikacija.naziv)
