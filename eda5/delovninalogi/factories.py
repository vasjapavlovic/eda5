import factory

from .models import Aktivnost


class AktivnostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Aktivnost


    naziv = 'Moja prva aktivnost'
