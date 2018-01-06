import factory

from .models import Arhiv


class ArhivFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Arhiv

    oznaka = '01'
    naziv = 'Arhiv 1'
