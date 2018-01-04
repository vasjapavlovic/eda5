from django.test import TestCase

from ..factories import AktivnostFactory

from ..models import Aktivnost


class AktivnostModelFactoryTest(TestCase):

    def setUp(self):

        self.aktivnost = AktivnostFactory()



    def test_verbose_name(self):

        zeljen_rezultat = 'Aktivnost'
        objekt = self.aktivnost
        dejanski_rezultat = objekt._meta.verbose_name
        self.assertEquals(dejanski_rezultat, zeljen_rezultat)



class AktivnostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        Aktivnost.objects.create(oznaka='A2', naziv="Aktivnost 1")
        Aktivnost.objects.create(oznaka='A3', naziv="Aktivnost 3")
        Aktivnost.objects.create(oznaka='A1', naziv="Aktivnost 2")



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


class DelovniNalogi_TODO(TestCase):

    def test_TODO(self):

        self.fail('Dokončaj dodajanje aktivnosti.')
