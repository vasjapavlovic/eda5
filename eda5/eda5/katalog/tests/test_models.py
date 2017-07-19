from django.test import TestCase

from ..models import TipArtikla

class TipArtiklaTest(TestCase):
    fixtures = [
        'katalog_models_testdata.json',
    ]

    def setUp(self):
        self.tipartikla = TipArtikla.objects.get(pk=1)

    def test__str__(self):
        self.assertEqual(
            self.tipartikla.__str__(),
            "(CR)Cevni Razvod"
        )