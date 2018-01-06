import factory


from .models import Zahtevek

from eda5.partnerji.factories import OsebaFactory



class ZahtevekFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Zahtevek

    nosilec = factory.SubFactory(OsebaFactory)
    vrsta = 5
    rok_izvedbe = "2017-11-11"
