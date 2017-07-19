from test_plus.test import TestCase
from ..models import Drzava, Posta


class TestDrzava(TestCase):

    fixtures = ['partnerji_models_testdata.json']

    def setUp(self):
        self.drzava = Drzava.objects.get(naziv='Slovenija', iso_koda='SI',)

    def test__str__(self):
        self.assertEqual(
            self.drzava.__str__(),
            "Slovenija (SI)"
        )


class TestPosta(TestCase):

    fixtures = ['partnerji_models_testdata.json']

    def setUp(self):
        self.posta = Posta.objects.get(postna_stevilka="5000")

    def test__str__(self):
        self.assertEqual(
            self.posta.__str__(),
            "5000 Nova Gorica"
        )
