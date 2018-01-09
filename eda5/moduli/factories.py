import factory

from .models import Modul
from .models import Zavihek

class ModulFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Modul

    oznaka = factory.Sequence(lambda n: u'md_{}'.format(n))
    naziv = 'Moj Modul'
    opis = 'Moj Opis'
    barva = '#41f4e5'
    url_ref = ''


class ZavihekFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Zavihek

    oznaka = factory.Sequence(lambda n: u'zav_{}'.format(n))
    naziv = 'Moj Zavihek'
    url_ref = ''
    modul = factory.SubFactory(ModulFactory)
