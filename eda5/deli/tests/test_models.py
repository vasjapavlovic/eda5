from django.test import TestCase

from ..models import Skupina, Podskupina, DelStavbe, ProjektnoMesto, Element


class SkupinaDelovTest(TestCase):
    fixtures = [
        'katalog_models_testdata.json',
        'deli_models_testdata.json',
    ]

    def setUp(self):
        self.skupina = Skupina.objects.get(pk=1)

    def test__str__(self):
        self.assertEqual(
            self.skupina.__str__(),
            "(A)Sistemi in Naprave"
        )


class PodskupinaDelovTest(TestCase):
    fixtures = [
        'katalog_models_testdata.json',
        'deli_models_testdata.json',
    ]

    def setUp(self):
        self.podskupina = Podskupina.objects.get(pk=1)

    def test__str__(self):
        self.assertEqual(
            self.podskupina.__str__(),
            "(AA)Ogrevanje in Hlajenje"
        )


class DelStavbeTest(TestCase):
    fixtures = [
        'katalog_models_testdata.json',
        'deli_models_testdata.json',
    ]

    def setUp(self):
        self.delstavbe = DelStavbe.objects.get(pk=1)

    def test__str__(self):
        self.assertEqual(
            self.delstavbe.__str__(),
            "(AA01)Primarni Sistem Ogrevanja Poslovni Prostori"
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.delstavbe.get_absolute_url(),
            "/moduli/deli/del/1/detail/"
        )

    def test_elementi_vsi(self):

        projektna_mesta = ProjektnoMesto.objects.filter(del_stavbe=self.delstavbe)
        projektno_mesto = projektna_mesta.first()
        elementi = projektno_mesto.elementi_aktivni
        element = elementi[0]

        self.assertEqual(
            element.projektno_mesto.oznaka,
            "01AA01"
        )

        self.assertEqual(
            element.tovarniska_st,
            "BBX20152232"
        )


class ProjektnoMestoTest(TestCase):

    fixtures = [
        'katalog_models_testdata.json',
        'deli_models_testdata.json',
    ]

    def setUp(self):
        self.projektnomesto = ProjektnoMesto.objects.get(pk=1)

    def test__str__(self):
        self.assertEqual(
            self.projektnomesto.__str__(),
            "(01AA01)Cevni Razvod-k2.g2.cr.1"
        )


class ElementTest(TestCase):

    fixtures = [
        'katalog_models_testdata.json',
        'deli_models_testdata.json',
    ]

    def setUp(self):
        self.element = Element.objects.get(pk=1)

    def test__str__(self):
        self.assertEqual(
            self.element.__str__(),
            "(BBX20152232)Blue Box-Frigus 102"
        )
