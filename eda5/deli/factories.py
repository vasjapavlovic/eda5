import factory


from .models import DelStavbe
from .models import Stavba
from .models import Skupina
from .models import Podskupina
from .models import ProjektnoMesto


class StavbaFactory(factory.DjangoModelFactory):
    class Meta:
        model = Stavba

    oznaka = factory.Sequence(lambda n: '{0}'.format(n))
    naziv = factory.Sequence(lambda n: 'Stavba {0}'.format(n))


class SkupinaFactory(factory.DjangoModelFactory):
    class Meta:
        model = Skupina

    oznaka = factory.Sequence(lambda n: '{0}'.format(n))
    naziv = factory.Sequence(lambda n: 'Skupina {0}'.format(n))


class PodskupinaFactory(factory.DjangoModelFactory):
    class Meta:
        model = Podskupina

    oznaka = factory.Sequence(lambda n: '{0}'.format(n))
    naziv = factory.Sequence(lambda n: 'Podskupina {0}'.format(n))
    skupina = factory.SubFactory(SkupinaFactory)


class DelStavbeFactory(factory.DjangoModelFactory):
    class Meta:
        model = DelStavbe

    oznaka = factory.Sequence(lambda n: '{0}'.format(n))
    naziv = factory.Sequence(lambda n: 'Podskupina {0}'.format(n))
    podskupina = factory.SubFactory(PodskupinaFactory)



class ProjektnoMestoFactory(factory.DjangoModelFactory):
    class Meta:
        model = ProjektnoMesto

    oznaka = factory.Sequence(lambda n: '{0}'.format(n))
    naziv = factory.Sequence(lambda n: 'Podskupina {0}'.format(n))
    del_stavbe = factory.SubFactory(DelStavbeFactory)
    tip_elementa = None
