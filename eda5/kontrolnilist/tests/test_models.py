from django.test import TestCase

from ..factories import AktivnostFactory
from ..factories import KontrolaSpecifikacijaFactory
from eda5.arhiv.factories import ArhivFactory
from ..factories import KontrolaSpecifikacijaOpcijaSelectFactory
from ..factories import KontrolaVrednostFactory

from eda5.deli.factories import ProjektnoMestoFactory

from ..models import Aktivnost
from ..models import KontrolaSpecifikacija
from ..models import KontrolaSpecifikacijaOpcijaSelect
from ..models import KontrolaVrednost
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


class KontrolaSpecifikacijaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        arhiv = ArhivFactory()
        arhiv.save()

        aps3 = KontrolaSpecifikacijaFactory(oznaka='APS3')
        aps1 = KontrolaSpecifikacijaFactory(oznaka='APS1')
        aps2 = KontrolaSpecifikacijaFactory(oznaka='APS2')

        aps3.save()
        aps1.save()
        aps2.save()

    def test_aktivnost_relacija(self):
        objekt = KontrolaSpecifikacija.objects.get(oznaka='APS1')
        reuslt = objekt.aktivnost
        self.assertFalse(reuslt is None)  # obstaja vnos

    def test_aktivnost_label(self):
        objekt = KontrolaSpecifikacija.objects.get(oznaka='APS1')
        result = objekt._meta.get_field('aktivnost').verbose_name
        self.assertEquals(result, 'aktivnost')

    def test_ordering(self):
        '''
        Seznam naj bo od najnižje aktivnosti do najvišje glede na oznako
        '''
        objekt_prvi = KontrolaSpecifikacija.objects.filter().first()
        self.assertEquals(objekt_prvi.oznaka, 'APS1')


    def test_vrednost_vrsta_label(self):
        objekt = KontrolaSpecifikacija.objects.get(oznaka='APS1')
        result = objekt._meta.get_field('vrednost_vrsta').verbose_name
        self.assertEquals(result, 'vrsta vrednosti')

    def test_vrednost_vrsta_default(self):
        objekt = KontrolaSpecifikacija.objects.get(oznaka='APS1')
        result = objekt._meta.get_field('vrednost_vrsta').default
        self.assertEquals(result, 1)


    def test_vrednost_vrsta_choices(self):
        '''
        Preverimo opcije izbire vrst vnosov
        '''
        objekt = KontrolaSpecifikacija.objects.get(oznaka='APS1')
        choices = objekt._meta.get_field('vrednost_vrsta').choices
        target = ((1, 'check'), (2, 'text'), (3, 'select'))
        self.assertEquals(choices, target)


class KontrolaSpecifikacijaOpcijaSelectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        arhiv = ArhivFactory()
        arhiv.save()

        os1 = KontrolaSpecifikacijaOpcijaSelectFactory()
        os1.save()

    def test_kontrola_specifiakcija_relacija(self):
        objekt = KontrolaSpecifikacijaOpcijaSelect.objects.first()
        reuslt = objekt.kontrola_specifikacija
        self.assertFalse(reuslt is None)  # obstaja vnos

    def test__str__(self):
        objekt = KontrolaSpecifikacijaOpcijaSelect.objects.first()
        result = objekt.__str__()
        cilj = '(' + objekt.oznaka + ')' + objekt.naziv
        self.assertEquals(result, cilj)



class KontrolaVrednostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        arhiv = ArhivFactory()
        arhiv.save()

        kv1 = KontrolaVrednostFactory()
        kv1.save()


    def test_inherith_osnovnakombinacija(self):
        '''
        testiramo, da se uvozijo vsi atributi iz
        osnovne kombinacije
        '''
        objekt = KontrolaVrednost.objects.first()
        result = objekt.oznaka
        self.assertFalse(result is None)  # obstaja vnos

        objekt = KontrolaVrednost.objects.first()
        result = objekt.oznaka_gen
        self.assertFalse(result is None)  # obstaja vnos

        objekt = KontrolaVrednost.objects.first()
        result = objekt.naziv
        self.assertFalse(result is None)  # obstaja vnos

        objekt = KontrolaVrednost.objects.first()
        result = objekt.opis
        self.assertFalse(result is None)  # obstaja vnos

        objekt = KontrolaVrednost.objects.first()
        result = objekt.status
        self.assertFalse(result is None)  # obstaja vnos

        objekt = KontrolaVrednost.objects.first()
        result = objekt.created
        self.assertFalse(result is None)  # obstaja vnos

        objekt = KontrolaVrednost.objects.first()
        result = objekt.updated
        self.assertFalse(result is None)  # obstaja vnos

    def test_vrednost_check_label(self):
        objekt = KontrolaVrednost.objects.first()
        result = objekt._meta.get_field('vrednost_check').verbose_name
        self.assertEquals(result, 'vrednost check')

    def test_vrednost_text_label(self):
        objekt = KontrolaVrednost.objects.first()
        result = objekt._meta.get_field('vrednost_text').verbose_name
        self.assertEquals(result, 'vrednost text')

    def test_vrednost_select_label(self):
        objekt = KontrolaVrednost.objects.first()
        result = objekt._meta.get_field('vrednost_select').verbose_name
        self.assertEquals(result, 'vrednost select')

    def test_kontrola_specifikacija_relacija(self):
        objekt = KontrolaVrednost.objects.first()
        result = objekt.kontrola_specifikacija
        self.assertFalse(result is None)  # obstaja vnos

    def test_delovni_nalog_relacija(self):
        objekt = KontrolaVrednost.objects.first()
        result = objekt.delovni_nalog
        self.assertFalse(result is None)  # obstaja vnos

    def test_projektno_mesto_relacija(self):
        objekt = KontrolaVrednost.objects.first()
        result = objekt.projektno_mesto
        self.assertFalse(result is None)  # obstaja vnos

    def test_verbose_name(self):
        objekt = KontrolaVrednost.objects.first()
        result = objekt._meta.verbose_name
        self.assertEquals(result, 'vrednost kontrole')

    def test_verbose_name_plural(self):
        objekt = KontrolaVrednost.objects.first()
        result = objekt._meta.verbose_name_plural
        self.assertEquals(result, 'vrednosti kontrol')
