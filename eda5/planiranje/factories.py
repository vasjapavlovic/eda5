import factory


from .models import Plan
from .models import PlaniranoOpravilo
from .models import SkupinaPlanov



class SkupinaPlanov(factory.django.DjangoModelFactory):

    class Meta:
        model = SkupinaPlanov

    oznaka = factory.Sequence(lambda n: '{0}'.format(n))
    naziv = factory.Sequence(lambda n: 'Skupina planov {0}'.format(n))


class PlanFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Plan

    oznaka = factory.Sequence(lambda n: '{0}'.format(n))
    naziv = factory.Sequence(lambda n: 'Plan {0}'.format(n))
    opis = factory.Sequence(lambda n: 'Opis plana {0}'.format(n))

    sklop = factory.SubFactory(SkupinaPlanov)


class PlaniranoOpraviloFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = PlaniranoOpravilo

    oznaka = factory.Sequence(lambda n: '{0}'.format(n))
    naziv = factory.Sequence(lambda n: 'Planirano Opravilo {0}'.format(n))
    namen = factory.Sequence(lambda n: 'Namen {0}'.format(n))
    obseg = factory.Sequence(lambda n: 'Obseg {0}'.format(n))
    perioda_predpisana_enota = 1
    perioda_predpisana_enota_kolicina = 1
    perioda_predpisana_kolicina_na_enoto = 1

    plan = factory.SubFactory(PlanFactory)
