from django.test import TestCase

from ..factories import AktivnostFactory

from ..models import Aktivnost


class AktivnostModelFactoryTest(TestCase):


    @classmethod
    def setUpTestData(cls):


        aktivnost3 = AktivnostFactory.create(oznaka="A3")
        aktivnost1 = AktivnostFactory.create(oznaka="A1")
        aktivnost2 = AktivnostFactory.create(oznaka="A2")

        aktivnost3.save()
        aktivnost1.save()
        aktivnost2.save()


        # aktivnost_list = AktivnostFactory.build_batch(2)



    def test_verbose_name(self):

        print(Aktivnost.objects.filter())

        zeljen_rezultat = 'Aktivnost'
        objekt = Aktivnost.objects.get(oznaka='A1')
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


# class DelovniNalogi_TODO(TestCase):
#
#     def test_TODO(self):
#
#         self.fail('Dokončaj dodajanje aktivnosti.')
