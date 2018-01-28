from django.test import TestCase

from ..factories import AktivnostFactory
from ..factories import KontrolaSpecifikacijaFactory
from ..factories import KontrolaSpecifikacijaOpcijaSelectFactory
from ..factories import KontrolaVrednostFactory
from eda5.arhiv.factories import ArhivFactory

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

        # pm1 = ProjektnoMestoFactory()
        # pm2 = ProjektnoMestoFactory()
        # pm3 = ProjektnoMestoFactory()

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

    def test_not_deleted_manager(self):
        aktivnost3 = Aktivnost.objects.get(oznaka="A3")
        aktivnost3.status = 5
        aktivnost3.save()

        aktivnost2 = Aktivnost.objects.get(oznaka="A2")
        aktivnost2.status = 3
        aktivnost2.save()

        vse_aktivnosti = Aktivnost.objects.filter()
        self.assertEquals(len(vse_aktivnosti), 3)

        not_deleted_aktivnosti = Aktivnost.objects.not_deleted()
        self.assertEquals(len(not_deleted_aktivnosti), 2)




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

    def test_kontrola_skupina_relacija(self):
        objekt = KontrolaSpecifikacija.objects.get(oznaka='APS1')
        reuslt = objekt.kontrola_skupina
        self.assertFalse(reuslt is None)  # obstaja vnos

    def test_kontrola_skupina_label(self):
        objekt = KontrolaSpecifikacija.objects.get(oznaka='APS1')
        result = objekt._meta.get_field('kontrola_skupina').verbose_name
        self.assertEquals(result, 'Skupina kontrol')

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
