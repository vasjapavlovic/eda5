from django.test import TestCase

from ..models import PredajaLastnine, Daljinec, PredajaDaljinca


class TestPredajaLastnine(TestCase):

    fixtures = [
        'partnerji_models_testdata.json',
        'etaznalastnina_models_testdata.json',
        'predaja_lastnine_models_testdata.json',
    ]

    def setUp(self):
        self.predaja = PredajaLastnine.objects.get(pk=1)


    def test__str__(self):
        self.assertEqual(
            self.predaja.__str__(),
            "0001 | predaja v last | 10330"
        )


class TestDaljinec(TestCase):

    fixtures = [
        'partnerji_models_testdata.json',
        'etaznalastnina_models_testdata.json',
        'predaja_lastnine_models_testdata.json',
    ]

    def setUp(self):
        self.daljinec_1 = Daljinec.objects.get(pk=1)
        self.daljinec_2 = Daljinec.objects.get(pk=2)

    def test__str__(self):
        self.assertEqual(
            self.daljinec_1.__str__(),
            "0001 | v uporabi"
        )
        self.assertEqual(
            self.daljinec_2.__str__(),
            "0002 | izklopljen"
        )


class TestPredajaDaljinca(TestCase):

    fixtures = [
        'partnerji_models_testdata.json',
        'etaznalastnina_models_testdata.json',
        'predaja_lastnine_models_testdata.json',
    ]

    def setUp(self):
        self.predaja_daljinca_1 = PredajaDaljinca.objecets.get(pk=1)

    def test__str__(self):
        self.assertEqual(
            self.predaja_daljinca_1.__str__(),
            "0001 | 2015-11-26"
        )
