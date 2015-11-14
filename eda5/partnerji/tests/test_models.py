from test_plus.test import TestCase
from ..models import Drzava, Posta


class TestDrzava(TestCase):

    def setUp(self):

        self.drzava = Drzava.objects.create(naziv='Slovenija',
                              iso_koda='SLO',
                              )

    def test__str__(self):

        self.assertEqual(
            self.drzava.__str__(),
            "Slovenija (SLO)"
        )

class TestPosta(TestCase):

    def setUp(self):

        self.drzava = Drzava.objects.create(naziv='Slovenija',
                              iso_koda='SLO',
                              )

        # SLO = Drzava.objects.get(naziv='Slovenija')


        self.posta = Posta.objects.create(postna_stevilka='5000',
                             naziv='Nova Grica',
                             drzava=self.drzava,
                             )

        # super(TestPosta, self).setUp()

    def test__str__(self):

        self.assertEqual(
            self.posta.__str__(),
            "5000 Nova Grica"
        )
