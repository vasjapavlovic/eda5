from django.test import TestCase

from ..factories import AktivnostFactory
from ..factories import ArhivFactory
from eda5.deli.factories import ProjektnoMestoFactory

from ..models import Aktivnost
from eda5.partnerji.models import Posta



class AktivnostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        arhiv = ArhivFactory()
        arhiv.save()

        pm1 = ProjektnoMestoFactory()
        pm2 = ProjektnoMestoFactory()
        pm3 = ProjektnoMestoFactory()

        aktivnost3 = AktivnostFactory.create(oznaka="A3", projektno_mesto=(pm1, pm2, pm3))
        aktivnost1 = AktivnostFactory.create(oznaka="A1", projektno_mesto=(pm1, pm2, pm3))
        aktivnost2 = AktivnostFactory.create(oznaka="A2", projektno_mesto=(pm1, pm2, pm3))

        aktivnost3.save()
        aktivnost1.save()
        aktivnost2.save()

    def test_verbose_name(self):
        zeljen_rezultat = 'Aktivnost'
        objekt = Aktivnost.objects.get(oznaka="A1")
        dejanski_rezultat = objekt._meta.verbose_name
        self.assertEquals(dejanski_rezultat, zeljen_rezultat)

    def test_verbose_name_plural(self):
        zeljen_rezultat = 'Aktivnosti'
        objekt = Aktivnost.objects.get(oznaka="A1")
        dejanski_rezultat = objekt._meta.verbose_name_plural
        self.assertEquals(dejanski_rezultat, zeljen_rezultat)

    def test_ordering(self):
        zeljen_rezultat = 'A1'
        objekt_list = Aktivnost.objects.filter()
        dejanski_rezultat = objekt_list[0].oznaka  #oznaka prvega na seznamu
        self.assertEquals(dejanski_rezultat, zeljen_rezultat)

    def test_opravilo_label(self):
        zeljen_rezultat = 'opravilo'
        objekt = Aktivnost.objects.get(oznaka='A1')
        dejanski_rezultat = objekt._meta.get_field('opravilo').verbose_name
        self.assertEquals(dejanski_rezultat, zeljen_rezultat)

    def test_opravilo_foreignKey(self):
        objekt = Aktivnost.objects.get(oznaka='A1')
        result_1 = objekt.opravilo
        self.assertFalse(result_1 is None)  # obstaja vnos opravila

    def test_projektno_mesto_foreignKey(self):
        objekt = Aktivnost.objects.get(oznaka='A1')
        result_1 = objekt.projektno_mesto.filter().count()
        self.assertEquals(result_1, 3)  # kontrola many to many da obstajajo 3 vnosi
