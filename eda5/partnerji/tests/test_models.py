from test_plus.test import TestCase
from ..models import Drzava, Posta


class TestDrzava(TestCase):

    def setUp(self):

        Drzava.objects.create(naziv='Slovenija', iso_koda='SLO',)

    def test__str__(self):

        drzava = Drzava.objects.get(naziv="Slovenija")

        self.assertEqual(
            drzava.__str__(),
            "Slovenija (SLO)"
        )


class TestPosta(TestCase):

    def setUp(self):

        Drzava.objects.create(naziv='Slovenija', iso_koda='SLO',)
        drzava = Drzava.objects.get(naziv="Slovenija")

        Posta.objects.create(postna_stevilka='5000', naziv='Nova Grica', drzava=drzava,)

    def test__str__(self):

        posta = Posta.objects.get(postna_stevilka="5000")

        self.assertEqual(
            posta.__str__(),
            "5000 Nova Grica"
        )
