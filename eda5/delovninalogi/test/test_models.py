from django.test import TestCase

from ..factories import AktivnostFactory, ArhivFactory


from ..models import Aktivnost

from eda5.partnerji.models import Posta



class AktivnostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        arhiv = ArhivFactory()
        arhiv.save()

        aktivnost3 = AktivnostFactory.create(oznaka="A3")
        aktivnost1 = AktivnostFactory.create(oznaka="A1")
        aktivnost2 = AktivnostFactory.create(oznaka="A2")

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
        result_1 = objekt.projektno_mesto
        self.assertFalse(result_1 is None)  # obstaja vnos projektnega_mesta
