from django.test import TestCase

from ..models import PredajaLastnine


class TestPredajaLastnine(TestCase):

    fixtures = [
        'partnerji_models_testdata.json',
        'etaznalastnina_models_testdata.json',
        'predaja_lastnine_models_testdata.json',
    ]



    def test_get_absolute_url(self):
        pass
