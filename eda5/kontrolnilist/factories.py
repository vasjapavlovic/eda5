import factory


from .models import Aktivnost
from .models import AktivnostParameterSpecifikacija
from .models import OpcijaSelect

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
