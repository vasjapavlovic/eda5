import factory

from .models import Drzava
from .models import Oseba
from .models import Partner
from .models import Posta

class DrzavaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Drzava

    iso_koda = factory.Sequence(lambda n: '{0}'.format(n))
    naziv = 'B'

class PostaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Posta

    postna_stevilka = factory.Sequence(lambda n: '{0}'.format(n))
    naziv = "A"
    drzava = factory.SubFactory(DrzavaFactory)


class PartnerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Partner

    kratko_ime = factory.Sequence(lambda n: '{0}'.format(n))
    naslov = factory.Sequence(lambda n: '{0}'.format(n))
    posta = factory.SubFactory(PostaFactory)
    davcna_st = factory.Sequence(lambda n: '{0}'.format(n))


class OsebaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Oseba

    podjetje = factory.SubFactory(PartnerFactory)
