from django.test import TestCase

from ..factories import AktivnostFactory
from ..factories import AktivnostParameterSpecifikacijaFactory
from eda5.arhiv.factories import ArhivFactory
from ..factories import OpcijaSelectFactory

from eda5.deli.factories import ProjektnoMestoFactory

from ..models import Aktivnost
from ..models import AktivnostParameterSpecifikacija
from ..models import OpcijaSelect
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


class AktivnostParameterSpecifikacijaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        arhiv = ArhivFactory()
        arhiv.save()

        aps3 = AktivnostParameterSpecifikacijaFactory(oznaka='APS3')
        aps1 = AktivnostParameterSpecifikacijaFactory(oznaka='APS1')
        aps2 = AktivnostParameterSpecifikacijaFactory(oznaka='APS2')

        aps3.save()
        aps1.save()
        aps2.save()

    def test_aktivnost_relacija(self):
        objekt = AktivnostParameterSpecifikacija.objects.get(oznaka='APS1')
        reuslt = objekt.aktivnost
        self.assertFalse(reuslt is None)  # obstaja vnos

    def test_aktivnost_label(self):
        objekt = AktivnostParameterSpecifikacija.objects.get(oznaka='APS1')
        result = objekt._meta.get_field('aktivnost').verbose_name
        self.assertEquals(result, 'aktivnost')

    def test_ordering(self):
        '''
        Seznam naj bo od najnižje aktivnosti do najvišje glede na oznako
        '''
        objekt_prvi = AktivnostParameterSpecifikacija.objects.filter().first()
        self.assertEquals(objekt_prvi.oznaka, 'APS1')


    def test_vrsta_vnosa_label(self):
        objekt = AktivnostParameterSpecifikacija.objects.get(oznaka='APS1')
        result = objekt._meta.get_field('vrsta_vnosa').verbose_name
        self.assertEquals(result, 'vrsta vnosa')


    def test_vrednost_vrsta_choices(self):
        '''
        Preverimo opcije izbire vrst vnosov
        '''
        objekt = AktivnostParameterSpecifikacija.objects.get(oznaka='APS1')
        choices = objekt._meta.get_field('vrsta_vnosa').choices
        target = ((1, 'check'), (2, 'text'), (3, 'select'))
        self.assertEquals(choices, target)


class OpcijaSelectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        arhiv = ArhivFactory()
        arhiv.save()

        os1 = OpcijaSelectFactory()
        os1.save()

    def test_aktivnost_parameter_specifikacija_relacija(self):
        objekt = OpcijaSelect.objects.first()
        reuslt = objekt.aktivnost_parameter_specifikacija
        self.assertFalse(reuslt is None)  # obstaja vnos

    def test__str__(self):
        objekt = OpcijaSelect.objects.first()
        result = objekt.__str__()
        cilj = '(' + objekt.oznaka + ')' + objekt.naziv
        self.assertEquals(result, cilj)
