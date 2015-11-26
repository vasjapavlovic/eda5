from django.test import TestCase

from ..models import LastniskaEnotaElaborat, LastniskaEnotaInterna, Program, LastniskaSkupina


class TestLastniskaEnotaElaborat(TestCase):

    fixtures = [
        'partnerji_models_testdata.json',
        'etaznalastnina_models_testdata.json',
    ]

    def setUp(self):
        self.le_elaborat = LastniskaEnotaElaborat.objects.get(oznaka="33")

    def test__str__(self):
        self.assertEqual(
            self.le_elaborat.__str__(),
            "33 | Delpinova ulica 18A, 5000 Nova Gorica"
        )


class TestLastniskaEnotaInterna(TestCase):

    fixtures = [
        'partnerji_models_testdata.json',
        'etaznalastnina_models_testdata.json',
    ]

    def setUp(self):
        self.le_interna_1 = LastniskaEnotaInterna.objects.get(oznaka="10330")
        self.le_interna_2 = LastniskaEnotaInterna.objects.get(oznaka="10961")

    def test__str__(self):
        self.assertEqual(
            self.le_interna_1.__str__(),
            "10330 | 33 | stanovanje"
        )
        self.assertEqual(
            self.le_interna_2.__str__(),
            "10961 | 96 | poslovni prostor"
        )


class TestProgram(TestCase):
    fixtures = [
        'partnerji_models_testdata.json',
        'etaznalastnina_models_testdata.json',
    ]

    def setUp(self):
        self.program = Program.objects.get(pk=1)

    def test__str__(self):
        self.assertEqual(
            self.program.__str__(),
            "300 | stanovanjski program"
        )


class TestLastniskaSkupina(TestCase):
    fixtures = [
        'partnerji_models_testdata.json',
        'etaznalastnina_models_testdata.json',
    ]

    def setUp(self):
        self.ls = LastniskaSkupina.objects.get(pk=1)

    def test__str__(self):
        self.assertEqual(
            self.ls.__str__(),
            "301 | stanovanjski program | vsa stanovanja"
        )