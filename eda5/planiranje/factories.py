import factory


from .models import Plan, PlanAktivnost, PlanKontrolaSkupina, PlanKontrolaSpecifikacija, PlanKontrolaSpecifikacijaOpcijaSelect
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


class PlanAktivnostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PlanAktivnost

    oznaka = factory.Sequence(lambda n: u'PlanAktivnost {}'.format(n))
    naziv = 'Moja planirana aktivnost'
    #opravilo = factory.SubFactory(OpraviloFactory)
    perioda_enota = 1
    perioda_enota_kolicina = 1
    perioda_kolicina_na_enoto = 1
    plan = factory.SubFactory(PlanFactory)


    @factory.post_generation
    def projektno_mesto(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for pm in extracted:
                self.projektno_mesto.add(pm)


class PlanKontrolaSkupinaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PlanKontrolaSkupina

    oznaka = factory.Sequence(lambda n: u'PKS {}'.format(n))
    naziv = 'Skupina kontrole'
    plan_aktivnost = factory.SubFactory(PlanAktivnostFactory)



class PlanKontrolaSpecifikacijaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PlanKontrolaSpecifikacija

    oznaka = factory.Sequence(lambda n: u'PAS {}'.format(n))
    naziv = 'Specifikacija kontrole'
    plan_aktivnost = factory.SubFactory(PlanAktivnostFactory)



class PlanKontrolaSpecifikacijaOpcijaSelectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PlanKontrolaSpecifikacijaOpcijaSelect

    oznaka = factory.Sequence(lambda n: 'Opcija {0}'.format(n))
    naziv = factory.Sequence(lambda n: 'Opcija {0}'.format(n))
    plan_kontrola_specifikacija = factory.SubFactory(PlanKontrolaSpecifikacijaFactory)
