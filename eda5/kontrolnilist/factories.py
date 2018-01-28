import factory


from .models import Aktivnost
from .models import KontrolaSkupina
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
    perioda_enota = 1
    perioda_enota_kolicina = 1
    perioda_kolicina_na_enoto = 1
    opravilo = factory.SubFactory(OpraviloFactory)


    # @factory.post_generation
    # def projektno_mesto(self, create, extracted, **kwargs):
    #     if not create:
    #         # Simple build, do nothing.
    #         return
    #
    #     if extracted:
    #         # A list of groups were passed in, use them
    #         for pm in extracted:
    #             self.projektno_mesto.add(pm)


class KontrolaSkupinaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = KontrolaSkupina


    naziv = factory.Sequence(lambda n: u'KS_{}'.format(n))
    aktivnost = factory.SubFactory(AktivnostFactory)



class KontrolaSpecifikacijaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = KontrolaSpecifikacija

    oznaka = factory.Sequence(lambda n: u'PAS {}'.format(n))
    naziv = 'Specifikacija kontrole'
    kontrola_skupina = factory.SubFactory(KontrolaSkupinaFactory)


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
