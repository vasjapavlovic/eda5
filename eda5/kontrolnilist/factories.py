import factory


from .models import Aktivnost
from .models import KontrolaSpecifikacija
from .models import KontrolaSpecifikacijaOpcijaSelect

from eda5.delovninalogi.factories import OpraviloFactory

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
