import factory

from .models import Aktivnost
from .models import Opravilo



class OpraviloFactory(factory.Factory):
    class Meta:
        model = Opravilo


class AktivnostFactory(factory.Factory):
    class Meta:
        model = Aktivnost

    oznaka = factory.Sequence(lambda n: u'Aktivnost {}'.format(n))
    naziv = 'Moja prva aktivnost'
    opravilo = factory.SubFactory(OpraviloFactory)
