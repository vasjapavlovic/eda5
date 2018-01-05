import factory

from .models import Aktivnost


class AktivnostFactory(factory.Factory):
    class Meta:
        model = Aktivnost


    naziv = 'Moja prva aktivnost'
    oznaka = factory.Sequence(lambda n: u'Aktivnost {}'.format(n))
