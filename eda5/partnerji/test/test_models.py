from test_plus.test import TestCase
from ..models import Drzava


class TestDrzava(TestCase):

    def setUp(self):

        Drzava.objects.create(naziv='Slovenija',
                              iso_koda='SLO',
                              )

        Drzava.objects.create(naziv='Nemčija',
                              iso_koda='DE',
                              )

    def test__str__(self):

        SLO = Drzava.objects.get(id=1)
        DE = Drzava.objects.get(id=2)

        self.assertEqual(
            SLO.__str__(),
            "Slovenija (SLO)"
        )

        self.assertEqual(
            DE.__str__(),
            "Nemčija (DE)"
        )
