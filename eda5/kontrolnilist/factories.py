import factory


from .models import Aktivnost
from .models import KontrolaSpecifikacija
from .models import KontrolaSpecifikacijaOpcijaSelect
from .models import KontrolaVrednost

from eda5.delovninalogi.factories import DelovniNalogFactory
from eda5.delovninalogi.factories import OpraviloFactory
from eda5.deli.factories import ProjektnoMestoFactory


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


class KontrolaSpecifikacijaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = KontrolaSpecifikacija

    oznaka = factory.Sequence(lambda n: u'PAS {}'.format(n))
    naziv = 'Specifikacija kontrole'
    aktivnost = factory.SubFactory(AktivnostFactory)



class KontrolaSpecifikacijaOpcijaSelectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = KontrolaSpecifikacijaOpcijaSelect

    oznaka = factory.Sequence(lambda n: 'Opcija {0}'.format(n))
    naziv = factory.Sequence(lambda n: 'Opcija {0}'.format(n))
    kontrola_specifikacija = factory.SubFactory(KontrolaSpecifikacijaFactory)


class KontrolaVrednostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = KontrolaVrednost

    oznaka = factory.Sequence(lambda n: 'kv{0}'.format(n))
    oznaka_gen = 'generirana oznaka'
    naziv = factory.Sequence(lambda n: 'Kontrola Vrednost {0}'.format(n))
    opis = 'opis'
    vrednost_text = 'abc'
    kontrola_specifikacija = factory.SubFactory(KontrolaSpecifikacijaFactory)
    delovni_nalog = factory.SubFactory(DelovniNalogFactory)
    projektno_mesto = factory.SubFactory(ProjektnoMestoFactory)
