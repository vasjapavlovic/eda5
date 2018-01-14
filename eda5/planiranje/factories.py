



class PlanFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Plan

    oznaka = factory.Sequence(lambda n: '{0}'.format(n))
    naziv = factory.Sequence(lambda n: '{0}'.format(n))
