import factory

from .models import Aktivnost
from .models import AktivnostParameterSpecifikacija
from .models import Opravilo
from .models import OpcijaSelect
from eda5.arhiv.models import Arhiv
from eda5.narocila.models import Narocilo
from eda5.partnerji.models import Partner, Oseba, Posta, Drzava
from eda5.zahtevki.models import Zahtevek

from eda5.deli.factories import ProjektnoMestoFactory




class ArhivFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Arhiv

    oznaka = '01'
    naziv = 'Arhiv 1'



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


class ZahtevekFactory(ArhivFactory, factory.django.DjangoModelFactory):
    class Meta:
        model = Zahtevek

    nosilec = factory.SubFactory(OsebaFactory)
    vrsta = 5
    rok_izvedbe = "2017-11-11"



class NarociloFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Narocilo

    oznaka = factory.Sequence(lambda n: '{0}'.format(n))
    predmet = factory.Sequence(lambda n: '{0}'.format(n))
    narocnik = factory.SubFactory(PartnerFactory)
    izvajalec = factory.SubFactory(PartnerFactory)
    datum_narocila = "2017-11-11"
    datum_veljavnosti = "2017-11-11"


class OpraviloFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Opravilo

    naziv = factory.Sequence(lambda n: 'Opravilo {0}'.format(n))
    zahtevek = factory.SubFactory(ZahtevekFactory)
    narocilo = factory.SubFactory(NarociloFactory)
    nosilec = factory.SubFactory(OsebaFactory)
    rok_izvedbe = "2017-11-11"


class AktivnostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Aktivnost

    oznaka = factory.Sequence(lambda n: u'Aktivnost {}'.format(n))
    naziv = 'Moja prva aktivnost'
    opravilo = factory.SubFactory(OpraviloFactory)

    @factory.post_generation
    def projektno_mesto(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for pm in extracted:
                self.projektno_mesto.add(pm)


class AktivnostParameterSpecifikacijaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AktivnostParameterSpecifikacija

    oznaka = factory.Sequence(lambda n: u'PAS {}'.format(n))
    naziv = 'Parameter aktivnosti specifikacija'
    aktivnost = factory.SubFactory(AktivnostFactory)



class OpcijaSelectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OpcijaSelect

    oznaka = factory.Sequence(lambda n: 'Opcija {0}'.format(n))
    naziv = factory.Sequence(lambda n: 'Opcija {0}'.format(n))
    aktivnost_parameter_specifikacija = factory.SubFactory(AktivnostParameterSpecifikacijaFactory)
