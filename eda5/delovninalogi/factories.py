import factory


from .models import Opravilo
from .models import DelovniNalog
from .models import VzorecOpravila


from eda5.narocila.models import Narocilo

from eda5.zahtevki.models import Zahtevek

from eda5.deli.factories import ProjektnoMestoFactory


from eda5.partnerji.factories import OsebaFactory
from eda5.partnerji.factories import PartnerFactory
from eda5.zahtevki.factories import ZahtevekFactory
from eda5.planiranje.factories import PlaniranoOpraviloFactory





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


class VzorecOpravilaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = VzorecOpravila

    oznaka = factory.Sequence(lambda n: 'vz_opr_{0}'.format(n))
    naziv = factory.Sequence(lambda n: 'Vzorec opravila {0}'.format(n))
    narocilo = factory.SubFactory(NarociloFactory)
    nosilec = factory.SubFactory(OsebaFactory)
    rok_izvedbe = "2017-11-11"
    planirano_opravilo = factory.SubFactory(PlaniranoOpraviloFactory)

    @factory.post_generation
    def aktivnost(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for akt in extracted:
                self.aktivnost.add(akt)


class DelovniNalogFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = DelovniNalog

    naziv = factory.Sequence(lambda n: 'Opravilo {0}'.format(n))
    opravilo = factory.SubFactory(OpraviloFactory)
    nosilec = factory.SubFactory(OsebaFactory)
